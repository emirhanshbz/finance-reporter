from transformers import pipeline

# Model pipeline'ı bir kez yükleyip bellekte tutmak daha verimli
classifier = pipeline("sentiment-analysis", model="ProsusAI/finbert")

def analyze_headlines(headlines):
    if not headlines:
        return []
    
    results = classifier(headlines)

    # Her sonucu başlıkla eşleştir
    labeled = []

    for headline, result in zip (headlines, results):
        labeled.append({
            "headline": headline,
            "sentiment": result["label"],
            "score": round(result["score"], 2)
        })


    return labeled