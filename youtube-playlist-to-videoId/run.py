from webbrowser import open as webopen
from inspect import getsourcefile
from os.path import dirname, abspath
from subprocess import run
from json import load
from os import remove


# Open Browser
webopen("https://developers.google.com/youtube/v3/docs/playlistItems/list#usage")


# Path names
base_path = dirname(abspath(getsourcefile(lambda:0)))
json_filename = r'\PlaylistItems.json'
json_path = base_path + json_filename


# Create a temporary file with instructions
instructions = (
"""
On Try this API, fill in these fields:
Part: id, status, snippet, contentDetails
maxResults: 50
playlistID: <YouTube PlaylistID>

<YouTube PlaylistID>
Youtube Playlist URL: https://www.youtube.com/playlist?list=PLxyaWvsfmq49REpw7XnAvhsLZI3ZbDScx
Youtube PlaylistID:                                         PLxyaWvsfmq49REpw7XnAvhsLZI3ZbDScx

Execute and overwrite this file with the raw JSON
""").lstrip().rstrip()

with open(json_path, 'w+') as f:
    f.write(instructions)


# Open the file in notepad for user to paste the raw JSON and remove after
run(f'notepad {json_path}')
with open(json_path, 'r', encoding='utf8') as f:
    playlist_items = load(f)
remove(json_path)

# get videoId from all the videos of the playlist
videoId = []
for item in playlist_items['items']:
    videoId.append(item['contentDetails']['videoId'])
    

print(videoId)


