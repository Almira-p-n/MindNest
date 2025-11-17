from app.utils import clear

def mood_check():
    clear()
    print("=== MOOD CHECKER ===")

    mood = input("Gimana perasaanmu hari ini? Plih salah satu dari senang/sedih/marah/cemas/capek/normal: ").lower()

    # ========================
    # DATABASE MERESKAN
    # ========================
    tips = {
        "senang": [
            "Nikmati momen ini tanpa mikir yang aneh-aneh.",
            "Simpan rasa ini sebagai energi buat hari-harimu nanti.",
            "Bagikan sedikit kebahagiaan ke orang lain—walau cuma senyum."
        ],
        "sedih": [
            "Ambil napas panjang 3x... biar tubuhmu rileks dulu.",
            "Tuliskan apa yang kamu rasakan. Jangan dipendem sendiri.",
            "Alihkan pelan-pelan: mandi air hangat, musik tenang, atau jalan sebentar."
        ],
        "marah": [
            "Jangan balas chat atau ngomong saat kamu masih panas.",
            "Tarik napas 4 detik — tahan 4 — keluar 4. Ulangi 5x.",
            "Tulis apa yang bikin kamu marah, lalu baca ulang setelah 10 menit."
        ],
        "cemas": [
            "Fokus ke hal-hal yang bisa kamu kontrol.",
            "Latihan grounding: sebutkan 5 benda yang kamu lihat sekarang.",
            "Kurangi skenario di kepala. Lakuin pelan-pelan aja."
        ],
        "capek": [
            "Istirahat dulu 10 menit tanpa HP.",
            "Minum air. Banyak cemas itu karena tubuh kurang cairan.",
            "Break dari overthinking, bukan dari hidup."
        ],
        "normal": [
            "Stabil itu bukan membosankan. Itu kekuatan.",
            "Lanjutkan ritme harimu dengan tenang dan mindful.",
            "Hari biasa juga penting untuk mengisi energi."
        ]
    }

    solutions = {
        "senang": "Pertahankan ritmemu. Kelola energi agar tidak cepat drop.",
        "sedih": "Kenali sumber sedihnya. Kalau bisa diatasi—atasi. Kalau tidak—lepaskan.",
        "marah": "Tunda respon. Evaluasi alasan marahmu secara objektif.",
        "cemas": "Buat batasan pikiran. Tidak semua harus dipikirkan sekarang.",
        "capek": "Tubuh dan pikiranmu minta istirahat. Dengarkan sinyalnya.",
        "normal": "Pelihara kestabilan ini. Jadikan hari ini kesempatan untuk berkembang."
    }

    affirmations = {
        "senang": "Kamu berhak bahagia tanpa rasa bersalah.",
        "sedih": "Sedihmu valid. Tapi kamu jauh lebih kuat dari rasa itu.",
        "marah": "Kamu tetap terkendali meski lagi panas.",
        "cemas": "Pikiranmu ramai, tapi hatimu tetap bisa tenang.",
        "capek": "Istirahatmu bukan kelemahan. Itu proses memulihkan diri.",
        "normal": "Ketenanganmu hari ini adalah pencapaian."
    }

    challenge = {
        "senang": "Coba tulis 3 hal yang bikin kamu bersyukur hari ini.",
        "sedih": "Coba 5 menit journaling tanpa mikir grammar.",
        "marah": "Coba diam selama 2 menit penuh dan fokus ke napas.",
        "cemas": "Coba teknik 5-4-3-2-1 grounding.",
        "capek": "Coba berdiri, tarik napas, lalu stretch 20 detik.",
        "normal": "Coba rencanakan 1 hal kecil yang bikin kamu maju selangkah."
    }

    # ========================
    # VALIDASI
    # ========================
    if mood not in tips:
        print("\nMood tidak dikenali. Coba lagi.")
        input("\nTekan enter untuk kembali.")
        return

    # ========================
    # OUTPUT
    # ========================
    print("\n=== HASIL ANALISIS ===")
    print(f"- Mood kamu: {mood.upper()}")

    print("\nTips buat kamu:")
    for t in tips[mood]:
        print(f"• {t}")

    print(f"\nSolusi jangka pendek: {solutions[mood]}")
    print(f"Affirmation: {affirmations[mood]}")
    print(f"Mini Challenge: {challenge[mood]}")

    input("\nTekan enter untuk kembali.")