FILE_MASSIME = 'Murphy_reads.txt'
FILE_ARGOMENTI = 'arguments.txt'


def read_murphy_file(nomefile):
    massime = []

    murphile = open(nomefile, 'r', encoding='utf-8')

    title = murphile.readline().rstrip()
    while title != '':
        enunciato = ''
        riga = murphile.readline().rstrip()
        while riga != '':
            enunciato += riga + ' '
            riga = murphile.readline().rstrip()

        massima = {'titolo': title, 'enunciato': enunciato}
        massime.append(massima)

        title = murphile.readline().rstrip()
    murphile.close()
    return massime


def read_arguments(filename):
    words = []
    infile = open(filename, 'r')
    for line in infile:
        if len(line) > 1:
            words.append(line.strip().lower())
    infile.close()
    return words


def search(massime, parole):
    relevant = []
    for massima in massime:
        lista_parole = massima['enunciato'].split()  # separa le parole in corrispondenza degli spazi
        for i in range(len(lista_parole)):
            lista_parole[i] = lista_parole[i].strip(',.;:\'\"()').lower()

        if set(parole).intersection(lista_parole) != set():
            relevant.append(massima)

    return relevant


def main():
    data = read_murphy_file(FILE_MASSIME)
    arguments = read_arguments(FILE_ARGOMENTI)

    relevant = search(data, arguments)

    for maxs in relevant:
        print(f"{maxs['titolo']} - ", end='')
        if len(maxs['enunciato']) >= 50:
            print(f"{maxs['enunciato'][:50]}...")
        else:
            print(f"{maxs['enunciato']}")

if __name__ == "__main__":
    main()
