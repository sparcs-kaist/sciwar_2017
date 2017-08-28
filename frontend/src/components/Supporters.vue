<template>
  <div class="supporters noto-sans">
    <div class="supporters-title">
      서포터즈가 되면...
      <p>아래의 <서포터즈 활용 동의서>를 숙지하시고 신청해 주세요.</p>
    </div>
    <table class="supporters-todo">
      <tr>
        <th>하나,</th><td>카이스트 서포터즈로서 최선을 다해 활동에 참여해주시기 바랍니다.</td>
      </tr>
      <tr>
        <th>둘,</th><td>6개의 경기 (축구, 농구, 야구, LOL, AI, 과학퀴즈) 중 3가지 이상의 경기를 관람해주셔야 합니다.</td>
      </tr>
      <tr>
        <th>셋,</th><td>서포터즈 티셔츠 및 각종 물품을 제공할 예정이니 9/21(목) 전야제에 꼭 참석하셔야 합니다.</td>
      </tr>
      <tr>
        <th>넷,</th><td>9/20(수) 저녁에 엘카의 경기 응원 교육이 있습니다.</td>
      </tr>
    </table>
    <table class="board">
      <thead>
        <tr>
          <th class="fc">번호</th>
          <th class="sc">이름</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="supporter in supportersRendered">
          <td class="fc">
            <router-link :to="{ name: 'supporters_view', params: { id:supporter.pk } }">
              <div>{{ supporter.pk }}</div>
            </router-link>
          </td>
          <td class="sc">
            <router-link :to="{ name: 'supporters_view', params: { id:supporter.pk } }">
              <div>{{ supporter.fields.name }}</div>
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
  name: 'supporters',
  data () {
    return {
      supportersRendered: [],
      page_range: [],
      max_page: {}
    }
  },
  created () {
    this.$http.get('/api/supporters/')
      .then((response) => {
        this.supporters = JSON.parse(response.data)
        this.max_page = parseInt((this.supporters.length - 1) / 10) + 1
        this.page_turn(1)
      })
  },
  methods: {
    page_turn: function (n) {
      while (this.supportersRendered.length) {
        this.supportersRendered.pop()
      }
      this.current_page = n
      if (this.supporters.length > this.current_page * 10) {
        for (let i = this.current_page * 10 - 10; i < (this.current_page * 10); i++) {
          this.supportersRendered.push(this.supporters[i])
        }
      } else {
        for (let i = this.current_page * 10 - 10; i < this.supporters.length; i++) {
          this.supportersRendered.push(this.supporters[i])
        }
      }
      // this.messages_rendered = JSON.stringify(this.messages_rendered)
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
    }
  }
}
</script>

<style>
.supporters-title {
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 10px;
  margin-bottom: 1.5rem;
}

.supporters-title > p {
  font-size: 28px;
  font-weight: 500;
}

.supporters-todo {
  margin-left: 20px;
  font-size: 32px;
}

.supporters-todo > tr > th {
  font-weight: 400;
  color: black;
  width: 120px;
}

.supporters-todo > tr > td {
  padding-bottom: 10px;
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
