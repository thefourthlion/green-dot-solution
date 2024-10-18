import random

def hangman():
    word_list = ["python", "java", "ruby", "javascript", "csharp", "cplusplus", "golang"]
    random_number = random.randint(0, len(word_list)-1)
    chosen_word = word_list[random_number]
    guessed_letters = []
    attempts = 10

    print("Let's play Hangman!")
    
    while attempts > 0:
        output_word = ""
        for letter in chosen_word:
            if letter.lower() in guessed_letters:
                output_word += letter
            else:
                output_word += "_"
        if output_word == chosen_word:
            print("Congratulations! You won. The word was: " + chosen_word)
            break
        print("Guess the word: ", output_word)
        print("Attempts left: ", attempts)
        guess = input("Please, guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed this letter: ", guess)
            elif guess not in chosen_word:
                print("Sorry, letter ", guess, " is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! ", guess, " is in the word.")
                guessed_letters.append(guess)
        else:
            print("Please enter a valid character.")
    else:
        print("Out of attempts. You lost. The word was: ", chosen_word)

hangman()