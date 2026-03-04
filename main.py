

# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of 100 heads and tails. Your program should break up the experiment into two parts: the first part generates a list of 100 randomly selected 'H' and 'T' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50 percent of the time and a 1 value the other 50 percent of the time.

import random

# the list holding 100 T or H
final_list = []
# increment the counter for the current item, and reset it if the next item does not match
six_counter = 0
# temp list
temp_list = []
# total matches of six
match_counter = 0

for i in range(100):
    # generate h (0) or t (1)
    h_or_t = random.randint(0, 1)
    if h_or_t == 0:
        final_list.append('H')
    else:
        final_list.append('T')

for i in range(len(final_list) - 1):
    current_value = final_list[i]
    next_value = final_list[i + 1]
    # print the temp list
    print(f'temp list: {temp_list}')
    # check if there are six matches of either T or H
    if six_counter == 6:
        print('WE GOT 6 MATCHES! INCREASE MATCH COUNTER BY 1')
        print(f'match counter was: {match_counter}')
        # increment the match counter to keep track
        match_counter += 1
        print(f'match counter is now: {match_counter}')
        # wipe the list once we have six matches and start again
        temp_list = []
    if current_value == next_value:
        print(f'WE FOUND A MATCH: current value: {current_value}, next value: {next_value}')
        temp_list.append(current_value)
        six_counter += 1
    else:
        # if the values do not match, wipe the list and reset the six counter
        print(f'current value: {current_value} does not match next value: {next_value}')
        temp_list = []
        six_counter = 0

# total number six matches
print(f'total matches: {match_counter}')