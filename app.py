from flask import Flask
import db

app = Flask(__name__)
app.teardown_appcontext(db.close_db_con)

@app.route('/') #ist immer die Einstiegsseite, die aufgerufen wird, wenn man die URL der Webseite eingibt
def index(): #dies wird aufgerufen, wenn die Route '/' aufgerufen wird
    return 'Hello, World! check it out!'

@app.route('/lists/')
def lists():
    db_con =db.get_db_con()
    sql_query = 'SELECT * FROM list'
    list_entries = db_con.execute(sql_query).fetchall()
    return render_template('lists.html', lists=list_entries)
    return 'Todo: implement lists'    

@app.route('/lists/<int:id>/')
def list(id):
    return f'Todo: implement list {id}'