<template>
  <div class="supporters-write noto-sans">
    <div class="head">서포터즈 신청하기
      <p>아래의 칸을 채워주세요</p>
    </div>
    <div class="supporter-name">
      <label>이름</label>
      <input name="supporter-name">
    </div>
    <div class="supporter-id">
      <label>학번</label>
      <input name="supporter-id">
    </div>
    <div class="supporter-department">
      <label>학과</label>
      <input name="supporter-department">
    </div>
    <div class="supporter-contact">
      <label>연락처</label>
      <input name="supporter-contact">
    </div>
    <div class="supporter-password">
      <label>비밀번호</label>
      <input name="supporter-password" type="password">
    </div>
    <div class="supporter-size">
      <label>티셔츠 사이즈</label>
      <select class="T-shirt">
        <option>XS</option>
        <option>S</option>
        <option>M</option>
        <option>L</option>
        <option>XL</option>
        <option>XXL</option>
      </select>
    </div>
    <router-link :to="{ name: 'supporters' }">
      <button class="submit" v-on:click="submit">제출</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'supporters_write',
  data () {
    return {
    }
  },
  created () {
  },
  methods: {
    submit () {
      let name = document.getElementsByName('supporter-name')[0].value
      let contact = document.getElementsByName('supporter-contact')[0].value
      let password = document.getElementsByName('supporter-password')[0].value
      let studentID = document.getElementsByName('supporter-id')[0].value
      let department = document.getElementsByName('supporter-department')[0].value
      let size = document.getElementsByClassName('T-shirt')[0].selectedIndex
      let crypto = require('crypto')
      let shasum = crypto.createHash('sha256')
      shasum.update(password)
      password = shasum.digest('hex')
      let data = { 'name': name, 'contact': contact, 'password': password, 'studentID': studentID, 'department': department, 'size': size }
      data = JSON.stringify(data)
      let url = '/api/supporters/'
      this.$http.put(url, data)
        .then((response) => {
          console.log('save successfully')
        })
    }
  }
}
</script>

<style>
.head {
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 10px;
  margin-bottom: 1.5rem;
}

.head > p {
  font-size: 32px;
  font-weight: 400;
}

.supporter-name {
  padding-bottom: 15px;
}

.supporter-name > label {
  font-size: 28px;
  margin-right: 20px;
  width: 200px;
  display: inline-block;
}

.supporter-name > input {
  font-size: 24px;
  font-weight: 200;
}

.supporter-id {
  padding-bottom: 15px;
}

.supporter-id > label {
  font-size: 28px;
  margin-right: 20px;
  width: 200px;
  display: inline-block;
}

.supporter-id > input {
  font-size: 24px;
  font-weight: 200;
}

.supporter-department {
  padding-bottom: 15px;
}

.supporter-department > label {
  font-size: 28px;
  margin-right: 20px;
  width: 200px;
  display: inline-block;
}

.supporter-department > input {
  font-size: 24px;
  font-weight: 200;
}

.supporter-contact {
  padding-bottom: 15px;
}

.supporter-contact > label {
  font-size: 28px;
  margin-right: 20px;
  display: inline-block;
  width: 200px;
}

.supporter-contact > input {
  font-size: 24px;
  font-weight: 200;
}

.supporter-password {
  padding-bottom: 15px;
}

.supporter-password > label {
  font-size: 28px;
  margin-right: 20px;
  width: 200px;
  display: inline-block;
}

.supporter-password > input {
   font-size: 24px;
   font-weight: 200;
}

.supporter-size {
  padding-bottom: 20px;
}

.supporter-size > label {
  font-size: 28px;
  margin-right: 20px;
  width: 200px;
  display: inline-block;
}

.supporter-size > select {
   font-size: 24px;
   font-weight: 200;
}

.supporters-write button {
  background-color: #555555;
  text-align: center;
  font-size: 20px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
  margin-bottom: 10px;
}

.submit {
  margin-top: 30px;
}
</style>
