import re
import random
import os

print("===========")
print("  HANGMAN")
print("===========")
again=1;
names=["python","java","actionscript","javascript","mortran","nickle","oberon","ruby","turboc","yorick"] #list of the words to guess

while again==1:
  out=0;
  
  
  value=random.randint(0,len(names)-1)
  word=names[value]; #picking a random word from the list

  if(len(names)==-1):   #when you run out of words 
     print("YOU ARE THE CHAMP")
     break

  names.remove(word);   #make sure the word doesnt repeat again
 
  pattern=r"[^aeiou]" 
  okay=re.sub(pattern,"_",word)  #replacing all characters other than vowels with _
  print(okay)
  win = 0
  for i in range(21):    
   
        va=input("Guess - ")  #taking input from user
        varr=0; 
  
        hi=list(okay)
        if va in word:    #checking if input character is in the word
          for le in word:
            if le==va:  
               okay=okay.replace(okay[varr],va)  #replacing the _ from the input letter in the appopriate positions
               hi[varr]=va
            varr=varr+1
        if va not in word:
            out=out+1;     #counter to check for 6 wrong guesses
        okay=''.join(hi)     
        print(okay+"      "+"X"*out) #no of strikes you currently have
        if(out==6):
          win=2
          break
        if("_" not in okay):  #check if we are done guessing the word
          win=1  
          break
        
  if win==1:
     print("YOU WIN")
  else:
     print("YOU LOSE")
  print(names)
  
  again=int(input("Want to play again - "))  #asking if we want to continue playing 
  print("\n\n")        
print("===========")
print("    END  ")
print("===========")

