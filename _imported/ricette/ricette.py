def main():
    (ingredient, method) = read_file_of_ricette("fusilli_alle_olive.txt")

    print("Ingredients: ")
    print(stampa_ingredienti(ingredient))

    print(f"Number of ingredients: {len(ingredient)}")

    foods = read_foods("foods.txt")

    (cost, calories) = calc_cost_calorie(ingredient, foods)

    print(f"Recipe cost: {cost:.2f}")
    print(f"Recipe calories: {calories:.2f}")


def read_file_of_ricette(filename):
    file_ricette = open(filename, "r")
    line = file_ricette.readline()

    ingredienti = []
    method = ""

    while "Method:" not in line:
        if "Ingredients" not in line and len(line) > 1:
            campi = line.rstrip().split(";")
            ingrediente = {"name": campi[0], "quantity": float(campi[1])}

            ingredienti.append(ingrediente)

        line = file_ricette.readline()

    while line != "":
        if "Method:" not in line:
            method += line.rstrip() + " "
        line = file_ricette.readline()

    file_ricette.close()

    return ingredienti, method


def stampa_ingredienti(ingredienti):
    risultato = ""
    for ingrediente in ingredienti:
        risultato += f'{ingrediente["name"]} - {ingrediente["quantity"]}\n'

    return risultato


def read_foods(nome_file):
    infile_cibi = open(nome_file, "r")

    cibi = []
    for line in infile_cibi:
        campi = line.rstrip().split(";")
        cibo = {"name": campi[0], "cost": float(campi[1]), "calorie": float(campi[2])}

        cibi.append(cibo)

    infile_cibi.close()

    return cibi


def calc_cost_calorie(ingredients, foods):
    cost = 0.0
    calories = 0.0

    for ingredient in ingredients:
        for food in foods:
            if ingredient["name"] == food["name"]:
                cost += ingredient["quantity"] / 1000 * food["cost"]
                calories += ingredient["quantity"] / 1000 * food["calorie"]

    return cost, calories



if __name__ == "__main__":
    main()
