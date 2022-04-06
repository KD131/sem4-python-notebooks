from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from api_keys import GOOGLE

# uses Google's python client API.
# stuff taken from here: https://github.com/youtube/api-samples/blob/master/python/my_uploads.py
def get_uploads_id(*, id=None, username=None):
    res = yt.channels().list(part='contentDetails', id=id, forUsername=username).execute()
    # assumes a search result and top one is the one we wanted
    return res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def get_vids(playlist_id):
    req = yt.playlistItems().list(part='contentDetails', playlistId=playlist_id, maxResults=50)
    links = []
    while req:
        res = req.execute()
        for item in res['items']:
            id = item['contentDetails']['videoId']
            links.append("https://youtube.com/watch?v=" + id + "\n")
        req = yt.playlistItems().list_next(req, res)
    return links

if __name__ == '__main__':
    yt = build('youtube', 'v3', developerKey=GOOGLE)
    try:
        uploads_id = get_uploads_id(id='UCrdoeFcC039Q4MzO8n0OEvg')
        if uploads_id:
            links = get_vids(uploads_id)
            with open('links_by_channel.txt', 'w') as f:
                f.writelines(links)
        else:
            print('There is no uploaded videos playlist for this user.')
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
