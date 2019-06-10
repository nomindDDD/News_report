from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config():
    # 配置debug
    DEBUG = True


# 将配置加载到app中
app.config.from_object(Config)
# 将app与数据库关联
db = SQLAlchemy(app)


@app.route("/")
def index():

    return "新闻主页"

if __name__ == "__main__":
    app.run()