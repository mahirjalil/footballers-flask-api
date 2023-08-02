from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AddFootballerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired(), Length(min=2, max=50)])
    club = StringField('Club', validators=[DataRequired(), Length(min=2, max=50)])
    shirt_number = IntegerField('Shirt number', validators=[DataRequired()])
    submit = SubmitField('Add Football player')
