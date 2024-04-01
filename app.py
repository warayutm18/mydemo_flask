from flask import Flask,render_template,request,redirect, url_for
import requests

app = Flask (__name__)

std_usr = None

@app.route('/home')
def index():
    login()
    return render_template("index.html",pp = std_usr)

@app.route('/engskill')
def engskill():
    return render_template("engskill.html")

@app.route('/digiskill')
def digiskill():
    return render_template("digiskill.html")

@app.route('/contact')
def Contact():
    return render_template("contact.html")
@app.route('/engscore')
def engcore():
    login()
    x = 'https://db.snru.ac.th/api-mysql/ept_getby_stdid/'
    y = std_usr
    z = x+y
    response = requests.get(z, verify=False)
    if response.status_code == 200:
        data = response.json()
        print(data[0]['student_id'])
    else:
        print('การร้องขอไม่สำเร็จ: ', response.status_code)

    return render_template("engscore.html",mydata = data)
  

@app.route('/', methods=['POST','GET'])
def login():
    global std_usr
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        std_usr = username
        return render_template('index.html')
        '''if username == '64102122143' and password == "1234":
            return render_template('index.html')
        else:
            return render_template('login.html')'''

    else:
        return render_template('login.html')
           

   

if __name__== "__main__":
    app.run(debug=True)

