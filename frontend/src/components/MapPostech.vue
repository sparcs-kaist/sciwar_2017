<template>
  <div class="map noto-sans">
    <div class="map-title">지도</div>
    <p>포스텍</p>
    <div class="map-overview">
      <div v-for="event in events" class="map-event button is-large">
        <label class="radio">
          <input v-on:click="radioClick(event, $event.target)" type="radio" name="map-event" :value="event">
          {{ event.fields.name_kor }}
        </label>
      </div>
      <div class="map-picture" v-on:click="discardCurrent()">
        <i
        v-for="location in locations"
        v-if="location.fields.school === 2"
        :id="location.fields.name_eng"
        class="fa fa-map-pin pin"
        aria-hidden="true"
        v-on:mouseover="setCurrent(location)"
        :style="pinCoordinate(location)"></i>
        <div v-if="currentLocation.hasOwnProperty('fields')" class="map-info">
          <p>{{ this.currentLocation.fields.name_kor }} {{ this.currentLocation.fields.name_eng }}</p>
          <p>{{ this.currentLocation.fields.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script scoped>
export default {
  name: 'map-postech',
  data () {
    return {
      currentLocation: {},
      locations: [],
      events: []
    }
  },
  created () {
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
      })
    this.$http.get('/api/locations/')
      .then((response) => {
        this.locations = JSON.parse(response.data)
      })
  },
  methods: {
    pinCoordinate (location) {
      return `position: relative; cursor:pointer; top: ${location.fields.top}px; left: ${location.fields.left}px`
    },
    setCurrent (location) {
      this.currentLocation = location
      return
    },
    radioClick (event, target) {
      console.log(event)
      for (let radio of target.parentNode.parentNode.parentNode.children) {
        radio.style.backgroundColor = 'rgb(242, 242, 242)'
      }
      target.parentNode.parentNode.style.backgroundColor = 'rgb(149, 179, 215)'
      for (let location of this.locations) {
        if (location.pk === event.fields.location) {
          if (this.currentLocation.hasOwnProperty('fields')) {
            document.getElementById(this.currentLocation.fields.name_eng).classList.remove('hover')
          }
          this.setCurrent(location)
          document.getElementById(location.fields.name_eng).classList.add('hover')
        }
      }
    },
    discardCurrent () {
      for (let pin of document.getElementsByClassName('pin')) {
        if (pin.classList.contains('hover')) pin.classList.remove('hover')
      }
      for (let radio of document.getElementsByClassName('map-event')) {
        radio.style.backgroundColor = 'rgb(242, 242, 242)'
      }
      this.currentLocation = {}
    }
  }
}
</script>

<style scoped>
.map-title {
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 10px;
  margin-bottom: 30px;
  display: inline;
}

.map > p {
  font-size: 40px;
  font-weight: 500;
  margin-bottom: 20px;
}

.map-info {
  margin-top: 30px;
  font-size: 24px;
  position: relative;
  top: 450px;
  left: 300px;
  width: 500px;
  background-color: white;
  padding: 5px 5px 5px 5px;
  border-radius: 10px;
}

.map-info > p:nth-child(1) {
  font-weight: 500;
  margin-bottom: -5px;
}

.map-events-list {
  width: 100px;
  margin-top: 10px;
  display: flex;
  flex-direction: column;
}

.map-event {
  padding: 0;
  border: 0;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  margin-right: 2px;
  background: rgb(242, 242, 242);
}

.map-event > .radio {
  padding: 8px 18px;
  width: 100%;
  height: 100%;
  font-size: 28px;
  color: black;
}

input[type="radio"] {
  display: none;
}

.map-overview {
  display: inline;
}

.map-picture {
  background-image: url('/static/images/map_postech/postech_map.jpg');
  background-size: contain;
  width: 880px;
  height: 650px;
  margin-bottom: 20px;
  position: relative;
  z-index: 1;
}

.pin {
  position: relative;
  z-index: 2;
  color: black;
  font-size: 30px;
}

.pin:hover {
  transform-origin: left bottom;
  transform: scale(1.5);
  color: rgba(8,49,110,1);
}

.hover {
  transform-origin: left bottom;
  transform: scale(1.5);
  color: rgba(8,49,110,1);
}
</style>
