<template>
  <div class="toto-view noto-sans">
    <div class="head">토토 조회하기</div>
    <div v-if="!certified" class="classified">
      <label>작성하실 때 사용하신 비밀번호를 입력해주세요</label><br>
      <input type="password" name="password">
      <button v-on:click="show()">확인</button>
    </div>
    <div v-if="certified" class="toto-content-view">
      <label class="control-label">Student ID</label>
      <input v-model="studentId" name="student_id" class="form-controll-small" v-on:keyup="showFormButton()" disabled>
      <label class="control-label">Name</label>
      <input v-model="name" name="name" class="form-controll-small" v-on:keyup="showFormButton()" disabled>
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
              <td><input v-model="scoreSoccerK" disabled></td>
              <td><input v-model="scoreSoccerP" disabled></td>
              <td class="winner"><span name="winnerSoccer">{{ winnerSoccer }}</span></td>
            </tr>
            <tr>
              <td>Baseball</td>
              <td><input v-model="scoreBaseballK" disabled></td>
              <td><input v-model="scoreBaseballP" disabled></td>
              <td class="winner"><span name="winnerBaseball">{{ winnerBaseball }}</span></td>
            </tr>
            <tr>
              <td>Basketball</td>
              <td><input v-model="scoreBasketballK" disabled></td>
              <td><input v-model="scoreBasketballP" disabled></td>
              <td class="winner"><span name="winnerBasketball">{{ winnerBasketball }}</span></td>
            </tr>
            <tr>
              <td>League of Legend</td>
              <td><input v-model="scoreLolK" disabled></td>
              <td><input v-model="scoreLolP" disabled></td>
              <td class="winner"><span name="winnerLol">{{ winnerLol }}</span></td>
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
              <td><input v-model="winnerQuiz" type="radio" class="radio-button" value="KAIST" disabled></td>
              <td><input v-model="winnerQuiz" type="radio" class="radio-button" value="POSTECH" disabled></td>
            </tr>
            <tr>
              <td>AI</td>
              <td><input v-model="winnerAI" type="radio" class="radio-button" value="KAIST" disabled></td>
              <td><input v-model="winnerAI" type="radio" class="radio-button" value="POSTECH" disabled></td>
            </tr>
            <tr>
              <td>Hacking Contest</td>
              <td><input v-model="winnerHacking" type="radio" class="radio-button" value="KAIST" disabled></td>
              <td><input v-model="winnerHacking" type="radio" class="radio-button" value="POSTECH" disabled></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'toto',
  data () {
    return {
      certified: false,
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
      winnerSoccer: 'None',
      winnerBaseball: 'None',
      winnerBasketball: 'None',
      winnerLol: 'None',
      winnerQuiz: 'KAIST',
      winnerAI: 'KAIST',
      winnerHacking: 'KAIST'
    }
  },
  created () {
    this.$http.get('/api/toto/' + this.$route.params.id + '/')
      .then((response) => {
        this.theRightPassword = JSON.parse(response.data)[0]
        this.theRightPassword = this.theRightPassword.fields.password
      })
  },
  methods: {
    show () {
      let crypto = require('crypto')
      let shasum = crypto.createHash('sha256')
      let password = document.getElementsByName('password')[0].value
      shasum.update(password)
      password = shasum.digest('hex')
      if (password === this.theRightPassword) {
        this.certified = true
        this.loadComplete()
      } else {
        alert('비밀번호가 틀렸습니다.')
      }
    },
    loadComplete () {
      this.$http.get('/api/toto/complete/' + this.$route.params.id + '/')
        .then((response) => {
          let data = JSON.parse(response.data)
          console.log(data)
          let schools = ['None', 'KAIST', 'POSTECH']
          this.studentId = data.studentId
          this.name = data.name
          this.scoreSoccerK = data.scoreSoccerK
          this.scoreSoccerP = data.scoreSoccerP
          this.scoreBaseballK = data.scoreBaseballK
          this.scoreBaseballP = data.scoreBaseballP
          this.scoreBasketballK = data.scoreBasketballK
          this.scoreBasketballP = data.scoreBasketballP
          this.scoreLolK = data.scoreLolK
          this.scoreLolP = data.scoreLolP
          this.winnerSoccer = schools[data.winnerSoccer]
          this.winnerBaseball = schools[data.winnerBaseball]
          this.winnerBasketball = schools[data.winnerBasketball]
          this.winnerLol = schools[data.winnerLol]
          this.winnerQuiz = schools[data.winnerQuiz]
          this.winnerAI = schools[data.winnerAI]
          this.winnerHacking = schools[data.winnerHacking]
        })
    }
  }
}
</script>

<style>
.head {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 20px;
}

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
  background-color:#D2D2D2;
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
