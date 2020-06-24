import MySQLdb

conn = MySQLdb.connect(
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
    return result

if __name__ == "__main__":
    app.run(debug=true)
