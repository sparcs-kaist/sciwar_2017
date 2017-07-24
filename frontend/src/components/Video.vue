<template>
  <div id="video">
    <iframe width="560" height="315" :src="link" frameborder="0" allowfullscreen></iframe>
  </div>
</template>

<script>
export default {
  name: 'video',
  created: function () {
    let id = this.$route.params.id
    this.$http.get(`/api/videos/${id}`)
      .then((response) => {
        this.video = JSON.parse(response.data)
        this.link = this.video[0].fields.link
      })
  },
  data () {
    return {
      link: []
    }
  }
}
</script>
