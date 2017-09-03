<template>
  <div id="event" class="noto-sans">
    <router-link :to="{ 'name': 'introduction' }" id="to-intro"></router-link>
    <div id="event-name">
      {{ event.fields.name_kor }} {{ event.fields.name_eng }}
    </div> 
    <div class="team">
      <p>KAIST</p>
      <p>POSTECH</p>
    </div>
    <div class="score">
      <div v-if="event.fields.score_k < 100" class="kaist-score">
        {{ event.fields.score_k }}
      </div>
      <div v-else style="font-size:70px;" class="kaist-score">
        {{ event.fields.score_k }}
      </div>
      <p class="vs">:</p>
      <div v-if="event.fields.score_p < 100" class="postech-score">
        {{ event.fields.score_p }}
      </div>
      <div v-else style="font-size:70px;" class="postech-score">
        {{ event.fields.score_p }}
      </div>
      <p class="winner-is">winner is...
      <span v-if="event.fields.winner == 0" class="winner-team none">TBD</span>
      <span v-if="event.fields.winner == 1" class="winner-team kaist">KAIST</span>
      <span v-else-if="event.fields.winner == 2" class="winner-team postech">POSTECH</span> 
      <router-link :to="{ name: 'videos' }" class="to-video">
        <br>경기 보러가기
        <i class="fa fa-youtube-play"></i>
      </router-link>
      </p>
    </div>
    <div class="time"><i class="fa fa-clock-o"></i>일시<span>{{ day }} {{ startTimeH }}:{{ startTimeM }}~{{ endTimeH }}:{{ endTimeM }}</span>
    </div>
    <div class="location"><i class="fa fa-map-marker"></i>위치<span>{{ locations[event.fields.location] }}</span>
      <div class="chevron" v-on:click="location()"><i class="fa fa-chevron-down"></i></div> 
      <div class="location-picture"></div>
    </div>
    <div class="player"><i class="fa fa-user"></i>선수단 목록
      <div v-on:click="player()" class="chevron"><i class="fa fa-chevron-down"></i></div>
      <div class="player-detail">
        <div>
          <div class="team-kaist">KAIST</div>
          <div class="players-list">
            <p v-for="player in playersK" class="">{{ player.fields.name }}</p>
          </div>
        </div>
        <div>
          <div class="team-postech">POSTECH</div>
          <div class="players-list">
            <p v-for="player in playersP" class="">{{ player.fields.name }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="cheer-message">
      <p>응원의 메시지</p>
      <router-link :to="{ name: 'cheermessage' }"><p>나도 한 마디<img src="/static/images/message.png" width="60"></p></router-link>
      <div class="messages">
        <p v-if="messages[0]">{{ messages[0].fields.content }}
        <span v-if="messages[0].fields.school == 1">to. KAIST</span>
        <span v-if="messages[0].fields.school == 2">to. POSTECH</span>
        </p>
        <p v-if="messages[1]">{{ messages[1].fields.content }}
        <span v-if="messages[1].fields.school == 1">to. KAIST</span>
        <span v-if="messages[1].fields.school == 2">to. POSTECH</span>
        </p>
        <p v-if="messages[2]">{{ messages[2].fields.content }}
        <span v-if="messages[2].fields.school == 1">to. KAIST</span>
        <span v-if="messages[2].fields.school == 2">to. POSTECH</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'event',
  data () {
    return {
      event: {},
      playersK: [],
      playersP: [],
      messages: [],
      locations: [],
      mapList: []
    }
  },
  created () {
    this.fetchData()
    this.locations = ['E11 창의학습관', 'W9 노천극장', 'N3 스포츠 컴플렉스', 'E17 운동장', 'N13 앞 학부운동장']
    this.mapList = ['map_E11, Creative Learning Building.png', 'map_W9, Outdoor Theater.png', 'map_N3, Sports Complex.png', 'map_E17, Stadium.png', 'map_In Front of N3, Main Playground.png']
  },
  watch: {
    '$route': 'fetchData'
  },
  mounted () {
  },
  updated () {
  },
  methods: {
    fetchData () {
      if (!((this.$route.params.id < 9 && this.$route.params.id > 2) || (this.$route.params.id === 11))) {
        document.getElementById('to-intro').click()
      }
      let uri = '/api/events/' + this.$route.params.id + '/'
      this.$http.get(uri)
        .then((response) => {
          this.event = JSON.parse(response.data)[0]
          let res = this.event.fields.start_time.split('T')
          this.day = res[0][6] + '월 ' + res[0].slice(8, 10) + '일'
          this.startTimeH = res[1].split('Z')[0].split(':')[0]
          this.startTimeM = res[1].split('Z')[0].split(':')[1]
          this.endTimeH = this.event.fields.end_time.split('T')[1].split('Z')[0].split(':')[0]
          this.endTimeM = this.event.fields.end_time.split('T')[1].split('Z')[0].split(':')[1]
          this.$http.get('/api/events/' + this.$route.params.id + '/players-k/')
            .then((response) => {
              this.playersK = JSON.parse(response.data)
            })
          this.$http.get('/api/events/' + this.$route.params.id + '/players-p/')
            .then((response) => {
              this.playersP = JSON.parse(response.data)
            })
          this.$http.get('/api/events/' + this.$route.params.id + '/messages/')
            .then((response) => {
              this.messages = JSON.parse(response.data)
              document.getElementsByClassName('location-picture')[0].style.background = "url('/static/images/" + this.mapList[this.event.fields.location] + "')"
            })
        })
    },
    location () {
      if (document.getElementsByClassName('location-picture')[0].style.height === '280px') {
        document.getElementsByClassName('location-picture')[0].style.height = '0'
        document.getElementsByClassName('location-picture')[0].style.display = 'none'
      } else {
        document.getElementsByClassName('location-picture')[0].style.height = '280px'
        document.getElementsByClassName('location-picture')[0].style.display = 'block'
      }
    },
    player () {
      if (document.getElementsByClassName('player-detail')[0].style.display === 'none') {
        document.getElementsByClassName('player-detail')[0].style.display = 'flex'
      } else {
        document.getElementsByClassName('player-detail')[0].style.display = 'none'
      }
    }
  }
}
</script>

<style>
html, body {
}

#event-name {
  position: absolute;
  left: 0;
  top: 144px;
  width: 100%;
  height: 100px;
  background-color: rgb(149, 179, 215);
  text-align: center;
  font-size: 67px;
  font-weight: 700;
  color: white;
  box-shadow: 0 3px 7px rgb(130 ,130, 130);
}

#event {
  padding-left: 15px;
}

.team {
  display: flex;
  flex-direction: row;
  margin-left: 100px;
}

.team > p {
  font-size: 36px;
}

.team > p:nth-child(1) {
  margin-right: 50px;
}

.team > p:nth-child(2) {
  margin-left: 30px;
}

.score {
  display: flex;
  flex-direction: row;
}

.vs {
  color: rgb(149, 179, 215);
  font-size: 110px;
  margin: 0 20px;
}

.score > div {
  width: 200px;
  height: 200px;
  background-color: rgb(242, 242, 242);
  border-radius: 20px;
  text-align: center;
  line-height: 180px;
  font-size: 140px;
  font-weight: 800;
}

.winner-is {
  margin-top: -30px;
  margin-left: 50px;
  width: 300px;
  font-size: 40px;
}

.winner-team {
  margin-top: -50px;
  font-size: 72px;
  font-weight: 800;
}

.winner-team.none {
  color: rgb(215, 215, 215);
}

.winner-team.kaist {
  color: rgb(42, 158, 229);
}

.winner-team.postech {
  color: rgb(255, 87, 151);
}

.to-video {
  margin-left: -10px;
  font-weight: 600;
  color: black;
}

.to-video > i {
  margin-top: 8px;
  color: rgb(148, 40, 37);
}

.time {
  margin-top: 30px;
  font-size: 40px;
  font-weight: 500;
}

.time > i {
  margin-top: 8px;
  margin-right: 10px;
  font-size: 40px !important;
}

.time > span {
  margin-left: 30px;
  font-weight: 400;
}

.location {
  padding-top: 10px;
  font-size: 40px;
  font-weight: 500;
}

.location > i {
  margin-top: 8px;
  margin-left: 7px;
  margin-right: 13px;
  font-size: 40px !important;
}

.location > span {
  margin-left: 30px;
  font-weight: 400;
}

.player {
  padding-top: 5px;
  font-size: 40px;
  font-weight: 500;
}

.player > i {
  margin-top: 8px;
  margin-left: 2px;
  margin-right: 12px;
  font-size: 40px !important;
}

.chevron {
  text-align: right;
  margin-top: -50px;
  margin-bottom: -5px;
  width: 800px;
  cursor: pointer;
}

.location-picture {
  width: 628px;
  height: 0px;
  display: none;
  margin: 0 0 0 40px;
  margin-bottom: 20px;
}

.team-kaist {
  color: rgb(42, 158, 229);
  padding: 0 5px;
  background-color: white;
}

.team-postech {
  color: rgb(255, 87, 151);
  text-align: right;
  padding: 0 5px;
  background-color: white;
}

.players-list {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  background-color: rgb(242, 242, 242);
  padding: 0 5px;
  width: 100%;
  font-size: 30px; 
}

.player-detail > div:nth-child(1) > .players-list {
  border-radius: 0 0 0 5px;
  display: flex;
  justify-content: flex-start;
  flex-wrap: wrap;
}

.player-detail > div:nth-child(2) > .players-list {
  border-radius: 0 0 5px 0;
  display: flex;
  justify-content: flex-end;
  flex-wrap: wrap;
}

.players-list > p {
  margin: 0 5px;
}

.player-detail {
  display: none;
  border: 2px solid rgb(242, 242, 242);
  background-color: rgb(242, 242, 242);
  border-radius: 10px;
  width: 800px;
  font-size: 30px;
  flex-direction: row;
}

.player-detail > div{
  width: 50%;
}

.cheer-message {
  padding-top: 40px;
  width: 800px;
}

.cheer-message > p:nth-child(1) {
  font-size: 40px;
}

.cheer-message > a > p {
  font-size: 30px;
  float: right;
  margin-top: -50px;
  color: black;
  width: 230px;
}

.cheer-message > a > p > img {
  margin: 0 0 -15px 0;
}

.messages {
  margin-top: 10px;
  font-weight: 200;
}

.messages > p {
  font-size: 30px;
  padding: 0 10px;
  width: 780px;
}

.messages > p:nth-child(odd) {
  background-color: rgb(242, 242, 242);
  border-radius: 10px;
}

.messages > p > span{
  float: right;
  width: 200px;
}
</style>
