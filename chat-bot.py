import nltk
import random
from nltk.chat.util import Chat, reflections

# Definisi pola-pola dan respons yang sesuai
pola = [
    (r'hai|halo|hey|holla|hi|hello', ['Halo!', 'Hi!', 'Hai, ada yang bisa saya bantu?']),
    (r'apa kabar?', ['Baik. Terima kasih.', 'Bagus. Terima kasih.', 'Saya hanya sebuah program.']),
    (r'bagaimana kabarmu?', ['Saya hanya sebuah program.', 'Saya tidak punya perasaan, tapi terima kasih sudah bertanya.']),
    (r'siapa kamu?', ['Saya adalah chatbot yang diciptakan menggunakan Python.', 'Saya adalah program komputer yang disebut chatbot.']),
    (r'(keluar|exit|bye|sampai jumpa)', ['Sampai jumpa!', 'Selamat tinggal!', 'Goodbye!']),
    (r'(.*)', ['Maaf, saya tidak begitu mengerti apa yang kamu maksud.'])
]

# Inisialisasi chatbot
chatbot = Chat(pola, reflections)

def chat():
    print("Halo! Saya chatbot sederhana. Untuk keluar, cukup ketik 'keluar'.")
    while True:
        try:
            pertanyaan = input("Anda: ")
            respons = chatbot.respond(pertanyaan)
            print("Bot:", respons)
        except KeyboardInterrupt:
            print("Sampai jumpa!")
            break

if __name__ == "__main__":
    chat()
