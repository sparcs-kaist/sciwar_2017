<template>
  <div id="events">
    <p class="head">이벤트 현황 수정</p>
    <div v-for="event in events" class="internal-event">
      <div class="event-name">{{ event.fields.name_kor }}</div>
      <div class="event-status">
        <input class="input input-score" v-if="event.fields.type === 0" type="text" :value="event.fields.score_k" :name="'kaist' + event.pk">
        <input class="input input-score" v-if="event.fields.type === 0" type="text" :value="event.fields.score_p" :name="'postech' + event.pk">
        <div class="select">
          <select class="select-options">
            <option v-for="option in options" :value="option.value" :selected="option.value == event.fields.live">{{ option.text }}</option>
          </select>
        </div>
        <button class="button is-primary submit" v-on:click = selectClick($event) name="button">Submit</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'events',
  created () {
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
      })
  },
  data () {
    return {
      events: [],
      options: [
        { text: 'Pre', value: '0' },
        { text: 'Live', value: '1' },
        { text: 'Post', value: '2' }
      ]
    }
  },
  updated () {
    let e = document.getElementsByClassName('select-options')
    for (let select in e) {
      if (e[select].selectedIndex === 2) {
        e[select].disabled = true
        document.getElementsByName('button')[select].disabled = true
      }
    }
    let buttons = document.getElementsByTagName('button')
    for (let i in buttons) {
      let button = buttons[i]
      button.name = i
    }
  },
  methods: {
    selectClick (event) {
      let options = document.getElementsByClassName('select-options')
      console.log(event.target)
      let select = options[event.target.name]
      if (select.selectedIndex === 2) {
        options[event.target.name].disabled = true
        event.target.disabled = true
      }
      let targetName = event.target.name
      let pk = this.events[targetName].pk
      let url = '/api/events/' + pk + '/'
      let kaistpk = 'kaist' + pk
      let postechpk = 'postech' + pk
      let kaist = document.getElementsByName(kaistpk)[0].value
      let postech = document.getElementsByName(postechpk)[0].value
      let live = select.selectedIndex
      console.log(kaist, postech, live)
      let winner = 0
      if (live === 2) {
        console.log('live')
        if (kaist > postech) {
          winner = 1
        } else if (kaist < postech) {
          winner = 2
        }
      }
      this.$http.post(url, JSON.stringify({
        'live': live,
        'score_k': kaist,
        'score_p': postech,
        'pk': pk,
        'winner': winner
      }))
        .then((response) => {
          console.log('save successfully')
        })
    }
  }
}
</script>

<style>
@import '../../../node_modules/bulma/css/bulma.css';
#events {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top:10px;
}

.head {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 20px;
}

.internal-event {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 10px;
  width:100%;
}

.event-name {
}

.event-status {
  margin-right: 300px;
}

.input-score {
  width: 80px;
}

.select {
  margin: 0 20px;
  z-index: 0;
}

</style>
