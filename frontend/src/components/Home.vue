<template>
  <div class="home">
    <div class="image">
      <p class="noto-sans big">2018 SCIENCE WAR</p>
      <p class="kopub">카이스트포스텍학생대제전</p>
      <p class="noto-sans small">SEP. 14 - 15<sup class="th"> rd</sup> POSTECH</p>
    </div>
    <div class="current-cheer-message noto-sans">
      <div>
        <img src="/static/images/quote1.png" width="35" height="35">
        <p id="current-cheer-message">{{ messageContent }}</p>
        <img src="/static/images/quote2.png" width="35" height="35">
      </div>
      <p><span>to. </span>{{ messageTeam }}</p>
      <p><span>about. </span>{{ messageEvent }}</p>
    </div>
    <div class="events-status noto-sans">
      <p class="title">경기 현황</p>
      <div>
        <div v-for="event in events" class="status-event">
          <div v-if="event.fields.winner == 1 && (event.fields.type == 0 || event.fields.type == 1) && event.fields.live == 2" class="kaist-win">
            <p class="status-event-name">{{ event.fields.name_kor }}</p>
            <div class="status-event-score">
              <p v-if="parseInt(event.fields.score_k) < 100" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p v-else style="font-size:36px;" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p>:</p>
              <p v-if="parseInt(event.fields.score_p) < 100" class="status-event-postech-score">{{ event.fields.score_p }}</p>
              <p v-else style="font-size:36px;" class="status-event-postech-score">{{ event.fields.score_p }}</p>
            </div>
          </div>
          <div v-else-if="event.fields.winner == 2 && (event.fields.type == 0 || event.fields.type == 1) && event.fields.live == 2" class="postech-win">
            <p class="status-event-name">{{ event.fields.name_kor }}</p>
            <div class="status-event-score">
              <p v-if="parseInt(event.fields.score_k) < 100" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p v-else style="font-size:36px;" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p>:</p>
              <p v-if="parseInt(event.fields.score_p) < 100" class="status-event-postech-score">{{ event.fields.score_p }}</p>
              <p v-else style="font-size:36px;" class="status-event-postech-score">{{ event.fields.score_p }}</p>
            </div>
          </div>
          <div v-else-if="(event.fields.type == 0 || event.fields.type == 1) && event.fields.live == 1" class="none-win">
            <p class="status-event-name">{{ event.fields.name_kor }}</p>
            <div class="status-event-score">
              <p v-if="event.fields.score_k < 100" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p v-else style="font-size:36px;" class="status-event-kaist-score">{{ event.fields.score_k }}</p>
              <p>:</p>
              <p v-if="event.fields.score_p < 100" class="status-event-postech-score">{{ event.fields.score_p }}</p>
              <p v-else style="font-size:36px;" class="status-event-postech-score">{{ event.fields.score_p }}</p>
            </div>
          </div>
          <div v-else-if="(event.fields.type == 0 || event.fields.type == 1) && event.fields.live == 0" class="not-yet">
            <p class="status-event-name">{{ event.fields.name_kor }}</p>
            <p class="not-yet-date">{{ event.fields.start_time[6] }}월 {{ event.fields.start_time.slice(8,10) }}일</p>
            <p class="not-yet-time">{{ event.fields.start_time.slice(11,13) }}시 {{ event.fields.start_time.slice(14,16) }}분</p>
          </div>
        </div>
      </div>
    </div>
    <div class="supporters-recruit noto-sans">
      <p class="title">서포터즈가 되어주세요!</p>
      <div>
        <div><img src="static/images/supporters.svg" alt="supporters" width="200" height="200"></div>
        <p>하나! 공식 티셔츠 및 각종 응원도구 제공 Offering official T-shirts and various cheering tools<br>둘! 포스텍까지 왕복 버스 지원 및 숙소지원 Round-trip bus support to Postech and accommodation support<br>셋! 한정 기념품 및 신청자 한정 추첨 상품 Qualified souvenirs and applicants limited draw prizes<br>넷! 서포터즈만을 위한 특별 이벤트 Special events for supporters only<br>다섯! 서포터즈들에게 마일리지 점수 제공 Providing mileage points to supporters<br />서포터즈의 역할을 메뉴의 '서포터즈' 버튼을 눌러 확인하시고 신청해 주세요. Apply after checking the role of the supporters by pressing the "Supporters" button on the menu.</p>
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
      message: {}
    }
  },
  computed: {
    messageContent () {
      if (this.message.hasOwnProperty('fields')) {
        if (this.message.fields.content.length < 30) {
          document.getElementById('current-cheer-message').style.width = '300px'
        }
        return this.message.fields.content
      }
      return ''
    },
    messageTeam () {
      if (this.message.hasOwnProperty('fields')) {
        if (this.message.fields.school === 1) {
          return 'KAIST'
        } else {
          return 'POSTECH'
        }
      }
      return ''
    },
    messageEvent () {
      if (this.message.hasOwnProperty('fields')) {
        if (this.message.fields.hasOwnProperty('event')) {
          for (let event of this.events) {
            if (this.message.fields.event === event.pk) {
              return event.fields.name_kor
            }
          }
        }
        return '모두에게'
      }
      return ''
    }
  },
  created () {
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
      })
    this.$http.get('/api/cheermessage/')
      .then((response) => {
        this.message = JSON.parse(response.data)[0]
        // if (this.message.fields.event === 3) {
        //   this.messageEvent = '축구'
        // } else if (this.message.fields.event === 4) {
        //   this.messageEvent = '인공지능'
        // } else if (this.message.fields.event === 5) {
        //   this.messageEvent = '롤'
        // } else if (this.message.fields.event === 6) {
        //   this.messageEvent = '야구'
        // } else if (this.message.fields.event === 7) {
        //   this.messageEvent = '과학퀴즈'
        // } else if (this.message.fields.event === 8) {
        //   this.messageEvent = '농구'
        // } else if (this.message.fields.event === 10) {
        //   this.messageEvent = '모두에게'
        // } else if (this.message.fields.event === 11) {
        //   this.messageEvent = '해킹'
        // }
      })
  },
  mounted () {
    this.scrolled = window.scrollY
    document.getElementById('nav-bar').style.top = '623px'
    document.getElementById('sidebar-wrapper').style.top = '767px'
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

<style scoped>
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

.current-cheer-message > div > p {
  word-spacing: 1px;
  font-size: 35px;
  margin: auto;
  font-weight: 300;
  text-align: center;
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
  height: 144px;
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

.not-yet {
  background-color: rgb(242, 242, 242);
}

.not-yet-date {
  margin-top: 5px;
  font-size: 30px;
  text-align: center;
}

.not-yet-time {
  font-size: 30px;
  text-align: center;
  margin-top: -10px;
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

.supporters-recruit > div > div {
  margin-top: -10px;
  align-items: center;
  align-content: center;
  justify-content: center;
}

.supporters-recruit > div > div > img {
  align-self: center;
  margin-left: 350px;
}

.supporters-recruit > div > p {
  display: inline;
  left: 350px;
  font-size: 30px;
  word-break: keep-all;
  text-align: justify;
}

</style>
