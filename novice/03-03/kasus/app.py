from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jojo'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'coba'
mysql = MySQL(app)
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * member")
    rv = cur.fetchall()
    return render_template('home.html', member=rv)
    
if __name__ == '__main__':
    app.run(debug=True)
