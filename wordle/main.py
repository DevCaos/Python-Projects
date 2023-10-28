import random


def linha(tam=58):
    return '\033[1:97m-\033[m' * tam


def cabeçalho(txt):
    print(linha())
    print(f'\033[1:97m{txt.center(42)}\033[m')
    print(linha())


def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words


def is_valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses


def evaluate_guess(guess, word):
    str = ''

    for i in range(5):
        if guess[i] == word[i]:
            str += '\033[32m' + guess[i]
        else:
            if guess[i] in word:
                str += '\033[33m' + guess[i]
            else:
                str += '\033[0m' + guess[i]

    return str + '\033[0m'


def wordle(guesses, answers):

    cabeçalho('Welcome to Wordle! Get 6 chances to guess a 5-letter word.')
    secret_word = random.choice(answers)

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input('\033[34mEnter guess #' + str(attempts) + ': ').strip().lower()
        if not is_valid_guess(guess, guesses):
            print('\033[1:31mInvalid guess. Please enter an English word with 5 letters.')
            continue
        if guess == secret_word:
            print(f'Congrats! You guessed the word: {secret_word}.')
            break

        attempts += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)

        if attempts > max_attempts:
            print(f'\033[1:97mGame over. The secret word was: \033[1:32m{secret_word}\033[m.')


guesses = load_dictionary('guesses.txt')
answers = load_dictionary('answers.txt')

wordle(guesses, answers)
