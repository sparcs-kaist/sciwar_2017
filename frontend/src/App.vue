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
          <div class="navbar-name">
            <i class="fa fa-chevron-left" aria-hidden="ture"></i>
          </div>
          <div class="navbar-event-name">
            무슨무슨무 경기
          </div>
          <div class="navbar-name">
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
            카포전이란
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></a>
          <router-link :to="{ name: 'schedule' }" class="button">
            <div class="menu-images">
              <img src="/static/images/schedule.png" width="35">
            </div>
            <p>
            일정
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
          <router-link :to="{ name: 'supporters' }" class="button">
            <div class="menu-images">
              <img src="/static/images/supporters.svg" width="50">
            </div>
            <p>
            서포터즈
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
          <router-link :to="{ name: 'toto' }" class="button">
            <div class="menu-images">
              <img src="/static/images/toto.png" width="35">
            </div>
            <p>
            토토이벤트
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
          <router-link :to="{ name: 'map' }" class="button">
            <div class="menu-images">
              <img src="/static/images/map.png" width="50">
            </div>
            <p>
            지도
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
          <router-link :to="{ name: 'videos' }" class="button">
            <div class="menu-images">
              <img src="/static/images/image.png" width="35">
            </div>
            <p>
            비디오
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
      <div id="submenu">
        <div class="event-list" v-for="event in events">
          <router-link :to="{ name: 'event', params: { id: event.pk } }">
            <div class="menu-images">
              <img v-bind:src="'/static/images/' + event.fields.name_eng + '.png'" width="25" style="margin:6px 10px 0 5px;">
            </div>
            <p>
              {{ event.fields.name_kor }}
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p> 
          </router-link>
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
      events: []
    }
  },
  created () {
    window.addEventListener('click', this.submenu)
    window.addEventListener('resize', this.submenuLeft)
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
        this.kaistScore = 0
        this.postechScore = 0
        for (let i in this.events) {
          if (this.events[i].fields.winner === 1) {
            this.kaistScore += 1
          } else if (this.events[i].fields.winner === 2) {
            this.postechScore += 1
          }
        }
        document.getElementById('kaist-score').innerHTML = this.kaistScore
        document.getElementById('postech-score').innerHTML = this.postechScore
      })
  },
  updated () {
    let left = document.getElementById('sidebar-wrapper').offsetLeft + 300 + 'px'
    document.getElementById('submenu').style.left = left
    if (document.getElementsByClassName('image')[0]) {
      document.getElementsByClassName('contents')[0].style.margin = '767px auto 0 auto'
      document.getElementById('submenu').style.top = '865px'
    } else if (this.$route.params.id && this.$route.name === 'event') {
      document.getElementsByClassName('contents')[0].style.margin = '767px auto 0 auto'
      document.getElementsByClassName('contents')[0].style.margin = '244px auto 0 auto'
      document.getElementById('submenu').style.top = '342px'
      document.getElementById('nav-bar').style.top = '0px'
      document.getElementById('sidebar-wrapper').style.top = '244px'
    } else {
      document.getElementsByClassName('contents')[0].style.margin = '144px auto 0 auto'
      document.getElementById('submenu').style.top = '242px'
      document.getElementById('nav-bar').style.top = '0px'
      document.getElementById('sidebar-wrapper').style.top = '144px'
    }
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
    }
  }
}
</script>

<style lang="sass" src="bulma"></style>
<style>
@import '../node_modules/font-awesome/css/font-awesome.min.css';
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

.navbar-name.postech {
  font-size: 37px;
  font-weight: 300;
  height: 58px;
}

.navbar-name.today {
  font-size: 37px;
  font-weight: 300;
  height: 58px;
  margin-left: 5px;
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

.contents {
  height: 100%;
  margin: 144px auto 0 auto;
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

#submenu {
  position: absolute;
  display: none;
  left: 300px;
  top: 242px;
  padding: 15px 15px 5px 15px;
  background-color: rgba(242,242,242,1);
  z-index:1;
}

.event-list {
  width: 180px;
  margin-bottom: 10px;
}

.event-list > a{
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

.event-list > a > p {
  width: 100%;
  margin-top: 5px;
} 

.event-list > a > p > .fa.menu{
  float: right;
  margin-top: 4px;
}

.menu-images {
  margin-top: 2px;
}

.main {
  margin-left: 300px;
  padding: 50px 0 0 50px;
  width: 945px;
}

img {
  filter: grayscale(100%);
}
</style>
