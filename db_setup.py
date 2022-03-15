from app import app, db
from app.models import Question, Answer, Alias
filename = 'basic_db.txt'

questions = Question.query.all()
for q in questions:
    db.session.delete(q)

answers = Answer.query.all()
for a in answers:
    db.session.delete(a)

db.session.commit()

aliases = Alias.query.all()
for a in aliases:
    db.session.delete(a)

db.session.commit()

infile = open(filename)
raw = infile.read().split('\n')
cur_q_id = 0
cur_a_id = 0
for s in raw:
    if len(s) == 0:
        continue
    if (s[0] == '#'):
        cur_q_id += 1
        db.session.add(Question(question=s[1:]))
    else:
        cur_a_id += 1
        alias, answers, freq = s.split('|')
        db.session.add(Alias(alias=alias,frequency=int(freq)))
        answers = answers.split(';')
        for answer in answers:
            db.session.add(Answer(answer=answer,alias_id=cur_a_id,question_id=cur_q_id))
                    
db.session.commit()

