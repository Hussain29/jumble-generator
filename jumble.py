
import random    # using package random to use sample() function

# creating variables to take input of 4 'clue' strings
WORD1 = input("Enter the 1st word: ").upper()
WORD2 = input("Enter the 2nd word: ").upper()
WORD3 = input("Enter the 3rd word: ").upper()
WORD4 = input("Enter the 4th word: ").upper()

print('\n')

# taking input of 'riddle' string
RIDDLE = input("Enter the riddle word: ").upper()

print('\n')

# removing spaces from the 'riddle' string
RIDWOSPACE = RIDDLE.replace(" ", "")

# creating a string with all the letters from the 4 'clue' strings
MASTER = ''.join((WORD1, WORD2, WORD3, WORD4))

# creating variables to print later, for ease
BLANK = "[   ]"
REQ_LETTER = "[ _ ]"


# checking if the 'riddle' is solvable from the given 'clues'
if len(set(RIDWOSPACE) - set(MASTER)) == 0:
    print("Riddle can be solved.", end = '')
else:
    print("Riddle cannot be solved. Try Again.", end = '')

print('\n')

#creating a variable to control duplicate 'clue' letters
check = list(RIDWOSPACE)

#creating a list of the 4 'clue' words to iterate through
words = [WORD1,WORD2,WORD3,WORD4]

#print a seperating line
print('+-' + '-----'*(len(RIDDLE)) + '-+')

print('\n')
#block of code that prints the letters and positions

for word in words:    #here we're going through the 'words'
    JUMBLE = ''.join(random.sample(word, len(word)))    #jumbles the current word in the loop 
    for ch in JUMBLE:
        print("  "+ch+ "  ",end='')    #prints the letters from the jumble

    print("\n", end = '')    #now, we start printing blanks in the next line
    for ch in word:
        if ch in check:    #this checks if the letter is required to solve the riddle
            print(REQ_LETTER,end='')    #prints the underlined blank
            check.remove(ch)    #removes the letter so it doesnt check for it again
        else:
            print(BLANK,end='')    #prints regular blank

    print("\n")
    JUMBLE = ''

#print a seperating line
print('\n')
print('+-' + '-----'*(len(RIDDLE)) + '-+')

print('\n')    
#add riddle word blanks
print("Fill In The Riddle:")
print('\n')
for ch in RIDDLE:    #prints the blanks for the 'riddle' word
    if ch == " ":
        print("     ",end='')
    else:
        print(BLANK,end='')

print('\n')
#print a seperating line
print('\n')
print('+-' + '-----'*(len(RIDDLE)) + '-+')
print('\n')
