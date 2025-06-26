import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

symbols = ['@', '#', '$', '%', '&', '*']
pattern = ''.join(random.choices(symbols, k=5))

def memory_game():
    print("🧠 Pattern Memory Game")
    print("Memorize this pattern:")
    print(f"🔹 {pattern} 🔹")
    time.sleep(3)
    clear_screen()
    
    guess = input("Enter the pattern you saw: ")
    if guess == pattern:
        print("🎉 Correct! Your memory is sharp!")
    else:
        print(f"😢 Incorrect. The pattern was: {pattern}")
memory_game()