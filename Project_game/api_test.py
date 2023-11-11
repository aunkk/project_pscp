import requests

api_key = "e1c5932f6c96b34e1263878d1f8b7931"
city = input("country : ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# ดึงข้อมูลจาก API ที่เลือกไว้
res = requests.get(url).json()
weather = res['weather'][0]['main']

# print(weather)