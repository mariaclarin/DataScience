#mporting Libraries
from doctest import Example
from tkinter.tix import Tree
from bs4 import BeautifulSoup
import pandas as pd
import requests
import sys 

print("===========================================================================================")
#User Input. Inputs the series code and latest season based on the series they want to find.
codeInput = input('Hi! Please enter the series code from IMDB (e.g. tt4574334): ')
url = "https://www.imdb.com/title/" + codeInput +"/episodes?season=" #Url that contains all the seasons of the series. But pops an error if you try to access it in your browser.
url1 = "https://www.imdb.com/title/"+ codeInput +"/episodes?season=1" #Url of the first season of the series of the code the user entered. It's accessible in your browser.
seasonInput = int(input('Enter the latest season for this series (e.g. 4): '))

#Getting a response from the url
response = requests.get(url)
responseSeason1 = requests.get(url1) 

#Parsing with beautiful soup
soup  = BeautifulSoup(response.text, 'html.parser')
soupSeason1 = BeautifulSoup(responseSeason1.text, 'html.parser')

#Prints the title of the website (url1), which is the title of the series from the first season. 
print("===========================================================================================")
print("Series Title : ")
for title in soupSeason1.find_all('title'):
    print(title.get_text())

#User confirmation, if the user types Y/y, the program will continue, else, the system will exit()
titleConfirmation = input('Is this the series you are refering to? (Y/N) : ')
if titleConfirmation == "Y":
    run = True
elif titleConfirmation == "y":
    run = True
elif titleConfirmation == "N":
    print("---------------------------------------------------------------------------------------")
    print('Terminating Sequence. Please try again and ensure it is the right code to the series.')
    print("---------------------------------------------------------------------------------------")
    sys.exit()
elif titleConfirmation == "n":
    print("---------------------------------------------------------------------------------------")
    print('Terminating Sequence. Please try again and ensure it is the right code to the series.')
    print("---------------------------------------------------------------------------------------")
    sys.exit()
else :
    print("---------------------------------------------------------------------------------------")
    print("Invalid Confirmation! Please Try Again.")
    print("---------------------------------------------------------------------------------------")
    sys.exit()

#if the user has already confirmed the title of the series, the program will then do all the webscraping process !!!
while run==True:
    #Creating an empty list to later append the episode details to
    episodeList = []


    #Including each and every season of the series
    for season in range(1, seasonInput+1):
        #Getting a response from the url and parsing it with requests and BeautifulSoup
        response = requests.get( url + str(season) )#"https://www.imdb.com/title/tt4574334/episodes?season=" + str(season))
        soup = BeautifulSoup(response.text, 'html.parser') 

        #To find and recognize the relevant data found in the page, understanding from the inspect feature in google to find all the divs containing the data we need
        episodeData = soup.findAll('div', class_='info')
        imageData = soup.findAll('div', class_='image')
        # imageLink = []

        #A loop to divide and organize each data found in the episodeData found earlier based on the individual inspected elements
        for episodes in episodeData:
            
            #Season
            sn = season 
            #Episode No.
            episode_number = episodes.meta['content']
            #Title of the Episode
            title = episodes.a['title']
            #Episode Air Date
            airdate = episodes.find('div', class_='airdate').text.strip()
            #Rating of each episode
            rating = episodes.find('span', class_='ipl-rating-star__rating').text
            #Total Votes
            total_votes = episodes.find('span', class_='ipl-rating-star__total-votes').text
            #Description of each episode
            desc = episodes.find('div', class_='item_description').text.strip()
        
            #Putting all the details together and organizing them into one block
            episodeDetails = [season, episode_number, title, airdate, rating, total_votes, desc]
    

            #Adding/appending the episodeDetails to the previously empty list 
            episodeList.append(episodeDetails)
        


    #DataFraming with Pandas
    episodeList = pd.DataFrame(episodeList, columns=['season', 'episode_number', 'title', 'airdate', 'rating', 'total_votes', 'description'])
    episodeList.head()

    #Functions to format and clean up the display
    #commas and spaces
    def remove_str(votes):
        for r in ((',', ''), ('(', ''), (')', '')):
            votes = votes.replace(*r)
        return votes

    #formatting data types to suit the data.
    episodeList['total_votes'] = episodeList.total_votes.apply(remove_str).astype(int)
    episodeList['rating'] = episodeList.rating.astype(float)
    episodeList['airdate'] = pd.to_datetime(episodeList.airdate)

    #creating a head for the csv/spreadsheet layout
    episodeList.head()
    #creating infos for the csv/spreadsheet layout
    episodeList.info()

    #Converting to CSV
    episodeList.to_csv('IMDB_Series_Info.csv', index=False)
    run = False
    sys.exit()
