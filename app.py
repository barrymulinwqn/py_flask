import os
import sys
import sqlite3
import click
import webbrowser
from waitress import serve
from flaskwebgui import FlaskUI

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
# ui = FlaskUI(app, width=500, height=500)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app
app.config.update(DEBUG=True)



name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def home():
    return render_template('index.html', name=name, movies=movies)

@app.route('/about')
def recon():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/index')
def index():
    return render_template('index.html', name=name, movies=movies)

def start_flask(**server_kwargs):

    app = server_kwargs.pop("app", None)
    server_kwargs.pop("debug", None)

    try:
        import waitress

        waitress.serve(app, **server_kwargs)
    except:
        app.run(**server_kwargs)


if __name__ == '__main__':
    def saybye():
        print("on_exit bye")


    FlaskUI(
        server=start_flask,
        server_kwargs={
            "app": app,
            "port": 3000,
            "threaded": True,
        },
        width=800,
        height=600,
        on_shutdown=saybye,
    ).run()


    # serve(FlaskUI(
    #     app=app,
    #     server="flask",
    #     width=800,
    #     height=600,
    #     on_startup=lambda: print("helooo"),
    #     on_shutdown=lambda: print("byee"),
    # ).run())
    # webbrowser.open('http://localhost:6000')
    # app.run('0.0.0.0', port=6000, debug=True)
   #  serve(app.run(),host="127.0.0.1",
   # port=5000,
   # threads=2)


##  ORM
class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份


@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息


@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
def addnewdatatodb():
    """Add new data to SQLite db database."""
    from app import User, Movie
    user = User(name='Grey Li')
    m1 = Movie(title='Leon', year='1994')
    m2 = Movie(title='Mahjong', year='1996')
    db.session.add(user)
    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()
    click.echo('Add new User and Movies data to SQLite db database successfully.')  # 输出提示信息