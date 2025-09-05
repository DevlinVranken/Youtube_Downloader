import sys
import argparse
import subprocess
from pathlib import Path

def download(links, path):
    for l in links:
        try:
            command_string = "yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 192K -P " + path + " " + l
            command = command_string.split(" ")
            #print(command)
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Some Error: {e}")

def main():
    links = []
    from_file = False

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Download YouTube videos with custom options.")

    # Add arguments for file/link and save location
    parser.add_argument('-f', '--file', type=str, required=False, help='File location. When not specified you will need to enter the urls in the terminal. Enter one url per line.')
    parser.add_argument('-t', '--target', type=str, default=str(Path.home() / "Downloads" / "Youtube_Downloader"), help='Directory to save the video')
    parser.add_argument('-e', '--extention', type=str, default='mp3', help='File extention. This can be mp3 or mp4.')
    parser.add_argument('-a', '--available_formats', action='store_true', help="Displays which formats of the video are available for download.")

    # Parse the arguments
    args = parser.parse_args()

    if args.available_formats:
        url = input("Video url: ")
        ##display_formats(url)
        return # End the program here

    if not args.file:
        print("You can now enter URL's. Enter a video and press enter to add the next one. write end when you have all the video's you want")

        video = input("Video " + str((len(links) + 1)) + ": ")
        while video != "end":
            links.append(video)
            video = input("Video " + str((len(links) + 1)) + ": ")
    else:
        file = open(args.file, 'r')
        video = file.readline()
        while (video != ''):
            links.append(video)
            video = file.readline()
        file.close()

    if args.extention == 'mp3':
        download(links, args.target)
    elif args.extention == 'mp4':
        print("mp4 not supported yet")

if __name__ == "__main__":
    main()