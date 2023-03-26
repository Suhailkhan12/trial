from flask import Flask,render_template,request
import csv

app = Flask(__name__)





@app.route('/')
def contact():
    return render_template("index.html")


def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database:
        profile = data["image"]
        name = data["name"]
        user = data["email"]
        passw = data["password"]
        cpassw = data["confirm password"]
        while True:
            if passw != cpassw:
               return my_home()
            else:
               break

        csv_writer = csv.writer(database, delimiter=',', quotechar='|',quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([profile,name, user,passw,cpassw])


def my_home():
    return render_template("ero.html")

@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'Sign Up Succesfully'
    else:
        return 'something Wrong'
        




