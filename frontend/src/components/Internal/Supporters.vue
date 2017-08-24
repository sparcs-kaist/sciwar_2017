<template>
  <div class="internal-supporters noto-sans">
    <div class="internal-supporters-title">
      서포터즈 확인 페이지
    </div>
    <div class="supporters-status">
      <p>인원: {{ numSupporters }}</p>
      <div class="supporters-size">
        <p class="0">XS: {{ numXS }}</p>
        <p class="1">S: {{ numS }}</p>
        <p class="2">M: {{ numM }}</p>
        <p class="3">L: {{ numL }}</p>
        <p class="4">XL: {{ numXL }}</p>
        <p class="5">XXL: {{ numXXL }}</p>
      </div>
    </div>
    <table class="board">
      <thead>
        <tr>
          <th class="fc">번호</th>
          <th class="sc">팀이름</th>
          <th class="tc">인원 수</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="supporter in supportersRendered">
          <td class="fc">
            <router-link :to="{ name: 'internal_supporters_view', params: { id:supporter.pk } }">
              <div>{{ supporter.pk }}</div>
            </router-link>
          </td>
          <td class="sc">
            <router-link :to="{ name: 'internal_supporters_view', params: { id:supporter.pk } }">
              <div>{{ supporter.fields.nickname }}</div>
            </router-link>
          </td>
          <td class="tc">
            <router-link :to="{ name: 'internal_supporters_view', params: { id:supporter.pk } }">
              <div>{{ supporter.num }}</div>
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="paginator noto-sans">
      <div style="width:50px;"></div>
      <div>
        <button class="pg" v-on:click="page_turn(1)"><</button>
        <button class="pg" v-if="page_range[0] > 1" v-on:click="page_turn(page_range[0] - 1)">... </button> 
        <button class="pg" v-for="n in page_range" v-on:click="page_turn(n)">{{ n }}</button>
        <button class="pg" v-if="page_range[page_range.length - 1] < max_page" v-on:click="page_turn(page_range[page_range.length - 1] + 1)">...</button>
        <button class="pg" v-on:click="page_turn(max_page)">></button>
      </div>
      <router-link :to="{ name: 'supporters_write' }">
        <span class="write noto-sans">쓰기</span>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'supporters_check',
  data () {
    return {
      supportersRendered: [],
      page_range: [],
      max_page: {},
      numSupporters: 0,
      numXS: 0,
      numS: 0,
      numM: 0,
      numL: 0,
      numXL: 0,
      numXXL: 0
    }
  },
  created () {
    this.$http.get('/api/supporter-reg/')
      .then((response) => {
        this.supporterRegs = JSON.parse(response.data)
        this.max_page = parseInt((this.supporterRegs.length - 1) / 10) + 1
        this.supportersNum = new Array(this.supporterRegs[0].pk + 1).fill(0)
        console.log(this.supporterRegs.length)
        this.$http.get('/api/supporters/')
          .then((response) => {
            this.supporters = JSON.parse(response.data)
            this.numSupporters = this.supporters.length
            for (let i in this.supporters) {
              this.supportersNum[this.supporters[i].fields.registry]++
              if (this.supporters[i].fields.size === 0) {
                this.numXS++
              } else if (this.supporters[i].fields.size === 1) {
                this.numS++
              } else if (this.supporters[i].fields.size === 2) {
                this.numM++
              } else if (this.supporters[i].fields.size === 3) {
                this.numL++
              } else if (this.supporters[i].fields.size === 4) {
                this.numXL++
              } else if (this.supporters[i].fields.size === 5) {
                this.numXXL++
              }
            }
            let j = 0
            this.supportersNum.reverse()
            for (let i in this.supportersNum) {
              if (this.supportersNum[i] > 0) {
                this.supporterRegs[j]['num'] = this.supportersNum[i]
                j++
              }
            }
            console.log(this.supporterRegs)
            this.page_turn(1)
          })
      })
  },
  methods: {
    page_turn: function (n) {
      while (this.supportersRendered.length) {
        this.supportersRendered.pop()
      }
      this.current_page = n
      console.log(this.current_page)
      if (this.supporterRegs.length > this.current_page * 10) {
        for (let i = this.current_page * 10 - 10; i < (this.current_page * 10); i++) {
          this.supportersRendered.push(this.supporterRegs[i])
        }
      } else {
        for (let i = this.current_page * 10 - 10; i < this.supporterRegs.length; i++) {
          this.supportersRendered.push(this.supporterRegs[i])
        }
      }
      // this.messages_rendered = JSON.stringify(this.messages_rendered)
      console.log(this.supporterRegs)
      this.set_range()
    },
    set_range: function () {
      while (this.page_range.length) {
        this.page_range.pop()
      }
      var start = 0
      if (this.current_page % 5) {
        start = this.current_page - ((this.current_page % 5) - 1)
      } else {
        start = this.current_page - 4
      }
      for (let i = 0; i < 5; i++) {
        if (start > this.max_page) {
          break
        }
        this.page_range.push(start)
        start++
      }
      console.log(this.page_range)
    }
  }
}
</script>

<style>
.internal-supporters-title {
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 10px;
}

.supporters-status {
  font-size: 20px;
}

.supporters-todo {
  margin-left: 20px;
  font-size: 32px;
}

.supporters-todo > tr > th {
  font-weight: 400;
  color: black;
}

.board{
  margin-top: 50px;
  margin-left: 10px;
  margin-right: 10px;
  border-collapse: collapse;
  text-align: left;
  line-height: 1.6;
  vertical-align: top;
}

.board .fc {
  width: 200px;
  padding-left: 15px;
 }
 
.board .tc {
  width: 120px;
  padding-right: 15px;
}

.board > thead {
  font-size: 28px;
  padding-bottom: 10px;
}

.board > tbody {
  font-size: 25px;
  font-weight: 300;
  color: black;
}

.board > tbody > tr:nth-child(even) {
  background: #efefef;
}

.board > tbody > tr > td:first-child {
  border-bottom-left-radius: 10px;
  border-top-left-radius: 10px;
}

.board > tbody > tr > td:last-child {
  border-bottom-right-radius: 10px;
  border-top-right-radius: 10px;
}

.board > tbody > tr > td > a {
  width: 100%;
  color: black;
}

.paginator {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  margin-top: 20px;
}

.pg {
  margin-left: 1px;
  margin-right: 2px;
  background: #555555;
  border: none;
  color: white;
  text-align: center;
  display: inline-block;
  font-size: 20px;
  padding: 5px 10px;
  cursor: pointer;
}

.write {
  float: right;
  font-size: 20px;
  color: black;
  padding-left: 10px;
  cursor: pointer;
}
</style>
