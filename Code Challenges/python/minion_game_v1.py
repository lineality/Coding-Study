# Problem (User Problem)
#
# You Have:
#    string_input
#
# You Need:
#    winner of game, score
#
# You Must: 
#    # stuart -> start with consonant
#    # kevin -> start with a vowel
#    note: arbitrary malicious hidden rule snag,
#    "overlapping string matching"
#    Why?
# 
# Solution (Product / Feature for User)
#
# case:
# "fish"
# 1. iterate through whole word(string)
# 2. id letter as vowel or consonant(not-vowel)
# 3. make list of fragments starting with that letter
# 4. add that temp_list_of_fragments to set for vowel or set for consonant
# 5. count how many times, using: helper function for overlapping matches >:( 
# 6. determin which team won, ascribe arbitrary name to winner and print score
# Q: remove non-letter or case-senstive contents?
# 
# I Learned:
# (Compare to other solutions)

import re

# helper function
def overlapping_count_function(input_string_whole, fragment): 
  
    overlapping_count = 0
    start_here = 0
  
    # iterate through input_string_whole  
    while start_here < len(input_string_whole): 
  
        # Check for fragment from start_here to end 
        position = input_string_whole.find(fragment, start_here) 
  
        if position != -1: 
            # if fragment present, move start_here to next position 
            start_here = position + 1
  
            # increment 
            overlapping_count += 1

        else:  # found nothing
            break

    return overlapping_count 



def minion_game(string_input):

    vowels = ['a','e','i','o','u']
    vowel_flag = False
    counter_1 = 0
    counter_2 = 0

    vowel_team_set = set()
    consonant_team_set = set()

    vowel_team_score = 0
    consonant_team_score = 0

    # prep: Make all lower case letters (no spaces or numbers)
    # make all lower case
    string_input = string_input.lower()
    # remove symbols
    string_input = re.sub(r'\W', '', string_input)
    # remove numbers
    string_input = re.sub(r'\d', '', string_input)
    # remove spaces
    string_input = re.sub(r'\s', '', string_input)

    # 1. First Loop through word
    for i in range(0,len(string_input)):

        letter = string_input[counter_1]

        # 2. id letter (vowel or not)
        if letter in vowels:
            vowel_flag = True
        else:
            vowel_flag = False
        
        # reset for next loop
        counter_2 = counter_1 + 1  # slices up to not including
        temp_list_of_fragments = []

        for i in range(len(string_input) - counter_1):
            sliced_fragment = string_input[counter_1 : counter_2]


            if vowel_flag is False:
                  consonant_team_set.add(sliced_fragment)
            else:
                  vowel_team_set.add(sliced_fragment)

            # incriment fragment counter
            counter_2 += 1

        # incriment main counter
        counter_1 += 1
    
    # #inspection
    # print(consonant_team_set)
    # print(vowel_team_set)

    for fragment in consonant_team_set:
        consonant_team_score += overlapping_count_function(string_input, fragment)

    for fragment in vowel_team_set:
        vowel_team_score += overlapping_count_function(string_input, fragment)
        
        # # inspection
        # print(string_input.count(fragment))
        # print(fragment)

    #  #inspection
    # print(consonant_team_score) 
    # print(vowel_team_score) 

    if consonant_team_score == vowel_team_score:
        print('Draw')

    elif consonant_team_score > vowel_team_score:
        print('Stuart', consonant_team_score)

    elif consonant_team_score < vowel_team_score:
        print('Kevin', vowel_team_score)

