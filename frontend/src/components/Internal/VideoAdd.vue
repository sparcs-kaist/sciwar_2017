<template>
  <div class="videos-add noto-sans">
    <div class="head">비디오 추가</div>
    <label>title</label>
    <input class="input" name="title" type="text">
    <label>source</label>
    <input class="input" name="source" type="text" placeholder="ex) https://www.youtube.com/embed/jy_UiIQn_d0">
    <div class="radio-container">
      <label>live streaming 여부</label><br>
      <input type="radio" id="live0" value="0" v-model="live">
      <label v-on:click="radioClick(0)" for="live0" class="link">네</label>
      <input type="radio" id="live1" value="1" v-model="live">
      <label v-on:click="radioClick(1)" for="live1" class="link">아니요</label>
    </div>
    <p>해당 이벤트</p>
    <div v-for="event in events">
      <input type="checkbox" :value="event.pk" v-model="checkedEvents">
      <label>{{ event.fields.name_kor }}</label>
    </div>
    <router-link :to="{ name: 'videos' }"><button class="button is-primary submit" v-on:click=submitClick()>제출</button></router-link>
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
    parseUrl (src) {
      let token = src.split('/').pop()
      let idx = token.indexOf('v=')s
      if (idx !== -1) {
        token = token.slice(idx + 2)
        return token.slice(0, token.indexOf('&'))
      }
      return token
    },
    submitClick () {
      let title = document.getElementsByName('title')[0].value
      let source = this.parseUrl(document.getElementsByName('source')[0].value)
      let data = { 'title': title, 'source': source, 'event': this.checkedEvents, 'type': this.live }
      console.log(source)
      data = JSON.stringify(data)
      if (title && source) {
        this.$http.put('/api/videos/', data)
          .then((response) => {
            console.log('save successfully')
          })
      }
    },
    radioClick (num) {
      let link = document.getElementsByClassName('link')
      for (let i of link) {
        i.style.color = 'white'
      }
      link[num].style.color = 'black'
    }
  }
}
</script>

<style scoped>
.head {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 20px;
}

.input {
  margin-bottom: 10px;
}

.radio-container {
  font-size: 30px;
  margin-bottom: 10px;
}

.radio-container > .link {
  cursor: pointer;
}

.radio-container > input[type=radio] {
  display: none;
}

.link {
  background-color: #555555;
  text-align: center;
  font-size: 22px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
}
</style>
