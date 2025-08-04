### 🧠 How Mood Detection Works

This project uses the `TextBlob` library for basic sentiment analysis. It analyzes the **polarity** of the user's input text and maps it to a general mood category:

- `Polarity > +0.3` → **happy**
- `Polarity < -0.3` → **sad**
- Otherwise → **neutral**

⚠️ For example, if you write:

> "I’m feeling tired today."

This will be categorized as **sad**, since the word *"tired"* carries a slightly negative sentiment score in the underlying sentiment lexicon.

📌 This is a rule-based system and **not context-aware**. For more accurate mood detection, you can upgrade the NLP component to use pretrained transformer models or a custom classifier.
