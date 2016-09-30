# Paste your code into this box
print('Please think of a number between 0 and 100!')
low = 0.0
high = 100.0
ans = (high + low)//2.0
step = None

print("Is you secret number " + str(ans) + "?")

while True:
   
    step = input("Enter 'h' to indicate the guess is too\
    high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate\
    I guessed correctly.")
    
    if step == "l":
        low = ans
   
    elif step == "h":
        high = ans
    
    elif step == "c":
        break
    
    elif step !="l" or step !="h" or step !="c":
        print("Sorry, I did not understand your input.")
        
    ans = (high + low)//2.0
    print("Is you secret number " + str(ans) + "?") 
       
print("Game over. Your secret number was: " + str(ans))
