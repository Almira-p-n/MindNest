import json
import time
from app.mood_checker import mood_check
from app.diary_ai import diary_ai
from app.calm_box import calm_menu
from app.quotes import quotes
from app.utils import clear

def main():
    run = True
    while run:
        clear()
        print("=== MINDNEST ===")
        print("1. MoodCheck (cek suasana hati)")
        print("2. CalmBox (latihan relaksasi atau menenangkan diri) ")
        print("3. DiaryAI (curhat harian)")
        print("4. Quotes (memberikan kata-kata)")
        print("5. Exit")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            mood_check()
        elif pilihan == "2":
            calm_menu()
        elif pilihan == "3":
            diary_ai()
        elif pilihan == "4":
            quotes()
        elif pilihan == "5":
            print("Terimakasih telah menggunakan MINDNEST!")
            time.sleep(2)
            run = False
        else:
            input("Pilihan tidak valid, tekan enter.")


if __name__ == "__main__":
    main()
