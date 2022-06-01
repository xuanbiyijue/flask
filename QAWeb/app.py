from flask import Flask, session, g
import config
from exts import db, mail
from blueprints import qa_bp, user_bp
from flask_migrate import Migrate
from models import UserModel


app = Flask(__name__)
#绑定配置信息
app.config.from_object(config)
#db绑定app
db.init_app(app)
#绑定mail
mail.init_app(app)

migrate = Migrate(app, db)

#app绑定蓝图
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)

#钩子函数
@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            #给g绑定一个叫做user的变量，值为user
            # setattr(g, "user", user)
            g.user = user
        except:
            g.user = None

@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}




if __name__ == '__main__':
    app.run()
