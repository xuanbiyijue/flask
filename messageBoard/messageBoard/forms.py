from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, length
import wtforms


# 创建表单类
class HelloForm(FlaskForm):
    name = wtforms.StringField("Name", validators=[length(min=3, max=20), DataRequired()])
    body = wtforms.TextAreaField("Message", validators=[length(min=3, max=200), DataRequired()])
    submit = wtforms.SubmitField()
