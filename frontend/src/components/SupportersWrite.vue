<template>
  <div class="supporters-write noto-sans">
    <div class="head">서포터즈 신청하기
      <p>아래의 칸을 채워주세요</p>
    </div>
    <div class="team-name">
      <label>Team name</label>
      <input name="team-name">
    </div>
    <div class="team-password">
      <label>Password</label>
      <input name="team-password" type="password">
    </div>
    <div class="member">
      <button v-on:click="addClick()" class="member-add">멤버 추가</button>
      <button v-on:click="deleteClick(click)" class="member-add">멤버 삭제</button>
      <p class="count">{{ click }}명</p>
    </div>
    <div class="supporter-block">
      <div v-for="n in click" v-bind:style="styleSupporter" class="supporter">
        <label>Name</label>
        <input name="member-name" v-bind:style="styleInput"><br>
        <label>Gender</label>
        <select name="member-sex" v-bind:style="styleInput2" v-on:change="setLeader2(n, $event.target.selectedIndex)">
          <option selected>Male</option>
          <option>Female</option>
        </select>
        <br>
        <label>Student ID</label>
        <input name="member-id" v-bind:style="styleInput"><br>
        <label>Department</label>
        <input name="member-department" v-bind:style="styleInput"><br>
        <label>Phone</label>
        <input name="member-contact" v-bind:style="styleInput3"><br>
        <label>T-shirt size</label>
        <select name="member-size" v-bind:style="styleInput2">
          <option selected>XS(80)</option>
          <option>S(85)</option>
          <option>M(90)</option>
          <option>L(95)</option>
          <option>XL(100)</option>
          <option>XXL(105)</option>
          <option>XXXL(110)</option>
        </select>
        <br>
        <label v-if="checkLeader(n)" name="member-leader" style="font-weight:bold">Leader</label>
        <label v-else name="member-leader" v-on:click="setLeader(n)" style="cursor:pointer">Set to leader</label>
      </div>
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
      click: 0,
      currentLeaderF: 1,
      currentLeaderM: 1,
      styleSupporter: {
        backgroundColor: '#efefef',
        borderRadius: '5px',
        width: '280px',
        margin: '15px 15px 0 0',
        padding: '10px 7px 10px 17px',
        fontSize: '19px'
      },
      styleInput: {
        margin: '0 0 0 10px',
        width: 'calc(100% - 120px)',
        fontSize: '14px',
        display: 'inline-block',
        float: 'right'
      },
      styleInput2: {
        position: 'relative',
        top: '2px',
        margin: '0px 0 0 10px',
        fontSize: '15px',
        display: 'inline-block',
        float: 'right'
      },
      styleInput3: {
        margin: '0px 0 0 10px',
        width: 'calc(100% - 120px)',
        fontSize: '15px',
        display: 'inline-block',
        float: 'right'
      }
    }
  },
  created () {
  },
  methods: {
    addClick () {
      if (this.click === 12) {
        alert('한 팀에 최대 12명을 동륵할 수 있습니다.')
        return
      }
      this.click++
    },
    deleteClick (n) {
      let sex = document.getElementsByName('member-sex')[n - 1].selectedIndex
      if (this.checkLeader(n)) {
        if (sex) this.currentLeaderF = this.findSameSexLeader(n, sex)
        else this.currentLeaderM = this.findSameSexLeader(n, sex)
      }

      if (this.click > 0) {
        this.click--
      }
    },
    checkLeader (n) {
      if (this.currentLeaderM === n || this.currentLeaderF === n) return true
      return false
    },
    setLeader (n) {
      if (document.getElementsByName('member-sex')[n - 1].selectedIndex === 0) {
        if (this.currentLeaderM === this.currentLeaderF) this.currentLeaderF = n
        this.currentLeaderM = n
      } else {
        if (this.currentLeaderM === this.currentLeaderF) this.currentLeaderM = n
        this.currentLeaderF = n
      }
    },
    setLeader2 (n, sex) {
      if (sex) {
        if (document.getElementsByName('member-sex')[this.currentLeaderF - 1].selectedIndex !== sex) this.currentLeaderF = n
        if (this.currentLeaderM === n) this.currentLeaderM = this.findSameSexLeader(n, 0)
      } else {
        if (document.getElementsByName('member-sex')[this.currentLeaderM - 1].selectedIndex !== sex) this.currentLeaderM = n
        if (this.currentLeaderF === n) this.currentLeaderF = this.findSameSexLeader(n, 1)
      }
    },
    findSameSexLeader (n, sex) {
      let i = 1
      while (i <= this.click) {
        if (i !== n && document.getElementsByName('member-sex')[i - 1].selectedIndex === sex) return i
        ++i
      }
      if (sex) return this.currentLeaderM
      else return this.currentLeaderF
    },
    submit () {
      let teamName = document.getElementsByName('team-name')[0].value
      let teamPassword = document.getElementsByName('team-password')[0].value

      let nameList = document.getElementsByName('member-name')
      let sexList = document.getElementsByName('member-sex')
      let idList = document.getElementsByName('member-id')
      let departmentList = document.getElementsByName('member-department')
      let contactList = document.getElementsByName('member-contact')
      let sizeList = document.getElementsByName('member-size')
      let members = []

      let i = 0
      while (i < this.click) {
        let member = {
          'name': nameList[i].value,
          'sex': sexList[i].selectedIndex,
          'studentID': idList[i].value,
          'department': departmentList[i].value,
          'contact': contactList[i].value,
          'size': sizeList[i].selectedIndex,
          'isLeader': this.checkLeader(i + 1)
        }
        members.push(member)
        ++i
      }

      let crypto = require('crypto')
      let shasum = crypto.createHash('sha256')
      shasum.update(teamPassword)
      teamPassword = shasum.digest('hex')
      let data = { 'teamName': teamName, 'password': teamPassword, 'supporters': members }
      data = JSON.stringify(data)
      let url = '/api/supporters/'
      this.$http.put(url, data)
        .then((response) => {
          console.log(response)
          alert(response.data)
        })
    }
  }
}
</script>

<style scoped>
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

.supporter-block {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.submit {
  margin-top: 30px;
}
</style>
