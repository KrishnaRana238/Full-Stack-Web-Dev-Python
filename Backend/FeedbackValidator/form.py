from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length



class FeedbackForm(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    feedback = TextAreaField('Feedback', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Submit')

