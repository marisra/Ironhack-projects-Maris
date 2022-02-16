

from bs4 import BeautifulSoup
import requests
import pandas as pd

# The URL I will be using

url = "https://www.billboard.com/charts/hot-100/"

# I will save it as a variable.

response = requests.get(url)

# Here I can see what is inside.

response.content

# How did the request go? It is ok, if 200-299.

response.status_code

# I will have it as a nicer html code.

soup = BeautifulSoup(response.content, "html.parser")

soup

# Titles of the songs

soup.select(".c-title.a-no-trucate")[0].get_text()

# Singers

soup.select(".c-label.a-no-trucate")[0].get_text()

# Creating empty lists

title = []
artists = []

num_iter = len(soup.select(".c-title.a-no-trucate"))
num_iter

# I will add all songs and artists to new lists.

for song in range(num_iter):
    title.append(soup.select(".c-title.a-no-trucate")[song].get_text())
    artists.append(soup.select(".c-label.a-no-trucate")[song].get_text())

# I will use those lists to make a dataframe.

hot_songs = pd.DataFrame({"song_title":title, "artist(s)":artists})

hot_songs

# I will clean the table a bit. I will delete all /n.

hot_songs["song_title"] = hot_songs["song_title"].str.replace("\n", "")

hot_songs["artist(s)"] = hot_songs["artist(s)"].str.replace("\n", "")

hot_songs

# Here is a function to do everything above.

def html_to_dataframe(url, path1, path2):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    print("Status code: " + str(response.status_code))
    
    title = []
    artists = []

    num_iter = len(soup.select(path1))

    for song in range(num_iter):
        title.append(soup.select(path1)[song].get_text())
        artists.append(soup.select(path2)[song].get_text())
    
    hot_songs = pd.DataFrame({"song_title":title, "artist(s)":artists})
    
    hot_songs["song_title"] = hot_songs["song_title"].str.replace("\n", "")
    hot_songs["artist(s)"] = hot_songs["artist(s)"].str.replace("\n", "")
    
    return hot_songs
    
    
    
#".c-title.a-no-trucate" = path1    
#".c-label.a-no-trucate" = path2   
   
# Calling the function

html_to_dataframe("https://www.billboard.com/charts/hot-100/", ".c-title.a-no-trucate", ".c-label.a-no-trucate")

# I will save the table as csv.

# hot_songs.to_csv(r'hot_songs.csv', index = False)



# Function that takes a song as an input and then recommends another song.

# Option2 - in else, print Check if the entered song name is correct or this song is not in the hot list.
# FOR TYPOS: pip install pyspellchecker

# Later I can use try/except/else to test the correctness of input.

def hot_song_recommender():

    song_input = input("Please enter a name of a song: ").title()

    if song_input in hot_songs.values:
        print()
        print("Here is one song recommendation: ")
        print()
        print(hot_songs.sample())
    else:
        print("Please, check if you have any typos in the song name. If not, unfortunately, the song is not in the hot list.")


hot_song_recommender()





