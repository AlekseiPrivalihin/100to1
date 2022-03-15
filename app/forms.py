from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    answer = StringField('Type your answer', validators=[DataRequired()])
    submit = SubmitField('Send!')

class ResultForm(FlaskForm):
    submit = SubmitField('Play again')
