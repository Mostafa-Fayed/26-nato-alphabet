import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Enter a Word: ")
    try:
        letters_list = [alphabet_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Sorry only letters can be used")
        generate_phonetic()
    else:
        print(letters_list)


generate_phonetic()

