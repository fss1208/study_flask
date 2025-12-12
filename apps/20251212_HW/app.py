from flask import Flask, render_template, redirect, request, url_for, make_response, flash
from datetime import datetime
import os, math

app = Flask(__name__)
app.config['SECRET_KEY'] = '2AZMss3p5QPbcY2hBs' # flash 사용하는 경우 반드시 필요
folder_path = "C:\\SeSAC_AI_3rd\\flaskbook\\apps\\20251212_HW\\files"

def format_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

@app.route('/')
def index():
    files_list = []
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):   
                stats = os.stat(file_path)
                ext = os.path.splitext(filename)[1][1:].lower()
                files_list.append({
                    'name': filename,
                    'type': ext,
                    'ctime': format_time(stats.st_ctime),
                    'mtime': format_time(stats.st_mtime),
                    'size': format_size(stats.st_size)
                })
    else:
        flash("폴더가 존재하지 않습니다.")
    return render_template('index.html', folder_path=folder_path, files=files_list)

@app.route("/upload", methods=["POST"])
def upload():
    if (request.method == "POST"):
        try:
            file = request.files['selected_file']
            if bool(file.filename):
                file.save(os.path.join(folder_path, file.filename))
            else:
                flash("파일을 선택해주세요.")
        except Exception as e:
            flash(str(e))
    return redirect(url_for("index"))

@app.route("/delete/<filename>")
def delete(filename):
    try:
        os.remove(os.path.join(folder_path, filename))
    except Exception as e:
        flash(str(e))
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)