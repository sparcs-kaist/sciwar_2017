<template>
  <div class="supporters-write noto-sans">
    <div class="head">서포터즈 신청하기
      <p>아래의 칸을 채워주세요</p>
    </div>
    <div class="team-name">
      <label>팀 이름</label>
      <input name="team-name">
    </div>
    <div class="team-contact">
      <label>대표자 연락처</label>
      <input name="contact">
    </div>
    <div class="team-password">
      <label>비밀번호</label>
      <input name="password" type="password">
    </div>
    <div class="member">
      <button v-on:click="addClick()" class="member-add">멤버 추가</button>
      <button v-on:click="deleteClick()" class="member-add">멤버 삭제</button>
      <p class="count">{{ click }}명</p>
    </div>
    <div v-for="n in click" v-bind:style="styleSupporter" class="supporter">
      <label>이름</label>
      <input name="name"><br>
      <label>학번</label>
      <input name="studentID"><br>
      <label>학과</label>
      <input name="department"><br>
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
    <button class="submit" v-on:click="submit">제출</button>
  </div>
</template>

<script>
export default {
  name: 'supporters',
  data () {
    return {
      click: 0,
      styleSupporter: {
        border: '2px solid rgb(149, 179, 215)',
        borderRadius: '5px',
        width: '200px',
        margin: '10px 0 0 0',
        padding: '3px'
      }
    }
  },
  methods: {
    addClick () {
      this.click++
    },
    deleteClick () {
      if (this.click > 0) {
        this.click--
      }
    },
    submit () {
      let teamName = document.getElementsByName('team-name')[0].value
      let contact = document.getElementsByName('contact')[0].value
      let password = document.getElementsByName('password')[0].value
      console.log(teamName)
      console.log(contact)
      let nameList = document.getElementsByName('name')
      let studentIDList = document.getElementsByName('studentID')
      let departmentList = document.getElementsByName('department')
      let sizeList = document.getElementsByClassName('T-shirt')
      console.log(nameList)
      console.log(studentIDList)
      console.log(departmentList)
      console.log(sizeList)
      let supporters = []
      for (let i = 0; i < nameList.length; i++) {
        let name = nameList[i].value
        let studentID = studentIDList[i].value
        let department = departmentList[i].value
        let size = sizeList[i].selectedIndex
        let supporter = { 'name': name, 'studentID': studentID, 'department': department, 'size': size }
        supporters.push(supporter)
      }
      let data = { 'teamName': teamName, 'contact': contact, 'password': password, 'supporters': supporters }
      console.log(data)
      data = JSON.stringify(data)
      console.log(data)
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
  font-weight: 300;
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
  padding-bottom: 15px;
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
  margin-top: 20px;
}
</style>
