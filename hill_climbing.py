# Hill Climbing Program

import random
import string

def generate_random_solution(answer):
    l = len(answer)                                                                # Find the length of the answer
    return [random.choice(string.printable) for _ in range(l)]

def evaluate(solution, answer):
    print(solution)
    target = list(answer)
    diff = 0

    for i in range(len(target)):
        s = solution[i]
        t = target[i]

        diff += abs(ord(s) - ord(t))

    return diff

def mutate_solution(solution):
    ind = random.randint(0, len(solution) - 1)
    solution[ind] = random.choice(string.printable)
    return solution



def SimpleHillClimbing():
    answer = input("Enter the String:")

    best = generate_random_solution(answer)
    best_score = evaluate(best, answer)

    while True:
        print("Score:", best_score, " Solution:", "".join(best))

        if best_score == 0:
            print("\nTarget String Found!")
            break

        new_solution = mutate_solution(list(best))
        score = evaluate(new_solution, answer)

        if score < best_score:
            best = new_solution
            best_score = score

SimpleHillClimbing()
