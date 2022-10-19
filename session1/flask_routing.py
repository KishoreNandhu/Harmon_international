from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
   return 'Welcome everyone!!'

@app.route('/login')
def login_page():
   return 'This is login page!!'


@app.route('/logout')
def logout_page():
   return 'This is logout page!!'

if __name__ == '__main__':
   app.run()
