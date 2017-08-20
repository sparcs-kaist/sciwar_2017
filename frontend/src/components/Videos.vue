<template>
  <div class="videos noto-sans">
    <p class="videos-title">비디오 목록</p>
    <div class="video-list">
      <div v-for="video in videos" class="video">
        <div>
          <iframe width="280" height="280" :src="video.fields.link" frameborder="0" allowfullscreen></iframe>
          <p class="video-name"><router-link :to="{ name: 'video', params: { id: video.pk }}">{{ video.fields.name }}</router-link></p>
        </div>
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

<style>
.video-name > a {
  font-size: 32px;
  color: black;
}

.videos-title {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 10px;
}

.video-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.video {
  width: 290px;
}

.video > div {
  margin-right: 10px;
}
</style>
