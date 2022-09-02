
def venditori_ufficiali(filename):

    file = open(filename, 'r')

    venditori = {}
    for line in file:
        parti = line.strip().split()
        prodotto = parti[0]
        venditore = parti[1]

        venditori[prodotto] = {'ufficiale': venditore, 'rivenditori': set()}

    file.close()
    return venditori


def leggi_acquisti(venditori, filename):

    file = open(filename, 'r')

    for line in file:
        parti = line.strip().split()
        prodotto = parti[0]
        venditore = parti[1]
        venditori[prodotto]['rivenditori'].add(venditore)

    file.close()


def main():
    venditori = venditori_ufficiali('products.txt')
    leggi_acquisti(venditori, 'purchases.txt')

    print('Suspicious transactions list')
    for prodotto in venditori:
        ufficiale = venditori[prodotto]['ufficiale']
        rivenditori = venditori[prodotto]['rivenditori']
        if len(rivenditori) > 0 and rivenditori != {ufficiale}:
            print('Product code:', prodotto)
            print('Official dealer:', ufficiale)
            print('Dealer list:', end=' ')
            for rivenditore in rivenditori:
                print(rivenditore, end=' ')
            print('\n')


if __name__ == "__main__":
    main()
