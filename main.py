

# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of 100 heads and tails. Your program should break up the experiment into two parts: the first part generates a list of 100 randomly selected 'H' and 'T' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50 percent of the time and a 1 value the other 50 percent of the time.

import random

# the list holding 100 T or H
list_of_hundred = []
# increment the counter for the current item, and reset it if the next item does not match
streak_counter = 0
# temp list
matching_list = []
# total matches of six
match_counter = 0
# 10k counter
total_experiments = 0
# set counter
experiment_count = 10000

# perform this 10k times
while total_experiments < experiment_count:
    # increment ten thousand counter
    total_experiments += 1
    print(f'Starting run: {total_experiments}')

    for i in range(100):
        # generate h (0) or t (1)
        h_or_t = random.randint(0, 1)
        if h_or_t == 0:
            list_of_hundred.append('H')
        else:
            list_of_hundred.append('T')

    # check current length list_of_hundred
    print(f'List of 100: {len(list_of_hundred)}')

    for i in range(len(list_of_hundred) - 1):
        current_value = list_of_hundred[i]
        next_value = list_of_hundred[i + 1]
        # print the temp list
        print(f'Matching list: {matching_list}')
        # check if there are six matches of either T or H. we only need streak_counter to reach 5 because it compares the current value (5) to the next (6, a match). if we set streak_counter to 6, it would technically be 7 coins.
        if streak_counter == 5:
            print('Six matches!')
            # add the next value to the matching_list for a visual "completeness" of six
            matching_list.append(next_value)
            print(f'Match counter was: {match_counter}')
            # increment the match counter to keep track
            match_counter += 1
            print(f'Match counter is now: {match_counter}')
            # once we have a streak, break the loop to start a new experiement
            break
        if current_value == next_value:
            print(f'WE FOUND A MATCH: current value: {current_value}, next value: {next_value}')
            matching_list.append(current_value)
            streak_counter += 1
        else:
            # if the values do not match, wipe the list and reset the streak counter
            print(f'Current value: {current_value} does not match next value: {next_value}')
            matching_list = []
            streak_counter = 0
    # message that the first set has finished
    print(f'Experiment {total_experiments} has finished')
    print(f'Total matches for experiment {total_experiments}: {match_counter}')
    print(f'======================================================')
    # reset counters
    matching_list = []
    list_of_hundred = []
    streak_counter = 0

# total number six matches
print(f'Total matches from {total_experiments} experiments: {match_counter}')
# percentage that a streak occurred
print(f'Percentage of streaks that occurred: {match_counter / total_experiments:.2%}')