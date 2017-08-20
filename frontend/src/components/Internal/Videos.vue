<template>
  <div class="videos-add noto-sans">
    <label>title</label>
    <input class="input" name="title" type="text">
    <label>source</label>
    <input class="input" name="source" type="text" placeholder="ex) https://www.youtube.com/embed/jy_UiIQn_d0">
    <label>live streaming 여부</label><br>
    <input type="radio" value="0" v-model="live">
    <label>네</label>
    <input type="radio" value="1" v-model="live">
    <label>아니요</label>
    <p>해당 이벤트</p>
    <div v-for="event in events">
      <input type="checkbox" :value="event.pk" v-model="checkedEvents">
      <label>{{ event.fields.name_kor }}</label>
    </div>
    {{ live }}
    {{ checkedEvents }}
    <button class="button is-primary submit" v-on:click=submitClick()>제출</button>
  </div>
</template>

<script>
export default {
  name: 'videosAdd',
  data () {
    return {
      events: [],
      checkedEvents: [],
      live: []
    }
  },
  created () {
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
      })
  },
  methods: {
    submitClick () {
      let title = document.getElementsByName('title')[0].value
      let source = document.getElementsByName('source')[0].value
      let data = { 'title': title, 'source': source, 'event': this.checkedEvents, 'type': this.live }
      console.log(this.checkedEvents)
      data = JSON.stringify(data)
      console.log(data)
      this.$http.put('/api/videos/', data)
        .then((response) => {
          console.log('save successfully')
        })
    }
  }
}
</script>

<style>
.input {
  margin-bottom: 10px;
}
</style>
