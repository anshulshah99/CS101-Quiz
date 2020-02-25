from flask import Flask, render_template, session, flash, redirect, url_for, request
import psycopg2
import datetime
import random
from collections import OrderedDict
#from flask_sqlalchemy import SQLAlchemy
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#import models
#import forms
#import copy

date_time = datetime.datetime.today()
app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
app.url_map.strict_slashes = False

"""
@app.route('/', methods = ["GET", 'POST'])
def login():
    sec_nums = ["Other (TA's, Non-enrolled students, etc)", "01L Fri 10:05-11:20 (Physics)", "02L Fri 11:45-1:00", "03L/07L Fri 1:25-2:40", "04L Fri 3:05-4:20", "05L/09L Thu 3:05-4:20", "06L Fri 10:05-11:20 (SocPsy)",
                "08L Thu 11:45-1:00", "10L Thu 1:25-2:40", "11L Thu 4:40-5:55"]
    #user = Request.remote_user["uid"]
    #print(user)

    #if request.method == 'POST':
        #section = request.form['lab sections']

        #session["netid"] = uid

        #cur.execute("SELECT netid FROM students;")
        #all = cur.fetchall()
        #users = [u[0] for u in all]
        #if netid not in set(users):
            #if section.startswith("Other"):

            #else:
                #cur.execute("INSERT INTO students VALUES (%s, %s, %s, %s);", (netid, email, name, int(section[0:2])))
        #return redirect(url_for('concept'))
    return render_template('login.html', sections = sec_nums)
    """
#https://pythonspot.com/flask-web-forms/
con = psycopg2.connect(dbname='test')#, user="anshul")#, host='localhost')
con.autocommit = True
cur = con.cursor()
#cur.execute("""ALTER TABLE responses ADD COLUMN semester VARCHAR;""")
@app.route('/', methods = ["GET", 'POST'])
def login():
    sec_nums = ["Other (TA's, Non-enrolled students, etc)", "01L Fri 10:05-11:20 (Physics)", "02L Fri 11:45-1:00", "03L/07L Fri 1:25-2:40", "04L Fri 3:05-4:20", "05L/09L Thu 3:05-4:20", "06L Fri 10:05-11:20 (SocPsy)",
                "08L Thu 11:45-1:00", "10L Thu 1:25-2:40", "11L Thu 4:40-5:55"]
    if request.method == 'POST':
        name = request.form['name']
        netid = request.form['netid']
        section = request.form['lab sections']
        session["netid"] = netid
        #session['netid'] = netid
        cur.execute("""SELECT netid FROM students""")
        all = cur.fetchall()
        users = [u[0] for u in all]
        if netid not in set(users):
            if section.startswith("Other"):
                cur.execute("""INSERT INTO students VALUES (%s, %s, %s, 0);""", (netid, netid+"@duke.edu""", name))
            else:
                cur.execute("""INSERT INTO students VALUES (%s, %s, %s, %s);""", (netid, netid+"@duke.edu""", name, int(section[0:2])))
        return redirect(url_for('concept', net = netid))
    return render_template('login.html', sections = sec_nums, a = "test", b = "hello")

@app.route('/concept', methods = ["GET", "POST"])
def concept():
    cur.execute("""Select Distinct concept FROM questions;""")
    concepts = cur.fetchall()
    choices = [c[0] for c in concepts]
    if request.method == "POST":
        x = list(dict(request.form).values())
        ret = [x[i][0] if type(x[i][0]) == str else x[i][0][0] for i in range(len(x))]
        num_ques = ret[-1]
        types = ret[0:-1]
        #if type(val) != str:
            #val = x['values'][0]
        session["question_type"] = types
        net = session["netid"]
        session["number_questions"] = num_ques
        return redirect(url_for("quiz"))

    return render_template('concept.html', concepts = choices, net = session['netid'])

@app.route('/quiz', methods = ["GET", "POST"])
def quiz():
    if request.method == "GET":
        types = session["question_type"]
        number = int(session["number_questions"])
        questions = []
        remaining = len(types)
        for each in types:
            cur.execute("""SELECT qid, text, correct_ans, wrong_ans_1, wrong_ans_2, wrong_ans_3 FROM questions WHERE concept = %s;""", (each,))
            ret = cur.fetchall()
            if type(ret[0]) == list:
                ret = [i[0] for i in ret]
            random.shuffle(ret)
            ret = ret[0:number//remaining]
            number = number - (number//remaining)
            remaining -= 1
            questions.extend(ret)
        qids = [questions[i][0] for i in range(len(questions))]
        final_questions = [questions[i][1].replace(r'\r\n', '<br>').replace(r'\n', '<br>') for i in range(len(questions))]
        final_answers = [questions[i][2:] for i in range(len(questions))]
        d = {}
        for i in range(len(final_questions)):
            q_ans = list(final_answers[i])
            random.shuffle(q_ans)
            q_ans.append(final_answers[i][0])
            q_ans.append(qids[i])
            d[final_questions[i]] = q_ans
        session["sent_ques"] = d
    netid = session["netid"]
    timestamp = date_time.strftime('%d-%m-%Y')
    if request.method == "POST":
        res = OrderedDict(request.form)
        #print(session["sent_ques"])
        session["responses"] = [(a, b, session["sent_ques"][a][5]) for (a, b) in res.items()]
        for k, v in res.items():
            cur.execute("""SELECT rid FROM Responses;""")
            responses = cur.fetchall()
            responses = [r[0] for r in responses]

            rid = max(responses) + 1
            qid = session["sent_ques"][k][5]
            cur.execute("""SELECT * FROM responses;""")
            cur.execute("""INSERT INTO responses VALUES (%s, %s, %s, %s, %s, %s );""", (rid, netid, qid, v, timestamp, "Spring 20"))
        #res is a dictionary with key = questions and value = response
        return redirect(url_for("quiz_answers"))

    return render_template('quiz.html', q = final_questions, o = d)

@app.route('/results', methods=["GET", 'POST'])
def quiz_answers():
    answers = OrderedDict()
    responses = OrderedDict()
    correctness = OrderedDict()
    for k, v, q in session["responses"]:
        responses[k] = v
        cur.execute("""SELECT correct_ans FROM Questions WHERE qid = (%s);""", (q,))
        correct = cur.fetchall()
        answers[k] = correct[0][0]
        if v == correct[0][0]:
            correctness[k] = "Correct"
        else:
            correctness[k] = "Incorrect"
    if request.method == "POST":
        next_dict = dict(request.form)
        if 'choose' in next_dict.keys():
            return redirect(url_for("concept"))
        if 'stay' in next_dict.keys():
            return redirect(url_for("quiz"))
    return render_template('results.html', q = responses, c = answers, o = correctness, a = responses)

@app.route('/instructor', methods=["GET", 'POST'])
def instructor():
    if request.method == "POST":
        next_dict = dict(request.form)
        if 'data' in next_dict.keys():
            return redirect(url_for("analyze"))
        if 'question' in next_dict.keys():
            return redirect(url_for("add_question"))
    return render_template('instructor.html')

@app.route('/analyze', methods=["GET", 'POST'])
def analyze():
    cur.execute("""SELECT count(*) FROM responses;""")
    total = cur.fetchall()
    cur.execute("""SELECT count(distinct netid) FROM responses;""")
    studs = cur.fetchall()
    cur.execute("""SELECT concept, count(*) FROM responses, questions WHERE responses.qid = questions.qid GROUP BY concept;""")
    counts = cur.fetchall()
    if request.method == "POST":
        next_dict = dict(request.form)
        if 'lab' in next_dict.keys():
            return redirect(url_for("select_lab"))
        if 'student' in next_dict.keys():
            return redirect(url_for("select_student"))
    return render_template('analyze.html', total = total[0][0], counts = counts, studs = studs[0][0])

@app.route('/lab', methods=["GET", 'POST'])
def select_lab():
    options = ["Section " + str(i) for i in range(1, 13)]
    options.append("All")
    cur.execute("""Select Distinct(concept) FROM questions""")
    concepts = cur.fetchall()
    concepts = [c[0] for c in concepts]
    #concepts.append("All")
    session['concepts'] = concepts
    if request.method == "POST":
        sections = dict(request.form)
        session["labs"] = list(sections.keys())
        return redirect(url_for("analyze_lab"))
    return render_template('select_lab.html', labs = options, con = concepts)

@app.route('/analyze_lab', methods=["GET", 'POST'])
def analyze_lab():
    cur.execute("""SELECT total_num.lab_section, total_num.concept, correct_num.total_correct, total_num.total_responses
    FROM
    /*total correct responses for a concept by lab section */
    (SELECT questions.concept, students.lab_section, COUNT(*) AS total_correct
    FROM responses, students, questions
    WHERE responses.netid = students.netID
    AND questions.qid = responses.qid
    AND responses.ans_choice = questions.correct_ans
    GROUP BY questions.concept, students.lab_section)
        AS correct_num, 

    /*total responses regardless of incorrect/correct for a concept by lab section */
    (SELECT questions.concept, students.lab_section, COUNT(*) AS total_responses
    FROM responses, students, questions
    WHERE responses.netid = students.netID
    AND questions.qid = responses.qid
    GROUP BY questions.concept, students.lab_section)
        AS total_num
    WHERE correct_num.lab_section = total_num.lab_section
    AND correct_num.concept = total_num.concept
    GROUP BY total_num.concept, total_num.lab_section, correct_num.total_correct, total_num.total_responses
    ORDER BY total_num.lab_section, total_num.concept;
    """)
    output = cur.fetchall()
    print(output)
    sections = list(session["labs"])
    if 'All' in sections:
        labs = set([i for i in range(1, 13)])
    else:
        labs = set([int(val.split()[1]) for val in sections if val not in set(session['concepts'])])
    chosen_concepts = set([val for val in sections if val in set(session['concepts'])])
    print(labs)
    final_output = [o for o in output if o[0] in labs and o[1] in chosen_concepts]
    return render_template('analyze_lab.html', labs = final_output)

@app.route('/select_student', methods=["GET", 'POST'])
def select_student():
    if request.method == "POST":
        student = dict(request.form)
        #print("*****")
        #print(student['netid'])
        #print("*****")
        session["student"] = student['netid']
        return redirect(url_for("analyze_student"))
    return render_template("select_student.html")

@app.route('/analyze_student', methods=["GET", 'POST'])
def analyze_student():
    student_netid = session['netid']
    if type(student_netid) != str:
        student_netid = session['netid'][0]
    cur.execute("""SELECT tot_num.netid, tot_num.concept, correct_num.tot_correct, tot_num.tot_responses 
    FROM (SELECT responses.netid, questions.concept, COUNT(*) as tot_correct
    FROM responses, questions
    WHERE questions.qid = responses.qid
    AND questions.correct_ans = responses.ans_choice
    GROUP BY responses.netid, questions.concept) as correct_num, (SELECT responses.netid, questions.concept, COUNT(*) as tot_responses
    FROM responses, questions
    WHERE questions.qid = responses.qid
    GROUP BY responses.netid, questions.concept) as tot_num
    WHERE correct_num.netid = tot_num.netid
    AND correct_num.concept = tot_num.concept
    AND tot_num.netid = (%s);""", (student_netid,))
    output = cur.fetchall()
    return render_template("analyze_student.html", student = output )

@app.route('/analyze_self', methods=["GET", 'POST'])
def analyze_self():
    student_netid = session['netid']
    if type(student_netid) != str:
        student_netid = session['student'][0]
    cur.execute("""SELECT tot_num.netid, tot_num.concept, correct_num.tot_correct, tot_num.tot_responses 
    FROM (SELECT responses.netid, questions.concept, COUNT(*) as tot_correct
    FROM responses, questions
    WHERE questions.qid = responses.qid
    AND questions.correct_ans = responses.ans_choice
    GROUP BY responses.netid, questions.concept) as correct_num, (SELECT responses.netid, questions.concept, COUNT(*) as tot_responses
    FROM responses, questions
    WHERE questions.qid = responses.qid
    GROUP BY responses.netid, questions.concept) as tot_num
    WHERE correct_num.netid = tot_num.netid
    AND correct_num.concept = tot_num.concept
    AND tot_num.netid = (%s);""", (student_netid,))
    output = cur.fetchall()
    return render_template("analyze_student.html", student = output )


@app.route('/add_question', methods=["GET", 'POST'])
def add_question():
    cur.execute("""Select Distinct concept FROM questions""")
    concepts = cur.fetchall()
    choices = [c[0] for c in concepts]
    if request.method == 'POST':
        val = request.form['values']
        #qtype = request.form['type']
        text = request.form['text']
        correct_ans = request.form['correct_ans']
        wrong1 = request.form['wrong_ans1']
        wrong2 = request.form['wrong_ans2']
        wrong3 = request.form['wrong_ans3']
        #if val == "None":
            #newtype = qtype
        #if val != "None":
            #newtype = val

        cur.execute("""Select qid FROM questions""")
        qids = set([q[0] for q in cur.fetchall()])
        i = random.randint(0, 1000000)
        while i in qids:
            i = random.randint(0, 1000000)
        session['qid'] = i
        cur.execute("""INSERT INTO Questions VALUES(%s, %s, %s, %s, %s, %s, %s, %s );""", (i, val, None, text, correct_ans, wrong1, wrong2, wrong3))
        return redirect("confirm_add_question")
    return render_template("add_question.html", concepts = choices)

@app.route('/confirm_add_question', methods=["GET", 'POST'])
def confirm_add_question():
    if request.method == "POST":
        next_dict = dict(request.form)
        if 'add' in next_dict.keys():
            return redirect(url_for("add_question"))
        if 'analyze' in next_dict.keys():
            return redirect(url_for("analyze"))
    return render_template("confirm_add_question.html", i=session['qid'])

##Change over time for each student/lab section


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    con.commit()