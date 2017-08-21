<template>
  <div class="map noto-sans">
    <div class="map-title">지도</div>
    <p class="description">카이스트 전체지도</p>
    <div class="event-map"></div>
    <p class="dexription">경기별 위치</p>
    <div class="event-select">
      <div v-for="event in events" v-on:click="mapChange(event)" class="event button is-large">
        <label class="radio">
          <input v-on:click="radioClick()" type="radio" name="event" :value="event.pk" v-model="clicked">
          {{ event.fields.name_kor }}
        </label>
      </div>
    </div>
    <div class="event-detail-map"></div>
    <label class="location-text">{{ location }}</label>
  </div>
</template>

<script>
export default {
  name: 'map',
  data () {
    return {
      events: [],
      location: '',
      clicked: []
    }
  },
  created () {
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
        this.mapList = ['map_E11, Creative Learning Building.png', 'map_W9, Outdoor Theater.png', 'map_N3, Sports Complex.png', 'map_E17, Stadium.png', 'map_In Front of N3, Main Playground.png']
        this.locations = ['Creative Learning Building', 'Outdoor Theater', 'Sports Complex', 'Stadium', 'Main Playground']
        console.log(this.events[0])
        this.mapChange(this.events[0])
        this.clicked = this.events[0].pk
      })
  },
  mounted () {
    window.addEventListener('DOMContentLoaded', function () {
    }, false)
  },
  methods: {
    mapChange (event) {
      document.getElementsByClassName('event-detail-map')[0].style.height = '280px'
      document.getElementsByClassName('event-detail-map')[0].style.background = "url('/static/images/" + this.mapList[event.fields.location] + "')"
      console.log(event.fields.location)
      this.location = this.locations[event.fields.location]
    },
    radioClick () {
      for (let i of document.getElementsByClassName('event')) {
        i.style.background = 'rgb(242,242,242)'
      }
      event.target.parentNode.parentNode.style.background = 'rgb(149, 179, 215)'
      console.log(this.clicked)
    }
  }
}
</script>

<style>
.map-title {
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 10px;
}

.map > p {
  font-size: 40px;
  margin-bottom: 20px;
}

.event-select {
  margin-top: 10px;
  display: flex;
  flex-direction: row;
}

.event {
  padding: 0;
  border: 0;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  margin-right: 2px;
  background: rgb(242, 242, 242);
}

.event-select > .event:nth-child(1) {
  background: rgb(149, 179, 215);
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

.location-text {
  font-size: 40px;
  font-weight: 300;
  margin-bottom: 0px;
}

.event-detail-map {
  width: 628px;
  margin-top: 0;
}

.event-map {
  background-image: url('/static/images/kaist_map.png');
  width: 628px;
  height: 492px;
  margin: auto;
  margin-bottom: 20px;
}
</style>
