from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class TaskForm(FlaskForm):
    task = StringField("Task")
    completed = BooleanField("Completed", default=False)
    submit = SubmitField("Submit")
