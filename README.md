# jumble-generator

This program prints a 'Jumble Puzzle' for 4 given words and a riddle phrase along with a clue hinting at the riddle.

It takes input of 4 words, a riddle phrase, and a clue.

We first check if the riddle phrase can even be solved from the letters given in the 4 words.

Then after jumbling the words, we print each letter and then print the blank positions '[   ]' under them as a template to unjumble them.

And for the position that tells us that the letter is required to solve the riddle, print '[ _ ]'

Then after un-jumbling the letters, the user may take note of those underlined letters and try to solve the riddle phrase which is also presented in '[   ]' boxes, provided with the clue as well.
