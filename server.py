from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'somthing is wrong'


def write_to_file(data):
    with open('db.csv', newline='', mode='a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        csv_writer.writerow([email, subject, message])




