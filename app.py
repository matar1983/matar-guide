from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'matar_secret_key_2026'

# قائمة الأدوات (مخزنة مؤقتاً في الذاكرة)
tools = [
    {"name": "تشكيل النصوص العربية", "desc": "أداة ذكية لتشكيل الكلمات", "url": "#"},
    {"name": "تحويل التاريخ", "desc": "تحويل هجري وميلادي", "url": "#"}
]

@app.route('/')
def index():
    return render_template('index.html', tools=tools)

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        if request.form['user'] == 'matar' and request.form['pass'] == '123456':
            session['admin'] = True
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('admin'): return redirect(url_for('admin_login'))
    if request.method == 'POST':
        tools.append({"name": request.form['name'], "desc": request.form['desc'], "url": request.form['url']})
    return render_template('dashboard.html', tools=tools)

if __name__ == '__main__':
    app.run(debug=True)
