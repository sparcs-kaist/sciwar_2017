<template>
  <div class="supporters-write noto-sans">
    <div class="head">서포터즈 신청 수정
      <p>양식의 내용을 확인해주세요</p>
    </div>
    <div class="team-name">
      <label>팀 이름</label>
      <input name="team-name" v-bind:value="reg.fields.nickname">
    </div>
    <div class="team-contact">
      <label>대표자 연락처</label>
      <input name="contact" v-bind:value="reg.fields.contact">
    </div>
    <div class="team-password">
      <label>비밀번호</label>
      <input name="password" type="password" placeholder="기본값: 1234">
    </div>
    <div class="member">
      <button v-on:click="addClick()" class="member-add">멤버 추가</button>
      <button v-on:click="deleteClick()" class="member-add">멤버 삭제</button>
      <p class="count">{{ click + supporters.length }}명</p>
    </div>
    <div class="supporter-block">
      <div v-for="supporter in supporters" v-bind:style="styleSupporter" class="supporter">
        <label>이름</label>
        <input name="name" v-bind:style="styleInput" v-bind:value="supporter.fields.name"><br>
        <label>학번</label>
        <input name="studentID" v-bind:style="styleInput" v-bind:value="supporter.fields.student_id"><br>
        <label>학과</label>
        <input name="department" v-bind:style="styleInput" v-bind:value="supporter.fields.department"><br>
        <label>티셔츠 사이즈</label>
        <select class="T-shirt">
          <option :selected="supporter.fields.size === 1">XS</option>
          <option :selected="supporter.fields.size === 2">S</option>
          <option :selected="supporter.fields.size === 3">M</option>
          <option :selected="supporter.fields.size === 4">L</option>
          <option :selected="supporter.fields.size === 5">XL</option>
          <option :selected="supporter.fields.size === 6">XXL</option>
        </select>
      </div>
      <div v-for="n in click" v-bind:style="styleSupporter" class="supporter">
        <label>이름</label>
        <input name="name" v-bind:style="styleInput"><br>
        <label>학번</label>
        <input name="studentID" v-bind:style="styleInput"><br>
        <label>학과</label>
        <input name="department" v-bind:style="styleInput"><br>
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
    </div>
    <router-link :to="{ name: 'supporters' }">
      <button class="submit" v-on:click="submit">제출</button>
    </router-link>
    <router-link :to="{ name: 'supporters' }">
      <button class="del" v-on:click="del">삭제</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'supporters_mod',
  data () {
    return {
      reg: {},
      supporters: [],
      click: 0,
      styleSupporter: {
        backgroundColor: '#efefef',
        borderRadius: '5px',
        width: '230px',
        margin: '15px 15px 0 0',
        padding: '10px 7px 10px 17px',
        fontSize: '24px'
      },
      styleInput: {
        margin: '-10px 0 0 10px',
        width: '130px',
        fontSize: '15px',
        display: 'inline-block'
      }
    }
  },
  created () {
    let uri = '/api/supporters/complete/' + this.$route.params.id + '/'
    this.$http.get(uri)
      .then((response) => {
        this.reg = JSON.parse(response.data['reg'])[0]
        this.supporters = JSON.parse(response.data['supporters'])
      })
  },
  methods: {
    addClick: function () {
      this.click++
    },
    deleteClick: function () {
      if (this.click > 0) {
        this.click--
      } else if (this.click === 0 && this.supporters.length > 0) {
        this.supporters.pop()
      }
    },
    submit: function () {
      let nickname = document.getElementsByName('team-name')[0].value
      let contact = document.getElementsByName('contact')[0].value
      let password = document.getElementsByName('password')[0].value
      let nameList = document.getElementsByName('name')
      let studentIDList = document.getElementsByName('studentID')
      let departmentList = document.getElementsByName('department')
      let sizeList = document.getElementsByClassName('T-shirt')
      let supporterList = []
      for (let i = 0; i < nameList.length; i++) {
        let name = nameList[i].value
        let studentID = studentIDList[i].value
        let department = departmentList[i].value
        let size = sizeList[i].selectedIndex
        let supporter = { 'name': name, 'studentID': studentID, 'department': department, 'size': size }
        supporterList.push(supporter)
      }
      let crypto = require('crypto')
      let shasum = crypto.createHash('sha256')
      shasum.update(password)
      password = shasum.digest('hex')
      let data = { 'pk': this.reg.pk, 'nickname': nickname, 'contact': contact, 'password': password, 'supporters': supporterList }
      data = JSON.stringify(data)
      this.$http.post('/api/supporters/', data)
        .then((response) => {
          console.log('successful')
        })
    },
    del: function () {
      this.$http.delete('/api/supporters/' + this.$route.params.id + '/')
        .then((response) => {
          console.log('successful')
        })
    }
  }
}
</script>

<style>
.head {
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 20px;
  margin-bottom: 1.5rem;
}

.head > p {
  font-size: 32px;
  font-weight: 400;
}

.team-name {
  padding-bottom: 15px;
}

.team-name > label {
  font-size: 28px;
  margin-right: 20px;
  width: 200px;
  display: inline-block;
}

.team-name > input {
  font-size: 24px;
  font-weight: 200;
}

.team-contact {
  padding-bottom: 15px;
}

.team-contact > label {
  font-size: 28px;
  margin-right: 20px;
  display: inline-block;
  width: 200px;
}

.team-contact > input {
  font-size: 24px;
  font-weight: 200;
}

.team-password {
  padding-bottom: 20px;
}

.team-password > label {
  font-size: 28px;
  margin-right: 20px;
  width: 200px;
  display: inline-block;
}

.team-password > input {
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

.member {
  display: flex;
  margin-bottom: 10px;
}

.member > button {
  margin-right: 15px;
}

.member > p {
  margin-left: 10px;
  margin-top: -2px;
  font-size: 28px;
}

.submit {
  margin-top: 30px;
}

.supporter-block {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.del {
  margin-left: 10px;
  margin-top: 30px;
}
</style>
