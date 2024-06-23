import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f'\nYou have {lives} lives left')
        print('You have used these letters:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print(f'\nYour letter {user_letter} is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print(f'You died, the word was {word}')
    else:
        print(f'Congrats! You guessed the word {word}!!')


if __name__ == '__main__':
    hangman()