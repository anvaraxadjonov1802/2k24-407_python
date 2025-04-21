```markdown
# 🗂 2papka - Veb sahifani skreyp qilish loyihasi

Bu loyiha Selenium va BeautifulSoup yordamida veb sahifani avtomatik tarzda ochish, skroll qilish, kerakli tugmalarni bosish va sahifadan kerakli ma'lumotlarni ajratib olish uchun ishlab chiqilgan. Loyihada, shuningdek, ijtimoiy tarmoqlarga oid havolalar va ko‘nikmalar (skills) bo‘yicha ma’lumotlar ham yig‘iladi.

---

## 📌 Asosiy funksiyalar:

- Saytga avtomatik kirish
- Sahifa bo‘ylab harakatlanish (scroll)
- "View Details" tugmasini topib, bosish
- Sahifadagi:
  - Sarlavha (`title`)
  - Tavsif (`description`)
  - Rasm (`image_url`)
  - Sanalar (`obtained_date`)
  - Ko‘nikmalar (`skills`)
  - Ijtimoiy tarmoq havolalari (`social_links`)
  
  kabi ma'lumotlarni ajratib olish

---

## 🧰 Ishlatilgan texnologiyalar:

- `Python`
- `Selenium`
- `BeautifulSoup`
- `webdriver-manager`
- `psycopg2` (bazaga ulanish uchun tayyorlangan)
- `Chrome WebDriver`

---

## 📂 Loyihaning tuzilmasi:

```
2papka/
├── main.py              # Dastur ishga tushuvchi fayl
├── requirements.txt     # Zaruriy kutubxonalar
└── README.md            # Loyihaga oid hujjat (mana shu fayl)
```

---

## ⚙️ O‘rnatish va ishga tushirish:

```bash
# repozitoriyani klon qilish
git clone https://github.com/username/repository-name.git

# 2papka ichiga o‘tish
cd repository-name/2papka

# Kutubxonalarni o‘rnatish
pip install -r requirements.txt

# Dastur ishga tushiriladi
python main.py
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
