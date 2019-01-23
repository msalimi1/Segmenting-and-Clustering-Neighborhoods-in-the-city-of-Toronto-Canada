from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text

soup = BeautifulSoup(source, "lxml")

csv_file = open('postal_codes.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['PostalCode', 'Borough', 'Neighbourhood'])

for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
    data = items.find_all('td')
    try:
        PostalCode = data[0].text
        Borough = data[1].text
        Neighbourhood = data[1].find_next_sibling().text
    except IndexError:pass

    csv_writer.writerow([PostalCode, Borough, Neighbourhood])

csv_file.close()