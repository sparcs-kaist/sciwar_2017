<template>
  <div class="supporters noto-sans">
    <div class="supporters-title">
      서포터즈가 되면...
    </div>
    <div class="supporters-todo">
      <p>- 티셔츠를 나누어 드립니다.</p>
      <p>- 서포터즈 교육을 받아야 합니다.</p>
      <p>- 카포전 당일 참석을 해야 합니다.</p>
      <p>- 서포터즈 정원은 150명 입니다.</p>
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
          <td class="fc">{{ supporter.pk }}</td>
          <td class="sc">{{ supporter.fields.nickname }}</td>
          <td class="tc">{{ supporter.num }}</td>
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
  name: 'supporters',
  data () {
    return {
      supportersRendered: [],
      page_range: [],
      max_page: {}
    }
  },
  created () {
    this.$http.get('/api/supporter-reg/')
      .then((response) => {
        this.supporterRegs = JSON.parse(response.data)
        this.max_page = parseInt((this.supporterRegs.length - 1) / 10) + 1
        this.supportersNum = new Array(this.supporterRegs.length).fill(0)
        this.$http.get('/api/supporters')
          .then((response) => {
            this.supporters = JSON.parse(response.data)
            for (let i in this.supporters) {
              this.supportersNum[this.supporters[i].fields.registry - 1]++
            }
            for (let i in this.supporterRegs) {
              this.supporterRegs[i]['num'] = this.supportersNum[i]
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
.supporters-title {
  font-size: 60px;
}

.supporters-todo {
  font-size: 27px;
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
}

.board > tbody > tr:nth-child(even) {
  background: #efefef;
}

.paginator {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
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
