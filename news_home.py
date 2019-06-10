from flask import Flask

app = Flask(__name__)

class Config():
    # 配置
    DEBUG = True

# 将配置加载到app中
app.config.from_object(Config)

@app.route("/")
def index():

    return "新闻主页"

if __name__ == "__main__":
    app.run()