from flask import Flask, redirect, url_for, render_template, request
import psycopg2
import os

app=Flask(__name__,static_url_path='/static',static_folder='static')

DB_NAME = os.environ.get('DB_NAME', 'database1')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'Achanandhi')
DB_HOST = os.environ.get('DB_HOST', 'database1.cqio6rophgrr.ap-south-1.rds.amazonaws.com')
DB_PORT = os.environ.get('DB_PORT', '5432')


def connect_db():
    conn=psycopg2.connect(
        database= DB_NAME,
        user= DB_USER,
        password= DB_PASSWORD,
        host= DB_HOST,
        port= DB_PORT
    )
    return conn



def create_cursor():
    conn=connect_db()
    cur=conn.cursor()
    return conn,cur

def close_db(conn,cur):
    cur.close()
    conn.close()
    return conn,cur


def init_db():
    conn,cur=create_cursor()
    cur.execute('''
       CREATE TABLE IF NOT EXISTS user_details (
        name VARCHAR(255) PRIMARY KEY,
        quote TEXT NOT NULL,
        advice TEXT NOT NULL
    )   
''')
    conn.commit()
    close_db(conn,cur)


def create_user_data(name,quote,advice):
    conn,cur=create_cursor()
    cur.execute("INSERT INTO user_details (name,quote,advice) VALUES (%s,%s,%s)",(name,quote,advice))
    conn.commit()
    close_db(conn,cur)


init_db()


@app.route('/',methods=['POST','GET'])
def input():
    if request.method=='POST':
        name=request.form['username']
        quote=request.form['quote']
        advice=request.form['advice']
        if name and quote and advice:
            create_user_data(name,quote,advice)
            return redirect(url_for('output'))
        else:
            return "please fill out all fields"
    return render_template('index.html')



@app.route('/output',methods=['GET'])
def output():
    return render_template('response.html')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
