import argparse
import modules.webget as webget

parser = argparse.ArgumentParser(description="Tool to download from URL")
parser.add_argument("url", help="The URL path to download")
parser.add_argument("--destination", "-d", default="default_file.dat", help="The destination file to save the download in")
args = parser.parse_args()
print("Downloading " + args.url + " into " + args.destination)
webget.download(args.url, args.destination)
