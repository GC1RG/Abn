from flask import Flask, request, render_template, jsonify
import os
import requests
from llm_providers import send_prompt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = None
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        if prompt:
            response_text = send_prompt(prompt)
    return render_template('index.html', response_text=response_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
