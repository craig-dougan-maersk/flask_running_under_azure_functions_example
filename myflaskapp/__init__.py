from flask import Flask, render_template

app = Flask(__name__)
name = 'craig'

@app.route('/web/')
def home():
  return "<h1>Hello World</h1>"

@app.route('/web/index')
def webpage():
  return render_template('webpage.html', title='My page', myname=name)

if __name__ == "__main__":
  app.run(debug=True,port=8080)
