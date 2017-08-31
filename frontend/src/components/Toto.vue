<template>
  <div class="toto noto-sans">
    <div class="toto-title">
      토토이벤트
    </div>
    <p class="toto-guide">각 경기의 승자와 점수를 맞춰 주세요! 한 번 작성한 토토는 수정할 수 없으니 신중히 찍어주세요. 각 경기의 승자를 맞출 때마다 1점이 추가되고, 정확한 점수를 맞추면 가점이 추가됩니다. 가점은 야구와 농구 경기가 더 높습니다. 경기가 모두 끝나고 나면, 상위 랭커부터 상품을 선택하여 수령하실 수 있어요! </p>
    <div class="prize">
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
            <router-link :to="{ name: 'toto_view', params: { id: toto.pk } }">
              <div>{{ toto.num }}</div>
            </router-link>
          </td>
          <td class="sc">
            <router-link :to="{ name: 'toto_view', params: { id: toto.pk } }">
              <div>{{ toto.fields.name }}</div>
            </router-link>
          </td>
          <td class="tc">
            <router-link :to="{ name: 'toto_view', params: { id: toto.pk } }">
              <div>{{ toto.fields.total }}</div>
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
      <router-link :to="{ name: 'toto_write' }">
        <span class="write noto-sans">쓰기</span>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'toto',
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
        for (let toto of this.totoContents) {
          toto.fields.name = toto.fields.name.substr(0, 1) + '*' + toto.fields.name.substr(2)
        }
        this.max_page = parseInt((this.totoContents.length - 1) / 10) + 1
        let page = 1
        for (let i = this.totoContents.length; i--;) {
          this.totoContents[i].num = page
          page++
        }
        this.page_turn(1)
      })
  },
  methods: {
    page_turn: function (n) {
      while (this.totoRendered.length) {
        this.totoRendered.pop()
      }
      this.current_page = n
      if (this.totoContents.length > this.current_page * 10) {
        for (let i = this.current_page * 10 - 10; i < (this.current_page * 10); i++) {
          this.totoRendered.push(this.totoContents[i])
        }
      } else {
        for (let i = this.current_page * 10 - 10; i < this.totoContents.length; i++) {
          this.totoRendered.push(this.totoContents[i])
        }
      }
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
.toto-title {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 20px;
}

.toto-guide {
  font-size: 32px;
  margin-left: 24px;
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

