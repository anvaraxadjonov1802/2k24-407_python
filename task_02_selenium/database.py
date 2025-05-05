from models import connect_db, create_table


def save_all_certification_data(data):
    create_table()
    conn = connect_db()
    cursor = conn.cursor()

    # add certification
    cursor.execute("""
            INSERT INTO certifications (title, description, image_url, obtained_date)
            VALUES (%s, %s, %s, %s);
        """, (data['title'],
              data['description'],
              data['image_url'],
              data['obtained_date']))

    cursor.execute("""
    SELECT * from certifications
    WHERE title = %s;""", (data['title'],))
    certification_data = cursor.fetchone()
    certification_id = certification_data[0]

    # add skill
    for skill in data.get('skills', []):
        cursor.execute("""  
            INSERT INTO skills (certification_id, skill_name, covered) 
            VALUES (%s, %s, %s);
        """, (certification_id, skill['name'], skill.get('covered', False)))

    # add social links
    for link in data.get('social_links', []):
        cursor.execute("""  
            INSERT INTO social_media_links (certification_id, platform, url) 
            VALUES (%s, %s, %s);
        """, (certification_id, link['platform'], link['url']))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Barcha ma'lumotlar saqlandi saqlandi.")

def save_to_db(data):
    conn = connect_db()
    cursor = conn.cursor()



