from os import system
system('cls')

def part(list):
    natija = []
    for i in range(1, len(list)):
        chap = " ".join(list[:i])
        ong = " ".join(list[i:])
        natija.append((chap, ong))
    return natija

print(part(["az", "toto", "picaro", "zone", "kiwi"]))