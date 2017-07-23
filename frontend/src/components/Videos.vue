<template>
  <div class="videos">
    Videos
    <div v-for="video in videos" class="video">
      <div>
        <router-link :to="{ name: 'video', params: { id: video.pk }}">더보기</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'videos',
  created () {
    this.$http.get('/api/videos')
      .then((response) => {
        this.videos = JSON.parse(response.data)
      })
  },
  data () {
    return {
      videos: []
    }
  }
}
</script>
