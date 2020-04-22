import os
import numpy

var1 = []
var2 = []
placeholder = 0
wrong1 = 0
lt = ' '


def restart():
    d = (input("Do you want to restart? ")).upper()
    if d == "R":
        game(lt, var1, placeholder, wrong1, var2)

def compare(lt, var1, placeholder, wrong1, var2):
    correct1 = 0
    count = 0
    for var in var1:
        if lt == var:
            var2[count] = var
            correct1 += 1
            placeholder -= 1
            count += 1
        else:
            count += 1
    for var in var2:
        print(var, end=" ")
    print(hangmanseq[wrong1])

    if correct1 != 0:
        if placeholder == 0:
            print("Congratulations! You won!!")
            restart()
        else:
            guess(lt, var1, placeholder, wrong1, var2)
    else:
        wrong1 += 1
        print(hangmanseq[wrong1])
        if wrong1 == 9:
            print("You Lose!!")
            restart()
        else:
            guess(lt, var1, placeholder, wrong1, var2)


def guess(lt, var1, placeholder, wrong1, var2):
    flag = True
    g = input("What are you guessing, sentence(S) or letter(L)? ").upper()
    if g == "S":
        sent = set(input("What is the sentence? ").upper())
        sent0 = set(var1)
        if sent0 == sent:
            print("Congratulations! You won!!")
            restart()
        else:
            wrong1 += 1
            print(hangmanseq[wrong1])
            if wrong1 == 9:
                print("You Lose!!")
                restart()
            else:
                guess(lt, var1, placeholder, wrong1, var2)
    else:
        while flag == True:
            lt = input("Make a guess. ")
            lt = lt.upper()
            if lt == " ":
                print("Invalid guess. Try again.")
            else:
                flag = False
                compare(lt, var1, placeholder, wrong1, var2)


hangmanseq = [''' ''', '''
                 
                      |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                      |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                     _|_''', ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
               / \   _|_''']


def game(lt, var1, placeholder, wrong1, var2):
    var1 = list(input("Sentence? ").upper())
    os.system('cls')
    for var in var1:
        if var != ' ':
            var2.append(" _")
            print(" _", end=" ")
            placeholder += 1
        else:
            var2.append(" ")
            print("  ", end=" ")
    guess(lt, var1, placeholder, wrong1, var2)


game(lt, var1, placeholder, wrong1, var2)


'''


Ask for sentence 

Clear sentence after valid sentence inputted 

Display sentence, replacing letters with blanks 

ask for guess 

check guess with letters in sentence 

    if guess is wrong, display "WRONG" and display next graphic in hangman graphic, wrong += 1 

    if guess is correct, display 'CORRECT' and replace all letters in sentence which correspond with guess 

If all letters guessed before wrong == 10, then player wins 

if wrong == 10 before sentence guessed, player loses 

input R to restart game 











'''


#|\


'''

|
|
|
|
|     
|  
_____ 
|
|
|
|
|     
|  

_____ 
|     |   
|
|
|
|     
|  

_____ 
|     |   
|     O
|
|
|     
|  
_____ 
|     |   
|     O
|     |     
|     |
|     
|  



_____ 
|     |   
|     O
|   \\|     
|     |
|     
|  


_____ 
|     |   
|     O
|   \\|/     
|     |
|     
|  


_____ 
|     |   
|     O
|   \\|/     
|     |
|      \\ 
|  

_____ 
|     |   
|     O
|   \\|/     
|     |
|    / \\ 
|  



'''
