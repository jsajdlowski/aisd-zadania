from hashTable import HashTable

if __name__ == "__main__":
    # 278805 % 6 = 1
    # [W + OL]
    # rozmiary
    lengths = [1021]  # , 1024, 2039, 4093, 4096, 16381]

    file = open("./hash-table/nazwiskaASCII.txt").read().splitlines()

    surnames = []
    for entry in file:
        temp = entry.split(" ")
        surnames += [[int(temp[0]), temp[1]]]

    results = []
    for length in lengths:
        # 35%
        mTable35 = HashTable(length)

        m35 = 0
        for pair in surnames[:int(length * 0.35)]:
            m35 += mTable35.setItem(pair[1], pair)
        m35 /= int(length * 0.35)

        # 65%
        mTable65 = HashTable(length)

        m65 = 0
        for pair in surnames[:int(length * 0.65)]:
            m65 += mTable65.setItem(pair[1], pair)
        m65 /= int(length * 0.65)

        # 95%
        mTable95 = HashTable(length)

        m95 = 0
        for pair in surnames[:int(length * 0.95)]:
            m95 += mTable95.setItem(pair[1], pair)
        m95 /= int(length * 0.95)

        results.append([length, [m35, m65, m95]])

    for result in results:
        print(
            f"średnia liczba prób wstawienia elementow wynosi: {result[1][0]} dla m: {result[0]}")
        print(
            f"średnia liczba prób wstawienia elementow wynosi: {result[1][1]} dla m: {result[0]}")
        print(
            f"średnia liczba prób wstawienia elementow wynosi: {result[1][2]} dla m: {result[0]}")

# średnia liczba prób wstawienia elementow wynosi: 161.31652661064425 dla m: 1021
# średnia liczba prób wstawienia elementow wynosi: 314.4886877828054 dla m: 1021
# średnia liczba prób wstawienia elementow wynosi: 467.359133126935 dla m: 1021

# średnia liczba prób wstawienia elementow wynosi: 161.81564245810057 dla m: 1024
# średnia liczba prób wstawienia elementow wynosi: 315.4872180451128 dla m: 1024
# średnia liczba prób wstawienia elementow wynosi: 468.84156378600824 dla m: 1024

# średnia liczba prób wstawienia elementow wynosi: 339.4936886395512 dla m: 2039
# średnia liczba prób wstawienia elementow wynosi: 645.2332075471699 dla m: 2039
# średnia liczba prób wstawienia elementow wynosi: 951.0010325245224 dla m: 2039

# średnia liczba prób wstawienia elementow wynosi: 698.69343575419 dla m: 4093
# średnia liczba prób wstawienia elementow wynosi: 1312.2827067669173 dla m: 4093
# średnia liczba prób wstawienia elementow wynosi: 1926.1455761316872 dla m: 4093

# średnia liczba prób wstawienia elementow wynosi: 699.2016748080949 dla m: 4096
# średnia liczba prób wstawienia elementow wynosi: 1313.2828700225396 dla m: 4096
# średnia liczba prób wstawienia elementow wynosi: 1927.6363402724235 dla m: 4096

# średnia liczba prób wstawienia elementow wynosi: 2848.4533403104833 dla m: 16381
# średnia liczba prób wstawienia elementow wynosi: 5305.304968535737 dla m: 16381
# średnia liczba prób wstawienia elementow wynosi: 7762.131675342202 dla m: 16381
