<template>
  <div class="home">
    <div class="image">
      <p class="noto-sans big">2017 SCIENCE WAR</p>
      <p class="kopub">카이스트포스텍학생대제전</p>
      <p class="noto-sans small">OCT. 15 - 17<sup class="th"> th</sup> KAIST</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      scrolled: false
    }
  },
  created () {
    window.addEventListener('scroll', this.handleScroll)
    console.log('created')
  },
  mounted () {
    this.scrolled = window.scrollY
    console.log(this.scrolled)
    if (this.scrolled > 623) {
      console.log('if')
      document.getElementById('nav-bar').style.top = '0px'
      document.getElementById('sidebar-wrapper').style.top = '144px'
      document.getElementById('nav-bar').classList.add('fixed')
      document.getElementById('sidebar-wrapper').classList.add('fixed')
    } else {
      console.log('else')
      document.getElementById('nav-bar').classList.remove('fixed')
      document.getElementById('sidebar-wrapper').classList.remove('fixed')
      console.log(document.getElementById('nav-bar'))
      document.getElementById('nav-bar').style.top = '623px'
      console.log(document.getElementById('nav-bar'))
      document.getElementById('sidebar-wrapper').style.top = '767px'
    }
    console.log('mounted')
  },
  computed () {
  },
  methods: {
    handleScroll () {
      this.scrolled = window.scrollY
      if (this.scrolled > 623) {
        document.getElementById('nav-bar').style.top = '0px'
        document.getElementById('sidebar-wrapper').style.top = '144px'
        document.getElementById('nav-bar').classList.add('fixed')
        document.getElementById('sidebar-wrapper').classList.add('fixed')
      } else {
        document.getElementById('nav-bar').classList.remove('fixed')
        document.getElementById('sidebar-wrapper').classList.remove('fixed')
        document.getElementById('nav-bar').style.top = '623px'
        document.getElementById('sidebar-wrapper').style.top = '767px'
      }
    }
  },
  updated () {
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}

</script>

<style>
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

.th {
  font-size: 34px;
}

.home {
  width: 1295px;
}

#nav-bar {
  top: 623px;
}
</style>
