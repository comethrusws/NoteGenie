from transformers import pipeline

class QAModel:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def answer_question(self, context, question):
        result= self.qa_pipeline(question=question, context=context)
        return result['answer']
    

if __name__ == "__main__":
    context= "The Capital of France is Paris"
    question= "what is the capital of France?"
    qa_model= QAModel()
    answer= qa_model.answer_question(context, question)
    print(answer)