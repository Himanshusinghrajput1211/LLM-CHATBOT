from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# Load the text generation pipeline (LLM)
generator = pipeline("text-generation", model="gpt2")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = generator(user_input, max_length=100, num_return_sequences=1)[0]['generated_text']
    return render_template('index.html', user_input=user_input, response=response)

if __name__ == '__main__':
    app.run(debug=True)
