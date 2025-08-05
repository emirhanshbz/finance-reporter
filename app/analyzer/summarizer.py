from transformers import pipeline

# Summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(input_text):
    if not input_text or len(input_text.strip()) == 0:
        return "No summary available."
    
    summary = summarizer(input_text, max_length=60, min_length=20, do_sample=False)
    return summary[0]["summary_text"]