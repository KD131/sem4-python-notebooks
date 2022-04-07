import argparse

# There are different ways to edit the file inplace, like FileInput.
# Or you could just open through the file twice. Once for reading, once for writing.
# Here I just write to a different out file.
# Could also use regex to change the output file name instead of hard coding .txt,
# or using replace('.', '_fix.)
# I don't think there's support for timestamps. Those might be mangled.
# Might need regex to isolate the id string. Or a URL path lib.
# See yt_get_channel_vids_http.py for details on urllib.

# There's also a lib from Google to handle shorturls.
# See here https://github.com/googleapis/google-api-python-client/blob/main/samples/urlshortener/urlshortener.py
def fix_links(path):
    with open(path, 'r') as fi, open(path.replace('.txt', '_fix.txt'), 'w') as fo:
        for l in fi.readlines():
            fo.write(l.replace('youtu.be/', 'youtube.com/watch?v='))

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Fixes YouTube shortlinks and expands to full link.')
    parser.add_argument('path', help='The path to the input file.')
    args = parser.parse_args()
    # links.txt
    fix_links(args.path)
