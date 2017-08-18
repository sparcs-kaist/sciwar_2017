<template>
  <div class="home">
    <div class="image">
      <p class="noto-sans big">2017 SCIENCE WAR</p>
      <p class="kopub">카이스트포스텍학생대제전</p>
      <p class="noto-sans small">OCT. 15 - 17<sup class="th"> th</sup> KAIST</p>
    </div>
    <div class="current-cheer-message noto-sans">
      <div>
        <img src="/static/images/quote1.png" width="35" height="35">
        <p>{{ messageContent }}</p>
        <img src="/static/images/quote2.png" width="35" height="35">
      </div>
      <p><span>to. </span>{{ messageTeam }}</p>
      <p><span>about. </span>{{ messageEvent }}</p>
    </div>
    <div class="events-status noto-sans">
      <p class="title">경기 현황</p>
      <router-link :to="{ name: 'cheermessage' }" id="to-cheer-message">
        <p>응원메시지 남기러 가기<img src="/static/images/message.png" width="35"></p>
        
      </router-link>
      <div>
        <div v-for="event in events" class="status-event">
          <div v-if="event.fields.winner == 1 && event.fields.type == 0" class="kaist-win">
            <p class="status-event-name">{{ event.fields.name_kor }}</p>
            <div class="status-event-score">
              <p v-if="event.fields.score_k < 100" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p v-else style="font-size:36px;" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p>:</p>
              <p v-if="event.fields.score_p < 100" class="status-event-postech-score">{{ event.fields.score_p }}</p>
              <p v-else style="font-size:36px;" class="status-event-postech-score">{{ event.fields.score_p }}</p>
            </div>
          </div>
          <div v-else-if="event.fields.winner == 2 && event.fields.type == 0" class="postech-win">
            <p class="status-event-name">{{ event.fields.name_kor }}</p>
            <div class="status-event-score">
              <p class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p>:</p>
              <p class="status-event-postech-score">{{ event.fields.score_p }}</p>
            </div>
          </div>
          <div v-else-if="event.fields.type == 0" class="none-win">
            <p class="status-event-name">{{ event.fields.name_kor }}</p>
            <div class="status-event-score">
              <p v-if="event.fields.score_k < 100" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p v-else style="font-size:36px;" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p>:</p>
              <p v-if="event.fields.score_p < 100" class="status-event-postech-score">{{ event.fields.score_p }}</p>
              <p v-else style="font-size:36px;" class="status-event-postech-score">{{ event.fields.score_p }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="supporters-recruit noto-sans">
      <p class="title">서포터가 되어주세요!</p>
      <div>
        <img src="static/images/supporters.svg" alt="supporters" width="300" height="230"> 
        <p>어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      scrolled: false,
      events: [],
      messageContent: '',
      messageTeam: '',
      messageEvent: ''
    }
  },
  created () {
    this.$http.get('/api/events')
      .then((response) => {
        this.events = JSON.parse(response.data)
        console.log(this.events)
      })
    this.$http.get('/api/cheermessage')
      .then((response) => {
        this.message = JSON.parse(response.data)[0]
        console.log(this.message)
        console.log(this.message.fields.school)
        this.messageContent = this.message.fields.content
        if (this.message.fields.school === 1) {
          this.messageTeam = 'KAIST'
        } else {
          this.messageTeam = 'POSTECH'
        }
        if (this.message.fields.event === 1) {
          this.messageEvent = '축구'
        } else if (this.message.fields.event === 2) {
          this.messageEvent = '야구'
        }
      })
  },
  mounted () {
    this.scrolled = window.scrollY
    console.log(this.scrolled)
    document.getElementById('nav-bar').style.top = '623px'
    document.getElementById('sidebar-wrapper').style.top = '767px'
  },
  computed () {
  },
  methods: {
  },
  updated () {
    let statusEvents = document.getElementsByClassName('status-event')
    for (let i in statusEvents) {
      if (!statusEvents[i].children[0]) {
        statusEvents[i].style.display = 'none'
      }
    }
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}

</script>

<style>
html, body {
  color: black;
}

.contents {
  margin: 767px auto 0 auto;
}

.image {
  position: absolute !important;
  left: 0;
  top: 0;
  height: 623px;
  width: 100%;
  background-image: url('/static/images/home.png');
  background-size: cover;
  background-position: 50% 50%;
  text-align: center;
  display: flex !important;
  flex-direction: column;
  justify-content: center;
  padding: 0;
  box-shadow: 0 3px 7px rgb(20,20,50);
  z-index:2;
}

.current-cheer-message {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

.current-cheer-message > div{
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.current-cheer-message > div > p{
  align-self: flex-end;
  font-size: 35px;
  margin: 0 10px;
  font-weight: 300;
}

.current-cheer-message > div > img{
  height: 35px !important;
}

.current-cheer-message > p {
  font-size: 26px;
  font-weight: 300;
}

.current-cheer-message > p > span {
  font-weight: 500;
}

.th {
  font-size: 34px;
}

#nav-bar {
  top: 623px;
}

#home > p > .fa {
  color: rgb(70, 122, 184);
}

.title {
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 10px;
  color: black !important;
}

#to-cheer-message > p{
  font-size: 30px;
  margin-top: -75px;
  float: right;
  width:350px;
  color: black;
}

.events-status {
  margin: 90px auto 0 auto;
}

.events-status > div {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
}

.status-event {
  width: 20%;
  margin-right: 5px;
  margin-bottom: 10px;
}

.status-event > div{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.kaist-win {
  background-color: rgb(95, 182, 235);
}

.postech-win {
  background-color: rgb(255, 87, 151);
}

.none-win {
  background-color: rgb(242, 242, 242);
}

.status-event-name {
  text-align: center;
  font-size: 46px;
  margin-bottom: -15px;
}

.status-event-score {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  font-size: 60px;
}

.supporters-recruit {
  margin-top: 90px;
}

.supporters-recruit > div > img{
  float: left;
}

.supporters-recruit > div > p {
  display: inline;
  left: 350px;
  font-size: 32px;
}

</style>
