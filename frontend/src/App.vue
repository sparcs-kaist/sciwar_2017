<template>
  <div class="container">
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
      <div class="sidebar-left">
        <router-link :to="{ name: 'home' }" class="button">Home</router-link>
        <router-link :to="{ name: 'home' }" class="button">Home</router-link>
        <router-link :to="{ name: 'home' }" class="button">Home</router-link>
        <router-link :to="{ name: 'home' }" class="button">Home</router-link>
        <router-link :to="{ name: 'home' }" class="button">Home</router-link>
        <router-link :to="{ name: 'home' }" class="button">Home</router-link>
      </div>
      <div class="main">
        <router-view name="contents"></router-view>
      </div>
      <div class="sidebar-right">
        Hi
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="sass" src="bulma"></style>
<style>
@import '../static/global.css';
@import '../node_modules/font-awesome/css/font-awesome.min.css';
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
