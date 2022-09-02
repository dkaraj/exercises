from operator import itemgetter

FILENAME = 'bowling.txt'


def read_bowling(file_name):
    data = []
    bowling_file = open(file_name, 'r')
    for line in bowling_file:
        campi = line.rstrip().split(';')
        surname = campi[0]
        name = campi[1]
        point = campi[2:]
        for i in range(0, len(point)):
            point[i] = int(point[i])
        data.append({'surname': surname, 'name': name, 'point': point})
    return data


def calculate_totals(classifica):
    for atlet in classifica:
        atlet['totale'] = sum(atlet['point'])

        num_0 = 0
        num_10 = 0
        for pt in atlet['point']:
            if pt == 0:
                num_0 = num_0 + 1
            if pt == 10:
                num_10 = num_10 + 1
        atlet['num_0'] = num_0
        atlet['num_10'] = num_10


def main():
    data = read_bowling(FILENAME)
    calculate_totals(data)
    data.sort(key=itemgetter('totale'), reverse=True)

    for atlet in data:
        print(f"{atlet['surname']:20} {atlet['name']:20} {atlet['totale']}")

    max_zero = max([a['num_0'] for a in data])
    max_ten = max([a['num_10'] for a in data])

    if max_ten != 0:
        for atlet in data:
            if atlet['num_10'] == max_ten:
                print(
                    f"{atlet['surname']:20} {atlet['name']:20} has knocked down all the pins {max_ten} time"
                )

    if max_zero != 0:
        for atlet in data:
            if atlet['num_0'] == max_zero:
                print(
                    f"{atlet['surname']:20} {atlet['name']:20} has missed all the pins {max_zero} time"
                )


if __name__ == "__main__":
    main()
