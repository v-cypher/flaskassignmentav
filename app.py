from flask import Flask, render_template,request
import mysql.connector


app = Flask(__name__)

@app.route('/')
def entry():
	return render_template('index.html')

@app.route('/users',methods=['POST','GET'])
def result(): 
	mydb=mysql.connector.connect(
						host="remotemysql.com", 
						user="mfr1x74hEB",
						password="seO0CMfiMd",
						database="mfr1x74hEB"
								)
	"""mydb=mysql.connector.connect(
											host="localhost", 
											user="root",
											password="",
											database="webinar_registration"
											)"""
	mycursor=mydb.cursor()
	if request.method == 'POST':
		result = request.form.to_dict()
		fullname = result['fullname']
		email = result['email']
		phone = int(result['phone'])
		college = result['college']
		mycursor.execute("INSERT INTO participants(fullname, email, phone, college) VALUES (%s,%s,%s,%s)",(fullname, email, phone, college))
		mydb.commit()
		mycursor.close()
		return render_template('users.html',result=result)
	return render_template("index.html")

	

@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html")

if __name__=="__main__":
	app.run(debug=True)
