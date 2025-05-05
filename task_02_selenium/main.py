import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from database import save_all_certification_data
import json

def scrape_page(driver, url):
    driver.get(url)
    time.sleep(1)

    driver.find_elements('xpath', '//a')[4].click()
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, 1800)")
    time.sleep(2)

    driver.find_elements(By.CLASS_NAME, 'pagination-link')[0].click()
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(2)

    driver.find_elements(By.LINK_TEXT, 'View Details')[3].click()
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    title = soup.find('section', class_= 'certification-detail').find('h3').text.strip()
    desc = soup.find('div', class_='certification-description')
    full_text = desc.get_text(separator="\n").strip()
    lines = full_text.split('\n')
    desc = '\n'.join(lines[:4])
    image_tag = soup.find('div', class_='certification-image').find('img')
    image_url = image_tag['src'] if image_tag else None
    date_tag = soup.find('div', class_='certification-date').text.strip()
    data_tag_list = []
    for i in date_tag.split(' '):
        data_tag_list.append(i)

    obtained_date = data_tag_list[1]+'-'+data_tag_list[2]

    skill_data_dic = {}
    skill_data_list = []
    skill_name = soup.find_all('table')[0].find_all('td')
    # print(skill_name)
    for i in range(0,len(skill_name), 2):
        skill_data_dic["name"] = skill_name[i].text.strip()
        if skill_name[i+1].text.strip() == skill_name[1].text.strip():
            skill_data_dic["covered"] = True
        else:
            skill_data_dic["covered"] = False
        skill_data_list.append(skill_data_dic)


    # print(skill_data_dic)

    social_data_list = []

    social_media_links = soup.find_all('div', class_='social-links')[0].find_all('a')
    for i in range(0,len(social_media_links)):
        social_data_dic = {}
        social_data_dic["platform"] = social_media_links[i]['aria-label']
        social_data_dic["url"] = social_media_links[i]['href']
        social_data_list.append(social_data_dic)

    # Return parsed data
    return {
        "title": title,
        "description": desc,
        "image_url": image_url,
        "obtained_date": obtained_date,
        "skills": skill_data_list,
        "social_links": social_data_list,
    }


def write_to_json_file(data, filename="certification_data.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    data = scrape_page(driver, url="https://shaxzodbek.com/")
    if data:
        write_to_json_file(data)  # << bu yerda chaqiramiz
        save_all_certification_data(data)
    else:
        print("Ma'lumotlarni olishda xatolik yuz berdi.")


if __name__ == "__main__":
    main()




