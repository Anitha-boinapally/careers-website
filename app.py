print("Hello")
from flask import Flask,render_template,jsonify
app=Flask(__name__)
JOBS=[
{
  'id':1,
  'Role':'Data Analyst',
  'location':'Hyd,India'
},
{
  'id':2,
  'Role':'Data Analyst',
  'location':'Hyd,India'
},
{
  'id':3,
  'Role':'Data Analyst',
  'location':'Hyd,India'
}
]
@app.route("/")
def hello_world():
   return render_template('home.html',jobs=JOBS)
@app.route("/jobs")
def list_of_jobs():
  return jsonify(JOBS)
print(__name__)
if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)