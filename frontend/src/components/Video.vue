<template>
  <div id="video noto-sans">
    <div class="video-title">
      <p>{{ video.fields.name }}</p>
      <div v-if="video.fields.type == 0">LIVE</div>
    </div>
    <iframe id="frame" width="800" height="450" :src="link" frameborder="0" allowfullscreen></iframe>
    <div class="related-events">
      <p>연관 행사:</p>
      <router-link v-for="event in events" :to="{ name: 'event', params: { id: event.pk } }">
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
  </div>
</template>

<script>
export default {
  name: 'video',
  created: function () {
    this.loadVideo()
  },
  watch: {
    '$route': 'loadVideo'
  },
  data () {
    return {
      video: {},
      link: [],
      events: [],
      cheermessages: []
    }
  },
  methods: {
    loadVideo () {
      this.video = {}
      this.link = new Array(0)
      this.events = new Array(0)
      this.cheermessages = new Array(0)
      let videoId = this.$route.params.id
      this.$http.get(`/api/videos/${videoId}/`)
        .then((response) => {
          this.video = JSON.parse(response.data)[0]
          this.link = this.video.fields.link
          this.loadEvent(this.video.fields.event)
        })
    },
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
    mouseOver () {
      event.target.style.background = 'rgb(149,179,215)'
    },
    mouseLeave () {
      event.target.style.background = 'rgb(242,242,242)'
    }
  }
}
</script>

<style scoped>
.video-title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.video-title > p {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 10px;
  padding-bottom: 1.5rem;
  max-width: 700px;
  line-height: 3.6rem;
}

.video-title > div {
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
</style>
