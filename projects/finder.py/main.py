import requests as rq
import random as rd
from pyfiglet import Figlet
import json
import webbrowser as wb

def save_response(response, data):
    data.update({"url" : f"https://www.google.com/maps?q={response.get("lat")},{response.get('lon')}"})
    response.update({"url" : f"https://www.google.com/maps?q={response.get("lat")},{response.get('lon')}"})
    num = rd.randint(100,999)

    with open(f"saves/{response.get("country")}{num}.json" , "w", encoding="utf-8") as filejson:
        json.dump(response, filejson, indent = 4, ensure_ascii=False)

    with open(f"saves/{response.get("country")}{num}.md" , "w", encoding="utf-8") as filemd:
        for k, v in data.items():
            filemd.write(f"{k} - {v}\n")

def open_map(lat,lon):
    url = f"https://www.google.com/maps?q={lat},{lon}"
    wb.open(url)

def get_info_by_api(ip):
    print()
    try:
        response = rq.get(url=f"http://ip-api.com/json/{ip}").json()
        data = {
            'IP': response.get('query'),
            'Provider': response.get("isp"),
            'Organization': response.get('org'),
            'Country': response.get("country"),
            'City': response.get("city"),
            'Lat and Lon': (response.get("lat"), response.get("lon"))
        }

        for k, v in data.items():
            print(f"{k} - {v}")

        save_response(response,data)
        open_map(response.get('lat'),response.get("lon"))

    except rq.exceptions.ConnectionError:
        print(f'Check your conection - {rq.exceptions.ConnectionError}')

def main():
    preview = Figlet(font='slant')
    print(preview.renderText("FINDER"))
    print("Write IP")
    ip = input("> ")

    get_info_by_api(ip)

if __name__ =="__main__":
    main()
