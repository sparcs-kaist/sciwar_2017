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
          <th>이름</th>
          <td>{{ supporter.fields.name }}</td>
        </tr>
        <tr>
          <th>학번</th>
          <td>{{ supporter.fields.student_id }}</td>
        </tr>
        <tr>
          <th>학과</th>
          <td>{{ supporter.fields.department }}</td>
        </tr>
        <tr>
          <th>연락처</th>
          <td>{{ supporter.fields.contact }}</td>
        </tr>
        <tr>
          <th>사이즈</th>
          <td>{{ size[supporter.fields.size] }}</td>
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
      <div class="supporter-name">
        <label>이름</label>
        <input name="supporter-name" v-bind:value="supporter.fields.name">
      </div>
      <div class="supporter-id">
        <label>학번</label>
        <input name="supporter-id" v-bind:value="supporter.fields.student_id">
      </div>
      <div class="supporter-department">
        <label>학과</label>
        <input name="supporter-department" v-bind:value="supporter.fields.department">
      </div>
      <div class="supporter-contact">
        <label>연락처</label>
        <input name="supporter-contact" v-bind:value="supporter.fields.contact">
      </div>
      <div class="supporter-password">
        <label>비밀번호</label>
        <input name="supporter-password" type="password" placeholder="기본값: 1234">
      </div>
      <div class="supporter-size">
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
      theRightPassword: '',
      certified: false,
      edit: false,
      supporter: {},
      size: ['XS', 'S', 'M', 'L', 'XL', 'XXL']
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
        this.certified = true
        this.loadComplete()
      } else {
        alert('비밀번호가 틀렸습니다.')
      }
    },
    loadComplete: function () {
      let uri = '/api/supporters/complete/' + this.$route.params.id + '/'
      this.$http.get(uri)
        .then((response) => {
          this.supporter = JSON.parse(response.data)[0]
        })
    },
    showMod: function () {
      this.edit = true
    },
    submit: function () {
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
      let data = { 'pk': this.supporter.pk, 'name': name, 'contact': contact, 'password': password, 'studentID': studentID, 'department': department, 'size': size }
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
  padding-bottom: 20px;
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
