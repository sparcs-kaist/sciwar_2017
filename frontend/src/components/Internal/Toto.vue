<template>
  <div class="internal-toto noto-sans">
    <div class="internal-toto-title">
      토토이벤트
    </div>
    <table class="board">
      <thead>
        <tr>
          <th class="fc">번호</th>
          <th class="sc">이름</th>
          <th class="tc">점수</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="toto in totoRendered">
          <td class="fc">
            <router-link :to="{ name: 'internal_toto_view', params: { id: toto.pk } }">
              <div>{{ toto.num }}</div>
            </router-link>
          </td>
          <td class="sc">
            <router-link :to="{ name: 'internal_toto_view', params: { id: toto.pk } }">
              <div>{{ toto.fields.name }}</div>
            </router-link>
          </td>
          <td class="tc">
            <router-link :to="{ name: 'internal_toto_view', params: { id: toto.pk } }">
              <div>{{ toto.fields.total }}</div>
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="paginator noto-sans">
      <div>
        <button class="pg" v-on:click="page_turn(1)"><</button>
        <button class="pg" v-if="page_range[0] > 1" v-on:click="page_turn(page_range[0] - 1)">... </button>
        <button class="pg" v-for="n in page_range" v-on:click="page_turn(n)">{{ n }}</button>
        <button class="pg" v-if="page_range[page_range.length - 1] < max_page" v-on:click="page_turn(page_range[page_range.length - 1] + 1)">...</button>
        <button class="pg" v-on:click="page_turn(max_page)">></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'toto_check',
  data () {
    return {
      totoRendered: [],
      page_range: [],
      max_page: {}
    }
  },
  created () {
    this.$http.get('/api/toto-content/')
      .then((response) => {
        this.totoContents = JSON.parse(response.data)
        this.max_page = parseInt((this.totoContents.length - 1) / 10) + 1
        let page = 1
        for (let i = this.totoContents.length; i--;) {
          this.totoContents[i].num = page
          page++
        }
        this.totoNum = new Array(this.totoContents.length).fill(0)
        this.page_turn(1)
      })
  },
  methods: {
    page_turn: function (n) {
      while (this.totoRendered.length) {
        this.totoRendered.pop()
      }
      this.current_page = n
      console.log(this.current_page)
      if (this.totoContents.length > this.current_page * 10) {
        for (let i = this.current_page * 10 - 10; i < (this.current_page * 10); i++) {
          this.totoRendered.push(this.totoContents[i])
        }
      } else {
        for (let i = this.current_page * 10 - 10; i < this.totoContents.length; i++) {
          this.totoRendered.push(this.totoContents[i])
        }
      }
      console.log(this.totoContents)
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

<style scoped>
.internal-toto-title {
  font-size: 64px;
  font-weight: 700;
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

.board > tbody > tr > td > a {
  width: 100%;
  color: black;
}

.paginator {
  display: flex;
  flex-direction: row;
  justify-content: center;
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
