<template>
  <div class="toto noto-sans">
    <label class="control-label">Student ID</label>
    <input v-model="studentId" name="student_id" class="form-controll-small" placeholder="ex)20999999" v-on:keyup="check()">
    <label class="control-label">Name</label>
    <input v-model="name" name="name" class="form-controll-small" placeholder="ex)김카이" v-on:keyup="check()">
    <label class="control-label">Password</label>
    <input v-model="password" type="password" name="password" class="form-controll-small" v-on:keyup="check()">
		<div class="toto-content">
			<table class="toto-table board-table">
				<thead>
					<tr>
						<th></th>
						<th>KAIST</th>
						<th>POSTECH</th>
						<th>WINNER</th>
					</tr>
				</thead>
				<tbody>
          <tr v-for="event in events" v-if="event.fields.type !== 2">
            <td>{{ event.fields.name_kor }}</td>
            <td><input :id="event.fields.name_eng.concat('K')" placeholder="ex)3" v-on:keyup="getWinner(event.fields.name_eng);"></td>
						<td><input :id="event.fields.name_eng.concat('P')" placeholder="ex)0" v-on:keyup="getWinner(event.fields.name_eng);"></td>
            <td class="winner"><span :id="event.fields.name_eng.concat('Winner')">NONE</span></td>
          </tr>
				</tbody>
			</table>
		</div>
    <router-link :to="{ name: 'toto' }">
      <button v-on:click="submit()" class="board-button right form-button button is-primary" :disabled="!checkSubmit">제출</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'toto',
  data () {
    return {
      studentId: '',
      name: '',
      password: '',
      events: [],
      toto: [],
      checkSubmit: false
    }
  },
  created () {
    this.$http.get('/api/events/')
      .then((response) => {
        this.events = JSON.parse(response.data)
      })
  },
  methods: {
    check () {
      if (!this.studentId || !this.name || !this.password) {
        this.checkSubmit = false
        return
      }
      for (let event of this.events) {
        if (event.fields.type !== 2) {
          if (!document.getElementById(event.fields.name_eng.concat('K')).value || !document.getElementById(event.fields.name_eng.concat('P')).value) {
            this.checkSubmit = false
            return
          }
          if (isNaN(document.getElementById(event.fields.name_eng.concat('K')).value) || isNaN(document.getElementById(event.fields.name_eng.concat('P')).value)) {
            this.checkSubmit = false
            return
          }
        }
      }
      this.checkSubmit = true
    },
    getWinner (name) {
      var scoreK = parseInt(document.getElementById(name.concat('K')).value)
      var scoreP = parseInt(document.getElementById(name.concat('P')).value)
      if (scoreK > scoreP) {
        document.getElementById(name.concat('Winner')).innerHTML = 'KAIST'
      } else if (scoreK < scoreP) {
        document.getElementById(name.concat('Winner')).innerHTML = 'POSTECH'
      } else {
        document.getElementById(name.concat('Winner')).innerHTML = 'NONE'
      }
      this.check()
    },
    appendToto (event) {
      var eventToto = {}
      if (event.fields.type === 2) return
      eventToto['event'] = event.pk
      eventToto[`${event.fields.name_eng}K`] = parseInt(document.getElementById(event.fields.name_eng.concat('K')).value)
      eventToto[`${event.fields.name_eng}P`] = parseInt(document.getElementById(event.fields.name_eng.concat('P')).value)
      eventToto[`${event.fields.name_eng}Winner`] = document.getElementById(event.fields.name_eng.concat('Winner')).innerHTML
      return eventToto
    },
    submit () {
      let crypto = require('crypto')
      let shasum = crypto.createHash('sha256')
      shasum.update(this.password)
      this.toto = this.events.map(this.appendToto)
      this.toto = this.toto.filter(function (item) {
        return item
      })
      console.log(this.toto)
      let data = { 'studentID': this.studentId, 'name': this.name, 'password': shasum.digest('hex'), 'toto': this.toto }
      data = JSON.stringify(data)
      console.log(data)
      let url = '/api/toto/'
      this.$http.put(url, data)
        .then((response) => {
          alert(response.data)
        })
    }
  }
}
</script>

<style scoped>
.toto-content {
  width:100%;
}

.form-controll-small {
  display: block;
  height: 34px;
  padding-left: 6px;
  padding-right: 6px;
  color: #555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: inset 0 1px 1px rgba(0,0,0,.085);
  transition: border-color ease-in-out .15s, bax-shadow ease-in-out .15s;
  margin: 10px 0 20px 15px;
}

.form-controll-small:focus {
  border-color: #66afe9;
  outline: 0;
}

.table-title{
  margin-bottom:10px;
  margin-left:15px;
}

.toto-table {
  width: -moz-calc(100% - 32px) !important;
  width: -webkit-calc(100% - 32px) !important;
  width: calc(100% - 32px) !important;
  margin-right: 15px;
  margin-left: 15px;
}

.toto-table>tbody>tr>td>input {
  display: inline-block;
  height: 34px;
  padding-left: 6px;
  padding-right: 6px;
  color: #555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: inset 0 1px 1px rgba(0,0,0,.085);
  transition: border-color ease-in-out .15s, bax-shadow ease-in-out .15s;
}

.winner {
  width: 100px;
}

.quater>thead>tr, .quater>tbody>tr {
  width: 100%;
}

.quater>thead>tr>th, .quater>tbody>tr>td {
  width:25%;
}

.form-button:disabled {
  background-color: #555555 !important;
  border:#DDDDDD;
  cursor:auto;
}

.form-button {
  background-color: black !important;
}

h2 {
  font-size: 30px;
  margin-top: 40px;
}

thead > tr > th {
  padding-bottom: 10px;
}

tbody > tr > td {
  padding-bottom: 10px;
}

input[type="radio"] {
  box-shadow: none !important;
}
</style>
