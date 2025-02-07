from flask import Flask, request, session, redirect, url_for, render_template, Response
import os, openai
from datetime import timedelta
import sys

# create the flask app
app = Flask(__name__)
app.secret_key = os.urandom(30)

try:
    openai_api = sys.argv[1]
except:
    openai_api = os.getenv('apiKey')

openai.api_key = openai_api
openai.api_base = "https://dashscope.aliyuncs.com/compatible-mode/v1"

app.permanent_session_lifetime = timedelta(minutes=180)

# 模拟用户数据库，实际应用中应使用数据库
users = {
    "DeepSeek": os.getenv('chatbot')
}

def generate_text_stream(messages):
    response = openai.ChatCompletion.create(
        model="deepseek-r1",
        messages=messages,
        temperature=0,
        max_tokens=1024,
        stream=True  # 开启流式输出
    )
    for chunk in response:
        if 'choices' in chunk and len(chunk.choices) > 0 and 'delta' in chunk.choices[0] and 'content' in chunk.choices[0].delta:
            yield chunk.choices[0].delta.content

# 登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('chat'))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    return render_template('login.html')

# 登出路由
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('data', None)
    return redirect(url_for('login'))

# 修改系统提示路由
@app.route('/changesys', methods=['GET', 'POST'])
def changesys():
    if 'username' not in session:
        return redirect(url_for('login'))
    session.pop('data', None)
    if request.method == 'POST':
        # get the description submitted on the web page
        prompt = request.form.get('description')
        if len(prompt) > 0:
            session['system'] = prompt
            session['data'] = [{"role": "system", "content": session['system']},]
            return redirect(url_for('chat'))
    return render_template('changesys.html')

# 聊天路由
@app.route('/', methods=['GET', 'POST'])
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))
    if 'data' in session.keys():
        messages = session['data']
        if request.method == 'POST':
            # get the description submitted on the web page
            prompt = request.form.get('description')
            if len(prompt) > 0:
                session['data'].append({"role": "user", "content": prompt})
                messages = session['data']

                full_response = ""
                def stream():
                    nonlocal full_response
                    for chunk in generate_text_stream(messages):
                        full_response += chunk
                        yield chunk

                response = Response(stream(), mimetype='text/plain')
                messages.append({"role": "assistant", "content": full_response})
                session['data'] = messages
                return response
    else:
        session['system'] = "You are a helpful assistant."
        session['data'] = [{"role": "system", "content": session['system']},]
    return render_template('app_frontend.html', data=session['data'])

# boilerplate flask app code
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 13579))
    app.run(debug=False, host='0.0.0.0', port=port)