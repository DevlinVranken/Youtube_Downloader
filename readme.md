# Youtube Downloader
## Developers
* Devlin Vranken

## Purpose of the project
Personally, I like to download youtube music and put in on an USB stick to use in my car. I used to do this on those youtube converver websites you can find. However, I got tired of finding the one I trusted the most and just decided to make a project that would not only make me trust the downloading more, but also make the experience overall a lot better. Instead of having to put in an url, convert it, download it, and all that, this project gives you the ability to just put all url's in a txt file and download them all without any effort. However, the titles will have a weird tag at the ending and ofcourse metadata is not filled in.

## Requirements to run
* In order for this to run, you will need to install yt-dlp: https://github.com/yt-dlp/yt-dlp/wiki/Installation
* Have python installed on your pc

## Usage
### Method 1
1. In terminal, type "python .\Music_Downloader.py -t result_folder" **(no -f passed)**
2. The terminal will keep requesting video urls, input them one by one (url - enter, url - enter, url - enter, ...)
3. To stop inputting urls, input "end" and hit enter
4. The program will now go trough the list and download the contents

### Method 2
1. Create a txt file
2. Put all the urls inside the txt file, one url per line
3. In terminal, type "python .\Music_Downloader.py -t result_folder -f .\your_music_file.txt" **(-f passed)**
4. The program will now go trough the list and download the contents

## Arguments
* -f, --file: This is the txt file containing all the url's. If none is passed, you need to manually insert the urls and input "end" in order to stop entering url's and process your input
* -t, --target: This is the folder where you want to have all your downloads be put into. The standard is a folder named Youtube_Downloader which will appear in your downloads folder
* -e, --extention: The file's extention, for now only supporting mp3
* -a --available_formats: This is just used to display all the available formats in which a video can be downloaded. This does not work yet.

## User libraries
* argparse: Used for parsing the possible arguments which can be added to the command
* subprocess: Used to perform the command in a newly created shell
* pathlib from Path: Used for getting your own downloads folder