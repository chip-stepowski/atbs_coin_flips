

# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of 100 heads and tails. Your program should break up the experiment into two parts: the first part generates a list of 100 randomly selected 'H' and 'T' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50 percent of the time and a 1 value the other 50 percent of the time.

import random

final_list = []

for i in range(100):
    # generate h (0) or t (1)
    h_or_t = random.randint(0, 1)
    if h_or_t == 0:
        final_list.append('H')
    else:
        final_list.append('T')

# save to a list
print(f'final list: {final_list}')