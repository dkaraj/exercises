import operator


def read_data(file):
    SOGLIA = 200

    patient = {}
    for line in file:
        parti = line.strip().split()
        code = parti[0]
        ora = parti[1]
        value = int(parti[2])

        if value >= SOGLIA:
            if code not in patient:
                patient[code] = {'cod': code, 'n_sup': 1, 'sup': [ora + ' ' + str(value)]}
            else:
                patient[code]['n_sup'] += 1
                patient[code]['sup'].append(ora + ' ' + str(value))

    return patient


def main():
    file = open('glucometers.txt', 'r')
    patients = read_data(file)
    file.close()

    lista = sorted(patients.values(), key=operator.itemgetter('n_sup'), reverse=True)
    for patient in lista:
        for value in patient['sup']:
            print(patient['cod'], value)
        print()


if __name__ == "__main__":
    main()
