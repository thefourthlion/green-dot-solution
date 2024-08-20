```python
import random

def game():
    num = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != num:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")

    print(f"Congratulations! You've guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    game()
```