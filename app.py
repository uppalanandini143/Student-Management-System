from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Student Management System Working!</h1><h3>Demo URL Success!</h3><a href='/students'>View Students</a>"

@app.route('/students')
def students():
    return "<h2>Student List</h2><p>1. Nandini</p><p>2. Demo Student</p><a href='/'>Home</a>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
