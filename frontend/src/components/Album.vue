<template>
  <div class="album">
    <p class="videos-title">비디오 목록<router-link :to="{ name: 'videos' }">더보기</router-link></p>
    <div class="video-list">
      <div v-for="video in videos" class="video">
        <div>
          <iframe width="290" height="290" :src="video.fields.link" frameborder="0" allowfullscreen></iframe>
          <p class="video-name"><router-link :to="{ name: 'video', params: { id: video.pk }}">{{ video.fields.name }}</router-link></p>
        </div>
      </div>
    </div>
    <p class="images-title">이미지 목록</p>
  </div>
</template>

<script>
export default {
  name: 'album',
  created () {
    this.$http.get('/api/videos/')
      .then((response) => {
        this.videos = JSON.parse(response.data).slice(0, 3)
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
  font-size: 72px;
  font-weight: 700;
  margin-bottom: 10px;
}

.videos-title > a {
  font-size: 32px;
  float: right;
  margin-top: 50px;
  color: black;
}

.video-list {
  display: flex;
  flex-direction: row;
}

.video > div {
  margin-right: 10px;
}

.images-title {
  font-size: 72px;
  font-weight: 700;
  margin: 10px 0;
}

</style>
