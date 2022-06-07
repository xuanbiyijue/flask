from flask import flash, redirect, url_for, render_template, request
from messageBoard import app, db
from messageBoard.forms import HelloForm
from messageBoard.models import Message



# 主页
@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        # 获得表单信息后，创建记录
        message = Message(body=body, name=name)
        # 添加到数据库
        db.session.add(message)
        # 提交
        db.session.commit()

        # 提示信息
        flash("Done!")

    # 加载所有的记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)



@app.route('/test')
def test():
    return 'test'