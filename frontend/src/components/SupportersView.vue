<template>
  <div class="supporters-view noto-sans">
    <div v-if="vif" class="classified">
      <div class="head">서포터즈 조회하기</div>
      <label>작성하실 때 사용하신 비밀번호를 입력해주세요</label><br>
      <input type="password" name="password">
      <button v-on:click="show()">확인</button>
    </div>
    <div v-else-if="velseif" class="supporter-reg">
      <div class="head">서포터즈 조회하기</div>
      <table class="team-info">
        <tr>
          <th>팀 이름</th>
          <td>{{ supporterTeam.fields.name }}</td>
        </tr>
        <tr>
          <th>대표자 연락처</th>
          <td>{{ supporterTeam.fields.contact }}</td>
        </tr>
        <tr>
          <th>멤버</th>
          <td class="supporter-list">
            <ul v-for="member in members" class="supporter-info">{{ member.fields.name }} {{ showLeader(member.fields.is_leader) }}
              <li>{{ sex[member.fields.sex] }}</li>
              <li class="student-id">{{ member.fields.student_id }}</li>
              <li>{{ member.fields.department }}</li>
              <li>사이즈 {{ size[member.fields.size] }}</li>
            </ul>
          </td>
        </tr>
      </table>
      <div class="link-container">
        <router-link :to="{ name: 'supporters' }" class="link link1">목록으로</router-link>
      </div>
    </div>
    <div v-else-if="edit" class="supporter-mod">
      <div class="head">서포터즈 신청 수정
        <p>양식의 내용을 확인해주세요</p>
      </div>
      <div class="team-name">
        <label>팀 이름</label>
        <input name="team-name" v-bind:value="supporterTeam.fields.name" />
      </div>
      <div class="team-contact">
        <label>대표자 연락처</label>
        <input name="team-contact" v-bind:value="supporterTeam.fields.contact" />
      </div>
      <div class="team-password">
        <label>비밀번호</label>
        <input name="team-password" v-bind:value="supporterTeam.fields.password" />
      </div>
      <div class="members">
        <button v-on:click="addClick(); print()" class="member-add">멤버 추가</button>
        <button v-on:click="deleteClick()" class="member-add">멤버 삭제</button>
        <p class="count">{{ click + members.length }}명</p>
      </div>
      <div class="supporter-block">
        <div v-for="member in members" v-bind:style="styleMember" class="supporter">
          <label>이름</label>
          <input name="member-name" v-bind:style="styleInput" v-bind:value="member.fields.name"><br>
          <label>성별</label>
          <select name="member-sex" v-bind:style="styleInput2">
            <option :selected="member.fields.sex === 0">남성</option>
            <option :selected="member.fields.sex === 1">여성</option>
          </select>
          <label>학번</label>
          <input name="member-id" v-bind:style="styleInput" v-bind:value="member.fields.student_id"><br>
          <label>학과</label>
          <input name="member-department" v-bind:style="styleInput" v-bind:value="member.fields.department"><br>
          <label>티셔츠 사이즈</label>
          <select name="member-size" v-bind:style="styleInput2">
            <option :selected="supporter.fields.size === 0">85</option>
            <option :selected="supporter.fields.size === 1">90</option>
            <option :selected="supporter.fields.size === 2">95</option>
            <option :selected="supporter.fields.size === 3">100</option>
            <option :selected="supporter.fields.size === 4">105</option>
            <option :selected="supporter.fields.size === 5">110</option>
          </select>
          <label v-if="member.fields.is_leader">조장</label>
          <label v-else v-on:click="setLeader(this.members.indexOf(member) + 1)">조장으로 하기</label>
        </div>
        <div v-for="n in click" v-bind:style="styleMember" class="supporter">
          <label>이름</label>
          <input name="member-name" v-bind:style="styleInput"><br>
          <label>성별</label>
          <select name="member-sex">
            <option>남성</option>
            <option>여성</option>
          </select>
          <label>학번</label>
          <input name="member-id" v-bind:style="styleInput"><br>
          <label>학과</label>
          <input name="member-department" v-bind:style="styleInput"><br>
          <label>티셔츠 사이즈</label>
          <select name="member-size">
            <option>85</option>
            <option>90</option>
            <option>95</option>
            <option>100</option>
            <option>105</option>
            <option>110</option>
          </select>
          <label v-if="member.fields.is_leader">조장</label>
          <label v-else v-on:click="setLeader(this.members.length + n)">조장으로 하기</label>
        </div>
      <router-link :to="{ name: 'supporters' }">
        <button class="submit" v-on:click="submit">제출</button>
      </router-link>
      <router-link :to="{ name: 'supporters' }">
        <button class="del" v-on:click="del">삭제</button>
      </router-link>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'supporters_view',
  data () {
    return {
      theRightPassword: '',
      certified: false,
      edit: false,
      click: 0,
      supporterTeam: {},
      members: [],
      currentLeaderM: {},
      currentLeaderF: {},
      styleSupporter: {
        backgroundColor: '#efefef',
        borderRadius: '5px',
        width: '260px',
        margin: '15px 15px 0 0',
        padding: '10px 7px 10px 17px',
        fontSize: '24px'
      },
      styleInput: {
        margin: '-10px 0 0 10px',
        width: 'calc(100% - 83px)',
        fontSize: '15px',
        display: 'inline-block'
      },
      styleInput2: {
        position: 'relative',
        top: '-2px',
        margin: '0px 0 0 10px',
        fontSize: '15px',
        display: 'inline-block'
      },
      size: ['85', '90', '95', '100', '105', '110'],
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
      this.click++
    },
    deleteClick: function () {
      if (this.click > 0) {
        this.click--
      } else if (this.click === 0 && this.members.length > 0) {
        this.members.pop()
      }
    },
    setLeader: function (n) {

    },
    submit: function () {
      let teamName = document.getElementsByName('team-name')[0].value
      let teamContact = document.getElementsByName('team-contact')[0].value
      let teamPassword = document.getElementsByName('team-password')[0].value

      let nameList = document.getElementsByName('member-name')
      let idList = document.getElementsByName('member-id')
      let departmentList = document.getElementsByName('member-department')
      let sexList = document.getElementsByName('member-sex')
      let sizeList = document.getElementsByName('member-size')
      let supporterList = []
      for (let i = 0; i < nameList.length; i++) {
        let memberName = nameList[i].value
        let memberId = idList[i].value
        let memberDepartment = departmentList[i].value
        let memberSex = sexList[i].selectedIndex
        let memberSize = sizeList[i].selectedIndex
        let supporter = { 'name': memberName, 'sex': memberSex, 'studentID': memberId, 'department': memberDepartment, 'size': memberSize }
        supporterList.push(supporter)
      }

      let crypto = require('crypto')
      let shasum = crypto.createHash('sha256')
      shasum.update(teamPassword)
      teamPassword = shasum.digest('hex')
      let data = { 'pk': this.supporterTeam.pk, 'teamName': teamName, 'contact': teamContact, 'password': teamPassword, 'supporters': supporterList }
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
   width: 180px;
   padding: 10px 10px 10px 10px;
   text-align: center;
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
}

.link-container {
  margin-top: 20px;
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

.member {
  display: flex;
  margin-bottom: 10px;
}

.member > button {
  margin-right: 15px;
  background-color: #555555;
  text-align: center;
  font-size: 20px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
}

.member > p {
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
