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


def journaling_prompt():
    clear()
    print("=== JOURNALING PROMPT ===\n")

    print("Kita bakal journaling pelan-pelan ya…")
    print("Jawab sesuai hatimu. Nggak harus panjang.\n")
    input("Tekan enter untuk mulai...\n")

    answers = {}

    # -------------------------------
    #  PERTANYAAN 1
    # -------------------------------
    clear()
    print("1. Apa yang paling berat buatmu hari ini?\n")
    answers["berat"] = input("Jawabanmu: ")
    print("\nMakasih ya sudah jujur sama dirimu sendiri.")
    input("Tekan enter untuk lanjut...")

    # -------------------------------
    #  PERTANYAAN 2
    # -------------------------------
    clear()
    print("2. Siapa atau apa yang membuatmu merasa aman?\n")
    answers["aman"] = input("Jawabanmu: ")
    print("\nMakasih ya udah cerita. Indah rasanya ketika kita punya sesuatu atau seseorang yang bisa bikin hati kita merasa aman.\n"
        "Pegang perasaan itu baik-baik… karena rasa aman adalah tempat kita pulang waktu dunia terasa terlalu bising.\n" \
        "Apa pun bentuknya, kamu pantas punya ruang yang bikin kamu tenang, didengar, dan diterima apa adanya.")
    input("Tekan enter untuk lanjut...")

    # -------------------------------
    #  PERTANYAAN 3
    # -------------------------------
    clear()
    print("3. Hal apa yang ingin kamu lepaskan dari pikiranmu?\n")
    answers["lepaskan"] = input("Jawabanmu: ")
    print("\nTerima kasih sudah mau ngebuka sedikit isi kepala kamu… itu bukan hal yang gampang.\n" \
        "Apa pun yang kamu coba lepaskan hari ini, aku tahu itu pasti punya rasa yang berat buat kamu.\n" \
        "Tapi kamu berani ngomongin itu — dan keberanian kecil kayak gini sering jadi awal dari hati yang lebih ringan.\n" \
        "Pelan-pelan aja… nggak harus kuat sempurna, cukup hadir sama perasaanmu.\n" \
        "Aku di sini, dan kamu nggak lagi ngadepin ini sendirian.")
    input("Tekan enter untuk lanjut...")

    # -------------------------------
    #  PERTANYAAN 4
    # -------------------------------
    clear()
    print("4. Hal kecil apa yang berhasil kamu lakukan hari ini?\n")
    answers["kecil"] = input("Jawabanmu: ")
    print("\nItu keren banget, beneran. Kadang hal kecil justru yang paling berarti, karena dari situlah kita belajar bahwa kemajuan itu nggak selalu harus besar.\n" \
        "Kamu nyempetin diri buat ngelakuin itu dan itu tanda kamu tetap bergerak, meski pelan.\n" \
        "Banggain diri kamu sebentar… kamu layak ngerasain itu.")
    input("Tekan enter untuk lanjut...")

    # -------------------------------
    #  PERTANYAAN 5
    # -------------------------------
    clear()
    print("5. Perasaan apa yang paling dominan sekarang dan kenapa?\n")
    answers["perasaan"] = input("Jawabanmu: ")
    print("\nMakasih udah jujur sama perasaanmu.")
    input("Tekan enter untuk lihat rangkuman...")

    # -------------------------------
    #  AFIRMASI AKHIR
    # -------------------------------
    clear()
    print("=== RANGKUMAN & AFIRMASI ===\n")

    print("Dari jawabanmu barusan…")
    print("Aku bisa lihat kalau kamu lagi benar-benar mencoba memahami dirimu.\n")

    # Analisis sederhana berdasarkan jawaban terakhir (perasaan)
    final = answers["perasaan"].lower()

    if any(x in final for x in ["sedih", "kecewa", "nangis", "capek", "lelah", "hancur"]):
        print("Sepertinya kamu lagi nahan banyak hal… dan itu melelahkan.")
        print("Tapi kamu masih berusaha berdiri, dan itu bukti kekuatanmu.")
        print("Kamu nggak sendirian. Perasaan ini valid. Pelan-pelan ya.\n")

    elif any(x in final for x in ["takut", "cemas", "anxiety", "khawatir", "bingung"]):
        print("Kecemasan itu bukan salahmu. Pikiranmu cuma lagi penuh.")
        print("Kamu aman sekarang. Tarik napas pelan… kamu masih di sini, dan kamu bertahan.\n")

    elif any(x in final for x in ["senang", "bahagia", "lega", "tenang"]):
        print("Aku ikut seneng dengernya. Kamu pantas bahagia.")
        print("Semoga perasaan baik ini tetap tinggal di hatimu lebih lama.\n")

    else:
        print("Perasaanmu valid, walaupun sulit dijelaskan.")
        print("Yang penting kamu udah berani untuk merasakannya.")
        print("Itu langkah yang dewasa dan kuat.\n")

    print("Terima kasih sudah mau journaling hari ini.")
    print("Kamu sudah melakukan yang terbaik. Kamu pantas dan layak dipahami dan hidup di dunia ini.\n")
    print("TERIMAKASIH SUDAH BERTAHAN!.\n")

    input("Tekan enter untuk kembali...")