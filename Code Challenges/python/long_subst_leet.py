# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Problem (User's):
# You Have: an input string
# You Need: length of longest non-repeating 
# or rather unique characters in sequence substring in input_string
# You Must: output an integer
# define "repeat" as ever repeating (which...is bunkum)

# Solution (Feature / Product):
# idea:
# turn into a list
# make substrings based on where repeating characters are
# get indices of repeating characters
# these represent segment demarcation
# e.g.
#       aaaNOPeeeA
#       0123456789


# I Learned:


class Solution:
    def lengthOfLongestSubstring(self, input_string: str) -> int:

        indices_of_repeats_list = []

        return

