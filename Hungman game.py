import random

def hangman():
    print("🎮 Welcome to the Hangman Word Guessing Game!")

    words = ["good", "bad", "ugly", "beautiful", "smart"]
    word = random.choice(words)

    guessed_positions = set()  # Track positions instead of letters
    guessed_letters = set()     # Track attempted letters
    turns = 6

    while turns > 0:
        failed = 0

        print("\nWord: ", end="")
        for i, char in enumerate(word):
            if i in guessed_positions:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\n🎉 Congratulations! You guessed the word correctly.")
            break

        guess = input("\nEnter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet only.")
            continue

        if guess in guessed_letters and guess != 'o':
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            # Reveal only the first unrevealed occurrence
            for i, char in enumerate(word):
                if char == guess and i not in guessed_positions:
                    guessed_positions.add(i)
                    break
            print("✅ Correct guess!")
        else:
            turns -= 1
            print("❌ Wrong guess.")
            print(f"❤️ Remaining turns: {turns}")

            if turns == 0:
                print("\n💀 Game Over!")
                print(f"The correct word was: {word}")

if __name__ == "__main__":
    hangman()