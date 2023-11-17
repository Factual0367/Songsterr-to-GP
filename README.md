# Songsterr to Guitar Pro 

This script allows you to download tabs from Songsterr as Guitar Pro tabs.

## Installation

You need to have Python installed to run this script. To install the package, open a terminal (or PowerShell on Windows) and run the following command:

```bash
pip install https://github.com/onurhanak/Songsterr-to-GP/releases/download/v0.1/songsterr_to_gp-0.1-py3-none-any.whl
```

After the installation, you may need to open a new terminal session or refresh your current session.

## Usage

The script can be used to download songs from specific artists or to search for a particular song by an artist. Below are the usage instructions:

```bash
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

To download top tabs from a specific artist:
```bash
songsterr-to-gp --search-artist "Artist Name"
```
To search for a specific song by an artist:
```bash
songsterr-to-gp --search-song "Artist Name" "Song Title"
```
To specify a download path for the songs (default path is HOME_DIR/Tabs/):
```bash
songsterr-to-gp --download-path /path/to/directory
```





