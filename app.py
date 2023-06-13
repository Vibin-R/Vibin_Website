from flask import Flask,render_template

app = Flask(__name__)

PROJECTS = [{
 'name' : 'Web Phishing Detection',
  'summary' : 'Detect the ilegal scam websites',
    'link' : 'projlink'},
            {
 'name' : 'Solar Tracking System',
  'summary' : 'Detect the movement of the sun',
    'link' : 'projlink'},
            {
 'name' : 'RFID Tracker',
  'summary' : 'Security system that based on RFID',
    'link' : 'projlink'}]

@app.route('/')
def hello():
  return render_template('index.html',project=PROJECTS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)