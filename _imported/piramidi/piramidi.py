mappa = []
file = open('map.txt', 'r')
for line in file:
    fields = line.rstrip().split()

    for i in range(len(fields)):
        fields[i] = int(fields[i])
    mappa.append(fields)
file.close()

tops = []
n_righe = len(mappa)
n_colonne = len(mappa[0])

for r in range(len(mappa)):
    for c in range(len(mappa[r])):
        found = True

        if r > 0 and mappa[r][c] < mappa[r - 1][c]:
            found = False

        if r < n_righe - 1 and mappa[r][c] < mappa[r + 1][c]:
            found = False

        if c > 0 and mappa[r][c] < mappa[r][c - 1]:
            found = False

        if c < n_colonne - 1 and mappa[r][c] < mappa[r][c + 1]:
            found = False

        if r > 0 and c > 0 and mappa[r][c] < mappa[r - 1][c - 1]:
            found = False
        if r > 0 and c < n_colonne - 1 and mappa[r][c] < mappa[r - 1][c + 1]:
            found = False
        if r < n_righe - 1 and c > 0 and mappa[r][c] < mappa[r + 1][c - 1]:
            found = False
        if r < n_righe - 1 and c < n_colonne - 1 and mappa[r][c] < mappa[r + 1][c + 1]:
            found = False

        if mappa[r][c] > 0 and found:
            tops.append((mappa[r][c], r, c))

sum = 0
for top in tops:
    print(top[0], top[1], top[2])
    sum = sum + top[0]

print(f'Average height: {sum / len(tops)} m')
