import requests
from bs4 import BeautifulSoup
from csv import writer, reader

# for num in range(1,37):
url = "https://www.goodhousekeeping.com/holidays/valentines-day-ideas/g4093/valentines-day-quotes/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all(class_="slideshow-slide-dek")
with open("valentines-quotes.csv", "w") as file:
	csv_writer = writer(file)
	for quote in quotes:
		csv_writer.writerow([quote.p.get_text()])

with open("valentines-quotes.csv", "r") as file:
	csv_reader = reader(file)
	for row in csv_reader:
		print(row)