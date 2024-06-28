from transformers import pipeline

class Summarizer:
    def __init__(self):
        self.summarizer_pipeline = pipeline("summarization")
        
    def summarize_text(self, text):
        summary = self.summarizer_pipeline(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    

if __name__ == "__main__":
    text = "Your Text Here..."
    summarizer = Summarizer()
    summary = summarizer.summarize_text(text)
    print(summary)