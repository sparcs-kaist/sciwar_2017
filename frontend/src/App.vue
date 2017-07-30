<template>
  <div class="container">
    <div class="image">
      <p class="noto-sans big">2017 SCIENCE WAR</p>
      <p class="kopub">카이스트포스텍학생대제전</p>
      <p class="noto-sans small">OCT. 15 - 17<sup class="th"> th</sup> KAIST</p>
    </div>
    <div id="nav-bar">
      <div class="block">
        <router-link :to="{ name: 'home' }" class="button">Home</router-link>
        <router-link :to="{ name: 'album' }" class="button">album</router-link>
        <router-link :to="{ name: 'videos' }" class="button">videos</router-link>
        <router-link :to="{ name: 'schedule' }" class="button">schedule</router-link>
        <router-link :to="{ name: 'map' }" class="button">map</router-link>
      </div>
    </div>
    <div class="contents">
      <div id="sidebar-wrapper">
        <p id="menu">MENU</p>
        <div id="sidebar-left">
          <router-link :to="{ name: 'status_update' }" class="button">
            <div class="menu-images">
              <img src="/static/images/sciwar.png" width="35">
            </div>
            <p>
            카포전이란
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
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
              <img src="/static/images/supporters.png" width="50">
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
              <img src="/static/images/map.png" width="35">
            </div>
            <p>
            지도
              <i class="fa fa-chevron-right menu" aria-hidden="true"></i>
            </p></router-link>
          <router-link :to="{ name: 'album' }" class="button">
            <div class="menu-images">
              <img src="/static/images/image.png" width="35">
            </div>
            <p>
            사진&비디오
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
          <div v-on:click="topClick" id="top">
            <i class="fa fa-chevron-up" aria-hidden="ture"></i>
            <p style="margin-top: -24px;">TOP</p>
          </div>
        </div>
      </div>
      <div class="main">
        <router-view name="contents"></router-view>
      </div>
    </div>
    <div class="footer">
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      scrolled: false
    }
  },
  created () {
    console.log(2)
    window.addEventListener('scroll', this.handleScroll)
  },
  mounted () {
    this.navTop = document.getElementById('nav-bar').offsetTop
    this.sideTop = document.getElementById('nav-bar').offsetHeight + this.navTop + 'px'
    this.sideScrollTop = document.getElementById('nav-bar').offsetHeight + 'px'
    console.log(this.navTop)
  },
  methods: {
    handleScroll () {
      this.scrolled = window.scrollY
      console.log(this.scrolled)
      if (this.scrolled > this.navTop) {
        document.getElementById('nav-bar').classList.add('fixed')
        document.getElementById('sidebar-wrapper').classList.add('fixed')
        document.getElementById('nav-bar').style.top = '0px'
        document.getElementById('sidebar-wrapper').style.top = this.sideScrollTop
      } else {
        document.getElementById('nav-bar').classList.remove('fixed')
        document.getElementById('sidebar-wrapper').classList.remove('fixed')
        document.getElementById('nav-bar').style.top = '630px'
        document.getElementById('sidebar-wrapper').style.top = this.sideTop
      }
    },
    topClick () {
      window.scrollTo(0, 0)
    }
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang="sass" src="bulma"></style>
<style>
@import '../node_modules/font-awesome/css/font-awesome.min.css';
@import '../static/global.css';
@import url(//fonts.googleapis.com/earlyaccess/notosanskr.css);
@import url(//cdn.jsdelivr.net/font-kopub/1.0/kopubdotum.css);

.fixed {
  position: fixed !important;
}

.image {
  height: 630px;
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

.noto-sans {
  font-family: 'Noto Sans KR', sans-serif;
  color: white;
}

.noto-sans.big {
  font-size: 64px;
  font-weight: 900;
  letter-spacing: 10.3px;
  word-spacing: -3px;
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
}

.th {
  font-size: 34px;
}

.container {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 1295px;
  margin: 0 !important;
  padding: 0 !important;
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
}

#nav-bar {
  text-align: left;
  width:100%;
  height: 120px;
  position: absolute;
  top: 630px;
  background-color: rgba(8,49,110,1);
  box-shadow: 0 3px 7px rgb(130,130,130);
  z-index:1;
}

.block {
  width: 1295px;
  margin: 0 auto;
}

.contents {
  margin:120px auto 0 auto;
  display: flex;
  justify-content: space-between;
  ddbackground-color: rgba(187,100,100,1);
  height: 2000px;
  width:1295px;
}

#sidebar-wrapper {
  width: 300px;
  margin-top: 70px;
  position: absolute;
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

#home {
  margin-top: 15px;
  color: black;
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

.menu-images {
  margin-top: 2px;
}

.main {
  ddbackground-color: rgba(200,200,200,1);
  flex: auto;
  margin-left: 300px;
}
</style>
