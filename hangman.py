import random
word_list= ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)


display=[]
for x in range(len(chosen_word)):
     display+="_"



end_of_game=False

life=0

while not end_of_game:
    
    guess = input("Guess the letter ").lower()
    for num in range(len(chosen_word)):
            if(chosen_word[num] == guess):
                display[num]=guess
            
    
    print(display)
    if(guess not in display):
        life+=1
        if(life==5):
            end_of_game=True
            print("You lost")
    




    if('_' not in display):
         end_of_game=True
         print("You win")



word =""

for letter in  display:
     word+=letter


