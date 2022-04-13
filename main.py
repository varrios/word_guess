from valid_words import valid_words
import random
import time

def play_wordle():
    guess = ["_","_","_","_","_"]
    print(*guess)
    counter = 5
    start = time.process_time()
    answer = [i for i in valid_words[random.randrange(-1,len(valid_words))]]
    print(answer)
    print("\n")
    print(f"time executed: {time.process_time() - start} s")

if __name__ == '__main__':
    play_wordle()
