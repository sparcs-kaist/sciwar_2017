<template>
  <div class="schedule noto-sans">
    <div class="head">일정</div>
    <div v-for="date in dates" class="events-date">
      <p>9월  {{ date.split('-')[2] }}일</p>
      <div v-for="event in events" class="events-schedule">
          <div v-if="event.fields.start_time.split('T')[0] == date" class="event-schedule">
            <div v-if="event.fields.type == 0 || event.fields.type == 1">
              <router-link :to="{ name: 'event', params: { id: event.pk } }">
                <div class="event-name">
                  {{ event.fields.name_kor }} {{ event.fields.name_eng }}
                  <i class="fa fa-chevron-right"></i>
                </div>
              </router-link>
            </div>
            <div v-else>
              <router-link :to="{ name: 'introduction' }">
                <div class="event-name">
                  {{ event.fields.name_kor }} {{ event.fields.name_eng }}
                  <i class="fa fa-chevron-right"></i>
                </div>
              </router-link>
            </div>
            <div class="time-location">
              <div class="event-time">
                <i class="fas fa-clock" aria-hidden="true"></i>
                {{ event.fields.start_time.split('T')[1].split('Z')[0].split(':')[0] }}:{{ event.fields.start_time.split('T')[1].split('Z')[0].split(':')[1] }}&nbsp; &nbsp;
              </div>
              <div class="event-location">
                <i class="fas fa-map-marker-alt" aria-hidden="true"></i>
                {{ findLocation(event.fields.location) }}
              </div>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'schedule',
  data () {
    return {
      dates: [],
      events: [],
      locations: []
    }
  },
  created () {
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
        for (let i in this.events) {
          let date = this.events[i].fields.start_time.split('T')[0]
          if (this.dates.indexOf(date) === -1) {
            this.dates.push(date)
          }
        }
      })
    this.$http.get('/api/locations/')
      .then((response) => {
        this.locations = JSON.parse(response.data)
      })
  },
  methods: {
    findLocation (pk) {
      for (let i of this.locations) {
        if (i.pk === pk) return i.fields.name_kor
      }
      return ''
    }
  }
}
</script>

<style scoped>
.head {
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 10px;
  margin-bottom: 1.5rem;
}

.events-date {
  background-color: rgb(242, 242, 242);
  margin-bottom: 20px;
  padding: 10px 20px;
  border-radius: 10px;
}

.events-date > p {
  font-size: 30px;
  font-weight: 600;
  margin-left: 3px;
}

.events-schedule {
  margin-top: 8px;
}

.event-schedule {
  background-color: white;
  margin-bottom: 13px;
  border-radius: 10px;
  font-size: 43px;
  font-weight: 300;
  padding: 5px 10px 5px 13px;
}

.event-name {
  color: black;
  margin-right: 5px;
}

.event-name > i {
  margin-top: 27px;
  margin-left: 5px;
  font-size: 20px;
  color: rgb(70, 122, 184);
}

.time-location {
  display: flex;
  margin-top: 5px;
}

.event-time {
  margin-right: 10px;
  font-size: 35px;
  font-weight: 400;
}

.event-time > i {
  margin-top: 12px;
  font-size: 30px;
}

.event-location {
  flex: auto;
  font-size: 35px;
  font-weight: 400;
}

.event-location > i {
  margin-top: 12px;
  font-size: 30px;
}
</style>
