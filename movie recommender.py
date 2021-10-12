# this program is based on following reports:(chosing those only which are above 50%)
#https://www.statista.com/statistics/949810/favorite-movie-genres-in-the-us-by-age/
#https://www.statista.com/statistics/254115/favorite-movie-genres-in-the-us/
#and details gathered by social media and movie websites for the specific time in the year when people tend to watch a specific genre
#like in february there is an increase in romantic film viewers maybe because february being valentine month
from bs4 import BeautifulSoup
import requests
import datetime
import random
import webbrowser

this_month=datetime.datetime.now().month
this_hour=datetime.datetime.now().hour
print("Hi! I am a simple movie/TV show recommender. Answer few questions to begin with.")
genres=["comedy","sci-fi","horror","romance","animation","adventure","fantasy","comedy,romance","action,comedy","action","drama","mystery","crime"]
age=int(input("What is your age?(in numbers eg 42)"))
gender=input("What is your gender?(type F for female, M for male and X for others)").strip()
print("Alright. Please be patient till I fetch the perfect match for you.")
month={1: ['sci-fi', 'horror', 'animation', 'mystery'], 2: ['horror', 'romance', 'animation', 'fantasy', 'comedy,romance', 'drama'], 3: ['sci-fi', 'horror', 'animation', 'mystery'], 4: ['comedy', 'horror', 'animation', 'adventure', 'comedy,romance', 'action,comedy', 'drama'], 5: ['comedy', 'sci-fi', 'horror', 'romance', 'animation', 'adventure', 'fantasy', 'comedy,romance', 'action,comedy', 'action', 'drama', 'mystery', 'crime'], 6: ['horror', 'animation'], 7: ['comedy', 'sci-fi', 'horror', 'romance', 'animation', 'adventure', 'fantasy', 'comedy,romance', 'action,comedy', 'action', 'drama', 'mystery', 'crime'], 8: ['comedy', 'sci-fi', 'horror', 'romance', 'animation', 'adventure', 'fantasy', 'comedy,romance', 'action,comedy', 'action', 'drama', 'mystery', 'crime'], 9: ['comedy', 'sci-fi', 'horror', 'romance', 'animation', 'adventure', 'fantasy', 'comedy,romance', 'action,comedy', 'action', 'drama', 'mystery', 'crime'], 10: ['horror', 'romance', 'animation', 'adventure', 'fantasy', 'comedy,romance', 'action,comedy','drama', 'mystery', 'crime'], 11: ['adventure', 'action,comedy','action', 'mystery', 'crime'], 12: ['comedy', 'sci-fi', 'horror', 'romance', 'animation', 'adventure', 'fantasy', 'comedy,romance', 'action,comedy', 'action', 'drama', 'mystery', 'crime']}
night=["horror","romance","animation","fantasy","comedy,romance","drama","mystery","crime"]
if this_hour>20:
    recommend=night
else:
    recommend=month[this_month]
if age>=65 or gender=="F":
    genre=random.choice(recommend)
    while genre=="horror":
        genre=random.choice(recommend)
else :
    genre=random.choice(recommend)
url="https://www.imdb.com/search/title/?genres="+genre
html=requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
h3=soup.find_all("h3",attrs={'lister-item-header'})
movies=[]
for i in range(len(h3)):
    movies.append(h3[i].find("a").get("href"))
print("Here you go:")
webbrowser.open("https://www.imdb.com/"+random.choice(movies))



