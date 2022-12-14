from flask import Flask, request, redirect, render_template
from flask import session as login_session
import pyrebase
import random
import os

config = {
	"apiKey": "AIzaSyD7z3cUTWn7gCpBjd9HlRu84MU5_z6D4m4",
  	"authDomain": "rosemary-database.firebaseapp.com",
  	"databaseURL": "https://rosemary-database-default-rtdb.europe-west1.firebasedatabase.app",
  	"projectId": "rosemary-database",
  	"storageBucket": "rosemary-database.appspot.com",
  	"messagingSenderId": "1022436261843",
  	"appId": "1:1022436261843:web:98f13714b09255f241b926",
  	"measurementId": "G-45SE56F1MQ"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'



@app.route('/' , methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		user = request.form['user']
		passw = request.form['passw']
		if user == "admin" and passw == "admin1":
			return redirect('home')
		return redirect('/')




@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/add' , methods=['GET','POST'])
def add():
	if request.method == 'GET':
		return render_template('add.html' , data=[{'name':'Roza'}, {'name':'Hanan'}, {'name':'Sol'}, {'name':'Ameer'}, {'name':'Hamoodi'}, {'name':'Tarek'}, {'name':'Elias'}, {'name':'Waseem'}, {'name':'Ghassan'}, {'name':'Hisham'}, {'name':'William'}, {'name':'Jwan'} , {'name':'Tala'} , {'name':'Rosol'}] , data1=[{'time':'12:00'},{'time':'12:15'},{'time':'12:30'},{'time':'12:45'},{'time':'13:00'},{'time':'13:15'},{'time':'13:30'},{'time':'13:45'},{'time':'14:00'},{'time':'14:15'},{'time':'14:30'},{'time':'14:45'},{'time':'15:00'},{'time':'15:15'},{'time':'15:30'},{'time':'15:45'},{'time':'16:00'},{'time':'16:15'},{'time':'16:30'},{'time':'16:45'},{'time':'17:00'},{'time':'17:15'},{'time':'17:30'},{'time':'17:45'},{'time':'18:00'},{'time':'18:15'},{'time':'18:30'},{'time':'18:45'},{'time':'19:00'},{'time':'19:15'},{'time':'19:30'},{'time':'19:45'},{'time':'20:00'},{'time':'20:15'},{'time':'20:30'},{'time':'20:45'},{'time':'21:00'},{'time':'21:15'},{'time':'21:30'},{'time':'21:45'},{'time':'22:00'},{'time':'22:00 +'}])
	else:
		print("Creating Reservation Object")

		reserveObj = {
		"reserveName" : request.form['reserveName'],
		"fullName" : request.form['fullName'],
		"reserveTime" : request.form.get('comp_select1'),
		"reserveDay" : request.form['reserveDay'],
		"numOfpeople" : request.form.get('comp_select3'),
		"location" : request.form.get('comp_select2'),
		"phone_num" : request.form['phoneNum'],
		"waiterName" : request.form.get('comp_select'),
		"isEating" : request.form['isEating'],
		"closedMenu" : request.form['closedMenu'],
		"notes" : request.form['notes']
		}

		db.child("reservations").child(reserveObj["phone_num"]).set(reserveObj)
		#Make Object and send it to the databse

		print("Done!")
		return redirect('/home')


@app.route('/view' , methods=['GET' , 'POST'])
def view():
	if request.method == 'GET':
		res_list = []
		rese = db.child('reservations').get()
		for res in rese.each():
			res_list.append(res.val())
		return render_template('view.html' , Reservations = res_list)
	else:
		objId = request.form['deleteBtn']
		db.child("reservations").child(objId).remove()
		return redirect("/view")


if __name__ == '__main__':
	app.run(debug=True)


