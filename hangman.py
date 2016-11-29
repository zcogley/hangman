#HANGMAN
import random

word_list = [
  'HORSE',
  'KITTEN',
  'LEMON',
  'SAILBOAT',
  'ZEBRA',
  'DOGGIE',
  'POETRY',
  'DINNER',
  'READING',
  'HOTEL',
  'COLLEGE',
  'LIZARD',
  'ANAGRAM',
  'BROTHER',
  'SISTER',
  'BALLOON',
  'HOTDOG',
  'SALSA',
  'TURKEY',
  'KITCHEN',
  'LAUNDRY',
  'HARDWOOD',
  'BALL',
  'SOCCER',
  'LABRADOR'
]

our_word = random.choice(word_list)
guesses_left = 6
new_word = '_ ' * len(our_word)

print('Welcome to Hangman!')
print('You have {} guesses left'.format(guesses_left))
print('                  ')
print(new_word)
print('                  ')

while '_' in new_word:
    guess = input('> ').upper()
    if not guess.isalpha() or len(guess) > 1:
        print("That's not a good guess.")
        continue
    if guess in our_word:
        for ix in range(len(our_word)):
            if guess == our_word[ix]:
                new_word = new_word[:ix*2] + guess + new_word[ix*2+1:]
                print('You guessed a correct letter!')
                print('You have {} guesses left.'.format(guesses_left))
                print('                  ')
                print(new_word)
                print('                  ')
    else:
        print("Sorry, your guess wasn't correct.")
        guesses_left = guesses_left - 1
        print('You have {} guesses left.'.format(guesses_left))
        print('                  ')
        print(new_word)
        print('                  ')
        if guesses_left == 0:
            print('The Hangman got you this time!')
            print('The word was {}.'.format(our_word))
            break

else:
    print('You got the whole word! Congratulations, you won!')
