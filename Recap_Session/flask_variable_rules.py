from flask import Flask
app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome_name(name):
   return 'Welcome %s!' % name

if __name__ == '__main__':
   app.run(debug = True)
