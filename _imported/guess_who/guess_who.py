FILE_PERSONAGGI = 'characters.txt'
FILE_DOMANDE = 'question1.txt'


def read_characters(filename):
    f = open(filename, 'r', encoding='utf-8')

    proprieta = f.readline().rstrip().split(';')

    characters = []

    for line in f:
        valori = line.rstrip().split(';')
        character= {}
        for i in range(len(proprieta)):
            character[proprieta[i]] = valori[i]
        characters.append(character)
    return characters


def play_game(nome_file_partita, characters):
    characters_in_game = list(characters)

    f = open(nome_file_partita, 'r', encoding='utf-8')
    step = 0
    for line in f:
        property, value = line.rstrip().split('=')
        step += 1
        print(f'Step {step} - question: {property} = {value} ?')

        characters_in_game = [p for p in characters_in_game if p[property] == value]
        print('Selected characters:')
        for character in characters_in_game:
            for property in character:
                print(f'{property}:{character[property]}', end='  ')
            print()


    if len(characters_in_game) == 1:
        print("Congratulations, you win!")
    else:
        print("You lost...")


def main():
    characters = read_characters(FILE_PERSONAGGI)
    print(characters)

    play_game(FILE_DOMANDE, characters)


if __name__ == "__main__":
    main()
