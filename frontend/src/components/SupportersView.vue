<template>
  <div class="supporters-view noto-sans">
    <div class="head">서포터즈 조회하기</div>
    <div v-if="!certified" class="classified">
      <label>작성하실 때 사용하신 비밀번호를 입력해주세요</label><br>
      <input type="password" name="password">
      <button v-on:click="show()">확인</button>
    </div>
    <div v-if="certified" class="supporter-reg">
      <table class="team-info">
        <tr>
          <th>팀 이름</th>
          <td>{{ supporterReg.fields.nickname }}</td>
        </tr>
        <tr>
          <th>대표자 연락처</th>
          <td>{{ supporterReg.fields.contact }}</td>
        </tr>
        <tr>
          <th>멤버</th>
          <td class="supporter-list">
            <ul v-for="supporter in supporters" class="supporter-info">{{ supporter.fields.name }}
              <li class="student-id">{{ supporter.fields.student_id }}</li>
              <li>{{ supporter.fields.department }}</li>
              <li>사이즈 {{ supporter.fields.size }}</li>
            </ul>
          </td>
        </tr>
      </table>
      <div class="link-container">
        <router-link :to="{ name: 'supporters' }" class="link link1">목록으로</router-link>
        <router-link :to="{ name: 'supporters-mod' }" class="link link2">수정하기</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'supporters_view',
  data () {
    return {
      supporterReg: {},
      supporters: [],
      certified: false
    }
  },
  created () {
    let uri = '/api/supporters/' + this.$route.params.id
    this.$http.get(uri)
      .then((response) => {
        this.supporterReg = JSON.parse(response.data['reg'])[0]
        this.supporters = JSON.parse(response.data['supporters'])
      })
  },
  methods: {
    show: function () {
      if (document.getElementsByName('password')[0].value === this.supporterReg.fields.password) {
        this.certified = true
      } else {
        alert('비밀번호가 틀렸습니다.')
      }
    }
  }
}

</script>

<style>
.head {
  font-size: 64px;
  font-weight: 700;
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
  width: 150px;
  padding: 5px 9px 5px 9px;
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
  font-size: 20px;
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
</style>
