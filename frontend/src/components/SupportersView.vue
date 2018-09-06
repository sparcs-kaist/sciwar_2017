<template>
  <div class="supporters-view noto-sans">
    <div v-if="vif" class="classified">
      <div class="head">서포터즈 조회하기</div>
      <label>작성하실 때 사용하신 비밀번호를 입력해주세요</label><br>
      <input type="password" name="password" v-model="password">
      <button v-on:click="show()">확인</button>
    </div>
    <div v-else-if="velseif" class="supporter-reg">
      <div class="head">서포터즈 조회하기</div>
      <table class="team-info">
        <tr>
          <th>Team name</th>
          <td>{{ supporterTeam.fields.name }}</td>
        </tr>
        <tr>
          <th>Members</th>
          <td class="supporter-list">
            <ul v-for="member in members" class="supporter-info">{{ member.fields.name }} {{ showLeader(member.fields.is_leader) }}
              <li>{{ sex[member.fields.sex] }}</li>
              <li class="student-id">{{ member.fields.student_id }}</li>
              <li>{{ member.fields.department }}</li>
              <li>{{ member.fields.contact }}</li>
              <li>Size {{ size[member.fields.size] }}</li>
            </ul>
          </td>
        </tr>
      </table>
      <div class="link-container">
        <router-link :to="{ name: 'supporters' }" class="link link1">목록으로</router-link>
        <button type="button" class="link link2" v-on:click="showMod">수정하기</button>
      </div>
    </div>
    <div v-else-if="edit" class="supporter-mod">
      <div class="head">서포터즈 신청 수정
        <p>양식의 내용을 확인해주세요</p>
      </div>
      <div class="team-name">
        <label>Team name</label>
        <input name="team-name" v-bind:value="supporterTeam.fields.name" />
      </div>
      <div class="team-password">
        <label>Password</label>
        <input name="team-password" type="password" v-model="password"/>
      </div>
      <div class="members">
        <button v-on:click="addClick()" class="member-add">멤버 추가</button>
        <button v-on:click="deleteClick(members.length + click)" class="member-add">멤버 삭제</button>
        <p class="count">{{ click + members.length }}명</p>
      </div>
      <div class="supporter-block">
        <div v-for="(member,index) in members" v-bind:style="styleMember" class="supporter">
          <label>Name</label>
          <input name="member-name" v-bind:style="styleInput" v-bind:value="member.fields.name"><br>
          <label>Gender</label>
          <select name="member-sex" v-bind:style="styleInput2" v-on:change="setLeader2(index + 1, $event.target.selectedIndex)">
            <option :selected="member.fields.sex === 0">Male</option>
            <option :selected="member.fields.sex === 1">Female</option>
          </select>
          <br />
          <label>Student ID</label>
          <input name="member-id" v-bind:style="styleInput" v-bind:value="member.fields.student_id"><br>
          <label>Department</label>
          <input name="member-department" v-bind:style="styleInput" v-bind:value="member.fields.department"><br>
          <label>Phone</label>
          <input name="member-contact" v-bind:style="styleInput3" v-bind:value="member.fields.contact"><br>
          <label>T-shirt size</label>
          <select name="member-size" v-bind:style="styleInput2">
            <option :selected="member.fields.size === 0">XS(80)</option>
            <option :selected="member.fields.size === 1">S(85)</option>
            <option :selected="member.fields.size === 2">M(90)</option>
            <option :selected="member.fields.size === 3">L(95)</option>
            <option :selected="member.fields.size === 4">XL(100)</option>
            <option :selected="member.fields.size === 5">XXL(105)</option>
            <option :selected="member.fields.size === 6">XXXL(110)</option>
          </select>
          <br />
          <label v-if="checkLeader(index + 1)" name="member-leader" style="font-weight: bold">Leader</label>
          <label v-else v-on:click="setLeader(index + 1)" name="member-leader" style="cursor: pointer">Set to leader</label>
        </div>
        <div v-for="n in click" v-bind:style="styleMember" class="supporter">
          <label>Name</label>
          <input name="member-name" v-bind:style="styleInput"><br>
          <label>Gender</label>
          <select name="member-sex" v-bind:style="styleInput2" v-on:change="setLeader2(members.length + n, $event.target.selectedIndex)">
            <option>Male</option>
            <option>Female</option>
          </select>
          <br />
          <label>Student ID</label>
          <input name="member-id" v-bind:style="styleInput"><br>
          <label>Department</label>
          <input name="member-department" v-bind:style="styleInput"><br>
          <label>Phone</label>
          <input name="member-contact" v-bind:style="styleInput3"><br>
          <label>T-shirt size</label>
          <select name="member-size" v-bind:style="styleInput2">
            <option>XS(80)</option>
            <option>S(85)</option>
            <option>M(90)</option>
            <option>L(95)</option>
            <option>XL(100)</option>
            <option>XXL(105)</option>
            <option>XXXL(110)</option>
          </select>
          <br />
          <label v-if="checkLeader(members.length + n)" name="member-leader" style="font-weight: bold">Leader</label>
          <label v-else name="member-leader" v-on:click="setLeader(members.length + n)" style="cursor: pointer">Set to leader</label>
        </div>
      </div>
      <router-link :to="{ name: 'supporters' }">
        <button class="submit" v-on:click="submit">제출</button>
      </router-link>
      <router-link :to="{ name: 'supporters' }">
        <button class="del" v-on:click="del">삭제</button>
      </router-link>
  </div>
</div>
</template>

<script>
export default {
  name: 'supporters_view',
  data () {
    return {
      password: '',
      theRightPassword: '',
      certified: false,
      edit: false,
      click: 0,
      supporterTeam: {},
      members: [],
      currentLeaderM: 1,
      currentLeaderF: 1,
      styleMember: {
        backgroundColor: '#efefef',
        borderRadius: '5px',
        width: '280px',
        margin: '15px 15px 0 0',
        padding: '10px 7px 10px 17px',
        fontSize: '20px'
      },
      styleInput: {
        margin: '0 0 0 10px',
        width: 'calc(100% - 125px)',
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
        width: 'calc(100% - 125px)',
        fontSize: '15px',
        display: 'inline-block',
        float: 'right'
      },
      size: ['80', '85', '90', '95', '100', '105', '110'],
      sex: ['남', '여']
    }
  },
  created () {
    let uri = '/api/supporters/' + this.$route.params.id + '/'
    this.$http.get(uri)
      .then((response) => {
        this.theRightPassword = JSON.parse(response.data)[0]
        this.theRightPassword = this.theRightPassword.fields.password
      })
  },
  computed: {
    vif () {
      this.certified
      this.edit
      return !this.certified && !this.edit
    },
    velseif () {
      this.certified
      this.edit
      return this.certified && !this.edit
    }
  },
  methods: {
    show: function () {
      let crypto = require('crypto')
      let shasum = crypto.createHash('sha256')
      let password = document.getElementsByName('password')[0].value
      shasum.update(password)
      password = shasum.digest('hex')
      if (password === this.theRightPassword) {
        this.loadComplete()
      } else {
        alert('비밀번호가 틀렸습니다.')
      }
    },
    loadComplete: function () {
      let uri = '/api/supporters/complete/' + this.$route.params.id + '/'
      this.$http.get(uri)
        .then((response) => {
          this.supporterTeam = JSON.parse(response.data['supporter_team'])[0]
          this.members = JSON.parse(response.data['members'])
          for (let i = 0; i < this.members.length; i++) {
            if (this.members[i].fields.sex === 1 && this.members[i].fields.is_leader) this.currentLeaderF = i + 1
            if (this.members[i].fields.sex === 0 && this.members[i].fields.is_leader) this.currentLeaderM = i + 1
          }
          this.certified = true
        })
    },
    showMod: function () {
      this.edit = true
    },
    print: function () {
      console.log(this.members[0])
    },
    addClick: function () {
      if (this.click + this.members.length === 12) {
        alert('한 팀에 최대 12명을 동륵할 수 있습니다.')
        return
      }
      this.click++
    },
    deleteClick: function (n) {
      let sex = document.getElementsByName('member-sex')[n - 1].selectedIndex
      if (this.checkLeader(n)) {
        if (sex) this.currentLeaderF = this.findSameSexLeader(n, sex)
        else this.currentLeaderM = this.findSameSexLeader(n, sex)
      }

      if (this.click > 0) {
        this.click--
      } else if (this.click === 0 && this.members.length > 0) {
        this.members.pop()
      }
    },
    checkLeader: function (n) {
      if (this.currentLeaderM === n || this.currentLeaderF === n) return true
      return false
    },
    setLeader: function (n) {
      if (document.getElementsByName('member-sex')[n - 1].selectedIndex === 0) {
        if (this.currentLeaderM === this.currentLeaderF) this.currentLeaderF = n
        this.currentLeaderM = n
      } else {
        if (this.currentLeaderM === this.currentLeaderF) this.currentLeaderM = n
        this.currentLeaderF = n
      }
    },
    setLeader2: function (n, sex) {
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
      while (i <= this.members.length + this.click) {
        if (i !== n && document.getElementsByName('member-sex')[i - 1].selectedIndex === sex) return i
        ++i
      }
      if (sex) return this.currentLeaderM
      else return this.currentLeaderF
    },
    submit: function () {
      let teamName = document.getElementsByName('team-name')[0].value
      let teamPassword = document.getElementsByName('team-password')[0].value

      let nameList = document.getElementsByName('member-name')
      let idList = document.getElementsByName('member-id')
      let departmentList = document.getElementsByName('member-department')
      let contactList = document.getElementsByName('member-contact')
      let sexList = document.getElementsByName('member-sex')
      let sizeList = document.getElementsByName('member-size')
      let supporterList = []
      for (let i = 0; i < nameList.length; i++) {
        let memberName = nameList[i].value
        let memberId = idList[i].value
        let memberDepartment = departmentList[i].value
        let memberContact = contactList[i].value
        let memberSex = sexList[i].selectedIndex
        let memberSize = sizeList[i].selectedIndex
        let memberIsLeader = this.checkLeader(i + 1)
        let supporter = {
          'name': memberName,
          'sex': memberSex,
          'studentID': memberId,
          'department': memberDepartment,
          'contact': memberContact,
          'size': memberSize,
          'isLeader': memberIsLeader
        }
        supporterList.push(supporter)
      }

      let crypto = require('crypto')
      let shasum = crypto.createHash('sha256')
      shasum.update(teamPassword)
      teamPassword = shasum.digest('hex')
      let data = { 'pk': this.supporterTeam.pk, 'teamName': teamName, 'password': teamPassword, 'supporters': supporterList }
      data = JSON.stringify(data)
      this.$http.post('/api/supporters/', data)
        .then((response) => {
          console.log(response.data)
          alert(response.data)
        })
    },
    del: function () {
      this.$http.delete('/api/supporters/' + this.$route.params.id + '/')
        .then((response) => {
          console.log('successful')
        })
    },
    showLeader: function (bool) {
      if (bool) return '/ 조장'
      return ''
    }
  }
}

</script>

<style scoped>
.head {
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 20px;
  margin-bottom: 1.5rem;
}

.classified {
  display: block;
  font-size: 28px;
}

.classified > input {
  font-size: 20px;
}

.classified > button {
  background-color: #555555;
  text-align: center;
  font-size: 20px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
}

.team-info > tr {
  height: 30px;
}

.team-info > tr > th {
  font-size: 32px;
  width: 230px;
}

.team-info > tr > td {
  font-size: 28px;
}

.supporter-list {
   display: flex;
   flex-direction: row;
   flex-wrap: wrap;
 }

 .supporter-info {
   border-radius: 10px;
   background-color: #efefef;
   margin-right: 10px;
   margin-top: 10px;
   width: 200px;
   padding: 10px 10px 10px 10px;
   text-align: center;
   font-size: 28px;
 }

 .supporter-info > li {
   font-size: 20px;
   font-weight: 300;
   margin: 0 auto;
 }

.link {
  background-color: #555555;
  text-align: center;
  font-size: 22px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
  height: 40px;
}

.link-container {
  margin-top: 20px;
  width: 25%;
}

.link1 {
  float: left;
}

.link2 {
  float: right;
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

.members {
  display: flex;
  margin-bottom: 10px;
}

.members > button {
  margin-right: 15px;
  background-color: #555555;
  text-align: center;
  font-size: 20px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
}

.members > p {
  margin-left: 10px;
  margin-top: -2px;
  font-size: 28px;
}

.submit {
  margin-top: 30px;
  background-color: #555555;
  text-align: center;
  font-size: 20px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
}

.supporter-block {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.del {
  margin-left: 10px;
  margin-top: 30px;
  background-color: #555555;
  text-align: center;
  font-size: 20px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
}
</style>
