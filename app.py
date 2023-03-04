from flask import Flask, request, session, redirect, url_for, render_template
import os,openai
# create the flask app
app = Flask(__name__)
app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'
openai.api_key = "key"

@app.errorhandler(Exception)
def error_handler1(*args):
    return redirect('http://URL/logout')

@app.errorhandler(502)
def error_handler2(*args):
    return redirect('http://URL/logout')

def generate_text(messages):
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature = 0,
    max_tokens=1024,
    )
    
    output = response.choices[0].message.content.strip()
    return output

@app.route('/logout')
def logout():
    if 'system' in session.keys():
        session['data'] = [{"role": "system", "content": session['system']},]
    else:
        session['system'] = "You are a helpful assistant."
        session['data'] = [{"role": "system", "content": session['system']},]
    return redirect('http://URL/')

@app.route('/changesys', methods=['GET','POST'])
def changesys():
    session.pop('data', None)
    if request.method == 'POST':  
        # get the description submitted on the web page
        prompt = request.form.get('description')
        if len(prompt)>0:
            session['system'] = prompt
            session['data'] = [{"role": "system", "content": session['system'] },]
            return redirect('http://URL/') 
    return render_template('changesys.html')

@app.route('/', methods=['GET','POST'])
def chat():
    
    if 'data' in session:

        messages = session['data']
        if request.method == 'POST':  
            # get the description submitted on the web page
            prompt = request.form.get('description')
            if len(prompt)>0:
                session['data'].append({"role": "user", "content": prompt},)
                
                messages = session['data']
                a_description = generate_text(messages)
                
                messages.append({"role": "assistant", "content": a_description},)
                session['data'] = messages
        
    else:
        session['system'] = "You are a helpful assistant."
        session['data'] = [{"role": "system", "content": session['system']},]
    
    return render_template('app_frontend.html', data = session['data'])


# boilerplate flask app code
if __name__ == "__main__":
    port = int(os.environ.get('PORT',80))
    app.run(debug=True, host='0.0.0.0', port=port)
