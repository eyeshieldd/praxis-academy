from flask import Flask, render_template, request
import mysql.connector as mariadb

app = Flask(__name__)
@app.route('/')
def list():
    conn=mariadb.connect(user='jojo', password='123', database='coba')
    cur=conn.cursor()
    cur.execute("select * from member")
    rows=cur.fetchall()
    return render_template("home.html" , rows=rows)
  
    
if __name__ == '__main__':
    app.run(debug=True)
