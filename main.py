from flask import *
import json
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
# BASE_URL = 'http://jaink7069.pythonanywhere.com/'
app = Flask(__name__)

data = pd.read_csv('Book1.csv')
lent = len(data)
data_set= []
for i in range(lent):
    data_set.append([str(int(data['year'][i])), data['name'][i], data['field'][i], data['branch'][i], data['url'][i], data['pos'][i]])



driver = webdriver.Chrome("Enter-Location-Of-Your-Web-Driver")
    # Logging into LinkedIn
driver.get("https://linkedin.com/uas/login")
    # time.sleep(20)

username = driver.find_element("id", "username")
username.send_keys("rudra.psc20@gmail.com")  # Enter Your Email Address

pword = driver.find_element("id", "password")
pword.send_keys("rudra2811")  # Enter Your Password

driver.find_element("xpath", "//button[@type='submit']").click()

for i in range(lent):

    profile_url = data['url'][i]
    print(profile_url)



    driver.get(profile_url)  # this will open the link
    start = time.time()

    # will be used in the while loop
    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

        initialScroll = finalScroll
        finalScroll += 1000


        time.sleep(1)
        # You can change it as per your needs and internet speed

        end = time.time()

        # We will scroll for 20 seconds.
        # You can change it as per your needs and internet speed
        if round(end - start) > 0:
            break
    src = driver.page_source

    # Now using beautiful soup
    soup = BeautifulSoup(src, 'lxml')
    intro = soup.find('div', {'class': 'pv-text-details__left-panel'})



    experience = soup.find("li", {"class": "pv-text-details__right-panel-item"})
    company_loc = experience.find_all("div", {
        "inline-show-more-text inline-show-more-text--is-collapsed inline-show-more-text--is-collapsed-with-line-clamp inline"})


    data['pos'][i] = company_loc[0].get_text().strip()
@app.route('/data/',methods=['GET'])
def home_page():
    data2 = pd.read_csv('Book1.csv')
    lent2 = len(data2)
    data_set2 = []
    for i in range(lent2):
        data_set2.append([str(int(data['year'][i])), data['name'][i], data['field'][i], data['branch'][i], data['url'][i], data['pos'][i]])

    json_dump = json.dumps(data_set2)
    return json_dump
@app.route('/add/',methods=['GET'])
def add_page():
    user_query1 = str(request.args.get('year'))
    user_query2 = str(request.args.get('name'))
    user_query3 = str(request.args.get('field'))
    user_query4 = str(request.args.get('branch'))
    user_query5 = str(request.args.get('url'))
    data1 = pd.read_csv('Book1.csv')
    lent1 = len(data)
    data1.loc[lent1, 'year'] = user_query1
    data1.loc[lent1, 'name'] = user_query2
    data1.loc[lent1, 'field'] = user_query3
    data1.loc[lent1, 'branch'] = user_query4
    data1.loc[lent1, 'url'] = user_query5
    driver = webdriver.Chrome("Enter-Location-Of-Your-Web-Driver")
    # Logging into LinkedIn
    driver.get("https://linkedin.com/uas/login")
    # time.sleep(20)

    username = driver.find_element("id", "username")
    username.send_keys("rudra.psc20@gmail.com")  # Enter Your Email Address

    pword = driver.find_element("id", "password")
    pword.send_keys("rudra2811")  # Enter Your Password

    driver.find_element("xpath", "//button[@type='submit']").click()

    profile_url = data1.loc[lent1, 'url']
    print(profile_url)

    driver.get(profile_url)  # this will open the link
    start = time.time()

    # will be used in the while loop
    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

        initialScroll = finalScroll
        finalScroll += 1000

        time.sleep(1)
        # You can change it as per your needs and internet speed

        end = time.time()

        # We will scroll for 20 seconds.
        # You can change it as per your needs and internet speed
        if round(end - start) > 0:
            break
    src = driver.page_source

    # Now using beautiful soup
    soup = BeautifulSoup(src, 'lxml')
    intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

    experience = soup.find("li", {"class": "pv-text-details__right-panel-item"})
    company_loc = experience.find_all("div", {
        "inline-show-more-text inline-show-more-text--is-collapsed inline-show-more-text--is-collapsed-with-line-clamp inline"})


    user_query6 = company_loc[0].get_text().strip()

    data1.loc[lent1, 'pos'] = user_query6
    data1.to_csv('Book1.csv', index=False)
    data2 = pd.read_csv('Book1.csv')
    print(data2)

@app.route('/',methods=['GET'])
def mix_page():
    # user_query1, user_query2, user_query3, user_query4 = "default"
    user_query1 = str(request.args.get('year'))
    user_query2 = str(request.args.get('name'))
    user_query3 = str(request.args.get('field'))
    user_query4 = str(request.args.get('branch'))
    mix_set1 = []
    mix_set2 = []
    mix_set3 = []
    mix_set4 = []
    if user_query1 != "default":
        for x, i in enumerate(data_set):
            if data_set[x][0] == user_query1:
                mix_set1.append(data_set[x])
    if user_query2 != "default":
        for x, i in enumerate(data_set):
            if data_set[x][1] == user_query2:
                mix_set2.append(data_set[x])
    if user_query3 != "default":
        for x, i in enumerate(data_set):
            if data_set[x][2] == user_query3:
                mix_set3.append(data_set[x])
    if user_query4 != "default":
        for x, i in enumerate(data_set):
            if data_set[x][3] == user_query4:
                mix_set4.append(data_set[x])
    # lst3 = [value for value in lst1 if value in lst2] intersection
    # final_list = lst1 + lst2 union
    result_set = []
    if user_query1 != "default":
        result_set = mix_set1
    elif user_query2 != "default":
        result_set = mix_set2
    elif user_query3 != "default":
        result_set = mix_set3
    elif user_query4 != "default":
        result_set = mix_set4
    else:
        result_set = data_set
    if user_query1 != "default":
        result_set = [value for value in result_set if value in mix_set1]
    if user_query2 != "default":
        result_set = [value for value in result_set if value in mix_set2]
    if user_query3 != "default":
        result_set = [value for value in result_set if value in mix_set3]
    if user_query4 != "default":
        result_set = [value for value in result_set if value in mix_set4]
    json_dump = json.dumps(result_set)
    return json_dump
if __name__=='__main__':
    app.run(port=7777)