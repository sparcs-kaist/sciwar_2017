<template>
  <div class="toto noto-sans">
    <label class="control-label">Student ID</label>
    <input v-model="studentId" name="student_id" class="form-controll-small" v-on:keyup="showFormButton()" placeholder="ex)20999999">
    <label class="control-label">Name</label>
    <input v-model="name" name="name" class="form-controll-small" v-on:keyup="showFormButton()" placeholder="ex)김카이">
    <label class="control-label">Password</label>
    <input v-model="password" type="password" name="password" class="form-controll-small" v-on:keyup="showFormButton()">
		<div class="toto-content">
			<h2 class="table-title">스포츠 종목 점수맞추기</h2>
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
					<tr>
						<td>Soccer</td>
						<td><input v-model="scoreSoccerK" name="score1_1" placeholder="ex)4" v-on:keyup="getWinnerSoccer()"></td>
						<td><input v-model="scoreSoccerP" name="score1_2" placeholder="ex)0" v-on:keyup="getWinnerSoccer()"></td>
            <td class="winner"><span name="winnerSoccer">{{ winnerSoccer }}</span></td>
					</tr>
					<tr>
						<td>Baseball</td>
						<td><input v-model="scoreBaseballK" name="score2_1" placeholder="ex)12" v-on:keyup="getWinnerBaseball()"></td>
						<td><input v-model="scoreBaseballP" name="score2_2" placeholder="ex)1" v-on:keyup="getWinnerBaseball()"></td>
						<td class="winner"><span name="winnerBaseball">{{ winnerBaseball }}</span></td>
					</tr>
					<tr>
						<td>Basketball</td>
						<td><input v-model="scoreBasketballK" name="score3_1" placeholder="ex)67" v-on:keyup="getWinnerBasketball()"></td>
						<td><input v-model="scoreBasketballP" name="score3_2" placeholder="ex)51" v-on:keyup="getWinnerBasketball()"></td>
						<td class="winner"><span name="winnerBasketball">{{ winnerBasketball }}</span></td>
					</tr>
          <tr>
            <td>LOL</td>
            <td><input v-model="scoreLolK" name="score4_1" placeholder="ex)2" v-on:keyup="getWinnerLol()"></td>
            <td><input v-model="scoreLolP" name="score4_2" placeholder="ex)1" v-on:keyup="getWinnerLol()"></td>
            <td class="winner"><span name="winnerLol">{{ winnerLol }}</span></td>
          </tr>
          <tr>
            <td>AI</td>
            <td><input v-model="scoreAiK" name="score5_1" placeholder="ex)2" v-on:keyup="getWinnerAi()"></td>
            <td><input v-model="scoreAiP" name="score5_2" placeholder="ex)0" v-on:keyup="getWinnerAi()"></td>
            <td class="winner"><span name="winnerAi">{{ winnerAi }}</span></td>
          </tr>
				</tbody>
			</table>
			<h2 class="table-title">과학경기 승패 맞추기</h2>
			<table class="toto-table board-table quater">
				<thead>
					<tr>
						<th></th>
						<th>KAIST win</th>
						<th>POSTECH win</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>Science Quiz</td>
						<td><input v-model="winnerQuiz" type="radio" class="radio-button" value="KAIST"></td>
						<td><input v-model="winnerQuiz" type="radio" class="radio-button" value="POSTECH"></td>
					</tr>
					<tr>
						<td>Hacking Contest</td>
						<td><input v-model="winnerHacking" type="radio" class="radio-button" value="KAIST"></td>
						<td><input v-model="winnerHacking" type="radio" class="radio-button" value="POSTECH"></td>
					</tr>
				</tbody>
			</table>
		</div>
    <router-link :to="{ name: 'toto' }">
      <button v-on:click="submit()" class="board-button right form-button button is-primary" disabled>제출</button>
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
      scoreSoccerK: '',
      scoreSoccerP: '',
      scoreBaseballK: '',
      scoreBaseballP: '',
      scoreBasketballK: '',
      scoreBasketballP: '',
      scoreLolK: '',
      scoreLolP: '',
      scoreAiK: '',
      scoreAiP: '',
      winnerSoccer: 'None',
      winnerBaseball: 'None',
      winnerBasketball: 'None',
      winnerLol: 'None',
      winnerQuiz: 'KAIST',
      winnerAi: 'None',
      winnerHacking: 'KAIST'
    }
  },
  methods: {
    getWinnerSoccer () {
      if (parseInt(this.scoreSoccerK) > parseInt(this.scoreSoccerP)) {
        this.winnerSoccer = 'KAIST'
      } else if (parseInt(this.scoreSoccerK) < parseInt(this.scoreSoccerP)) {
        this.winnerSoccer = 'POSTECH'
      } else {
        this.winnerSoccer = 'None'
      }
      this.showFormButton()
    },
    getWinnerBaseball () {
      if (parseInt(this.scoreBaseballK) > parseInt(this.scoreBaseballP)) {
        this.winnerBaseball = 'KAIST'
      } else if (parseInt(this.scoreBaseballK) < parseInt(this.scoreBaseballP)) {
        this.winnerBaseball = 'POSTECH'
      } else {
        this.winnerBaseball = 'None'
      }
      this.showFormButton()
    },
    getWinnerBasketball () {
      if (parseInt(this.scoreBasketballK) > parseInt(this.scoreBasketballP)) {
        this.winnerBasketball = 'KAIST'
      } else if (parseInt(this.scoreBasketballK) < parseInt(this.scoreBasketballP)) {
        this.winnerBasketball = 'POSTECH'
      } else {
        this.winnerBasketball = 'None'
      }
      this.showFormButton()
    },
    getWinnerLol () {
      if (parseInt(this.scoreLolK) > parseInt(this.scoreLolP)) {
        this.winnerLol = 'KAIST'
      } else if (parseInt(this.scoreLolK) < parseInt(this.scoreLolP)) {
        this.winnerLol = 'POSTECH'
      } else {
        this.winnerLol = 'None'
      }
      this.showFormButton()
    },
    getWinnerAi () {
      if (parseInt(this.scoreAiK) > parseInt(this.scoreAiP)) {
        this.winnerAi = 'KAIST'
      } else if (parseInt(this.scoreAiK) < parseInt(this.scoreAiP)) {
        this.winnerAi = 'POSTECH'
      } else {
        this.winnerAi = 'None'
      }
      this.showFormButton()
    },
    showFormButton () {
      if (this.winnerSoccer !== 'None' &&
        this.winnerBaseball !== 'None' &&
        this.winnerBasketball !== 'None' &&
        this.winnerLol !== 'None' &&
        this.winnerAi !== 'None' &&
        this.studentId.length === 8 &&
        this.name !== '' &&
        this.password !== '') {
        document.getElementsByClassName('form-button')[0].disabled = false
      } else {
        document.getElementsByClassName('form-button')[0].disabled = true
      }
    },
    submit () {
      if (document.getElementsByClassName('form-button')[0].disabled === true) {
        alert('모든 칸을 바르게 채워주세요.')
        return
      }
      let crypto = require('crypto')
      let shasum = crypto.createHash('sha256')
      shasum.update(this.password)
      let data = { 'studentID': this.studentId, 'name': this.name, 'password': shasum.digest('hex'), 'scoreSoccerK': this.scoreSoccerK, 'scoreSoccerP': this.scoreSoccerP, 'scoreBaseballK': this.scoreBaseballK, 'scoreBaseballP': this.scoreBaseballP, 'scoreBasketballK': this.scoreBasketballK, 'scoreBasketballP': this.scoreBasketballP, 'winnerSoccer': this.winnerSoccer, 'winnerBaseball': this.winnerBaseball, 'winnerBasketball': this.winnerBasketball, 'scoreLolK': this.scoreLolK, 'scoreLolP': this.scoreLolP, 'winnerLol': this.winnerLol, 'winnerQuiz': this.winnerQuiz, 'scoreAiK': this.scoreAiK, 'scoreAiP': this.scoreAiP, 'winnerAI': this.winnerAi, 'winnerHacking': this.winnerHacking }
      data = JSON.stringify(data)
      let url = '/api/toto/'
      this.$http.put(url, data)
        .then((response) => {
          console.log('save successfully')
        })
    }
  }
}
</script>

<style>
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
  background-color: #555555;
  border:#DDDDDD;
  cursor:auto;
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
