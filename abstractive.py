from transformers import pipeline 

def abstractive_summary(text, max_length=100, min_length=30):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Example usage
if __name__ == "__main__":
    text = "Your input text here..."
    print(abstractive_summary(text))
