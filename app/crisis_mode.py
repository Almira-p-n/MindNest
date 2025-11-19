import random
from app.utils import clear

def crisis_mode():
    clear()
    quotes = [
        "Tidak semua yang hilang harus dicari kembali.",
        "Lelah itu wajar, berhenti sebentar bukan mundur.",
        "Beberapa orang hadir hanya untuk jadi pelajaran.",
        "Jaga hatimu; tidak semua tempat bisa ditinggali.",
        "Awal dari hidup yang berantakan adalah ibadah yang mulai dilalaikan.",
        "Jangan memaksakan hubungan yang cuma kamu perjuangkan sendiri; cinta yang sehat datang dari dua arah.",
        "Kamu boleh sedih, tapi jangan biarkan sedih mengatur arah hidupmu, kamu lebih besar dari rasa sakitmu.",
        "Pertemanan yang sehat tidak menuntut kamu menjelaskan semua hal; yang dewasa akan paham tanpa banyak klarifikasi.",
        "Hidup memang nggak selalu lembut, tapi kamu juga nggak diciptakan buat menyerah setiap kali badai lewat.",
        "Kalau kamu terus menunda ibadah, jangan heran kalau hati makin kosong, ketenangan selalu dimulai dari kembali pada Tuhan.",
        "Berhenti membuktikan dirimu ke orang yang tidak mau melihat; energimu terlalu berharga untuk mereka yang menunggu kamu jatuh.",
        "Jangan biarkan cinta membuatmu lupa harga dirimu; kalau hubungan itu bikin kamu kehilangan jati diri, lepaskan sebelum kamu ikut hancur.",
        "Kamu nggak harus kuat sendirian, tapi jangan biarkan lingkungan yang salah membuatmu lemah, pilih siapa yang kamu izinkan dekat dengan hidupmu.",
        "Disakiti itu bagian dari hidup, tapi membiarkan rasa sakit mengatur masa depanmu adalah pilihan, dan kamu terlalu pintar untuk jatuh di lubang yang sama dua kali.",
        "Kalau hidup mulai terasa berantakan, mulai dari akar: ibadahmu, lingkunganmu, pola pikirmu. Hidup nggak akan berubah kalau kamu mempertahankan kebiasaan yang merusakmu."
    ]

    while True:
        print("\n" + "'" + random.choice(quotes) + "'")
        print("\n" + "'" + random.choice(quotes) + "'")
        input("\nTekan ENTER untuk lanjut...")

        lanjut = input("\nLanjut? (y/t): ").lower().strip()

        if lanjut != "y":
            print("\nKemarin juga berat, tapi selesai 'kan?")
            print("SEMANGAT & TERIMAKASIH TELAH MENGGUNAKAN SYSTEM MINDNEST")
            input("\nTekan ENTER untuk kembali...")
            break
