from flask import Flask, render_template, jsonify

app = Flask(__name__)
PROJECTS = [
   {
   'id' : 1,
   'title' : 'Kyle and Weber Wind  Design Project',
   'Project Type': 'Power World Software Design Project',
   'Description' : 'Power System Design Project',
},

{
   'id' : 2,
   'title' : 'Python Game Design Project',
   'Project Type': 'Python Programming Project',
   'Description' : 'Aim Trainer and Platformer Game Design',
},

{
   'id' : 3,
   'title' : 'Stadium Seat Design Project',
   'Project Type' : 'Controls Product Engineering Project',
   'Description' : 'Electrical and Controls Engineering Project',
},

{
   'id' : 4,
   'title' : 'Web Design  Design Project',
   'Project Type': 'Web Design Python Programming Project',
   'Description' : 'Computer Programming Project',
},




{
   'id' : 5,
   'title' : 'AutoCad Design Project',
   'Project Type': 'Building Design with AutoCad',
   'Description' : 'FreecodeCamp  Engineering Design Project',
}
]






@app.route("/")
def hello_Carl():
    return render_template('home.html', jobs = PROJECTS, person_name = 'Carl Mworia Njoroge')

@app.route("/api/jobs")
def list_jobs():
   return jsonify(PROJECTS)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug= True)