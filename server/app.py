import tkinter as tk
from api.routes import app
from tkinter import filedialog
from ai.pdf_extractor import extract_text_from_pdf
from ai.qa_model import QAModel
from ai.summarizer import Summarizer

def upload_pdf():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def main():
    print("Please select a PDF file to upload.")
    pdf_path = upload_pdf()
    if not pdf_path:
        print("No file selected. Exiting.")
        return

    print(f"Extracting text from {pdf_path}...")
    text = extract_text_from_pdf(pdf_path)
    
    qa_model = QAModel()
    summarizer = Summarizer()
    
    while True:
        print("\nMenu:")
        print("1. Ask a question")
        print("2. Summarize text")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            question = input("Enter your question: ")
            answer = qa_model.answer_question(text, question)
            print("Answer:", answer)
        elif choice == '2':
            summary = summarizer.summarize_text(text)
            print("Summary:", summary)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app.run(debug=True)