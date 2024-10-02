import mysql.connector
from flask import Flask,request,redirect,url_for,render_template

app = Flask(__name__)

# database connection funtion

def get_db_connection():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'contact_db'
    )

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute('INSERT INTO contacts (name,email,message) VALUES (%s,%s,%s)',
                (name,email,message))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return 'Thank you for your message!'




if __name__ == '__main__':
    app.run(debug=True)
