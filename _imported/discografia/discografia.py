from operator import itemgetter

FILE_PRINCIPALE = 'artists.txt'


def read_artists(nome_file):
    artisti = []
    with open(nome_file, 'r', encoding='utf-8') as f:
        for line in f:
            campi = line.rstrip().split(';')
            artisti.append({
                'code': campi[0],
                'file': campi[1]
            })
    return artisti


def read_tracks(artista):
    brani = []
    with open(artista['file'], 'r', encoding='utf-8') as f:
        for line in f:
            campi = line.rstrip().split(';')
            brani.append({
                'code': artista['code'],
                'year': int(campi[0]),
                'brano': campi[1]
            })
    return brani


def stampa_per_anni(tracks):
    year = 0

    for track in tracks:
        if track['year'] != year:
            year = track['year']
            print(f'Year {year}:')
        print(f'{track["brano"]:30s}{track["code"]}')


def main():
    artists = read_artists(FILE_PRINCIPALE)
    tracks = []
    for art in artists:
        track_artist = read_tracks(art)
        tracks.extend(track_artist)

    tracks.sort(key=itemgetter('year'))

    stampa_per_anni(tracks)


if __name__ == "__main__":
    main()
