<template>
  <div class="map noto-sans">
    <div class="map-title">지도</div>
    <p>카이스트 전체지도</p>
    <div class="event-map">
      <i class="fa fa-map-pin pin" aria-hidden="true"></i>
    </div>
    <div class="description">
      <p>경기별 위치</p><label>{{ location }}</label>
    </div>
    <div class="event-select">
      <div v-for="event in events" v-on:click="mapChange(event)" class="map-event button is-large">
        <label class="radio">
          <input v-on:click="radioClick()" type="radio" name="map-event" :value="event.pk" v-model="clicked">
          {{ event.fields.name_kor }}
        </label>
      </div>
    </div>
    <div class="event-detail-map"></div>
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
      if (event.fields.location === 2) {
        document.getElementsByClassName('pin')[0].style.paddingLeft = '315px'
        document.getElementsByClassName('pin')[0].style.paddingTop = '200px'
      } else if (event.fields.location === 0) {
        document.getElementsByClassName('pin')[0].style.paddingLeft = '310px'
        document.getElementsByClassName('pin')[0].style.paddingTop = '270px'
      } else if (event.fields.location === 1) {
        document.getElementsByClassName('pin')[0].style.paddingLeft = '145px'
        document.getElementsByClassName('pin')[0].style.paddingTop = '240px'
      } else if (event.fields.location === 3) {
        document.getElementsByClassName('pin')[0].style.paddingLeft = '555px'
        document.getElementsByClassName('pin')[0].style.paddingTop = '350px'
      } else if (event.fields.location === 4) {
        document.getElementsByClassName('pin')[0].style.paddingLeft = '270px'
        document.getElementsByClassName('pin')[0].style.paddingTop = '200px'
      }
    },
    radioClick () {
      for (let i of document.getElementsByClassName('map-event')) {
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
  font-weight: 500;
  margin-bottom: 20px;
}

.description {
  margin-top: 30px;
  font-size: 40px;
  display: flex;
}

.description > p {
  font-weight: 500;
  width: 300px;
}

.description > label {
  font-weight: 300;
  width: 100%;
}

.event-select {
  margin-top: 10px;
  display: flex;
  flex-direction: row;
}

.map-event {
  padding: 0;
  border: 0;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  margin-right: 2px;
  background: rgb(242, 242, 242);
}

.event-select > .map-event:nth-child(1) {
  background: rgb(149, 179, 215);
}

.map-event > .radio {
  padding: 8px 18px;
  width: 100%;
  height: 100%;
  font-size: 28px;
}

input[type="radio"] {
  display: none;
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
  position: relative;
  z-index: 1;
}

.pin {
  position: relative;
  z-index: 2;
  color: red;
  font-size: 30px;
}
</style>
