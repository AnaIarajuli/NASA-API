# import requests
# import json
# #
# key = '6QUqTutiwZggAdrINghs5NpeK6yuaqTKGcceHhLb'
# payload = {'api_key': key}
# url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos'
#
#
#         #გამოიყენეთ requests მოდულის მინიმუმ 3-4 ფუნქცია/ატრიბუტი (მაგ. get(), status_code, header)
# r = requests.get(url, params=payload)
# print(r.status_code)
# print(r.headers)
# print(r.text)


#         #შეინახეთ json ფორმატის მონაცემი json ფაილში სტრუქტურული სახით (json მოდულის ფუნქციის გამოყენებით)
#
# res = r.json()
# with open('marsRoverData.json', 'w') as file:
#     json.dump(res, file, indent=4)

#
#         #გამოიყენეთ json/dict ობიექტთან სამუშაო ფუნქციები და დაბეჭდეთ თქვენთვის საინტერესო ინფორმაცია, რასაც გსურთ რომ API-ს მეშვეობით მიწვდეთ
#
# with open('marsRoverData.json', 'r') as file:
#     res = json.load(file)
# #
# def get_info(list_index, info):
#     return res['latest_photos'][list_index][info]

# rover = get_info(0, 'rover')
# print(rover)
# mars_date = get_info(0, 'sol')
# print(mars_date)
#
# # image_url = get_info(0, 'img_src')
# # image_result = requests.get(image_url)
# # img_file = open('2022-05-11.jpg', 'wb')
# # img_file.write(image_result.content)


#         #შეინახეთ თქვენთვის საინტერესო ინფორმაცია ბაზაში (შექმენით ცხრილი პითონის მეშვეობით, აღწერეთ მოკლე კომენტარის სახით)
# import json
# import sqlite3
#
# conn = sqlite3.connect('MarsData.sqlite')
# cursor = conn.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS mars
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 sol INTEGER,
#                 rover_name VARCHAR(40),
#                 img_src VARCHAR(40))''')
#
# mars_info = []
# info = json.load(open('marsRoverData.json'))
#
# for row in info['latest_photos']:
#     marsInfo = (row['sol'], row['rover']['name'], row['img_src'])
#     mars_info.append(marsInfo)
#
# print(mars_info)
#
#
# cursor.executemany("INSERT INTO mars (sol, rover_name, img_src) VALUES (?, ?, ?)", mars_info)
# conn.commit()
#
# conn.close()