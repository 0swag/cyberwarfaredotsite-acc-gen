from rgbprint import gradient_scroll, Color
import requests
from bs4 import BeautifulSoup
from random import randint, sample
import threading

def generate_account(url, usern, pw, ref_num):
    for i in range(0, int(times/100)):
        session = requests.Session()
        session.headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    }

        response1 = session.get(url)
        soup = BeautifulSoup(response1.content, "html.parser")
    
        token_elem = soup.find("input", {"name": "token"})
        token_value = token_elem["value"]
    
        sess_cookie = session.cookies.get("PHPSESSID")
        rand_lett = "".join(sample('abcdefghijklmnopqrstuvwxyz', 8))
        name = rand_lett
    
        gradient_scroll(
            f" > {name}:{pw + rand_lett}", 
    start_color=Color.orange, 
    end_color=Color.red
)
        response2 = session.post(
        url,
        headers={
            "Referer": url,
            "Cookie": f"PHPSESSID={sess_cookie}"
        },
        data={
            "username": name,
            "email": f"{usern}{randint(0, 9999)}@gmail.com",
            "password_1": rand_lett,
            "password_2": rand_lett,
            "Referral": ref_num,
            "token": token_value,
            "reg_user": ""
        }
    )



url = "https://cyberwarfare.site/register.php"
times = int(input("\n> Number of accounts to generate: "))
usern = input("\n> Username: ")
pw = input("\n> Password: ")
ref_num = input("\n> Referer Number: ")
threads = []

for _ in range(800):
    thread = threading.Thread(target=generate_account, args=(url, usern, pw, ref_num))
    thread.start()


#print("============================================\n              FINISHED\n============================================")


