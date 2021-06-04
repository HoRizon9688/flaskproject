from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return render_template("index.html")


@app.route('/movie')
def movie():
    datalist = []
    database = sqlite3.connect('movie250.db')
    cursor = database.cursor()
    sql = '''select * from movie250'''
    data = cursor.execute(sql)
    for item in data:
        datalist.append(item)
    cursor.close()
    database.close()

    return render_template("movie.html", movies=datalist)


@app.route('/rating')
def rating():
    rating = []
    num = []
    database = sqlite3.connect('movie250.db')
    cursor = database.cursor()
    sql = '''select rating, count(rating) from movie250 group by rating'''
    data = cursor.execute(sql)
    for i in data:
        rating.append(i[0])
        num.append((i[1]))

    score = []
    rank = []
    new_sql = '''select id, rating from movie250 group by id'''
    new_data = cursor.execute(new_sql)
    for j in new_data:
        rank.append(j[0])
        score.append(j[1])
    cursor.close()
    database.close()
    return render_template("rating.html", rating=rating, num=num, rank=rank, score=score)


# 待完善
@app.route('/word')
def word():
    return render_template("word.html")


# 待完善
@app.route('/team')
def team():
    return render_template("team.html")


# @app.route('/admin/')
# def hello_admin():
#     return 'hello admin'
#
#
# @app.route('/user/<identity>')
# def hello_user(identity):
#     if identity == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=identity))
#
#
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return "hello {} , you are a guest now".format(guest)
#
#
# # 表单提交
# @app.route('/register')
# def test_register():
#     return render_template("register.html")
#
#
# # 接受表单提交的路由需要指明能够接受post请求，默认只接受get请求
# @app.route('/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
