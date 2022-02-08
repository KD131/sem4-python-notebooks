import argparse
import modules.webget as webget
import os.path as path
# we import from the teacher's modules folder, so the current folder is notebooks/

parser = argparse.ArgumentParser(description="Tool to download from URL")
parser.add_argument("url", help="The URL path to download")
parser.add_argument("--destination", "-d", help="The destination file to save the download in")
args = parser.parse_args()

if not args.destination:
    args.destination = path.basename(path.normpath(args.url))
print("Downloading " + args.url + " into " + args.destination)
webget.download(args.url, args.destination)
