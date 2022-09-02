from operator import itemgetter

SPORTIVI = 'sportivi.csv'
ZODIACO = 'zodiaco.csv'
RESULT = 'result.txt'

def read_sportivi():
    file= open(SPORTIVI, "r", encoding="UTF-8")
    sports = []

    for line in file:
        dati = line.rstrip().split(',')
        riga = []
        for i in range(len(dati)):
            riga.append(dati[i])
        sports.append(riga)

    file.close()
    return sports


def read_zodiaco():
    file = open(ZODIACO, "r", encoding="UTF-8")
    zodiaco = []

    for line in file:
        dati = line.rstrip().split(',')
        riga = []
        for i in range(len(dati)):
            riga.append(dati[i])
        zodiaco.append(riga)

    file.close()

    return zodiaco


def find_sign(birthd, signs):
    sign_found = " "

    for sign in signs:
        dd_begin = sign[1].split('/')[1] + sign[1].split('/')[0]
        dd_end = sign[2].split('/')[1] + sign[2].split('/')[0]

        if (birthd >= dd_begin) and (birthd <= dd_end):
            sign_found = sign[0]
            return sign_found

    return "Capricorn"


def calculate_points(zodiaco, sportivi):
    point = {}

    for j in range(len(zodiaco)):
        point[zodiaco[j][0]] = 0

    for i in range(len(sportivi)):
        nato = sportivi[i][3].split('/')[1] + sportivi[i][3].split('/')[0]
        segno = find_sign(nato, zodiaco)
        point[segno] = point[segno] + int(sportivi[i][1])

    return point


def main():
    sportivi = read_sportivi()
    zodiaco = read_zodiaco()
    punti = calculate_points(zodiaco, sportivi)
    sorted_points = sorted(punti.items(), key=itemgetter(1), reverse=True)
    result = open(RESULT,'w+')


    for i in range(len(sorted_points)):
        asterischi = (sorted_points[i][1] * 50)//sorted_points[0][1]
        row = str(sorted_points[i][0]) + " " + str(sorted_points[i][1])  + " " +"*"*asterischi

        result.write( f"{row}\n")
        print(f'{sorted_points[i][0]:10s} {sorted_points[i][1]:4d}', "*"*asterischi)


if __name__ == "__main__":
    main()
