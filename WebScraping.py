# Project : Web scraper using BeautifulSoup4 and requests 
import requests 
from bs4 import BeautifulSoup 
 
oyo_url = "https://www.oyorooms.com/hotels-in-mumbai/"
 
req = requests.get(oyo_url) 
content = req.content 
 
soup = BeautifulSoup(content, "html.parser") 
 
all_hotels = soup.find_all("div", {"class": "hotelCardListing"}) 
 
for hotel in all_hotels: 
    hotel_name = hotel.find("h1", {"class": "listingContentHeader__h1"}).text 
    print(hotel_name)
