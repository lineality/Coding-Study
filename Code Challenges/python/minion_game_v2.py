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
# There are different ways of looking at the rules,
# which to some extent brings up the questions of
# overlapping matches, which is not addressed in the rules.
# e.g. for "B" why is the string minus index the same as the 
# the number of "B" strings? Count backwards removing a letter
# each of those is string starting with B, and so on for each 
# letter.
# Again, this only works if the rules include overlapping matches.


def minion_game(input_string):
    # set vowels
    vowels_list = ['A','E','I','O','U']
    # reset scores to zero
    consonant_team_score, vowel_team_score = 0, 0

    # calculate scores
    # 
    for index_1 in range(len(input_string)):
        if input_string[index_1] in vowels_list:
            vowel_team_score += len(input_string)-index_1
            # # inspection
            # print(input_string[index_1], len(input_string)-index_1)
        else:
            consonant_team_score += len(input_string)-index_1
            # # inspection
            # print(input_string[index_1], len(input_string)-index_1)

    # print winner
    if consonant_team_score == vowel_team_score:
        print("Draw")
    elif consonant_team_score > vowel_team_score:
        print("Stuart", consonant_team_score)
    else:
        print("Kevin", vowel_team_score)


minion_game("BANANA")
