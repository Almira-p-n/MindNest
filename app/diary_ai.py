from app.utils import clear

def diary_ai():
    clear()
    print("=== DIARY AI ===")
    teks = input("Tulis curhatanmu hari ini:\n\n").lower()

    # =========================================
    # DATA MOOD LENGKAP
    # =========================================
    moods = {
        "bahagia": [
            "senang", "bahagia", "happy", "ceria", "semangat", "lega",
            "bersyukur", "tenang", "bangga", "puas", "suka", "gembira"
        ],
        "sedih": [
            "sedih", "nangis", "kecewa", "terluka", "rapuh", "galau",
            "nyesek", "hampa", "sunyi", "sendiri"
        ],
        "marah": [
            "marah", "kesal", "sebel", "jengkel", "benci",
            "muak", "emosi"
        ],
        "capek": [
            "capek", "lelah", "letih", "pusing", "stress", "stres",
            "overthinking", "bosan"
        ],
        "cemas": [
            "takut", "cemas", "khawatir", "gelisah", "anxious",
            "panik"
        ]
    }

    negator_words = ["tidak", "ga", "gak", "nggak", "bukan", "engga", "tdk"]
    words = teks.split()

    # =========================================
    # EMOTION SCORING
    # =========================================
    score = {m: 0 for m in moods}

    for i, w in enumerate(words):
        for mood_name, mood_list in moods.items():
            if w in mood_list:
                if i > 0 and words[i-1] in negator_words:
                    # contoh: "ga sedih" -> jadi positif (counter mood)
                    if mood_name in ["bahagia"]:
                        score["sedih"] += 1
                    else:
                        score["bahagia"] += 1
                else:
                    score[mood_name] += 1

    # =========================================
    # MOOD FINAL
    # =========================================
    detected_mood = max(score, key=score.get)
    max_value = score[detected_mood]

    if max_value == 0:
        detected_mood = "netral"

    # =========================================
    # STRESS LEVEL CALCULATION
    # =========================================
    stress_keywords = ["capek", "lelah", "stress", "stres", "pusing", "overthinking"]
    stress_score = sum(w in stress_keywords for w in words)

    if stress_score >= 5:
        stress_level = "TINGGI"
    elif stress_score >= 2:
        stress_level = "SEDANG"
    else:
        stress_level = "RENDAH"

    # =========================================
    # EMOTION KEYWORDS (TOP 3)
    # =========================================
    emotion_hits = {}
    for mood_name, mood_list in moods.items():
        for w in words:
            if w in mood_list:
                emotion_hits[w] = emotion_hits.get(w, 0) + 1

    emotion_keywords = sorted(emotion_hits.items(), key=lambda x: x[1], reverse=True)
    emotion_keywords = [i[0] for i in emotion_keywords[:3]]

    # =========================================
    # INTI CERITA
    # =========================================
    sentences = [s.strip() for s in teks.split(".") if s.strip()]
    longest = max(sentences, key=len) if sentences else ""

    # =========================================
    # KATA DOMINAN
    # =========================================
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    umum = max(freq, key=freq.get)

    # =========================================
    # SARAN BERDASARKAN MOOD
    # =========================================
    advice = {
        "bahagia": "Enjoy your moment! Simpan rasa ini, biar jadi bensin buat hari lain.",
        "sedih": ("Aku ngerti rasanya nggak mudah. Tapi kamu kuat, kamu steady, "
                  "kamu tetap elegan meskipun lagi sakit. Ambil nafas."),
        "marah": "Tarik napas pelan. Emosi itu valid, tapi kamu tetap punya kendali.",
        "capek": "Istirahat bukan dosa. Kamu manusia, bukan mesin.",
        "cemas": "Pikiranmu sibuk, tapi kamu tetap bisa mengatur ritmenya. One step at a time.",
        "netral": "Hari ini stabil. Good. Konsisten itu kekuatan."
    }

    # =========================================
    # OUTPUT
    # =========================================
    print("\n=== RINGKASAN ===")
    print(f"- Mood dominan: {detected_mood.upper()}")
    print(f"- Stress level: {stress_level}")
    print(f"- Emotion keywords: {emotion_keywords if emotion_keywords else 'Tidak terdeteksi'}")
    print(f"- Inti cerita: {longest}")
    print(f"- Kata dominan: '{umum}'")
    print(f"- Saran AI: {advice.get(detected_mood, 'Tetap tenang.')}")

    input("\nTekan enter untuk kembali.")