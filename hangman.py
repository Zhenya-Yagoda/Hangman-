# Problem Set 2, hangman.py
# Name: Yagoda Eugenia
# Collaborators:
# Time spent: 3 days

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
# secret_word = 'apple'
# letters_guessed = []
letters_guessed = []



def load_words():    
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in wordlist:
      if i not in letters_guessed:
        return False  
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    user_letters = []
    for i in secret_word:
      if i in letters_guessed:
        user_letters.append(i)
      else :
        user_letters.append('_')
    user_word=''.join(user_letters)
    return user_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters=string.ascii_lowercase
    list_of_a_l=list(available_letters)
    for i in letters_guessed:
      list_of_a_l.remove(i)
    available_letters=''.join(list_of_a_l)
    return available_letters
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    l_of_s_w=len(secret_word)
    guesses = 6
    warning = 3
    print('Welcome to the game Hangman!\nI am thinking of a word that is ', l_of_s_w ,' letters long.')
    while 0<guesses<=6:
      
      if is_word_guessed(secret_word, letters_guessed)==False :
        print('-----------------------------------\nYou have ',warning,' warnings left.\nYou have ', guesses, ' guesses left.\nAvailable letters: ', get_available_letters(letters_guessed))
        u_res=str(input('Please guess a letter: '))
        if len(u_res)==1:
          if u_res.isalpha()==True:
            u_res.lower()
            if u_res not in letters_guessed:
              letters_guessed.append(u_res)
              if u_res in secret_word:
                print('Good guess: ',get_guessed_word(secret_word, letters_guessed) )
                is_word_guessed(secret_word, letters_guessed)
              else:
                if u_res in ['a','e','i','o','u','y'] :
                  guesses-=2
                  print('Oops! That letter is not in my word.\nPlease guess a letter: ',get_guessed_word(secret_word, letters_guessed) )  
                else:
                  guesses-=1
                  print('Oops! That letter is not in my word.\nPlease guess a letter: ',get_guessed_word(secret_word, letters_guessed) )  
            else:
              if warning!=0:
                warning-=1
                print('Oops! You\'ve already guessed that letter. You now have ',warning,' warnings: ' , get_guessed_word(secret_word, letters_guessed))
              else :
                guesses-=1
                print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed) )
                warning=3
          else :
            if warning!=0:
              warning-=1
              print('Oops! That is not a valid letter. You have ',warning,' warnings left:',get_guessed_word(secret_word, letters_guessed))
            else :
              guesses-=1
              print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed) )
              warning=3
        else:
          if warning!=0:
            warning-=1
            print('Oops! That is not a valid letter. You have ',warning,' warnings left:',get_guessed_word(secret_word, letters_guessed))
          else :
            guesses-=1
            print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed) )
            warning=3
      else:
        print('Congratulations, you won!\nYour total score for this game is:' , guesses*len(set(secret_word)))
        break
    else:
        print('-----------------------------------\nSorry, you ran out of guesses. The word was else :' , secret_word)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    hits=[]
    my_word=list(my_word.replace(' ','')) 
    other_word=list(other_word) 
    if len(my_word)!=len(other_word):
      return False
    else: 
      for i in range(len(my_word)):
        if my_word[i] != '_' and my_word[i]!=other_word[i] :
          return False
      for i in range(len(other_word)):
        k=i+1
        for k in range(len(my_word)):
          if other_word[i]==other_word[k] and my_word[i]!=my_word[k]:
            return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_of_hits=[]
    for i in wordlist:  
      if match_with_gaps(my_word,i):
        list_of_hits.append(i)
    if len(list_of_hits)==0:
      print('No matches found')
    else :
      print('Possible word matches are', end=' ')
      for item in list_of_hits:
        print(item,end=' ' )
    print('')
    
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    l_of_s_w=len(secret_word)
    guesses = 6
    warning = 3
    print('Welcome to the game Hangman with hints!\nI am thinking of a word that is ', l_of_s_w ,' letters long.')
    while 0<guesses<=6:
      
      if is_word_guessed(secret_word, letters_guessed)==False :
        print('-----------------------------------\nYou have ',warning,' warnings left.\nYou have ', guesses, ' guesses left.\nAvailable letters: ', get_available_letters(letters_guessed))
        u_res=str(input('Please guess a letter: '))
        if u_res=='*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif len(u_res)==1:
          if u_res.isalpha()==True:
            u_res.lower()
            if u_res not in letters_guessed:
              letters_guessed.append(u_res)
              if u_res in secret_word:
                print('Good guess: ',get_guessed_word(secret_word, letters_guessed) )
                is_word_guessed(secret_word, letters_guessed)
              else:
                if u_res in ['a','e','i','o','u','y'] :
                  guesses-=2
                  print('Oops! That letter is not in my word.\nPlease guess a letter: ',get_guessed_word(secret_word, letters_guessed) )  
                else:
                  guesses-=1
                  print('Oops! That letter is not in my word.\nPlease guess a letter: ',get_guessed_word(secret_word, letters_guessed) )  
            else:
              if warning!=0:
                warning-=1
                print('Oops! You\'ve already guessed that letter. You now have ',warning,' warnings: ' , get_guessed_word(secret_word, letters_guessed))
              else :
                guesses-=1
                print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed) )
                warning=3
          else :
            if warning!=0:
              warning-=1
              print('Oops! That is not a valid letter. You have ',warning,' warnings left:',get_guessed_word(secret_word, letters_guessed))
            else :
              guesses-=1
              print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed) )
              warning=3
        else:
          if warning!=0:
            warning-=1
            print('Oops! That is not a valid letter. You have ',warning,' warnings left:',get_guessed_word(secret_word, letters_guessed))
          else :
            guesses-=1
            print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:',get_guessed_word(secret_word, letters_guessed) )
            warning=3
      else:
        print('Congratulations, you won!\nYour total score for this game is:' , guesses*len(set(secret_word)))
        
        break
    else:
        print('-----------------------------------\nSorry, you ran out of guesses. The word was else :' , secret_word)

   



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
ok=False
while not ok:
  x=input('Choose a game to play:\nhangman (enter 1) or hangman with hints (enter 2) -')
  if x=='1':
    if __name__ == "__main__":  
        # pass

        # To test part 2, comment out the pass line above and
        # uncomment the following two lines.
        
        secret_word = choose_word(wordlist)
    hangman(secret_word)
    ok=True
  elif x=='2':
    ###############
        
        # To test part 3 re-comment out the above lines and 
        # uncomment the following two lines. 
        
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    ok=True
  else:
    print('Error!Enter 1 or 2.')
