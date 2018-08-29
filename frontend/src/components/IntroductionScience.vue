<template>
  <div class="introduction noto-sans">
    <p class="head">과학경기 소개</p>
    <router-link v-for="event in events" :to="{ name: 'event', params: { id: event.pk } }">
      <div class="introduction-form">
        <p class="introduction-name">{{ event.fields.name_kor }}</p>
        <div class="introduction-contents">
          <img :src="`/static/images/events/${event.fields.name_eng}.png`" width="400" height="400">
          <p class="introduction-message">{{ event.fields.about }}</p>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'intro-science',
  data () {
    return {
      events: []
    }
  },
  created () {
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
        this.events = this.events.filter((event) => { return event.fields.type === 1 })
      })
  }
}
</script>

<style scoped>
.head {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 1.5rem;
}

.introduction-contents {
  display: flex;
  flex-direction: row;
  align-items: center;
  color: black;
}

.introduction-contents > img {
  height: 150px;
  width: 150px;
  margin: 0 0 0 30px;
  filter: grayscale(0%);
}

.introduction-message {
  font-size: 24px;
  font-weight: 300;
  text-align: justify;
  margin: 0 20px 0 30px;
  word-break: keep-all;
  color: black;
}

.introduction-form {
  font-size: 30px;
  font-weight: 600;
  color: black;
  border-radius: 10px;
  background-color: #efefef;
  padding-bottom: 15px;
  padding-top: 5px;
  margin-bottom: 50px;
}

.introduction-name {
  text-align: justify;
  margin-left: 20px;
}

img {
  border-radius: 10px;
}
</style>
