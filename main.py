def backpack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    #tworzenie tablic
    for i in range(1, n + 1):
        for c in range(1, capacity + 1):
            if weights[i - 1] <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - weights[i - 1]] + values[i - 1])
            else:
                dp[i][c] = dp[i - 1][c]


    selected_items = []
    c = capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            selected_items.append(i - 1)
            c -= weights[i - 1]

    #wydruk
    return dp[n][capacity], selected_items

#słownik
items = {
    "śpiwór": (10, 10),
    "szczoteczka do zębów": (10, 1),
    "pasta do zębów": (5, 1),
    "koc": (8, 7),
    "bluza": (9, 5),
    "woda": (9, 2),
    "ręcznik": (5, 3),
    "tablet": (8, 2),
    "jedzenie": (10, 5),
    "buty": (7, 3),
    "latarka": (6, 3),
    "zegarek": (4, 2),
    "konsola": (6, 4),
    "piłka": (4, 3),
    "płyn": (8, 2)
}

#tablica z wartosciami
values = [item[0] for item in items.values()]
weights = [item[1] for item in items.values()]

#pojemnosc plecaka
capacity = 18


max_value, selected_item_indices = backpack(values, weights, capacity)
print("Maksymalna wartość:", max_value)
print("Wybrane przedmioty:")

for index in selected_item_indices:
    item_name = list(items.keys())[index]
    print(f"- {item_name}")

