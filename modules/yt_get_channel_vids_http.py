# You can decode/encode urls and parameter using the urllib.parse module.
# But I think it's easier to just concat here because I'm always sure there's at least one parameter so I don't have to worry about there being '?' or not.
# The workflow for managing paramters with urllib is super arse by the way. Something like:
#   url = 'url_here'
#   split = parse.urlsplit(url)                    # returns named tuple, so we can access query like split.query or split['query'] but we can't edit it.
#   lst = list(split)                              # so we can change the value. Admittedly, you chain this on the above line to save space.
#   dct = dict(parse.parse_qsl(split.query))       # or lst[3] which we can also just assign to a new string from the get-go, lst[3] = 'new_params'.
#   dct['key'] = 'value'                           # adds new pair.
#   lst[3] = parse.urlencode(dct)                  # parses dict to param str.
#   url = parse.unsplit(lst)                       # this is fucking stupid.
# There's a shorter way using urljoin, so at least there's that. But you still have to split --> dict --> add pair --> join

from urllib.error import HTTPError
import requests

from api_keys import GOOGLE

# bit indecisive on whether to just concat things or use formatting. I don't think concatting would work in every case.
base_url = 'https://www.googleapis.com/youtube/v3/'
credentials = '&key=' + GOOGLE
channel_url = base_url + 'channels?part=contentDetails' + credentials
playlist_url = base_url + 'playlistItems?part=contentDetails&maxResults=50&playlistId={}' + credentials
pagination = '&pageToken={}'

def get_uploads_id(*, id=None, username=None):
    # Could've also made the parameters like a dict and used requests' support for that.
    # Probably a lot cleaner, but I've already set up for doing string concats.
    url = channel_url
    if id:
        url += '&id=' + id
    if username:
        url += '&forUsername=' + username
    r = requests.get(url)
    r.raise_for_status()
    return r.json()['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def get_vids(playlist_id):
    # The loop logic caused me some trouble. The block of the loop should fetch a new response and handle that, then test if there are more pages.
    # Not the other way around. Not getting a new response at the end of the block and continuing the loop if that response has more pages.
    # That would always exclude the last page.
    # In a normal while loop, the correct way is this: check if more pages (cond of while) --> fetch --> handle current response.
    # However this insinuates a do-while loop. We would still want to do all this to the first request regardless of page count, and then start the loop.
    # Normal while would then involve a lot of code repetition, or a lot of abstraction which wouldn't be that bad, really.
    # So this is what the below loop is. A do-while emulation (while True, break if).
    # Shit like this is why the googleapiclient is easier to use.
    url = playlist_url.format(playlist_id)
    links = []
    pageToken = ''
    while True:
        r = requests.get(url + pagination.format(pageToken))
        r.raise_for_status()
        res = r.json()
        for item in res['items']:
            id = item['contentDetails']['videoId']
            links.append("https://youtube.com/watch?v=" + id + "\n")
        pageToken = res.get('nextPageToken')
        if not pageToken:
            break
    return links

if __name__ == '__main__':
    try:
        uploads_id = get_uploads_id(id='UCrdoeFcC039Q4MzO8n0OEvg')
        if uploads_id:
            links = get_vids(uploads_id)
            with open('links_by_channel2.txt', 'w') as f:
                f.writelines(links)
        else:
            print('There is no uploaded videos playlist for this user.')
    except HTTPError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
