from flask import *
import pymysql.cursors

pymysql.install_as_MySQLdb()
app = Flask(__name__)

conn = pymysql.connect(
 user='root',
 passwd='passwordmysql',
 host='localhost',
 db='tutorial')

cur = conn.cursor()

sql = "select * from users"
cur.execute(sql)

result = cur.fetchall()

cur.close
conn.close

from lamp_0 import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({cursor.description[i][0]: data[0][i]
                    for i in range(0, len(data[0]))})

if __name__ == "__main__":
    app.run(debug=true)
