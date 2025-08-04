from textblob import TextBlob
from spotify_api import get_playlist_for_mood

def classify_mood_advanced(text):
    text = text.lower()

    keyword_moods = {
        "happy": ["joy", "awesome", "great", "excited", "love", "fantastic", "wonderful"],
        "sad": ["tired", "hopeless", "cry", "depressed", "low", "unmotivated", "exhausted"],
        "angry": ["angry", "mad", "furious", "annoyed", "hate"],
        "romantic": ["love", "crush", "heart", "romantic", "miss"],
        "lonely": ["alone", "lonely", "nobody", "isolated"],
        "chill": ["calm", "relax", "peaceful", "easy", "slow"],
        "energetic": ["hyped", "energy", "power", "pumped", "strong"]
    }

    for mood, keywords in keyword_moods.items():
        for word in keywords:
            if word in text:
                return mood

 
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.3:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    else:
        return "neutral"

if __name__ == "__main__":
    print("🎧 Welcome to Ezgi's Jukebox – Advanced Mood Edition")
    user_input = input("How are you feeling today? Tell me in a sentence: ")

    mood = classify_mood_advanced(user_input)
    print(f"\n🧠 Detected Mood: {mood}")

    playlist = get_playlist_for_mood(mood)
    print(f"🎵 Suggested Playlist: {playlist['name']}")
    print(f"🔗 Listen here: {playlist['url']}")
