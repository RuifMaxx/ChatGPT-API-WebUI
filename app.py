from flask import Flask, request, jsonify, render_template
import os,openai
# create the flask app
app = Flask(__name__)

openai.api_key = "your_key"

def generate_text(prompt):
    # Set up the parameters for the API request
    model_engine = "text-davinci-003"

    # Call the OpenAI API to generate text
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the API response
    output = response.choices[0].text.strip()

    return output

# what html should be loaded as the home page when the app loads?
@app.route('/')
def home():
    return render_template('app_frontend.html', prediction_text="")

@app.route('/chat', methods=['GET','POST'])
def chat():
    # get the description submitted on the web page
    prompt = request.form.get('description')
    if request.method == 'POST':
        a_description = generate_text(prompt)
    else:
        a_description = '请向我提问'
    return render_template('app_frontend.html', prediction_text=a_description)


# boilerplate flask app code
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
