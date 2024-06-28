from flask import Flask, request, jsonify
from ai.pdf_extractor import extract_text_from_pdf
from ai.qa_model import QAModel
from ai.summarizer import Summarizer
import os

app = Flask(__name__)
qa_model = QAModel()
summarizer = Summarizer()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filepath = os.path.join('/tmp', file.filename)
        file.save(filepath)
        text = extract_text_from_pdf(filepath)
        return jsonify({"text": text}), 200

@app.route('/question', methods=['POST'])
def ask_question():
    data = request.get_json()
    context = data.get('context', '')
    question = data.get('question', '')
    answer = qa_model.answer_question(context, question)
    return jsonify({"answer": answer}), 200

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data.get('text', '')
    summary = summarizer.summarize_text(text)
    return jsonify({"summary": summary}), 200

if __name__ == "__main__":
    app.run(debug=True)
