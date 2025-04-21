# Task02 Selenium: Web Scraping and Database Integration

## 📖 Project Overview

This Python project automates web scraping of target web pages using **Selenium** and **BeautifulSoup4**, then processes and stores the extracted data in a **PostgreSQL** database.


---

## 🔍 Key Features

- 🚀 **Automated Browsing**: Launches a browser, navigates, scrolls, and clicks through pages
- 🧹 **Data Extraction**: Parses HTML to pull out titles, descriptions, images, dates, skills, and social links
- 🐘 **Database Integration**: Uses `psycopg2` to insert and update scraped data in PostgreSQL
- 📄 **Output Logging**: Saves raw results to a text file at `output/data.txt`


---

## 📁 Project Structure

```plaintext
Task1_lab1/
├── config.py         # Configuration settings (DB credentials, URLs, etc.)
├── database.py       # PostgreSQL connection and CRUD functions
├── main.py           # Entry point: orchestrates scraping and DB operations
├── models.py         # Data model definitions (classes/structures)
├── output/
│   └── data.txt      # Captured/raw scraped output
├── requirements.txt  # Python dependencies
```


---

## 🛠 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/anvaraxadjonov1802/2k24-407_python.git
   cd 2k24-407_python/task_02_selenium
   ```
2. **Create and activate a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate       # Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```


---

## ⚙️ Configuration

Edit `config.py` to match your environment:

```python
# Database settings
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'your_database'
DB_USER = 'your_user'
DB_PASSWORD = 'your_password'
```


---

## 🚀 Running the Project

Execute the main script to start scraping and database insertion:

```bash
python main.py
```

- Scraped data will be appended to `output/data.txt`
- Parsed records will be stored in your PostgreSQL database


---


