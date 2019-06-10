from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

app = Flask(__name__)


class Config():
    # 配置debug
    DEBUG = True
    # 未配置数据库信息运行报错,配置数据库项
    # 配置数据库链接对象：mysql数据库,用户root,密码:mysql,数据库地址:端口号,数据库名
    SQLALCHEMY_DATABASE_URI = "mysql://root:msql@127.0.0.1:3306/new_git"
    # 设置不跟踪数据,提高数据查询效率
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 将配置加载到app中
app.config.from_object(Config)
# 将app与mysql数据库关联
db = SQLAlchemy(app)
# 配置redis数据库
redis_store = StrictRedis(host="127.0.0.1",port=6379)


@app.route("/")
def index():

    return "新闻主页"

if __name__ == "__main__":
    app.run()