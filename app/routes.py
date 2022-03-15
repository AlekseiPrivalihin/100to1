from app import app
from app.forms import QuestionForm, ResultForm
from flask import render_template, redirect, url_for
import random
from app import db
from app.models import Question, Answer, Alias

question_pool = ['Name a reason you might get rid of an old family heirloom.',
                 'Where do kids nowadays spend most of their time?',
                 'Tell me something many people do just once a week.',
                 'Name a reason a person might wake up at 2:00 in the morning.',
                 'Name something you might eat with a hamburger.'] # TODO: DB

@app.route('/', methods=['GET', 'POST'])
def home():
    n_questions = len(Question.query.all())
    question_id = random.randint(1, n_questions)
    return redirect(url_for('question', question_id_raw=str(question_id)))

    
@app.route('/question?<question_id_raw>', methods=['GET', 'POST'])
def question(question_id_raw):
    question_id = int(question_id_raw)
    form = QuestionForm()
    n_questions = len(Question.query.all())
    question = Question.query.get(question_id).question
    if form.validate_on_submit():
        return redirect(url_for('result', question_id_raw=str(question_id), answer=form.answer.data.strip().lower()))

    return render_template('base.html', question=question, form=form)


@app.route('/result?<question_id_raw>;<answer>', methods=['GET', 'POST'])
def result(question_id_raw, answer):
    question_id = int(question_id_raw)
    question = Question.query.get(question_id).question
    possible_answers = Answer.query.filter_by(question_id=question_id).all()
    alias_id = 0
    frequency = 0
    for pos_ans in possible_answers:
        if pos_ans.answer in answer:
            alias_id = pos_ans.alias_id
            break

    if alias_id != 0:
        alias = Alias.query.get(alias_id)
        answer = alias.alias
        frequency = alias.frequency

    form = ResultForm()
    if form.validate_on_submit():
        return redirect('/')

    print(form.errors)
    return render_template('base.html', question=question, answer=answer, frequency=frequency, form=form)



