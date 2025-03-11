from os import system
system('cls')

def sorted_alphabet(alphabet, q):
    alphabet_list = [word.strip() for word in alphabet.replace(',', ' ').split()]
    srt_list = sorted(alphabet_list, key=lambda soz: (soz[q - 1].lower(), soz.lower()))
    return ', '.join(srt_list)

print(sorted_alphabet("bid, zag", 2))
print(sorted_alphabet("apple, banana, mango", 3))
print(sorted_alphabet("car, bus, bike, airplane", 2))