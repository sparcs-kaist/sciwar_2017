<template>
  <div class="toto noto-sans">
    <label class="control-label">Student ID</label>
    <input name="student_id" class="form-controll-small" onchange="show_formbutton()" placeholder="ex)20999999">
    <label class="control-label">Name</label>
    <input name="name" class="form-controll-small" onchange="show_formbutton()" placeholder="ex)김카이">
		<div class="toto-content">
			<h2 class="table-title">스포츠 종목 점수맞추기</h2>
			<table class="toto-table board-table">
				<thead>
					<tr>
						<th></th>
						<th>KAIST</th>
						<th>POSTECH</th>
						<th>WINNER</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>Football</td>
						<td><input name="score1_1" placeholder="ex)4" onchange="get_winner1()"></td>
						<td><input name="score1_2" placeholder="ex)0" onchange="get_winner1()"></td>
						<td class="winner"><span name="winner1">NONE</span></td>
					</tr>
					<tr>
						<td>Baseball</td>
						<td><input name="score2_1" placeholder="ex)12" onchange="get_winner2()"></td>
						<td><input name="score2_2" placeholder="ex)1" onchange="get_winner2()"></td>
						<td class="winner"><span name="winner2">NONE</span></td>
					</tr>
					<tr>
						<td>Basketball</td>
						<td><input name="score3_1" placeholder="ex)67" onchange="get_winner3()"></td>
						<td><input name="score3_2" placeholder="ex)51" onchange="get_winner3()"></td>
						<td class="winner"><span name="winner3">NONE</span></td>
					</tr>
					<tr>
						<td>League of Legend</td>
						<td><input name="score4_1" placeholder="ex)3" onchange="get_winner4()"></td>
						<td><input name="score4_2" placeholder="ex)0" onchange="get_winner4()"></td>
						<td class="winner"><span name="winner4">NONE</span></td>
					</tr>
				</tbody>
			</table>
			<h2 class="table-title">과학경기 승패 맞추기</h2>
			<table class="toto-table board-table quater">
				<thead>
					<tr>
						<th></th>
						<th>KAIST win</th>
						<th>POSTECH win</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>Science Quiz</td>
						<td><input type="radio" class="radio-button" name="winner5" value="1"></td>
						<td><input type="radio" class="radio-button" name="winner5" value="2"></td>
					</tr>
					<tr>
						<td>AI</td>
						<td><input type="radio" class="radio-button" name="winner6" value="1"></td>
						<td><input type="radio" class="radio-button" name="winner6" value="2"></td>
					</tr>
					<tr>
						<td>Hacking Contest</td>
						<td><input type="radio" class="radio-button" name="winner7" value="1"></td>
						<td><input type="radio" class="radio-button" name="winner7" value="2"></td>
					</tr>
				</tbody>
			</table>
		</div>
		<input class="board-button right form-button button is-primary" type="submit" value="Apply" disabled/>
  </div>
</template>

<script>
export default {
  name: 'toto'
}
</script>

<style>
.toto-content {
  width:100%;
}

.form-controll-small {
  display: block;
  height: 34px;
  padding-left: 6px;
  padding-right: 6px;
  color: #555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: inset 0 1px 1px rgba(0,0,0,.085);
  transition: border-color ease-in-out .15s, bax-shadow ease-in-out .15s;
  margin: 10px 0 20px 15px;
}

.form-controll-small:focus {
  border-color: #66afe9;
  outline: 0;
}

.table-title{
  margin-bottom:10px;
  margin-left:15px;
}

.toto-table {
  width: -moz-calc(100% - 32px) !important;
  width: -webkit-calc(100% - 32px) !important;
  width: calc(100% - 32px) !important;
  margin-right: 15px;
  margin-left: 15px;
}

.toto-table>tbody>tr>td>input {
  display: inline-block;
  height: 34px;
  padding-left: 6px;
  padding-right: 6px;
  color: #555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: inset 0 1px 1px rgba(0,0,0,.085);
  transition: border-color ease-in-out .15s, bax-shadow ease-in-out .15s;
}

.winner {
  width: 100px;
}

.quater>thead>tr, .quater>tbody>tr {
  width: 100%;
}

.quater>thead>tr>th, .quater>tbody>tr>td {
  width:25%;
}

.form-button:disabled {
  background-color:#D2D2D2;
  border:#DDDDDD;
  cursor:auto;
}

h2 {
  font-size: 30px;
  margin-top: 40px;
}

thead > tr > th {
  padding-bottom: 10px;
}

tbody > tr > td {
  padding-bottom: 10px;
}

input[type="radio"] {
  box-shadow: none !important;
}
</style>
