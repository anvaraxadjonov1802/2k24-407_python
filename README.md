# Task1_lab1

Bu loyiha Python tilida yozilgan va ma'lumotlar bazasi bilan ishlovchi sertifikatlash tizimi loyihasining birinchi laboratoriya topshirig'idir.

## 📌 Loyihaning maqsadi

Loyihaning asosiy maqsadi — `certification_data.txt` faylidan ma'lumotlarni o'qib olish, ularni ma'lumotlar bazasiga saqlash, so‘ngra kerakli amallarni bajarish (filtrlash, ko‘rish, va hokazo). 

## 📁 Loyihadagi asosiy fayllar

- `main.py` — Dastur ishga tushadigan asosiy fayl.
- `config.py` — Bazaga ulanish konfiguratsiyalari.
- `database.py` — Ma'lumotlar bazasi bilan ishlovchi funksiyalar.
- `models.py` — ORM model tavsiflari.
- `requirements.txt` — Loyihaga kerakli kutubxonalar ro‘yxati.
- `certification_data.txt` — Sertifikatlash bilan bog‘liq xom ma’lumotlar.

## ▶️ Ishga tushirish

1. Repozitoriyani yuklab oling yoki klon qiling:
   ```bash
   git clone https://github.com/yourusername/Task1_lab1.git
   cd Task1_lab1
2. Virtual muhit yarating (ixtiyoriy, lekin tavsiya etiladi):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows uchun: venv\Scripts\activate
3. Kerakli kutubxonalarni o‘rnating:
   ```bash
   pip install -r requirements.txt
4. Dasturni ishga tushiring:
   ```bash
   python main.py
   
## 🛠 Texnologiyalar
Python 3.9+

SQLite (yoki SQLAlchemy)

Standart kutubxonalar (os, sys, va h.k.)

## 💡 Foydalanish
Dastur certification_data.txt faylini o‘qiydi va ma’lumotlarni ma'lumotlar bazasiga joylashtiradi. Siz main.py faylidan foydalanib, asosiy funksiyalarni ishga tushirishingiz mumkin.

## 👨‍💻 Muallif
Ism: Anvar Axadjonov

E-mail: axadjonov123@gmail.com

GitHub: anvaraxadjonov1802
