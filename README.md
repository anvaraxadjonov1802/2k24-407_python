```markdown
# 🗂 2papka - Veb sahifa scraper va ma'lumotlar bazasi integratsiyasi

Bu papkada veb sahifani avtomatik tarzda skreyp qilish va olinadigan ma’lumotlarni ma’lumotlar bazasiga yozish bo‘yicha Python loyihasi joylashgan. Loyiha `Selenium`, `BeautifulSoup`, va `psycopg2` kutubxonalaridan foydalanadi.

---

## 📁 Loyihaning tuzilmasi:

- `main.py` — asosiy ishga tushadigan fayl, barcha jarayonlarni boshqaradi
- `config.py` — konfiguratsiyalar (masalan: baza ma’lumotlari, URL-lar)
- `database.py` — PostgreSQL bilan ishlovchi funksiyalar
- `models.py` — ma’lumotlar tuzilmasi va ularni qayta ishlash
- `output/` — skreyp qilingan ma’lumotlar saqlanadigan joy (agar faylga yozilsa)
- `requirements.txt` — zarur kutubxonalar ro‘yxati

---

## 🧰 Ishlatilgan texnologiyalar:

- Python 3.x
- Selenium
- BeautifulSoup4
- psycopg2
- webdriver-manager

---

## ⚙️ O‘rnatish:

```bash
# repozitoriyani klon qilish
git clone https://github.com/username/repo-nomi.git

# papkaga o‘tish
cd repo-nomi/2papka

# virtual muhit yaratish (ixtiyoriy)
python -m venv venv
source venv/bin/activate  # yoki Windows: venv\Scripts\activate

# kerakli kutubxonalarni o‘rnatish
pip install -r requirements.txt

```

---

## 💡 Eslatma

> Ushbu loyiha Google Chrome brauzeri va `chromedriver` bilan ishlaydi. `webdriver-manager` esa kerakli driver’ni avtomatik yuklaydi.

---

## 🤝 Hissa qo‘shish

Agar sizda yaxshilash bo‘yicha fikrlar bo‘lsa, bemalol `pull request` yuboring yoki `issue` oching.

---

## 📄 Litsenziya

Ushbu loyiha [MIT License](LICENSE) ostida tarqatiladi.

---

```

---

Agar loyihada qo‘shimcha fayllar yoki imkoniyatlar mavjud bo‘lsa, ayting — `README.md`ni yanada boyitib beraman. Yoki `psycopg2` bilan ishlatiladigan qism ham bo‘lsa, uni ham qo‘shib beraman.
