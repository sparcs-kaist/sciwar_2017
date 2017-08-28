<template>
  <div class="noto-sans">
    <div class="head">응원의 한마디 남기기</div>
    <div class="first-form">
      <p class="question">하실 말씀을 적어주세요!&nbsp; &nbsp; &nbsp; {{ message.length }}자/140자</p>
      <textarea v-model="message" v-on:keyup="lengthCheck()"></textarea>
    </div>
    <div class="second-form">
      <p class="question">응원하는 학교</p>
      <select id="school-selector" class="selector">
        <option value="1" selected>KAIST</option>
        <option value="2">POSTECH</option>
      </select>
    </div>
    <div class="third-form">
      <p class="question">응원하는 경기</p>
      <select id="event-selector" class="selector">
        <option value="3" selected>축구</option>
        <option value="4">인공지능</option>
        <option value="5">롤</option>
        <option value="6">야구</option>
        <option value="7">과학퀴즈</option>
        <option value="8">농구</option>
        <option value="10">모두에게</option>
      </select>
    </div>
    <router-link :to="{ name: 'cheermessage' }">
      <button class="submit-button" v-on:click="submit()">쓰기</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'cheermessage-write',
  data () {
    return {
      message: ''
    }
  },
  methods: {
    lengthCheck: function () {
      if (this.message.length > 140) {
        alert('글자수는 140자 이하로 해주세요!')
        this.message = this.message.substr(0, 140)
        return 1
      }
      return 0
    },
    submit: function () {
      if (this.lengthCheck()) {
        return
      }
      let content = this.message
      let school = document.getElementById('school-selector').value
      let event = document.getElementById('event-selector').value
      let data = { 'content': content, 'school': school, 'event': event }
      data = JSON.stringify(data)
      this.$http.put('/api/cheermessage/', data)
        .then((response) => {
          console.log('success')
        })
    }
  }
}
</script>

<style>
.head{
   font-size: 64px;
   font-weight: 700;
   padding-bottom: 10px;
   margin-bottom: 1.5rem;
}

.question {
  font-size: 32px;
  padding-bottom: 15px;
}

.first-form > textarea {
  width:500px;
  height:250px;
  font-size: 28px;
  font-weight: 200;
}

.first-form {
  margin-bottom: 30px;
  margin-left: 15px;
}

.second-form {
  margin-bottom: 30px;
  margin-left: 15px;
}

.third-form {
  margin-bottom: 30px;
  margin-left: 15px;
}

.selector {
  font-size: 28px;
  font-weight: 200;
}

.submit-button {
  margin-left: 15px;
  background-color: #555555;
  text-align: center;
  font-size: 20px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 9px;
}
</style>
