from app import app, db_conn

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"+db_conn.selectFrom("Select * from usr")
