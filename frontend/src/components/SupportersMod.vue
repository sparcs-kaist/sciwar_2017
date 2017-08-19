<template>
  <div class="supporters-write noto-sans">
    <div class="head">서포터즈 신청하기
      <p>아래의 칸을 채워주세요</p>
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
      <input name="password" type="password" v-bind:value="reg.fields.password">
    </div>
    <div class="member">
      <button v-on:click="addClick()" class="member-add">멤버 추가</button>
      <button v-on:click="deleteClick()" class="member-add">멤버 삭제</button>
      <p class="count">{{ click }}명</p>
    </div>
    <div class="supporter-block">
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
    let uri = '/api/supporters/complete/' + this.$route.params.id
    this.$http.get(uri)
      .then((response) => {
        this.reg = JSON.parse(response.data['reg'])[0]
        this.supporters = JSON.parse(response.data['supporters'])
        console.log(this.reg)
        console.log(this.supporters)
      })
  },
  methods: {
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
</style>
