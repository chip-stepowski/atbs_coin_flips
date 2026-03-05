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

    for i in range(len(list_of_hundred) - 1):
        current_value = list_of_hundred[i]
        next_value = list_of_hundred[i + 1]
        # check if there are six matches of either T or H. we only need streak_counter to reach 5 because it compares the the current and next values (a match, which meets our criteria)
        if streak_counter == 5:
            # increment the match counter to keep track
            match_counter += 1
            # once we have a streak, break the loop to start a new experiement
            break
        if current_value == next_value:
            matching_list.append(current_value)
            streak_counter += 1
        else:
            # if the values do not match, wipe the list and reset the streak counter
            matching_list = []
            streak_counter = 0
    # message that the first set has finished
    print(f'Experiment {total_experiments} has finished')
    print(f'==============================================')
    # reset counters
    matching_list = []
    list_of_hundred = []
    streak_counter = 0

# total number six matches
print(f'Total matches from {total_experiments} experiments: {match_counter}')
# percentage that a streak occurred
print(f'Percentage of streaks that occurred: {match_counter / total_experiments:.2%}')