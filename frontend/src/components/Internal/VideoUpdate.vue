<template>
  <div id="video noto-sans">
    <div class="internal-video-title">
      <p>{{ video.fields.name }}</p>
      <div v-if="video.fields.type == 0">LIVE</div>
    </div>
    <iframe id="frame" width="800" height="450" :src="generateUrl(link)" frameborder="0" allowfullscreen></iframe>
    <div class="related-events">
      <p>연관 행사:</p>
      <router-link v-for="event in events" v-if="event.fields.type !== 2" :to="{ name: 'event', params: { id: event.pk } }">
        <label v-on:mouseover="mouseOver()" v-on:mouseleave="mouseLeave()">{{ event.fields.name_kor }}</label>
      </router-link>
    </div>
    <div class="video-cheermessages-title">
      <p>응원의 메세지</p>
      <router-link :to="{ name: 'cheermessage' }"><p>나도 한 마디<img src="/static/images/message.png" width="50"></p></router-link>
    </div>
    <div class="video-cheermessages">
      <p v-if="cheermessages[0]">{{ cheermessages[0].fields.content }}
      <span v-if="cheermessages[0].fields.school == 1">to. KAIST</span>
      <span v-if="cheermessages[0].fields.school == 2">to. POSTECH</span>
      </p>
      <p v-if="cheermessages[1]">{{ cheermessages[1].fields.content }}
      <span v-if="cheermessages[1].fields.school == 1">to. KAIST</span>
      <span v-if="cheermessages[1].fields.school == 2">to. POSTECH</span>
      </p>
      <p v-if="cheermessages[2]">{{ cheermessages[2].fields.content }}
      <span v-if="cheermessages[2].fields.school == 1">to. KAIST</span>
      <span v-if="cheermessages[2].fields.school == 2">to. POSTECH</span>
      </p>
    </div>
    <div class="radio-container">
      <label>live streaming 여부</label><br>
      <input type="radio" id="live0" :value="0" v-model="live">
      <label :style="`color:${radioClick(0)}`" for="live0" class="link radio-label">네</label>
      <input type="radio" id="live1" :value="1" v-model="live">
      <label :style="`color:${radioClick(1)}`" for="live1" class="link radio-label">아니요</label>
    </div>
    <div class="button-container">
      <router-link :to="{ name: 'videos_check' }"><button v-on:click="submit()" class="link">제출</button></router-link>
      <router-link :to="{ name: 'videos_check' }"><button v-on:click="del()" class="link">삭제</button></router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'video',
  created: function () {
    this.video = {}
    let videoId = this.$route.params.id
    this.$http.get(`/api/videos/${videoId}/`)
      .then((response) => {
        this.video = JSON.parse(response.data)[0]
        this.link = this.video.fields.link
        this.loadEvent(this.video.fields.event)
        this.live = this.video.fields.type
      })
  },
  mounted: function () {
    this.radioClick(this.live)
  },
  data () {
    return {
      video: {},
      link: [],
      events: [],
      cheermessages: [],
      live: 0
    }
  },
  methods: {
    loadEvent (events) {
      for (let eventId of events) {
        let uri1 = `/api/events/${eventId}/`
        let uri2 = `/api/events/${eventId}/messages/`
        this.$http.get(uri1)
          .then((response) => {
            this.events.push(JSON.parse(response.data)[0])
          })
        this.$http.get(uri2)
          .then((response) => {
            this.cheermessages.push.apply(this.cheermessages, JSON.parse(response.data))
          })
      }
    },
    generateUrl (key) {
      return `http://www.youtube.com/embed/${key}`
    },
    mouseOver () {
      event.target.style.background = 'rgb(149,179,215)'
    },
    mouseLeave () {
      event.target.style.background = 'rgb(242,242,242)'
    },
    submit () {
      let data = { 'pk': this.$route.params.id, 'type': this.live }
      this.$http.post('/api/videos/' + this.$route.params.id + '/', JSON.stringify(data))
        .then((response) => {
          console.log('successful')
        })
    },
    del () {
      this.$http.delete('/api/videos/' + this.$route.params.id + '/')
        .then((response) => {
          console.log('successful')
        })
    },
    radioClick (num) {
      if (this.live === num) return 'black'
      return 'white'
    }
  }
}
</script>

<style scoped>
.internal-video-title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.internal-video-title > p {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 10px;
  padding-bottom: 1.5rem;
  max-width: 700px;
  line-height: 3.6rem;
}

.internal-video-title > div {
  border: none;
  padding: 2px 7px 4px 7px;
  font-size: 30px;
  height: 50px;
  font-weight: 600;
  background-color: rgb(188, 77, 77);
  color: white;
  margin-top: 20px;
  float: right;
}

#frame {
  margin-left: auto;
  margin-right: auto;
  display: table;
}

.related-events {
  margin-left: 40px;
  display: flex;
  flex-direction: row;
  margin-top: 10px;
}

.related-events > p {
  font-size: 32px;
  margin-right: 10px;
}

.related-events > a {
  margin-top: 5px;
}

.related-events > a > label {
  border: none;
  border-radius: 5px;
  padding: 3px 8px 3px 8px;
  font-size: 28px;
  font-weight: 600;
  background-color: rgb(242, 242, 242);
  margin-left: 10px;
  cursor: pointer;
  color: black;
}

.video-cheermessages-title {
  display: flex;
  flex-direction: row;
  margin-top: 25px;
  justify-content: space-between;
}

.video-cheermessages-title > p {
  font-size: 40px;
  font-weight: 500;
}

.video-cheermessages-title > a > p {
  font-size: 28px;
  display: block;
  float: right;
  margin-top: 5px;
  color: black;
  width: 230px;
  font-weight: 500;
}

.video-cheermessages-title > a > p > img {
  margin: 0 0 -15px 0;
}

.video-cheermessages {
  margin-top: 10px;
  font-weight: 200;
}

.video-cheermessages > p {
  font-size: 30px;
  padding: 0 20px;
  width: 890px;
}

.video-cheermessages > p:nth-child(odd) {
  background-color: rgb(242, 242, 242);
  border-radius: 10px;
}

.video-cheermessages > p > span {
  float: right;
  width: 200px;
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
