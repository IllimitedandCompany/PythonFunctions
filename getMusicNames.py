import requests

# Replace 'YOUR_API_KEY' with your actual Last.fm API key
API_KEY = 'YOUR_API_KEY'

def search_artist(artist_name):
    base_url = 'http://ws.audioscrobbler.com/2.0/'

    # Define the parameters for the API request
    params = {
        'method': 'artist.search',
        'artist': artist_name,
        'api_key': API_KEY,
        'format': 'json'
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Extract artist information from the response
        artists = data.get('results', {}).get('artistmatches', {}).get('artist', [])
        if artists:
            # Take the first artist (you can loop through the list if needed)
            first_artist = artists[0]
            artist_name = first_artist.get('name', '')
            mbid = first_artist.get('mbid', '')

            # Now you can fetch the top tracks for this artist
            top_tracks = get_top_tracks(mbid)
            return artist_name, top_tracks
        else:
            return None
    else:
        print('Error:', response.status_code)
        return None

def get_top_tracks(artist_mbid):
    params = {
        'method': 'artist.gettoptracks',
        'mbid': artist_mbid,
        'api_key': API_KEY,
        'format': 'json'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        top_tracks = data.get('toptracks', {}).get('track', [])
        return [track.get('name', '') for track in top_tracks]
    else:
        print('Error:', response.status_code)
        return []

if __name__ == "__main__":
    artist_name = input("Enter the name of the artist: ")
    result = search_artist(artist_name)
    
    if result:
        artist, top_tracks = result
        print(f"Artist: {artist}")
        print("Top Tracks:")
        for track in top_tracks:
            print(f"- {track}")
    else:
        print("Artist not found.")
