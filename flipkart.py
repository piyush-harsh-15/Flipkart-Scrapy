from bs4 import BeautifulSoup
import requests
import re
import csv

search = input("What do you want to search? ")

url = f"https://www.flipkart.com/search?q={search}"
page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")

csv_file = open('flipkart_results.csv', 'w', encoding='utf-8')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price', 'Link'])

page_ind = soup.find(class_='_2MImiq').span
pg_btm = str(page_ind).split("<")[1]
pg_num = str(pg_btm).split(" ")[-1]
print("total result pages: " +pg_num)
pge = int(pg_num)

for pg in range(pge):
    url = f"https://www.flipkart.com/search?q={search}&page={pg}"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    device_name = soup.find(class_= "_4rR01T").string
    device_price = soup.find(class_= "_30jeq3 _1_WHN1").string
    link = soup.find(class_= "_1fQZEK")["href"]
    print("Device: "+device_name +" Price: " +device_price+ " Link: " +link)
    print()

    csv_writer.writerow([device_name, device_price, link])

csv_file.close()





