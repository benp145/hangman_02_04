import random

words = ['obsequious', 'jazz', 'reconnoiter', 'counterfeiting', 'malarial', 'anemones', 'mercurial', 'vassal', 'anasazi', 'ojibwe', 'iriquois']



class Game:
    def __init__(self):
        self.letters = []
        self.wrong_letters = []
        

    def user_display(self):
        print("\n","="*50,"\n")
        for i in self.letters:
            print(i, end=' ')
        print("\n"*2,"="*50,"\n")
    
    def display_wrong_letters(self):
        if self.strikes < 7:
            print("incorrect guesses:")
            for letter in self.wrong_letters:
                print(letter, end=" ")
            print("\n")

    def correct(self, guess):
        indices = []
        for i in range(len(self.answer)):
            if self.answer[i] == guess:
                indices.append(i)
        for j in indices:
            self.letters[j] = guess
        print("Great guess!!")


    def incorrect(self, guess):
        self.strikes -= 1
        self.wrong_letters.append(guess)
        if self.strikes > 1:
            print(f"Uh oh! You guessed incorrectly! Only {self.strikes} guesses remaining")
        elif self.strikes == 1:
            print(f"Uh oh! You guessed incorrectly! Careful now! Only 1 guesses remaining")
        elif self.strikes == 0:
            print("So sorry, you have guessed your last incorrect guess. You are now dead. RIP")
            print(f"Your word was {self.answer}\n")

    def win(self):
        self.user_display()
        print(f"Congradulations, You correctly guessed the word!\n")
        
    def play(self):
        self.letters = []
        self.wrong_letters = []
        self.answer = random.choice(words)
        self.strikes = 7
        for i in range(len(self.answer)):
            self.letters.append("_")
        print("\nWelcome to hangman! Guess the letters that are in the word. Don't guess incorrectly 7 times, or you will be hanged!!")
        while self.strikes > 0:
            self.user_display()
            self.display_wrong_letters()
            guess = input("Guess a letter: ").lower()
            if len(guess) > 1:
                print("enter one letter at a time please!")
            elif len(guess) ==0:
                print("please type a letter before hitting enter!")
            elif guess in self.letters or guess in self.wrong_letters:
                print(f"You've already guessed {guess}!\n")
            elif guess in self.answer:
                self.correct(guess)
            else:
                self.incorrect(guess)

            if "_" not in self.letters:
                self.win()
                break

        print("Thanks for playing!!")
        again = input("Would you like to play again? (y/n): ").lower()
        if again == 'y':
            self.strikes = 7
            self.play()
        else: 
            print("\nSee you next time!")


my_game = Game()
my_game.play()


