---

```markdown
<h1 align="center">📁 2papka - Veb Sahifa Scraper & Ma'lumotlar Bazasi Integratsiyasi</h1>

<p align="center">
  <b>Veb sahifalarni avtomatlashtirilgan tarzda skreyp qilish, ma'lumotlarni qayta ishlash va PostgreSQL bazasiga yozish loyihasi.</b>
</p>

---

## 📂 Papka tuzilmasi

```
2papka/
├── config.py         # Loyihaning sozlamalari
├── database.py       # PostgreSQL bilan aloqa funksiyalari
├── main.py           # Loyihaning ishga tushiriladigan fayli
├── models.py         # Ma'lumotlar tuzilmalari
├── output/           # Skreyp qilingan natijalar
└── requirements.txt  # Kutubxonalar ro'yxati
```

---

## 🛠 Texnologiyalar

- 🐍 Python 3.x  
- 🌐 Selenium  
- 🧼 BeautifulSoup4  
- 🐘 psycopg2  
- ⚙️ Webdriver Manager  

---

## 📦 O‘rnatish

```bash
# 1. Repozitoriyani yuklab oling
git clone https://github.com/username/repo-nomi.git

# 2. Papkaga kiring
cd repo-nomi/2papka

# 3. Virtual muhit yarating (ixtiyoriy)
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 4. Kutubxonalarni o'rnating
pip install -r requirements.txt
```

---

## 🚀 Ishga tushirish

```bash
python main.py
```

📝 *Eslatma:* `config.py` faylida sozlamalarni moslab chiqing (bazaga ulanish ma’lumotlari, URL, va h.k.).

---

## 💡 Qisqacha izohlar

- **`config.py`** — Barcha sozlamalar (URL, baza konfiguratsiyasi).
- **`database.py`** — Bazaga ulanish, jadval yaratish va yozish funksiyalari.
- **`main.py`** — Jarayonlarni boshqaruvchi asosiy fayl.
- **`models.py`** — Ma’lumotlar modelini belgilovchi sinflar.
- **`output/`** — Chiqarilgan fayllar va skreyp natijalari.
- **`requirements.txt`** — Barcha kerakli kutubxonalar ro‘yxati.

---

## 🤝 Hissa qo‘shish

> Takliflaringizni va tuzatishlaringizni mamnuniyat bilan kutamiz!  
> Pull Request yuboring yoki `issue` oching.

---
