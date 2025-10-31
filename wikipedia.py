from bs4 import BeautifulSoup
import requests
countryName = input("type your country:")

url = f"https://en.wikipedia.org/wiki/{countryName}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}
response  = requests.get(url= url, headers= headers)

if response.status_code == 200:
    soap = BeautifulSoup(response.text, "html.parser")
    tittle = soap.find("span", class_ = "mw-page-title-main")

    if tittle :
        print(f"\n Tittle: {tittle.text.strip}")

    print("\nSummary:")
    paragraph = soap.find_all("p")

    for par in paragraph[:3]:
        print(f"{par.text.strip()}\n")
    
    print("\nInfo_box:")
    info_box = soap.find("table", class_="infobox")
    if info_box:
          for row in info_box.find_all("tr"):
            header = row.find("th")
            data = row.find("td")
            if header and data:
                print(f"{header.text.strip()}: {data.text.strip()}")
    else:
        print("Inbox not found:")
else:
    print("Page not found or blocked")