from flask import Flask, render_template, session, flash, redirect, url_for, request, Request
import flask
import psycopg2
from datetime import datetime
import random
import os
import sys
from collections import OrderedDict

app = Flask(__name__)

app.secret_key = 's3cr3t'
app.config.from_object('config')
app.url_map.strict_slashes = False

PSYCOPG2_POSTGRESQL_URI = 'postgres://cs101quizuser:9kys42tjlINgVFX1p8HD@localhost:5432/cs101quiz'

con = psycopg2.connect(PSYCOPG2_POSTGRESQL_URI)

con.autocommit = True
cur = con.cursor()

@app.route('/', methods = ["GET", "POST"])
def concept():
    email = flask.request.environ['REMOTE_USER']
    uname = flask.request.environ['displayName']
    uid = flask.request.environ['uid']
    session["uid"] = uid
    cur.execute("""SELECT netid FROM students;""")
    studs = cur.fetchall()
    students = [s[0] for s in studs]
    cur.execute("""Select concept, function FROM questions;""")
    concepts = set(cur.fetchall())
    temp = [c for c in concepts if str(c[0]) in ('Lists', 'Strings', 'Math operators')]
    choices = sorted([str(c[0]) if c[1] is None else str(c[0]) + " - " + str(c[1]) for c in temp])
    if request.method == "POST":
        x = list(dict(request.form).values())
        ret = [x[i].split(" - ") for i in range(len(x))]
        num_ques = ret[-1][0]
        types = ret[0:-1]
        session["question_type"] = types
        session["number_questions"] = num_ques
        return redirect(url_for("quiz"))
    return render_template('concept.html', concepts = choices)

@app.route('/quiz', methods = ["GET", "POST"])
def quiz():
    if request.method == "GET":
        types = session["question_type"]
        number = int(session["number_questions"])
        questions = []
        remaining = len(types)
        for each in types:
            cur.execute("""SELECT qid, text, correct_ans, wrong_ans_1, wrong_ans_2, wrong_ans_3 FROM questions WHERE concept = %s and function = %s;""", (each[0], each[1]))
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
        random.shuffle(final_questions)
        final_answers = [[questions[i][2].replace(r'\n', '<br>'), questions[i][3].replace(r'\n', '<br>'), questions[i][4].replace(r'\n', '<br>'), questions[i][5].replace(r'\n', '<br>')] for i in range(len(questions))]
        d = {}
        for i in range(len(final_questions)):
            q_ans = list(final_answers[i])
            random.shuffle(q_ans)
            q_ans.append(final_answers[i][0])
            q_ans.append(qids[i])
            d[final_questions[i]] = q_ans
        session["sent_ques"] = d
    uid = session["uid"]
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y %H:%M:%S")
    if request.method == "POST":
        res = OrderedDict(request.form)
        session["responses"] = [(a, b, session["sent_ques"][a][5]) for (a, b) in res.items()]
        for k, v in res.items():
            cur.execute("""SELECT rid FROM Responses;""")
            responses = cur.fetchall()
            responses = [r[0] for r in responses]
            rid = max(responses) + 1
            qid = session["sent_ques"][k][5]
            cur.execute("""SELECT * FROM responses;""")
            cur.execute("""INSERT INTO responses VALUES (%s, %s, %s, %s, %s, %s );""", (rid, uid, qid, v.replace("<br>", r"\n"), timestamp, "Spring 20"))
        return redirect(url_for("quiz_answers"))
    return render_template('quiz.html', q = final_questions, o = d)


@app.route('/results', methods=["GET", 'POST'])
def quiz_answers():
    answers = OrderedDict()
    res = session["responses"]
    responses = OrderedDict()
    correctness = OrderedDict()
    for k, v, id in res:
        responses[k] = v
        cur.execute("""SELECT correct_ans FROM Questions WHERE qid = (%s);""", (id,))
        correct = cur.fetchall()
        answers[k] = correct[0][0].replace(r"\n", "<br>")
        if v.replace('<br>', r'\n') == correct[0][0]:
            correctness[k] = "Correct"
        else:
            correctness[k] = "Incorrect"
    if request.method == "POST":
        next_dict = dict(request.form)
        if 'choose' in next_dict.keys():
            return redirect(url_for("concept"))
        if 'stay' in next_dict.keys():
            return redirect(url_for("quiz", question_type = session["question_type"]))
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
    cur.execute("""SELECT count(*) FROM responses WHERE semester = 'Spring 20';""")
    total = cur.fetchall()
    cur.execute("""SELECT count(distinct netid) FROM responses WHERE semester = 'Spring 20';""")
    studs = cur.fetchall()
    cur.execute("""SELECT concept, count(*) FROM responses, questions WHERE responses.qid = questions.qid and responses.semester = 'Spring 20' GROUP BY concept;""")
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
    sections = list(session["labs"])
    if 'All' in sections:
        labs = set([i for i in range(1, 13)])
    else:
        labs = set([int(val.split()[1]) for val in sections if val not in set(session['concepts'])])
    chosen_concepts = set([val for val in sections if val in set(session['concepts'])])
    final_output = [o for o in output if o[0] in labs and o[1] in chosen_concepts]
    return render_template('analyze_lab.html', labs = final_output)

@app.route('/select_student', methods=["GET", 'POST'])
def select_student():
    if request.method == "POST":
        student = dict(request.form)
        session["student"] = student['netid']
        return redirect(url_for("analyze_student"))
    return render_template("select_student.html")

@app.route('/analyze_student', methods=["GET", 'POST'])
def analyze_student():
    student_netid = session['uid']
    if type(student_netid) != str:
        student_netid = session['student'][0]
    cur.execute("""SELECT tot_num.netid, tot_num.concept, tot_num.function, correct_num.tot_correct, tot_num.tot_responses 
                FROM (SELECT responses.netid, questions.concept, questions.function, COUNT(*) as tot_correct
                FROM responses, questions
                WHERE questions.qid = responses.qid and responses.semester = 'Spring 20'
                AND questions.correct_ans = responses.ans_choice
                GROUP BY responses.netid, questions.concept, questions.function) as correct_num, 
                (SELECT responses.netid, questions.concept, questions.function, COUNT(*) as tot_responses
                FROM responses, questions
                WHERE questions.qid = responses.qid and responses.semester = 'Spring 20'
                GROUP BY responses.netid, questions.concept, questions.function) as tot_num
                WHERE correct_num.netid = tot_num.netid
                AND correct_num.concept = tot_num.concept
                AND correct_num.function = tot_num.function
                AND tot_num.netid = (%s);""", (student_netid,))
    output = cur.fetchall()
    return render_template("analyze_student.html", student = output )

@app.route('/analyze_self', methods=["GET", 'POST'])
def analyze_self():
    student_netid = session['uid']
    if type(student_netid) != str:
        student_netid = session['student'][0]
    cur.execute("""SELECT tot_num.netid, tot_num.concept, tot_num.function, correct_num.tot_correct, tot_num.tot_responses 
                FROM (SELECT responses.netid, questions.concept, questions.function, COUNT(*) as tot_correct
                FROM responses, questions
                WHERE questions.qid = responses.qid and responses.semester = 'Spring 20'
                AND questions.correct_ans = responses.ans_choice
                GROUP BY responses.netid, questions.concept, questions.function) as correct_num, (SELECT responses.netid, questions.concept, questions.function, COUNT(*) as tot_responses
                FROM responses, questions
                WHERE questions.qid = responses.qid and responses.semester = 'Spring 20'
                GROUP BY responses.netid, questions.concept, questions.function) as tot_num
                WHERE correct_num.netid = tot_num.netid
                AND correct_num.concept = tot_num.concept
                AND tot_num.netid = (%s);""", (student_netid,))
    output = cur.fetchall()
    print(student_netid)
    print(output)
    return render_template("analyze_student.html", student = output)


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


if __name__ == '__main__':

    #cur.execute("""SELECT * FROM Questions""")
    app.run()
    con.commit()