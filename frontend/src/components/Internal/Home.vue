<template>
  <div class="internal-home noto-sans">
    <p class="head">링크 목록</p>
    <router-link :to="{ name: 'videos_check' }">Videos</router-link>
    <router-link :to="{ name: 'supporters_check' }">Supporters</router-link>
    <router-link :to="{ name: 'toto_check' }">Toto</router-link>
    <router-link :to="{ name: 'status_update' }">Events</router-link>
  </div>
</template>

<script>
export default {
  name: 'internalHome'
}
</script>

<style scoped>
.internal-home {
  display: flex;
  flex-direction: column;
}

.internal-home > a {
  color: black;
  font-size: 20px;
}

.head {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 20px;
}
</style>
