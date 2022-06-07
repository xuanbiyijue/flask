from flask import Flask
from messageBoard import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment


# 使用包组织代码时，以硬编码写出包名称作为程序名称
app = Flask('messageBoard')

# 绑定配置信息
app.config.from_object(config)

# 绑定数据库
db = SQLAlchemy(app)
# db.init_app(app)

# 绑定bootstrap
bootstrap = Bootstrap(app)

# 数据库迁移
migrate = Migrate(app, db)

# 绑定moment
moment = Moment(app)

# 为防止循环调用，放在最下方
from messageBoard import views, errors


if __name__ == '__main__':
    app.run()