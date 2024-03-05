import random;
import string;

from words import list_words;
from hangman_diagrams import visual_lives;


def get_valid_word(list_words):
    word = random.choice(list_words);

    while '-' in word or ' ' in word:
        word = random.choice(list_words);

    return word.upper();


def hangman():

    print("==============================");
    print("Welcome to the Hangman Game!");
    print("==============================");

    word = get_valid_word(list_words);

    letters_to_guess = set(word);
    guessed_letters = set();
    alphabet = set(string.ascii_uppercase);

    lives = 7;

    while len(letters_to_guess) > 0 and lives > 0:
        print(f" {lives} left and you have used these letters: {' '.join(guessed_letters)} ");

        # ACTUAL STATE OF THE WORD
        list_word = [letter if letter in guessed_letters else '-' for letter in word];
        
        # ACTUAL STATE HANGMAN
        print(visual_lives[lives]);

        # SEPARATED LETTERS WITH SPACE
        print(f"Words: {' '.join(list_word)} ");

        user_letter = input("Choose a letter: ").upper();

        # If the user's letter is in the alphabet and not in the letter's set already entered, it adds the letter to the set of entered letters
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter);

            # If the letter is in the word, remove the letter from the set of letter to be guessed.
            # If it is not in the word, remove a live.
            if user_letter in letters_to_guess:
                letters_to_guess.remove(user_letter);
                print('');
            else:
                lives = lives - 1;
                print(f"\n Your letter, {user_letter} is not in the word");
        
        #If the chosen letter by the user is already entered 
        elif user_letter in guessed_letters:
            print("\n You already picked up that letter. Please choose a new one");

        else:
            print("\n This letter is not valid");

    # The game comes at this line when all the letters are guessed or when the user run out of lives
    if lives == 0:
        print(visual_lives[lives]);
        print(f"Hangman! Game Over. The correct word is: {word} ");
    else:
        print(f"Congratulations! You guessed the word: {word} ");


hangman();

