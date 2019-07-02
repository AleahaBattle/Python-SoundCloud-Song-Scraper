from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os

# get new, top, mix, track, and artist urls
# url for top songs 
top = 'https://soundcloud.com/charts/top'

# url for new songs 
new = 'https://soundcloud.com/charts/new'

# search for tracks
track = 'https://soundcloud.com/search/sounds?q='

# search for artists
artist = 'https://soundcloud.com/search/people?q='

# mix query added to end of tracks search url for songs > 30min
mix_end = '&filter.duration=epic'

# create a selenium browser, edit browser in real time using python
# click buttons, login, logout, etc through browser

browser = webdriver.Chrome('/Users/aleahab/Downloads/chromedriver')

browser.get('https://soundcloud.com')

# menus to welcome user and ask for input
# main menu
print('\n>>> Welcome to the Soundcloud Scrapper!')
print('>>> Explore the Top / New & Hot Charts for all Genres')
print('>>> Search for tracks, artists, and mixes\n')

# loop continues until user chooses to exit
while True:
    # Menu items to choose from
    print('>>> Menu')
    print('>>> 1 - Search for a track')
    print('>>> 2 - Search for an artist')
    print('>>> 3 - Search for a mix')
    print('>>> 4 - Top Charts')
    print('>>> 5 - New & Hot Charts')
    print('>>> 0 - Exit\n')
    
    # ask the user for their choice from menu
    choice = int(input('\n>>> Your choice: '))

    # Exit Browser
    if choice == 0:
        browser.quit()
        break
    
    # Search for a track
    if choice == 1:
        # get name of track
        name = input('Name of the track: ')
        name.replace(' ', '%20')
        browser.get(track + name)
        continue

    # Search for the name of the artist
    if choice == 2:
        # get name of track
        name = input('Name of the artist: ')
        name.replace(' ', '%20')
        browser.get(artist + name)
        continue

    # Search for a mix
    if choice == 3:
        # get name of track
        name = input('Name of the mix: ')
        name.replace(' ', '%20')
        browser.get(track + name + mix_end)
        continue

    # Get the top 50 tracks for a genre
    if choice == 4:
        # get html tags from top url, for top songs 
        request = requests.get(top)
        # parse html with lxml module
        soup = BeautifulSoup(request.text, 'lxml')
        # print(request.text)
        while True:
            print('>>> Genres Available: \n')

            # query to search for genre links
            genres = soup.select('a[href*=genre]')[2:]

            # add genre links to list
            genre_links = []

            # print all available genre links, idx used to select genre
            for idx, genre in enumerate(genres):
                print(f'{idx}: {genre.text}')
                genre_links.append(genre.get('href'))

            # ask the user for their choice from genre menu
            choice = input('\n>>> Your choice (press x to go back to the main menu): ')
            print()

            # exit genre menu
            if choice == 'x':
                break
            else:
                choice = int(choice)

            # use genre url
            genre_url = 'https://soundcloud.com' + genre_links[choice]
            # get html tags from genre url
            genre_request = requests.get(genre_url)
            # parse html with lxml module
            soup = BeautifulSoup(genre_request.text, 'lxml')
            print(genre_request.text)
            
            # add track links to list
            track_links = []
            track_names = []
            
            # print all available track links, idx used to select track
            tracks = soup.select('h2')[3:]
            for idx, track in enumerate(tracks):
                track_links.append(track.a.get('href'))
                track_names.append(track.text)
                print(f'{idx + 1}: {track.text}\n')

            # song selection loop
            while True:
                choice = input('\n>>> Your choice (press x to change selection to a new genre): ')
                
                # select a new genre
                if choice == 'x':
                    break
                else:
                    choice = int(choice) - 1
                print(f'Now playing: {track_names[choice]}\n')
                
                # use genre url
                track_url = 'https://soundcloud.com' + track_links[choice]
                # get track
                browser.get(track_url)
    
    # Get the new and hot tracks for a genre
    if choice == 5:
        # get html tags from top url, for top songs 
        request = requests.get(new)
        # parse html with lxml module
        soup = BeautifulSoup(request.text, 'lxml')
        # print(request.text)
        while True:
            print('>>> Genres Available: \n')

            # query to search for genre links
            genres = soup.select('a[href*=genre]')[2:]

            # add genre links to list
            genre_links = []

            # print all available genre links, idx used to select genre
            for idx, genre in enumerate(genres):
                print(f'{idx}: {genre.text}')
                genre_links.append(genre.get('href'))

            # ask the user for their choice from genre menu
            choice = input('\n>>> Your choice (press x to go back to the main menu): ')
            print()

            # exit genre menu
            if choice == 'x':
                break
            else:
                choice = int(choice)

            # use genre url
            genre_url = 'https://soundcloud.com' + genre_links[choice]
            # get html tags from genre url
            genre_request = requests.get(genre_url)
            # parse html with lxml module
            soup = BeautifulSoup(genre_request.text, 'lxml')
            print(genre_request.text)
            
            # add track links to list
            track_links = []
            track_names = []
            
            # print all available track links, idx used to select track
            tracks = soup.select('h2')[3:]
            for idx, track in enumerate(tracks):
                track_links.append(track.a.get('href'))
                track_names.append(track.text)
                print(f'{idx + 1}: {track.text}\n')

            # song selection loop
            while True:
                choice = input('\n>>> Your choice (press x to change selection to a new genre): ')
                
                # select a new genre
                if choice == 'x':
                    break
                else:
                    choice = int(choice) - 1
                print(f'Now playing: {track_names[choice]}\n')
                
                # use genre url
                track_url = 'https://soundcloud.com' + track_links[choice]
                # get track
                browser.get(track_url)

print('Goodbye!')
