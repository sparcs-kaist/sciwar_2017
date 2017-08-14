<template>
  <div class="supporters-write">
    <label>팀 이름</label>
    <input name="team-name"><br>
    <label>대표자 연락처</label>
    <input name="contact"><br>
    <label>비밀번호</label>
    <input name="password" type="password"><br>
    <button v-on:click="addClick()" class="member-add">멤버 추가</button>
    <button v-on:click="deleteClick()" class="member-add">멤버 삭제</button></button>
    {{ click }}명
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
    <button v-on:click="submit">submit</button>
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
</style>
