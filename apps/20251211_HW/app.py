from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)

# flash 사용하는 경우 반드시 필욘
app.config['SECRET_KEY'] = '2AZMss3p5QPbcY2hBs'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/mtable", methods=["POST"])
def mtable():
    try:
        if (bool(request.form["no"])):
            no = int(request.form["no"])
            if (no >= 1 and no <= 9):
                return redirect(url_for("print", number=no))
            else:
                flash("1 ~ 9 사이의 숫자를 입력해주세요.")
        else:
            flash("아직 아무 숫자도 입력이 안되었습니다.")
    except Exception as e:
        flash("{} {}".format(type(e), e))
    return redirect(url_for("index"))

@app.route("/<int:number>")
def print(number):
    return render_template('index.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)