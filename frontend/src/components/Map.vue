<template>
  <div class="map noto-sans">
    <div class="map-title">지도</div>
    <div class="event-select">
      <div v-for="event in events" v-on:click="mapChange(event)" class="event button is-large">
        <label class="radio">
          <input v-on:click="radioClick()" type="radio" name="event">
          {{ event.fields.name_kor }}
        </label>
      </div>
    </div>
    <div class="event-detail-map"></div>
    <div class="event-map">
    </div>
  </div>
</template>

<script>
export default {
  name: 'map',
  data () {
    return {
      events: []
    }
  },
  created () {
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
      })
    this.mapList = ['map_E11, Creative Learning Building.png', 'map_W9, Outdoor Theater.png', 'map_N3, Sports Complex.png', 'map_E17, Stadium.png', 'map_In Front of N3, Main Playground.png']
  },
  updated () {
    console.log(document.getElementsByClassName('event')[0])
    document.getElementsByName('event')[0].click()
  },
  methods: {
    mapChange (event) {
      document.getElementsByClassName('event-detail-map')[0].style.height = '280px'
      document.getElementsByClassName('event-detail-map')[0].style.background = "url('/static/images/" + this.mapList[event.fields.location] + "')"
    },
    radioClick () {
      for (let i of document.getElementsByClassName('event')) {
        i.style.background = 'rgb(242,242,242)'
      }
      event.target.parentNode.parentNode.style.background = 'rgb(242,242,242)'
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

.event-select {
  display: flex;
  flex-direction: row;
}

.event {
  padding: 0;
  border: 0;
  border-radius: 0;
  margin-right: 5px;
}

.event > .radio {
  padding: 8px 18px;
  width: 100%;
  height: 100%;
}

input[type="radio"] {
  display: none;
}

.event-detail-map {
  width: 628px;
  margin-top: 10px;
}

.event-map {
  background-image: url('/static/images/kaist_map.png');
  width: 628px;
  height: 492px;
  margin: 10px 0;
}
</style>
