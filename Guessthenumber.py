import random

# Welcome message for the game
print('***************** Number guessing game *****************') 

# User chooses the lower bound of the guessing range
lower=int(input('Enter lower value: '))
# User chooses the upper bound of the guessing range
upper=int(input('Enter upper value: '))

# Computer generates a random number between lower and upper
ans=random.randint(lower,upper)


# Prepare clues about the secret number
if ans % 2 == 0:
    even_odd = "The number is even."
else:
    even_odd = "The number is odd."

if ans % 5 == 0:
    multiple_5 = "The number is a multiple of 5."
else:
    multiple_5 = "The number is not a multiple of 5."

if ans % 3 == 0:
    multiple_3 = "The number is a multiple of 3."
else:
    multiple_3 = "The number is not a multiple of 3."

ends_with = "The number ends with the digit " + str(ans)[-1] + "."
starts_with = "The number starts with the digit " + str(ans)[0] + "."
digit_count = "The number has " + str(len(str(ans))) + " digit(s)."


# Store all possible clues in a list
clues = [
    even_odd,
    multiple_5,
    multiple_3,
    ends_with,
    starts_with,
    digit_count,
]

# Randomly pick 3 clues to use in the game
selected_clues = random.sample(clues, 3)

# Ask user to choose difficulty until valid input is given
while True:
    diff=int(input("Enter difficulty (1, 2, or 3): "))
    if diff in [1,2,3]:
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

# Difficulty 1: Easy mode (10 tries, -10 points each wrong guess)
if diff==1:

          score=100
          print('You have chosen 1(Easy). You have 10 tries')

          for chance in range(10):

              if 9-chance<3:
                  clue_index =chance-(10-3)
                  print()
                  print("Clue:", selected_clues[clue_index - 1])
                  print()
              
              print()
              print('No of chances remaining:',10-chance)
                  
              guess = int(input('Enter your guess from '+str(lower)+' to '+str(upper)+': '))
              
              if chance==9 and guess!=ans:
                  print()
                  print('You are out of tries. The answer is',ans)
                  print('Your score: 0 out of 100')
                  break

              if guess>upper or guess<lower:
                  print('Your guess is out of range')
                  continue
                
              if guess==ans:
                  print(ans,'is the correct answer. You have guessed in',chance+1,'tries. Congratulations')
                  print('Your Score:',score,'out of 100')
                  break
              else:
                  score-=10
                
              if not guess==ans:
                  if guess>ans:
                      print()
                      print('Too high. You have',10-chance-1,'tries more')
                      upper=guess-1
                  elif guess<ans:
                      print()
                      print('Too low. You have',10-chance-1,'tries more')
                      lower=guess=+1
                  continue

# Difficulty 2: Medium mode (7 tries, -14 points each wrong guess)
elif diff==2:

          score=100 
          print('You have chosen 2(Medium). You have 7 tries')

          for chance in range(7):

              if 6-chance<3:
                  clue_index =chance-(7-3)
                  print()
                  print("Clue:", selected_clues[clue_index - 1])
                  print()
              
              print()
              print('No of chances remaining:',7-chance)
              
              guess = int(input('Enter your guess from '+str(lower)+' to '+str(upper)+': '))
              
              if chance==6 and guess!=ans:
                  print()
                  print('You are out of tries. The answer is',ans)
                  print('Your Score: 0 out of 100')
                  break

              if guess>upper or guess<lower:
                  print('Your guess is out of range')
                  continue
                
              if guess==ans:
                  print(ans,'is the correct answer. You have guessed in',chance+1,'tries. Congratulations')
                  print('Your Score:',score,'out of 100')
                  break
              else:
                  score-=14
                
              if not guess==ans:
                  if guess>ans:
                      print()
                      print('Too high. You have',7-chance-1,'tries more')
                      upper=guess-1
                  elif guess<ans:
                      print()
                      print('Too low. You have',7-chance-1,'tries more')
                      lower=guess+1
                  continue

# Difficulty 3: Hard mode (5 tries, -20 points each wrong guess)
elif diff==3:

          score=100     
          print('You have chose 3(Hard). You have 5 tries')

          for chance in range(5):

              if 4-chance<3:
                  clue_index =chance-(5-3)
                  print()
                  print("Clue:", selected_clues[clue_index - 1])
                  print()
              
              print()
              print('No of chances remaining:',5-chance)
              
              guess = int(input('Enter your guess from '+str(lower)+' to '+str(upper)+': '))

              if chance==4 and guess!=ans:
                  print()
                  print('You are out of tries. The answer is',ans)
                  print('Your Score: 0 out of 100')
                  break

              if guess>upper or guess<lower:
                  print('Your guess is out of range')
                  continue
                
              if guess==ans:
                  print(ans,'is the correct answer. You have guessed in',chance+1,'tries. Congratulations')
                  print('Your Score:',score,'out of 100')
                  break
              else:
                  score-=20
                
              if not guess==ans:
                  if guess>ans:
                      print()
                      print('Too high. You have',5-chance-1,'tries more')
                      upper=guess-1
                  elif guess<ans:
                      print()
                      print('Too low. You have',5-chance-1,'tries more')
                      lower=guess+1
                  continue


                                            
