from flask import Flask, render_template
from os import listdir

app = Flask(__name__)

@app.route("/")
def template_test():
    pic_list = listdir("static/")
    return render_template('displaypic.html', pic_list=pic_list)

if __name__ == '__main__':
    app.run(debug=True)
