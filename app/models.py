from app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return "Question: " + self.question

class Alias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(32))
    frequency = db.Column(db.Integer)

    def __repr__(self):
        return "Alias: " + self.alias

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(32))
    alias_id = db.Column(db.Integer, db.ForeignKey('alias.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    def __repr__(self):
        return "Answer: " + self.answer
