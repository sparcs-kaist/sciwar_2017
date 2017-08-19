<template>
  <div class="schedule noto-sans">
    <div v-for="date in dates" class="events-date">
      {{ date.split('-')[1] }}-{{ date.split('-')[2] }}
      <div v-for="event in events" class="events-schedule">
        <div v-if="event.fields.start_time.split('T')[0] == date" class="event-schedule">
          <div class="event-name">
            {{ event.fields.name_eng }}
          </div>
          <div class="time-location">
            <div class="event-time">
              {{ event.fields.start_time.split('T')[1].split('Z')[0].split(':')[0] }}:{{ event.fields.start_time.split('T')[1].split('Z')[0].split(':')[1] }}
            </div>
            <div class="event-location">
              {{ locations[event.fields.location] }}
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
        console.log(this.dates)
      })
    this.locations = ['Creative Learning Building', 'Outdoor Theater', 'Sports Complex', 'Stadium', 'Main Playground']
  }
}
</script>

<style>
.events-date {
  background-color: rgb(242, 242, 242);
  margin-bottom: 20px;
  padding: 10px 20px;
  font-size: 40px;
}

.events-schedule {
}

.event-schedule {
}

.event-name {
}

.time-location {
  display: flex;
}

.event-time {
  margin-right: 10px;
}

.event-location {
  flex: auto;
}
</style>
