<template>
  <div class="videos noto-sans">
    <p class="videos-title">비디오 목록</p>
    <p class="videos-sub-title">현재 라이브 중인 동영상</p>
    <div class="live-videos">
      <div v-for="video in videoLive" class="video">
        <div>
          <iframe width="280" height="250" :src="video.fields.link" frameborder="0" allowfullscreen></iframe>
          <p class="video-name"><router-link :to="{ name: 'video', params: { id: video.pk }}">{{ video.fields.name }}</router-link></p>
        </div>
      </div>
    </div>
    <p class="videos-sub-title">경기별 동영상</p>
    <div v-on:click="filterChange(1)" class="event button is-large">
      <label class="radio">
        <input v-on:click="radioClick(event)" type="radio" name="event" value=0>
        전체
      </label>
    </div>
    <div v-for="event in events" v-on:click="filterChange(event)" class="event button is-large">
      <label class="radio">
        <input v-on:click="radioClick(event)" type="radio" name="event" :value="event.pk">
        {{ event.fields.name_kor }}
      </label>
    </div>
    <div class="video-list">
      <div v-for="video in videosRendered" class="video">
        <div>
          <iframe width="280" height="250" :src="video.fields.link" frameborder="0" allowfullscreen></iframe>
          <p class="video-name"><router-link :to="{ name: 'video', params: { id: video.pk }}">{{ video.fields.name }}</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'videos',
  data () {
    return {
      videosRendered: [],
      videos: [],
      events: [],
      videoLive: []
    }
  },
  created () {
    this.$http.get('/api/videos/')
      .then((response) => {
        this.videos = JSON.parse(response.data)
        this.videosRendered = JSON.parse(JSON.stringify(this.videos))
        for (let i of this.videos) {
          if (i.fields.type === 0) {
            this.videoLive.push(i)
          }
        }
        console.log(this.videoLive)
      })
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
      })
  },
  mounted () {
    document.getElementsByName('event')[0].click()
  },
  methods: {
    filterChange (event) {
      console.log(event)
      if (event === 1) {
        this.videosRendered = JSON.parse(JSON.stringify(this.videos))
      } else {
        this.videosRendered = []
        for (let i of this.videos) {
          if (i.fields.event.indexOf(event.pk) !== -1) {
            this.videosRendered.push(i)
          }
        }
      }
    },
    radioClick () {
      for (let i of document.getElementsByClassName('event')) {
        i.style.background = 'rgb(242,242,242)'
      }
      event.target.parentNode.parentNode.style.background = 'rgb(149,179,215)'
    }
  }
}
</script>

<style>

.video-name > a {
  font-size: 28px;
  font-weight: 300;
  color: black;
  padding-left: 5px;
  padding-right: 5px;
  margin-bottom: 10px;
}

.videos-sub-title {
  font-size: 40px;
  font-weight: 500;
  margin-bottom: 20px;
}

.videos-title {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 10px;
  padding-bottom: 1.5rem;
}

.event {
  padding: 0;
  border: 0;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  margin-right: 2px;
  background: rgb(242, 242, 242);
}

.event > .radio {
  padding: 8px 18px;
  width: 100%;
  height: 100%;
  font-size: 28px;
}

input[type="radio"] {
  display: none;
}

.live-videos {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin-bottom: 30px;
}

.video-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin-top: 10px;
}

.video {
  width: 290px;
  margin-bottom: 10px;
}

.video > div {
  margin-right: 10px;
}
</style>
