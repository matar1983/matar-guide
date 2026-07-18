# app.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'matar_secret_key_2026'

# قائمة الأدوات (يمكن لاحقاً نقلها لقاعدة بيانات)
tools = [
    {"name": "تشكيل النصوص العربية", "desc": "أداة ذكية لتشكيل الكلمات", "url": "/tool/diacritics"},
    {"name": "تحويل التاريخ", "desc": "تحويل هجري وميلادي", "url": "/tool/date"}
]

@app.route('/')
def index():
    return render_template('index.html', tools=tools)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('admin'): return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        new_tool = {
            "name": request.form['name'],
            "desc": request.form['desc'],
            "url": request.form['url']
        }
        tools.append(new_tool)
    return render_template('dashboard.html', tools=tools)
