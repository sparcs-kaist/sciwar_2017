<template>
  <div class="event noto-sans">
    <div id="event-name">
      {{ event.fields.name_kor }} {{ event.fields.name_eng }}
    </div> 
    <div class="team">
      <p>KAIST</p>
      <p>POSTECH</p>
    </div>
    <div class="score">
      <div class="kaist-score">
        {{ event.fields.score_k }}
      </div>
      <p class="vs">:</p>
      <div class="postech-score">
        {{ event.fields.score_p }}
      </div>
      <p class="winner-is">winner is...
      <span v-if="event.fields.winner == 1" class="winner-team kaist">KAIST</span>
      <span v-else-if="event.fields.winner == 2" class="winner-team postech">POSTECH</span> 
      <router-link :to="{ name: 'album' }" class="to-video">
        <br>경기 보러가기
        <i class="fa fa-youtube-play"></i>
      </router-link>
      </p>
    </div>
    <div class="time"><i class="fa fa-clock-o"></i>일시<span>{{ day }} {{ startTimeH }}:{{ startTimeM }} - {{ endTimeH }}:{{ endTimeM }}</span>
    </div>
    <div class="location"><i class="fa fa-map-marker"></i>위치<span>{{ event.fields.location }}</span>
      <div class="chevron" v-on:click="location()"><i class="fa fa-chevron-down"></i></div> 
      <img class="location-picture" width="500">
    </div>
    <div class="player"><i class="fa fa-user"></i>선수단 목록
      <div class="chevron"><i class="fa fa-chevron-down"></i></div>
      <div class="team-kaist">KAIST</div>
      <p v-for="player in playersK" class="player-list">{{ player.fields.name }}</p>
      <div class="team-postech">POSTECH</div>
      <p v-for="player in playersP" class="player-list">{{ player.fields.name }}</p>
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
      playersP: []
    }
  },
  created () {
    this.fetchData()
    console.log(document.getElementsByClassName('fa-chevron-down'))
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
      let uri = '/api/events/' + this.$route.params.id
      console.log(uri)
      this.$http.get(uri)
        .then((response) => {
          this.event = JSON.parse(response.data)[0]
          console.log(this.event)
          let res = this.event.fields.start_time.split('T')
          this.day = res[0]
          this.startTimeH = res[1].split('Z')[0].split(':')[0]
          this.startTimeM = res[1].split('Z')[0].split(':')[1]
          this.endTimeH = this.event.fields.end_time.split('T')[1].split('Z')[0].split(':')[0]
          this.endTimeM = this.event.fields.end_time.split('T')[1].split('Z')[0].split(':')[1]
          this.$http.get('/api/events/' + this.$route.params.id + '/players-k')
            .then((response) => {
              this.playersK = JSON.parse(response.data)
              console.log('playersK', this.playersK)
            })
          this.$http.get('/api/events/' + this.$route.params.id + '/players-p')
            .then((response) => {
              this.playersP = JSON.parse(response.data)
              console.log('playersP', this.playersP)
            })
        })
    },
    location () {
      if (document.getElementsByClassName('location-picture')[0].style.height === '400px') {
        document.getElementsByClassName('location-picture')[0].style.height = '0'
        document.getElementsByClassName('location-picture')[0].style.display = 'none'
      } else {
        document.getElementsByClassName('location-picture')[0].style.height = '400px'
        document.getElementsByClassName('location-picture')[0].style.display = 'block'
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
  color: white;
  box-shadow: 0 3px 7px rgb(130 ,130, 130);
}

.team {
  display: flex;
  flex-direction: row;
  margin-left: 80px;
}

.team > p {
  font-size: 24px;
}

.team > p:nth-child(1) {
  margin-right: 25px;
}

.team > p:nth-child(2) {
  margin-left: 25px;
}

.score {
  display: flex;
  flex-direction: row;
}

.vs {
  color: rgb(149, 179, 215);
  font-size: 72px;
  margin: 0 11px;
}

.score > div {
  width: 150px;
  height: 150px;
  background-color: rgb(242, 242, 242);
  border-radius: 20px;
  text-align: center;
  line-height: 135px;
  font-size: 96px;
  font-weight: 800;
}

.winner-is {
  margin-left: 30px;
  width: 200px;
  font-size: 26px;
}

.winner-team {
  font-size: 48px;
  font-weight: 800;
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
  font-size: 26px;
  font-weight: 500;
}

.time > i {
  margin-top: 8px;
  margin-right: 10px;
}

.time > span {
  margin-left: 30px;
}

.location {
  font-size: 26px;
  font-weight: 500;
}

.location > i {
  margin-top: 8px;
  margin-left: 4px;
  margin-right: 13px;
}

.location > span {
  margin-left: 30px;
}

.player {
  font-size: 26px;
  font-weight: 500;
}

.player > i {
  margin-top: 8px;
  margin-left: 2px;
  margin-right: 12px;
}

.chevron {
  text-align: right;
  margin-top: -35px;
  margin-bottom: -5px;
  width: 500px;
  cursor: pointer;
}

.location-picture {
  height: 0px;
  display: none;
}
</style>
