from operator import itemgetter


def calc_points(p):
    return sum(p) - max(p) - min(p)


def main():
    try:
        filep = open("scores.txt", "r")
    except OSError:
        print("file not found")
        return 0

    scores = {}
    female_winner = {'surname': '', 'name': '', 'point': 0}

    for line in filep:
        dati = line.split()

        country = dati[3]
        if country not in scores:
            scores[country] = 0

        p = [float(d) for d in dati[4:]]

        sco = calc_points(p)

        scores[country] += sco

        if dati[2] == 'F' and sco > female_winner['point']:
            female_winner['surname'] = dati[0]
            female_winner['name'] = dati[1]
            female_winner['point'] = sco

    print('Female Winner:', female_winner['surname'], female_winner['name'],
          female_winner['point'])

    nazioni_ordinate = sorted(scores.items(), key=itemgetter(1), reverse=True)
    print("Overall nations ranking ")
    i = 1
    for (country, point) in nazioni_ordinate[:3]:
        print(i, country, "Total Score: %.2f" % point)
        i += 1

if __name__ == "__main__":
    main()
