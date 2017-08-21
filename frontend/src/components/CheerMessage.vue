<template>
  <div id="cheermessage">
    <div class="info noto-sans">
      <p class="info-head">응원의 메세지</p>
      <img src="/static/images/message.png"  class="info-img">
      <p class="info-parag">어어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌어쩌구쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구</p>
    </div>
    <table class="board noto-sans">
      <thead>
        <tr>
          <th class="fc">경기</th>
          <th class="sc">내용</th>
          <th class="tc">팀</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="message in messages_rendered">
          <td class="fc" v-if="message.fields.event === 1">축구</td>
          <td class="fc" v-if="message.fields.event === 7">야구</td>
          <td class="sc">{{ message.fields.content }}</td>
          <td class="tc" v-if="message.fields.school === 1">KAIST</td>
          <td class="tc" v-else-if="message.fields.school === 2">POSTECH</td>
        </tr>
      </tbody>
    </table>
    <div class="paginator noto-sans">
      <div>
        <select id="event-type">
          <option value="0" selected>모두보기</option>
          <option value="1">축구</option>
          <option value="7">야구</option>
        </select>
        <span class="write" v-on:click="select_event()">확인</span>
      </div>
      <div>
        <button class="pg" v-on:click="page_turn(1)"><</button>
        <button class="pg" v-if="page_range[0] > 1" v-on:click="page_turn(page_range[0] - 1)">... </button> 
        <button class="pg" v-for="n in page_range" v-on:click="page_turn(n)">{{ n }}</button>
        <button class="pg" v-if="page_range[page_range.length - 1] < max_page" v-on:click="page_turn(page_range[page_range.length - 1] + 1)">...</button>
        <button class="pg" v-on:click="page_turn(max_page)">></button>
      </div>
      <router-link :to="{ name: 'cheermessage-write' }">
        <span class="write noto-sans">쓰기</span>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'cheermessage',
  data () {
    return {
      messages: [],
      messages_event: [],
      messages_rendered: [],
      page_range: []
    }
  },
  created () {
    this.$http.get('/api/cheermessage/')
      .then((response) => {
        this.messages = JSON.parse(response.data)
        console.log(this.messages.length)
        this.current_page = 1
        this.event_type = 0
        this.select_event(0)
        this.max_page = parseInt((this.messages.length - 1) / 10) + 1
      })
  },
  methods: {
    page_turn: function (n) {
      while (this.messages_rendered.length) {
        this.messages_rendered.pop()
      }
      this.current_page = n
      console.log(this.current_page)
      if (this.messages_event.length > this.current_page * 10) {
        for (let i = this.current_page * 10 - 10; i < (this.current_page * 10); i++) {
          this.messages_rendered.push(this.messages_event[i])
        }
      } else {
        for (let i = this.current_page * 10 - 10; i < this.messages_event.length; i++) {
          this.messages_rendered.push(this.messages_event[i])
        }
      }
      // this.messages_rendered = JSON.stringify(this.messages_rendered)
      console.log(this.messages_rendered)
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
    },
    select_event: function () {
      var eventID = parseInt(document.getElementById('event-type').value)
      while (this.messages_event.length) {
        this.messages_event.pop()
      }
      console.log(eventID)
      if (eventID === 0) {
        for (let i = 0; i < this.messages.length; i++) {
          this.messages_event.push(this.messages[i])
        }
      } else {
        for (let i = 0; i < this.messages.length; i++) {
          if (this.messages[i].fields.event === eventID) {
            this.messages_event.push(this.messages[i])
          }
        }
      }
      console.log(this.messages_event)
      this.max_page = parseInt((this.messages_event.length - 1) / 10) + 1
      this.page_turn(1)
    }
  }
}
</script>

<style>
.info{
}

.info-head{ 
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 10px;
  margin-bottom: 1.5rem;
}

.info-img{
  float: left;
  margin-top: -50px;
  margin-left: -30px;
  margin-bottom: -100px;
  padding-bottom: -100px;
  width: 350px;
}

.info-parag{
  display: inline;
  font-size: 32px;
}

.board{
  margin-top: 50px;
  margin-left: 10px;
  margin-right: 10px;
  text-align: left;
  line-height: 1.6;
  vertical-align: top;
  position: relative;
  z-index:1;
}

.board .fc {
  width: 200px;
  padding-left: 15px;
 }
 
.board .tc {
  width: 100px;
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

.board > tbody > tr > td:first-child {
  border-bottom-left-radius: 10px;
  border-top-left-radius: 10px;
}

.board > tbody > tr > td:last-child {
  border-bottom-right-radius: 10px;
  border-top-right-radius: 10px;
}

.paginator {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding-top: 20px;
  padding-bottom: 20px;
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
