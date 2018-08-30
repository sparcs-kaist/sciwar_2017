<template>
  <div class="container">
    <div id="nav-bar">
      <div class="block">
        <div class="navbar-name kaist">
          KAIST
        </div>
        <p id="kaist-score"></p>
        <div class="navbar-name postech">
          POSTECH
        </div>
        <p id="postech-score"></p>
        <div class="navbar-name today">
          TODAY
        </div>
        <div class="events">
          <div class="navbar-name" v-on:click="moveLeft()">
            <i class="fa fa-chevron-left" aria-hidden="ture"></i>
          </div>
          <div class="navbar-event-name">
            <div v-if="eventsRendered[currentIndex]">
              <router-link :to="{ name: 'event', params: { id: eventsRendered[currentIndex].pk } }">{{ eventsRendered[currentIndex].fields.name_kor }}</router-link>
              <router-link v-if="videosRendered[currentIndex] != 0" :to="{ name: 'video', params: { id: videosRendered[currentIndex].pk } }" class="to-streaming">LIVE</router-link>
            </div>
          </div>
          <div class="navbar-name" v-on:click="moveRight()">
            <i class="fa fa-chevron-right" aria-hidden="ture"></i>
          </div>
        </div>
      </div>
    </div>
    <div class="contents">
      <div id="sidebar-wrapper">
        <p id="menu">MENU</p>
        <div id="sidebar-left">
          <a class="button">
            <div class="menu-images">
              <img src="/static/images/sciwar.png" width="35">
            </div>
            <p>
            Kapo-Jeon?
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></a>
          <router-link :to="{ name: 'schedule' }" class="button">
            <div class="menu-images">
              <img src="/static/images/schedule.png" width="35">
            </div>
            <p>
            Schedule
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
          <router-link :to="{ name: 'supporters' }" class="button">
            <div class="menu-images">
              <img src="/static/images/supporters.svg" width="50">
            </div>
            <p>
            Supporters
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
          <router-link :to="{ name: 'toto' }" class="button">
            <div class="menu-images">
              <img src="/static/images/toto.png" width="35">
            </div>
            <p>
            Lottery
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
          <router-link :to="{ name: 'map' }" class="button">
            <div class="menu-images">
              <img src="/static/images/map.png" width="50">
            </div>
            <p>
            Map
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
          <router-link :to="{ name: 'videos' }" class="button">
            <div class="menu-images">
              <img src="/static/images/image.png" width="35">
            </div>
            <p>
            Videos
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
            <router-link :to="{ name: 'cheermessage' }" class="button">
              <div class="menu-images">
                <img src="/static/images/message.png" width="50">
              </div>
              <p>
              Comments
                <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
              </p></router-link>
        </div>
        <div id="home-top">
          <router-link :to="{ name: 'home' }">
            <div id="home">
              <p>
                <i class="fa fa-chevron-left home" aria-hidden="ture"></i>
                HOME
              </p>
            </div>
          </router-link>
        </div>
      </div>
      <div class="logos">
        <p>주관 및 후원</p>
        <img src="/static/images/netmarble.PNG" class="logo" width="300" height="100" />
        <img src="/static/images/imgeffectlogo.png" class="logo" width="300" height="100" />
        <img src="/static/images/WideKAPOlogo.png" class="logo" width="300" height="100" />
      </div>
      <div id="submenu">
        <div class="event-list">
          <div>
            <router-link :to="{ name: 'introduction' }">
              <div class="menu-images">
                <img src="/static/images/sciwar.png" width="25" style="margin:6px 10px 0 5px">
              </div>
              <p class="submenu-event-name">
                카포전 소개
                <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
              </p>
            </router-link>
          </div>
        </div>
        <div class="event-list">
          <div>
            <router-link :to="{ name: 'intro-sports' }">
              <div class="menu-images">
                <img v-bind:src="'/static/images/face.png'" width="30px" style="margin:5px 8px 0 4px;">
              </div>
              <p class="submenu-event-name">
                운동 경기
                <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
              </p>
            </router-link>
          </div>
        </div>
        <div class="event-list">
          <div>
            <router-link :to="{ name: 'intro-science' }">
              <div class="menu-images">
                <img v-bind:src="'/static/images/questionmark.png'" width="22" style="margin:7px 10px 0 5px;">
              </div>
              <p class="submenu-event-name">
                과학 경기
                <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
              </p>
            </router-link>
          </div>
        </div>
      </div>
      <div class="main">
        <router-view name="contents"></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      events: [],
      eventsRendered: [],
      videos: [],
      videosRendered: [],
      currentIndex: 0,
      kaistScore: 0,
      postechScore: 0
    }
  },
  created () {
    window.addEventListener('click', this.submenu)
    window.addEventListener('resize', this.submenuLeft)
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
        this.renderEvent()
      })
  },
  mounted () {
    this.relocateContents()
  },
  updated () {
    this.relocateContents()
  },
  methods: {
    submenu (event) {
      let button = document.getElementsByClassName('button')[0]
      if ((event.target === button || event.target.parentNode === button || event.target.parentNode.parentNode === button)) {
        document.getElementById('submenu').style.display = 'block'
      } else {
        document.getElementById('submenu').style.display = 'none'
      }
    },
    submenuLeft (event) {
      let left = document.getElementById('sidebar-wrapper').offsetLeft + 300 + 'px'
      document.getElementById('submenu').style.left = left
    },
    renderEvent () {
      this.eventRendered = new Array(0)
      this.today = new Date()
      this.dd = this.today.getDate()
      this.mm = this.today.getMonth() + 1
      this.yyyy = this.today.getFullYear()
      if (this.dd < 10) {
        this.dd = '0' + this.dd
      }
      if (this.mm < 10) {
        this.mm = '0' + this.mm
      }
      this.today = this.yyyy + '-' + this.mm + '-' + this.dd
      for (let i in this.events) {
        if (this.events[i].fields.winner === 1 && this.events[i].fields.live === 2) {
          this.kaistScore += 1
        } else if (this.events[i].fields.winner === 2 && this.events[i].fields.live === 2) {
          this.postechScore += 1
        }
        if (this.today === this.events[i].fields.start_time.slice(0, 10)) {
          this.eventsRendered.push(this.events[i])
        }
      }
      this.$http.get('/api/videos/')
        .then((response) => {
          this.videos = JSON.parse(response.data)
          this.videosRendered = new Array(0)
          for (let i = 0; i < this.eventsRendered.length; i++) {
            this.videosRendered.push(0)
          }
          for (let x in this.eventsRendered) {
            if (this.eventsRendered[x].fields.live === 0) {
              continue
            } else if (this.eventsRendered[x].fields.live === 1) {
              for (let video of this.videos) {
                if (video.fields.event.indexOf(this.eventsRendered[x].pk) > -1 && video.fields.type === 0) {
                  this.videosRendered[x] = video
                  break
                }
              }
            }
          }
        })
    },
    moveLeft () {
      if (this.currentIndex > 0) {
        this.currentIndex--
      } else if (this.currentIndex === 0) {
        this.currentIndex = this.eventsRendered.length - 1
      }
    },
    moveRight () {
      if (this.currentIndex < this.eventsRendered.length - 1) {
        this.currentIndex++
      } else if (this.currentIndex === this.eventsRendered.length - 1) {
        this.currentIndex = 0
      }
    },
    relocateContents () {
      let left = document.getElementById('sidebar-wrapper').offsetLeft + 290 + 'px'
      document.getElementById('submenu').style.left = left
      if (document.getElementsByClassName('image')[0]) {
        document.getElementsByClassName('contents')[0].style.margin = '767px auto 0 auto'
        document.getElementById('submenu').style.top = '865px'
        document.getElementsByClassName('logos')[0].style.top = '1470px'
      } else if (this.$route.params.id && this.$route.name === 'event') {
        // document.getElementsByClassName('contents')[0].style.margin = '767px auto 0 auto'
        document.getElementsByClassName('contents')[0].style.margin = '244px auto 0 auto'
        document.getElementById('submenu').style.top = '342px'
        document.getElementById('nav-bar').style.top = '0px'
        document.getElementById('sidebar-wrapper').style.top = '244px'
        document.getElementsByClassName('logos')[0].style.top = '947px'
      } else {
        document.getElementsByClassName('contents')[0].style.margin = '144px auto 0 auto'
        document.getElementById('submenu').style.top = '242px'
        document.getElementById('nav-bar').style.top = '0px'
        document.getElementById('sidebar-wrapper').style.top = '144px'
        document.getElementsByClassName('logos')[0].style.top = '847px'
      }
      document.getElementById('kaist-score').innerHTML = this.kaistScore
      document.getElementById('postech-score').innerHTML = this.postechScore
    }
  }
}
</script>

<style lang="sass" src="bulma"></style>
<style>
@import '../node_modules/@fortawesome/fontawesome-free/css/all.css';
@import '../static/global.css';
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);
@import url(//cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css);

html {
  height: 100%;
  overflow-y: hidden !important;
  color: black;
}

body {
  overflow-x: scroll !important;
  height: 100%;
  color: black;
}

.fixed {
  position: fixed !important;
}

.noto-sans {
  font-family: 'Noto Sans KR', sans-serif;
}

.noto-sans.big {
  font-size: 64px;
  font-weight: 900;
  letter-spacing: 10.3px;
  word-spacing: -3px;
  color: white;
}

.kopub {
  color: white;
  font-family: 'KoPub Dotum';
  font-size: 109px;
  letter-spacing: 12.8px;
  font-weight: 900;
  text-shadow: 2px 2px 2px black;
}

.noto-sans.small {
  font-size: 50px;
  font-weight: 900;
  letter-spacing: 0px;
  word-spacing: -3px;
  color: white;
}
</style>

<style scoped>
.container {
  overflow-y: initial;
  width: 100% !important;
  max-width: 100% !important;
  min-width: 1295px;
  height: 100%;
  margin: 0 !important;
  padding: 0 !important;
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
  color: black;
}

#nav-bar {
  text-align: left;
  width:100%;
  height: 144px;
  position: absolute;
  top: 0px;
  background-color: rgba(8,49,110,1);
  box-shadow: 0 3px 7px rgb(130,130,130);
  z-index:1;
}

.block {
  width: 1295px;
  margin: 18px auto 0 auto;
  display: flex;
  flex-direction: row;
  color: white;
  font-family: 'Noto Sans KR', sans-serif;
}

.block > p {
  margin: -30px 20px 0px 15px;
  font-size: 100px;
  font-weight: 700;
}

.navbar-name {
  padding: 0px 12px 2px 12px;
  background-color: rgb(6, 38, 86);
  border-radius: 7px;
  letter-spacing: 0.8px;
}

.navbar-name.kaist {
  font-size: 37px;
  font-weight: 300;
  height: 58px;
}

#kaist-score {
  margin-left: 30px;
  margin-right: 50px;
}

#postech-score {
  margin-left: 30px;
  margin-right: 50px;
}

.navbar-name.postech {
  font-size: 37px;
  font-weight: 300;
  height: 58px;
}

.events {
  width: 40%;
}

.navbar-name.today {
  font-size: 37px;
  font-weight: 300;
  height: 58px;
}

.to-streaming {
  border: none;
  font-size: 35px;
  padding: 3px 12px 5px 12px;
  font-weight: 600;
  cursor: pointer;
  background-color: rgb(188, 77, 77);
  color: white;
  vertical-align: middle;
  margin-left: 10px;
  margin-top: -5px;
}

.events {
  margin: 25px 0px 0px 12px;
  display: flex;
  flex-direction: row;
}

.events > .navbar-name {
  width: 30px;
  height: 55px;
  margin-top: 10px;
  cursor: pointer;
}

.events > .navbar-name > .fa {
  font-size: 25px;
  margin: 14px 0 0 -6px;
}

.navbar-event-name {
  margin: -15px 10px 0 10px;
  width: 500px;
  font-size: 60px;
  text-align: center;
  letter-spacing: -2px;
}

.navbar-event-name > div > a {
  color: white;
}

.contents {
  height: 100%;
  margin: 767px auto 0 auto;
  display: flex;
  justify-content: space-between;
  width:1295px;
  color: black;
}

#sidebar-wrapper {
  width: 300px;
  margin-top: 50px;
  position: absolute;
  color: black;
}

#menu {
  text-align: right;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 900;
  font-size: 32px;
  color: rgb(149,179,215);
}

#home-top {
  display:flex;
  flex-direction: row;
  justify-content: space-between;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 300;
  font-size: 26px;
}

#home-top > a {
  width: 50%;
}

#home-top > div {
  width: 50%;
}

#home {
  margin-top: 15px;
  color: black;
  width: 100%;
}

#home > p {
  width: 100%;
}

#home > p > .fa {
  width: 10%;
}

#home:hover > p > .fa {
  color: rgb(119, 149, 185);
}

#top > .fa {
  color: rgb(149, 179, 215);
}

#top:hover > .fa {
  color: rgb(119, 149, 185);
}

.fa.home {
  margin-top: 9px;
  color: rgb(149,179,215);
}

.fa.menu {
  font-size: 21px !important;
  margin-top: 8px;
  color: rgb(149,179,215);
  float: right;
}

a:hover > p > .fa {
  color: rgb(119, 149, 185);
}

#top {
  float: right;
  text-align: right;
}

#top:hover {
  cursor: pointer;
}

#sidebar-left {
  width: 300px;
  display: flex;
  flex-direction: column;
  background-color: rgba(242,242,242,1);
  padding: 20px 25px 5px 25px;
}

#sidebar-left > a {
  height: 60px;
  margin-bottom:15px;
  border: 0;
  border-radius: 0;
  font-weight: 400;
  font-size: 24px;
  padding-right: 5px;
}

#sidebar-left > a > p {
  text-align: left;
  width: 100%;
  margin-top: -4px;
  margin-left: 10px;
}

#sidebar-left > a:nth-child(3) > p {
  margin-left: 0px;
}

#sidebar-left > a:nth-child(3) > div {
  margin-left: -2px;
}

#sidebar-left > a:nth-child(5) > p {
  margin-left: 0px;
}

#sidebar-left > a:nth-child(5) > div {
  margin-left: -2px;
}

#sidebar-left > a:nth-child(7) > p {
  margin-left: -2px;
}

#sidebar-left > a:nth-child(7) > div {
  margin-left: -2px;
  margin-top: 4px;
}

#submenu {
  position: absolute;
  display: none;
  left: 590px;
  top: 865px;
  padding: 15px 15px 5px 15px;
  background-color: rgba(242,242,242,1);
  z-index: 10;
}

.logos {
  margin-top: 50px;
  font-size: 18px;
  filter: grayscale(0%);
  position: absolute;
  top: 1470px;
  display: flex;
  flex-direction: column;
}

.logo {
  margin-top: 15px;
}

.logo:nth-child(3) {
  margin-top: 20px;
  filter: invert(80%);
}

.logo:nth-child(4) {
  margin-top: 5px;
}

.event-list {
  width: 180px;
  margin-bottom: 10px;
}

.event-list > div > a {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  background-color: white;
  font-size: 20px;
  font-weight: 400;
  color: black;
  height: 40px;
}

.event-list > div > a > p {
  width: 100%;
  margin-top: 5px;
}

.event-list > div > a > div {
  margin: 3px 5px 0 5px;
}

.event-list > div > a > p > .fa.menu{
  float: right;
  margin-top: 4px;
  margin-right: 5px;
}

.menu-images {
  margin-top: 2px;
}

.main {
  margin-left: 300px;
  padding: 50px 0 0 50px;
  width: 945px;
}

img:not(.logo) {
  filter: grayscale(100%);
}
</style>
