<template>
  <div id="cheermessage">
    <div class="info noto-sans">
      <p class="info-head">응원의 메세지</p>
      <img src="/static/images/message.png"  class="info-img">
      <p class="info-parag">카포전을 재밌게 즐기고 계신가요? 수고하는 우리편 선수들과 가슴졸이며 지켜보고 있는 학우들에게 응원의 한 마디를 남겨주세요!</p>
    </div>
    <table class="board noto-sans">
      <thead>
        <tr>
          <th class="fc">경기</th>
          <th class="sc">내용</th>
          <th class="tc">팀</th>
          <th class="fourth">좋아요</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="message in messages_rendered">
          <td class="fc">{{ find_event_name(message) }}</td>
          <td class="sc">{{ message.fields.content }}</td>
          <td class="tc" v-if="message.fields.school === 1">KAIST</td>
          <td class="tc" v-else-if="message.fields.school === 2">POSTECH</td>
          <td class="fourth" :id="'toggle'.concat(message.pk)" v-on:click="add_like($event, message); toggle($event.target)">
            <i class="fas fa-thumbs-up" :style="initialFas(message.pk)"></i>
            <i class="far fa-thumbs-up" :style="initialFar(message.pk)"></i>
            {{ message.fields.likes }}개</td>
        </tr>
      </tbody>
    </table>
    <div class="paginator noto-sans">
      <div>
        <select id="event-type">
          <option value="all" selected>모든 경기</option>
          <option value="no-specific">모두에게</option>
          <option v-for="event in events" v-if="event.fields.type != 2" :value="event.pk">{{ event.fields.name_kor }}</option>
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
      <router-link :to="{ name: 'cheermessage_write' }">
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
      events: [],
      messages: [],
      messages_event: [],
      messages_rendered: [],
      page_range: [],
      likedMessages: []
    }
  },
  created () {
    this.likedMessages = localStorage.getItem('likedMessages')
    if (this.likedMessages) this.likedMessages = JSON.parse(this.likedMessages)
    console.log(this.likedMessages)
    this.$http.get('/api/cheermessage/')
      .then((response) => {
        this.messages = JSON.parse(response.data)
        this.current_page = 1
        this.event_type = 0
        this.select_event()
        this.max_page = parseInt((this.messages.length - 1) / 10) + 1
      })
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
      })
  },
  methods: {
    find_event_name: function (message) {
      if (message.fields.hasOwnProperty('event')) {
        for (let event of this.events) {
          if (event.pk === message.fields.event) {
            return event.fields.name_kor
          }
        }
      }
      return '모두에게'
    },
    toggle: function (target) {
      if (target.tagName === 'I') target = target.parentNode
      if (target.children[1].style.display !== 'none') {
        target.children[1].style.display = 'none'
        target.children[0].style.display = 'inline-block'
      } else {
        target.children[0].style.display = ''
        target.children[1].style.display = ''
      }
    },
    initialFar: function (pk) {
      if (!this.likedMessages) return ''
      let idx = this.likedMessages.indexOf(pk)
      if (idx === -1) return ''
      else return 'display: none'
    },
    initialFas: function (pk) {
      if (!this.likedMessages) return ''
      let idx = this.likedMessages.indexOf(pk)
      if (idx === -1) return ''
      else return 'display: inline-block'
    },
    add_like: function (event, message) {
      let target = event.target
      if (target.tagName === 'I') target = target.parentNode
      if (target.children[1].style.display !== 'none') {
        let data = JSON.stringify({ 'add': true })
        this.$http.post('/api/cheermessage/' + message.pk + '/', data)
          .then((response) => {
            message.fields.likes += 1
            if (!this.likedMessages) {
              this.likedMessages = [message.pk]
            } else {
              this.likedMessages.push(message.pk)
            }
            localStorage.setItem('likedMessages', JSON.stringify(this.likedMessages))
          })
      } else {
        let data = JSON.stringify({ 'add': false })
        this.$http.post('/api/cheermessage/' + message.pk + '/', data)
          .then((response) => {
            message.fields.likes -= 1
            let idx = this.likedMessages.indexOf(message.pk)
            if (idx > -1) this.likedMessages.splice(idx, 1)
            localStorage.setItem('likedMessages', JSON.stringify(this.likedMessages))
          })
      }
    },
    page_turn: function (n) {
      while (this.messages_rendered.length) {
        this.messages_rendered.pop()
      }
      this.current_page = n
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
    },
    select_event: function () {
      var eventID = document.getElementById('event-type').value
      // console.log(eventID)
      while (this.messages_event.length) {
        this.messages_event.pop()
      }
      if (eventID === 'all') { // show all
        for (let i = 0; i < this.messages.length; i++) {
          this.messages_event.push(this.messages[i])
        }
      } else if (eventID === 'no-specific') { // show messages with no specific event tied to it
        for (let i = 0; i < this.messages.length; i++) {
          if (!this.messages[i].fields.event) {
            this.messages_event.push(this.messages[i])
          }
        }
      } else {
        for (let i = 0; i < this.messages.length; i++) {
          if (this.messages[i].fields.event === parseInt(eventID)) {
            this.messages_event.push(this.messages[i])
          }
        }
      }
      this.max_page = parseInt((this.messages_event.length - 1) / 10) + 1
      this.page_turn(1)
    }
  }
}
</script>

<style scoped>
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
  width: 130px;
  padding-left: 15px;
 }

.board .tc {
  width: 100px;
  padding-right: 15px;
}

.board .fourth {
  width: 100px;
  cursor: pointer;
}

.fourth > .far {
  margin-right: 5px;
}

.fourth > .fas {
  display: none;
  margin-right: 5px;
}

.fourth:hover > .far {
  display: none;
}

.fourth:hover > .fas {
  display: inline-block;
  margin-right: 5px;
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

.board .sc {
  padding-right: 10px;
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
