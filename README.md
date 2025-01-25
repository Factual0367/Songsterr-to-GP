# Songsterr to Guitar Pro 

This script allows you to download tabs from Songsterr as Guitar Pro tabs. If you are looking for an app to do the same check out [TabStop](https://github.com/onurhanak/TabStop).

## Installation

You need to have Python installed to run this script. To install the package, open a terminal (or PowerShell on Windows) and run the following command:

```
pip install https://github.com/Factual0367/Songsterr-to-GP/releases/download/v0.2/songsterr_to_gp-0.2-py3-none-any.whl
```

After the installation, you may need to open a new terminal session or refresh your current session.

## Usage

The script can be used to download songs from specific artists or to search for a particular song by an artist. Below are the usage instructions:

```
usage: songsterr-to-gp [-h] [--download-path DOWNLOAD_PATH] [--search-artist SEARCH_ARTIST]
                       [--search-song ARTIST SONG]
                       [artists ...]

Download songs from artists.

positional arguments:
  artists               List of artists to download songs for

options:
  -h, --help            show this help message and exit
  --download-path DOWNLOAD_PATH
                        Directory to save downloaded songs
  --search-artist SEARCH_ARTIST
                        Search for an artist
  --search-song ARTIST SONG
                        Search for a song by an artist
```
## Examples

To download top tabs from a specific artist(s):
```
songsterr-to-gp "Artist Name" "Artist Name 2" "Artist Name 3"
```
To search for a specific song by an artist:
```
songsterr-to-gp --search-song "Artist Name" "Song Title"
```
To specify a download path for the songs (default path is HOME_DIR/Tabs/):
```
songsterr-to-gp --download-path /path/to/directory
```

## Disclaimer

Please note that I do not own any of the tabs provided by this script. All tabs are the property of Songsterr and their respective authors. This tool is designed to facilitate downloading tabs for personal use and should be used in compliance with Songsterr's terms of service and copyright laws.

**Important:**
- The use of this script and the downloaded tabs is entirely at your own discretion and risk.
- This script is provided for educational use only.
- I am not responsible for any misuse of the tabs or any copyright infringement caused by the users of this script.
- Users are encouraged to support the artists and the creators of the tabs by considering official sources or purchasing their music and tablatures.

By using this script, you acknowledge and agree to these terms.





