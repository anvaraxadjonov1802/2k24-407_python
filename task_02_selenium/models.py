import psycopg2
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
        )
        print("PostgreSQL bazasiga ulanish muvaffaqiyatli!")
    except Exception as e:
        print(f"Ulanishda xato: {e}")
        exit()
    return conn

def create_table():

    conn = connect_db()
    cur = conn.cursor()

    create_certifications_table = '''
    CREATE TABLE IF NOT EXISTS certifications (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        image_url VARCHAR(255),
        obtained_date VARCHAR(20), 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    '''

    create_skills_table = '''   
    CREATE TABLE IF NOT EXISTS skills (
        id SERIAL PRIMARY KEY,
        certification_id INT REFERENCES certifications(id) ON DELETE CASCADE,
        skill_name VARCHAR(255),
        covered BOOLEAN DEFAULT FALSE
    );
    '''

    create_social_media_links_table = '''
    CREATE TABLE IF NOT EXISTS social_media_links (
        id SERIAL PRIMARY KEY,
        certification_id INT REFERENCES certifications(id) ON DELETE CASCADE,
        platform VARCHAR(255),
        url VARCHAR(255)
    );
    '''


    # Jadvalni yaratish
    try:
        cur.execute(create_certifications_table)
        cur.execute(create_skills_table)
        cur.execute(create_social_media_links_table)
        conn.commit()  # O'zgartirishlarni saqlash
        print("Jadvallar yaratildi!")
    except Exception as e:
        print(f"Jadval yaratishda xato: {e}")
        conn.rollback()

    # Cursorni yopish
    cur.close()