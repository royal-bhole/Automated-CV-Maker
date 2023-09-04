from flask import Flask , render_template , request
from flask_ngrok import run_with_ngrok
app = Flask(__name__)

run_with_ngrok(app)

@app.route('/')
def student():
    return render_template('studentCV.html')

@app.route('/hello/' ,methods=['POST'])
def hello():
    name = request.form['uname']
    email = request.form['email']
    contact = request.form['contact']
    obj = request.form['obj']
    dob = request.form['dob']
    add = request.form['add']
    clg = request.form['clg']
    gpa = request.form['gpa']
    gpy = request.form['gpy']
    gpb = request.form['gpb']
    gps = request.form['gps']
    tp = request.form['tp']
    tpy = request.form['tpy']
    tpb = request.form['tpb']
    bp = request.form['bp']
    bpy = request.form['bpy']
    bpb = request.form['bpb']
    lang = request.form['lang']
    skill = request.form['skill']
    ec = request.form['ec']
    achievements = request.form['achievements']
    proj = request.form['proj']
    hob = request.form['hob']
    return render_template('cv.html' ,obj = obj , gpa = gpa,gps = gps ,contact = contact, gpb = gpb , achievements=achievements, uname = name , email = email , dob = dob , add = add,clg=clg,gpy=gpy,tp = tp,tpy=tpy,tpb=tpb,bp=bp,bpy=bpy,bpb=bpb,lang=lang,skill=skill,ec=ec,proj=proj,hob=hob)

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)
if __name__ == '__main__':
    app.run()

        # name = uname
        # email = email
        # contact = contact
        # date of birth = dob
        # address = add
        # Highest qualification = qual
        # Name of Institute = clg
        # CGPA = gp
        # Graduation passing year = gpy
        # 12th percentage = tp
        # 12th passing year = tpy
        # 12th passing = tpb
        # 12th passing subjects = tps
        # 10th percentage = bp
        # 10th passing year = bpy
        # 10th passing board = bpb
        # 10th passing subjects = bps
        # Languages known = lang
        # Skills = skills
        # any extra curricular activites = ec
        # Projects = proj
        # Hobbies = hob
        # Branch of interest = boi




























#Main data id's
        #name = uname
        #email = email
        #date of birth = dob
        #address = add
        #Highest qualification = qual
        #Name of Institute = clg
        #CGPA = gp
        #Graduation passing year = gpy
        #12th percentage = tp
        #12th passing year = tpy
        #12th passing = tpb
        #12th passing subjects = tps
        #10th percentage = bp
        #10th passing year = bpy
        #10th passing board = bpb
        #10th passing subjects = bps
        #Languages known = lang
        #Skills = skills
        #any extra curricular activites = ec
        #Projects = proj
        #Hobbies = hob
        #Branch of interest = boi
