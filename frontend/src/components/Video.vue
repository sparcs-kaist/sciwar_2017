<template>
  <div id="video noto-sans">
    <p class="video-name">{{ video.fields.name }}</p>
    <iframe width="800" height="450" :src="link" frameborder="0" allowfullscreen></iframe>
  </div>
</template>

<script>
export default {
  name: 'video',
  created: function () {
    let id = this.$route.params.id
    this.$http.get(`/api/videos/${id}`)
      .then((response) => {
        this.video = JSON.parse(response.data)[0]
        console.log(this.video)
        this.link = this.video.fields.link
        console.log(this.link)
      })
  },
  data () {
    return {
      video: {},
      link: []
    }
  }
}
</script>

<style>
.video-name {
  font-size: 50px;
  font-weight: 700;
  margin-bottom: 10px;
}
</style>
