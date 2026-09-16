def generate_hashtag(s):

    if s == "" or s == " ":
        return False

    list_word = s.split(" ")
    hastag_word = "#"

    for x in list_word:
        hastag_word += x.title()

    if len(hastag_word) >= 140:
        return False

    return hastag_word


generate_hashtag("    Hello     World   " )
# generate_hashtag('Codewars')# '#Codewars', 'Should handle a single word.'
# generate_hashtag('Codewars      ')# '#Codewars', 'Should handle trailing whitespace.'
# generate_hashtag('      Codewars')# '#Codewars', 'Should handle leading whitespace.'
# generate_hashtag('Codewars Is Nice')# '#CodewarsIsNice', 'Should remove spaces.'
# generate_hashtag('codewars is nice')# '#CodewarsIsNice', 'Should capitalize first letters of words.'
# generate_hashtag('CoDeWaRs is niCe')# '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.'
# generate_hashtag('c i n')# '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.'
# generate_hashtag('codewars  is  nice')# '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.'
        
"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""