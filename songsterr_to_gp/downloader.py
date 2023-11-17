import os
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from tqdm import tqdm
import sys
import argparse
from pathlib import Path

def get_default_download_path():
    return Path.home() / 'Tabs'

class SongDownloader:
    def __init__(self, download_path):
        self.download_path = Path(download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Connection': 'keep-alive',
        }

    def get_song_list(self, artists, song_name=None):
        songs = {}
        for artist in artists:
            params = {'pattern': artist}
            if song_name:
                params['pattern'] += f" {song_name}"  
            response = requests.get('https://www.songsterr.com/', params=params, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            songs_div = soup.find('div', {'data-list': 'songs'})
            hrefs = [a.get('href') for a in songs_div.find_all('a')] if songs_div else []
            songs[artist] = [{'name': href.split('/')[-1].split('-tab-')[0], 'id': href.split('-s')[-1]} for href in hrefs]

        return songs

    def download_gpx(self, songs_list):
        for artist, songs in songs_list.items():
            artist_path = self.download_path / artist
            artist_path.mkdir(exist_ok=True)
            for song in tqdm(songs, desc=f"Downloading songs for {artist}"):
                try:
                    song_name, song_id = song['name'], song['id']
                    response = requests.get(f'https://www.songsterr.com/a/ra/player/song/{song_id}.xml')
                    root = ET.fromstring(response.text)
                    attachment_url_element = root.find('.//attachmentUrl')
                    if attachment_url_element is not None:
                        attachment_url = attachment_url_element.text
                        self.download_file(attachment_url, artist_path, song_name)
                    else:
                        print(f'No attachment URL for {song_name}')
                except Exception as e:
                    print(f"Error downloading {song_name}: {e}")

    def download_file(self, url, artist, song_name):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                extension = url.split('.')[-1]
                filename = f"{artist}/{song_name}.{extension}"
                with open(filename, 'wb') as file, tqdm(
                    unit='B', unit_scale=True, unit_divisor=1024, total=int(response.headers.get('content-length', 0)), 
                    desc=f"Saving {song_name}", leave=False
                ) as bar:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                            bar.update(len(chunk))
            else:
                print(f'Failed to download {song_name}')
        except Exception as e:
            print(f"Error in downloading file {song_name}: {e}")

    def download_specific_song(self, artist, song_query):
        songs_list = self.get_song_list([artist])
        specific_song = [song for song in songs_list[artist] if song_query.lower() in song['name'].lower()]
        if specific_song:
            self.download_gpx({artist: specific_song})
        else:
            print(f"No song found for {song_query} by {artist}")

def main():
    parser = argparse.ArgumentParser(description='Download songs from artists.')
    parser.add_argument('artists', nargs='*', help='List of artists to download songs for')
    parser.add_argument('--download-path', type=str, default=get_default_download_path(), help='Directory to save downloaded songs')
    parser.add_argument('--search-artist', help='Search for an artist')
    parser.add_argument('--search-song', nargs=2, metavar=('ARTIST', 'SONG'), help='Search for a song by an artist')
    args = parser.parse_args()

    downloader = SongDownloader(download_path=args.download_path)

    if args.search_artist:
        downloader.search_artists(args.search_artist)
    elif args.search_song:
        artist, song_query = args.search_song
        songs_list = downloader.get_song_list([artist], song_query)
        downloader.download_gpx(songs_list)
    else:
        if args.artists:
            songs_list = downloader.get_song_list(args.artists)
            downloader.download_gpx(songs_list)
        else:
            parser.print_help()
            sys.exit(1)

if __name__ == "__main__":
    main()
