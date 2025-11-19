import time
from app.utils import clear

def calm_menu():
    clear()
    print("=== CALMBOX ===")
    print("Pilih menu:")
    print("1. Breathing (Latihan Nafas)")
    print("2. Grounding (Menenangkan Pikiran)")
    print("3. Journaling Prompt (Panduan Menulis Perasaan)")
    print("4. Kembali")

    pilih = input("\nPilih (1-4): ")

    if pilih == "1":
        breathing()
    elif pilih == "2":
        grounding()
    elif pilih == "3":
        journaling_prompt()
    elif pilih == "4":
        return
    else:
        return calm_menu()


def breathing():
    clear()
    print("=== LATIHAN NAFAS ===\n")

    print("Latihan ini berguna untuk:")
    print("- Meredakan cemas atau panik")
    print("- Membuat tubuhmu lebih rileks")
    print("- Mengembalikan fokus saat pikiran berantakan")
    print("- Menurunkan ketegangan di dada\n")

    print("Ikuti dengan pelan:")
    time.sleep(1)
    print("• Tarik napas 4 detik...")
    time.sleep(4)
    print("• Tahan 4 detik...")
    time.sleep(4)
    print("• Lepaskan perlahan 4 detik...")
    time.sleep(4)
    print("\nUlangi 5 kali.")

    print("\nKamu nggak harus sempurna. Kamu cuma perlu mencoba. Sedikit tenang pun sudah kemenangan.")
    input("\nTekan enter untuk kembali...")


def grounding():
    clear()
    print("=== GROUNDING ===\n")

    print("Grounding itu apa?")
    print("• Grounding adalah teknik menenangkan pikiran dengan mengajakmu kembali ke realita saat ini.")
    print("• Ini membantu waktu kamu overthinking, cemas, atau pikiran lari ke mana-mana.")
    print("• Bisa bikin kepala lebih ringan dan tubuh lebih tenang.\n")

    print("Coba lakukan teknik 5-4-3-2-1:")
    print("• Sebutkan 5 hal yang bisa kamu lihat.")
    print("• Sebutkan 4 hal yang bisa kamu sentuh.")
    print("• Sebutkan 3 hal yang bisa kamu dengar.")
    print("• Sebutkan 2 hal yang bisa kamu cium aromanya.")
    print("• Sebutkan 1 hal yang benar-benar kamu syukuri hari ini.\n")

    print("Tenang… kamu aman sekarang. Kamu hadir di momen ini. Kamu nggak sendirian.")
    input("\nTekan enter untuk kembali...")


def detect_emotion(user_text):
    user_text = user_text.lower()

    SENTIMENT_MAP = {
        "sedih": "sedih",
        "kecewa": "sedih",
        "kehilangan": "sedih",
        "hancur": "sedih",
        
        "capek": "lelah",
        "lelah": "lelah",
        "letih": "lelah",

        "marah": "marah",
        "kesel": "marah",
        "benci": "marah",

        "bingung": "bingung",
        "gatau": "bingung",
        "ga tau": "bingung",

        "cemas": "cemas",
        "takut": "cemas",
        "khawatir": "cemas",

        "senang": "senang",
        "lega": "senang",
    }

    for keyword, emotion in SENTIMENT_MAP.items():
        if keyword in user_text:
            return emotion
    
    return "netral"


def get_affirmation(emotion):
    """
    Afirmasi human-friendly berdasarkan emosi.
    Tanpa library, variasi dijaga manual.
    """

    AFFIRM = {
        "sedih": [
            "Aku bisa ngerasain sedih yang kamu bawa. Itu bukan tanda kamu lemah—itu tandanya kamu manusia, dan kamu masih berjuang.",
            "Sedihmu valid. Kamu sudah menahan banyak hal sendirian, dan itu bukan hal kecil.",
        ],
        "lelah": [
            "Kalau kamu lelah, itu wajar. Kamu sudah melangkah sejauh ini meskipun rasanya berat.",
            "Kelelahanmu bukan berarti kamu gagal—itu pertanda kamu sudah terlalu lama kuat sendirian.",
        ],
        "marah": [
            "Marah itu wajar. Ada batas yang mungkin dilanggar, dan kamu berhak merasa begitu.",
            "Emosi marahmu adalah sinyal dari diri sendiri bahwa ada yang gak beres di sekitarmu.",
        ],
        "bingung": [
            "Rasa bingung itu manusiawi. Kamu lagi belajar memahami arah hidupmu, pelan-pelan aja.",
            "Kadang hidup terasa abu-abu, tapi kamu tetap bisa melangkah sedikit demi sedikit.",
        ],
        "cemas": [
            "Rasa cemas itu berat, tapi kamu nggak berjalan sendirian. Kamu masih bernapas, itu sudah bukti kekuatan.",
            "Cemas bukan berarti kamu lemah. Itu cuma bukti kamu peduli banyak hal terlalu dalam.",
        ],
        "senang": [
            "Senang baca kamu punya titik terang hari ini. Kamu pantas untuk ngerasain momen-momen ringan.",
            "Perasaan senangmu itu berharga—nikmati sebentar, kamu layak bahagia.",
        ],
        "netral": [
            "Makasih ya udah cerita. Kamu harus tetap semangat untuk menjalani hari-hari kamu.",
        ]
    }

    # pilih salah satu (manual pseudo-random)
    options = AFFIRM[emotion]
    idx = (len(options) * 7 + 3) % len(options)
    return options[idx]


def extract_keywords(text):
    """
    Ambil kata penting (manual).
    Untuk rangkuman akhir.
    """
    words = text.split()
    picked = []

    for w in words:
        if len(w) > 4:  # kata agak panjang biasanya penting
            picked.append(w)
        if len(picked) == 3:
            break
    
    return picked


def journaling_prompt():
    print("\n=== MODE JOURNALING — MindNest ===")
    print("Tulis jawabanmu dengan jujur. Aku di sini bukan buat nilai kamu, tapi buat nemenin.\n")

    questions = [
        "1. Apa yang paling mengganggu pikiranmu hari ini? (misal: rasa sedih/rasa marah/dsb.)",
        "2. Kenapa hal itu membuatmu merasa seperti itu?",
        "3. Hal kecil apa yang sebenarnya kamu butuhkan sekarang?"
    ]

    user_answers = []

    for q in questions:
        print(q)
        answer = input("Jawabanmu: ")

        user_answers.append(answer)

        emotion = detect_emotion(answer)
        affirmation = get_affirmation(emotion)

        print("\n")
        print(affirmation)
        print("-" * 55)

    # ⬇ Rangkuman adaptif
    print("\n=== Rangkuman untukmu ===")
    print("Dari apa yang kamu ceritakan barusan, aku bisa lihat kalau kamu lagi menghadapi sesuatu yang nggak mudah.")

    print("\nBeberapa hal yang paling terasa dari ceritamu:")
    for ans in user_answers:
        kws = extract_keywords(ans)
        if kws:
            print("- " + " ".join(kws))
    
    print("\n=== Afirmasi Penutup ===")
    print("Terima kasih sudah jujur sama dirimu sendiri barusan. Itu langkah besar.")
    print("Kamu nggak harus kuat setiap hari cukup tetap bertahan satu langkah kecil aja.")
    print("Apa pun yang kamu rasakan, kamu nggak sendiri, dan kamu jauh lebih kuat dari yang kamu pikirkan.")

    print("\nTekan ENTER untuk kembali...")
    input()
