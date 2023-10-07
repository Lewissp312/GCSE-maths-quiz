#imports
from natsort import natsorted 
#a function that can sort integer values when they are attached to strings
##############################################################################################################################################################

#position finding functions

#finding the position of a student in the tiers and struggle folders:

def tierAndStrugglesPosition():
  studentStruggles=open("studentStruggles.txt","r+") #reading from files
  struggles=studentStruggles.readlines() 
  studentCount=0
  for entry in struggles:
    if name in entry:
      global tierStrugglePos
      tierStrugglePos=studentCount #files organised for sequential access - this can be used by functions that involve the tier file and the student struggles file, as both are organised in the same order. This allows for instant access to the student's entry, without having to search through the file each time.
    studentCount=studentCount+1
  studentStruggles.close()

#finding a student's position on the leaderboard:

def leaderboardPosition():
  global leaderboardPos
  global realLeaderboardPos
  global leaderboardNum
  studentCount=0
  leaderboardNum=""
  leaderboard=open("leaderboard.txt","r") #reading from files
  scores=leaderboard.readlines()
  for entry in scores:
    if name in entry:
      realLeaderboardPos=studentCount #this is the true position of that student in the file. Used for file operations
      leaderboardPos=studentCount+1 #The student's position on the leaderboard where the leaderboard starts at one instead of zero. This can be used throughout the program to access a student's position on the leaderboard instantly without having to sequentially search the file again. 
      for i in entry:
        if i in str(basic):
          leaderboardNum=leaderboardNum+i
    studentCount=studentCount+1
  studentCount=0

##############################################################################################################################################################

#login

def loginFunc():
  global name
  logins={} #dictionary
  logCount=1
  login=open("loginInfo.txt","r") #reading from a file
  for i in login:
    i=i.strip("\n")
    if logCount%2==1: #dictionary/files organised for sequential access - the login values are all stored with the name being first, followed by the password. This means that all names will be in an odd space and all passwords will be in an even space. This algorithm determines whether the entry is odd or even. If it's odd, it will be stored as pastI so it can be added to a dictionary along with the next entry, which will be that name's password.
      pastI=i 
    if logCount%2==0:
      logins[pastI]=i
    logCount=logCount+1
  loginFlag=True
  while loginFlag==True:
    print("If you wish to exit the program, type quit")
    username=input("Enter your username ")
    if username=="quit":
      print("Thanks for using")
      quit()
    password=input("Enter your password ")
    if password=="quit":
      print("Thanks for using")
      quit()
    if username=="John" and password=="84288428!A": #accesses the teacher account
      print("Username and password accepted")
      teacherName="John"
      login.close()
      teacherAcc(teacherName)
    elif username in logins:
      if logins[username]==password:
        print("Username and password accepted")
        name=username
        tierAndStrugglesPosition()
        menu()
      else:
        print("Username and password do not match, try again")
    else:
      print("Username not found, try again") #handles erroneous data
  login.close()


##############################################################################################################################################################

#menu functions

#finding the user's tier

def tierAssignment():
  global tier
  tierNums=[1,2,3,4,5]
  studentTiers=open("studentTiers.txt","r") #reading from files
  tiers=studentTiers.readlines()
  for i in tiers[tierStrugglePos]: #An example of the tierStrugglePos variable being used to avoid another sequential search
    if i in str(tierNums):
      tier=i
  studentTiers.close()

#allows a user to check their position on the leaderboard

def leaderboardRanking():
  leaderboardPosition()
  if leaderboardPos==1: #a use of the leaderboardPos variable, the use of which means that the leaderboard does not have to be searched through again here
    print("You're at position one in the leaderboard with a score of " + leaderboardNum + "! Congratulations!")
  elif leaderboardPos<=5:
    print("You're in position " + str(leaderboardPos) + " on the leaderboard with a score of " + leaderboardNum + "! Well done for making it into the top 5!")
  elif leaderboardPos<=10:
    print("You're in position " + str(leaderboardPos) + " on the leaderboard with a score of " + leaderboardNum + "! Well done for making it into the top 10!")
  else:
    print("You're in position " + str(leaderboardPos) + " on the leaderboard with a score of " + leaderboardNum)


##############################################################################################################################################################

  
#menus

def menu():
  mainFlag=True
  while mainFlag==True:
    import random #allows for random number selection from a list which is crucial for this program
    import math #maths calculations - helps with square roots for tier 3, sine cos and tan for tier 4, and Pi for tier 4 and 5
    exampleCheck=False #boolean value used for option 2 of the menu. If the example check is true, the quiz part of the program will be skipped, and a user can go straight to viewing the examples
    tier1Qs=[["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"]] #lists and dictionaries that are used to house questions and examples. The questions lists are two dimensional, and the examples lists and numbers lists are both one dimensional
    tier1Es=["","","","","","","","","",""]
    tier2Qs=[["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"]]
    tier2Es=["","","","","","","","","",""]
    tier3Qs=[["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"]]
    tier3Es=["","","","","","","","","",""]
    tier4Qs=[["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"]]
    tier4Es=["","","","","","","","","",""]
    tier5Qs=[["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"],["x","x"]]
    tier5Es=["","","","","","","","","",""]
    global basic
    global teens
    global twenties
    global thirties
    global forties
    global fifties
    basic = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    teens = [11, 12, 13, 14, 15, 16, 17, 18, 19]
    twenties = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    thirties = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
    forties = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    fifties = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
    #As both the tier and leaderboard position of a user change throughout the quizzes, these functions are repeated and the values are reassigned every time the user goes back to the menu.
    tierAssignment() 
    leaderboardPosition()
    choice=input("Hello " + name + "! Welcome to the quiz, what would you like to do?\n 1.) Start a quiz\n 2.) Select a tier and see some examples for it\n 3.) Check your position on the leaderboard\n 4.) Check your tier \n 5.) Check the topics you're struggling with \n 6.) Log out \n 7.) Stop the quiz\n Type menu at any time to return here\n\n")
  
    if choice=="1":
      userQuiz=input("Which quiz would you like to do (1-5)? ")
      if userQuiz=="1":
        quizTier=1 #as the functions for both tier 1 and tier 2 quizzes are combined, the quizTier variable is used to keep track of what tier quiz the user is currently doing
        print("Remember to add the units!\n")
        tier12Quiz(tier1Qs,tier2Qs,tier1Es,tier2Es,quizTier,exampleCheck,random)
      elif userQuiz=="2":
        if int(tier)>=2: #used to check whether the user has a high enough tier to access this quiz yet
          quizTier=2
          print("Remember to add the units!\n")
          tier12Quiz(tier1Qs,tier2Qs,tier1Es,tier2Es,quizTier,exampleCheck,random)
        else:
          print("Sorry, but you cannot access this quiz yet, you need to score a 10 on the tier 1 quiz\n")
      elif userQuiz=="3":
        if int(tier)>=3:
          quizTier=3
          print("Remember to add the units!")
          tier34Quiz(tier3Qs, tier3Es, tier4Qs, tier4Es,quizTier, exampleCheck,random,math)
        else:
          print("Sorry, but you cannot access this quiz yet, you need to score a 10 on the tier 2 quiz\n")
      elif userQuiz=="4":
        if int(tier)>=4:
          print("For this quiz, angle A is the angle to the left of the hypotenuse and to the right of the left upright side, and angle B is the angle beneath the hypotenuse and above the base. This quiz is in degrees\n")
          quizTier=4
          tier34Quiz(tier3Qs, tier3Es, tier4Qs, tier4Es,quizTier, exampleCheck,random,math)
        else:
          print("Sorry, but you cannot access this quiz yet, you need to score a 10 on the tier 3 quiz\n")
      elif userQuiz=="5":
        if int(tier)>=5:
          print("For this quiz, pi has been rounded to three decimal places. Remember to add the units!\n")
          quizTier=5
          tier5Quiz(tier5Qs, tier5Es,quizTier, exampleCheck,random,math)
        else:
          print("Sorry, but you cannot access this quiz yet, you need to score a 10 on the tier 4 quiz\n")
      elif userQuiz=="menu":
        menu()
      else:
        print("This is not a valid quiz\n") #factors out erroneous inputs
        
        
    elif choice=="2":
      userQuiz=input("Which quiz would you like to see examples for?")
      if userQuiz=="1":
        print("Quiz one deals with the perimeters of shapes")
        quizTier=1
        exampleCheck=True #this skips the answering part of the program
        tier12Quiz(tier1Qs,tier2Qs,tier1Es,tier2Es,quizTier,exampleCheck,random)
      elif userQuiz=="2":
        if int(tier)>=2:
          print("Quiz two deals with areas of shapes")
          quizTier=2
          exampleCheck=True
          tier12Quiz(tier1Qs,tier2Qs,tier1Es,tier2Es,quizTier,exampleCheck,random)
        elif int(tier)<2:
          print("Sorry, but you cannot access this quiz yet, you need to score a 10 on the tier 1 quiz\n")
      elif userQuiz=="3":
        if int(tier)>=3:
          print("Quiz three deals with the Pythagorean theorem, and using it to work out the missing side of a right angled triangle")
          quizTier=3
          exampleCheck=True
          tier34Quiz(tier3Qs, tier3Es, tier4Qs, tier4Es,quizTier, exampleCheck,random,math)
        elif int(tier)<3:
          print("Sorry, but you cannot access this quiz yet, you need to score a 10 on the tier 2 quiz\n")
      elif userQuiz=="4":
        if int(tier)>=4:
          print("Quiz four deals with sohcahtoa, and using it to work out the missing angle of a right angled triangle")
          quizTier=4
          exampleCheck=True
          tier34Quiz(tier3Qs, tier3Es, tier4Qs, tier4Es,quizTier, exampleCheck,random,math)
        elif int(tier)<4:
          print("Sorry, but you cannot access this quiz yet, you need to score a 10 on the tier 3 quiz\n")
      elif userQuiz=="5":
        if int(tier)==5:
          print("Quiz five deals with various circle calculations")
          quizTier=5
          exampleCheck=True
          tier5Quiz(tier5Qs, tier5Es,quizTier, exampleCheck,random,math)
        elif int(tier)<5:
          print("Sorry, but you cannot access this quiz yet, you need to score a 10 on the tier 4 quiz\n")
      elif userQuiz=="menu":
        menu()
      else:
        print("This is not a valid quiz\n") #factors out erroneous inputs
        
    elif choice=="3":
      leaderboardRanking()
    
    elif choice=="4":
      print("You are currently on tier " + tier + "\n")

    elif choice=="5":
      struggles=open("studentStruggles.txt","r") #reading from files
      students=struggles.readlines() 
      if "perimeters" not in students[tierStrugglePos] and "areas" not in students[tierStrugglePos] and "Pythagoras" not in students[tierStrugglePos] and "sohcahtoa" not in students[tierStrugglePos] and "circles" not in students[tierStrugglePos]: #tierStrugglePos being used to skip another sequential search through the file
        print("You are not struggling with anything at the moment, well done!")
      else:
        print("You are currently struggling with:\n")
        if "perimeters" in students[tierStrugglePos]:
          print("Perimeters\n")
        if "areas" in students[tierStrugglePos]:
          print("Areas\n")
        if "Pythagoras" in students[tierStrugglePos]:
          print("Pythagoras\n")
        if "sohcahtoa" in students[tierStrugglePos]:
          print("Sohcahtoa\n")
        if "circles" in students[tierStrugglePos]:
          print("Circles\n")
    
    elif choice=="6":
      loginFunc()
    
    elif choice=="7":
      print("Thanks for using!") 
      quit() #ends the program

    elif choice=="menu":
      menu() 
      
    else:
      print("Please pick an option from 1 to 7\n") #factors out erroneous inputs


#teacher account. The admin account from which details about students can be accessed. This includes their tier, their position on the leaderboard, and what they're struggling with. Their entries in these files can also be changed, such as resetting a student's score to 0, and their tier to one. Students can also be added and removed to and from the quiz

def teacherAcc(teacherName):
  global name
  global basic
  lowerLetters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #one dimensional lists used for checking whether new passwords have the required characters or whether student names are just letters
  capitals=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  symbols=["!","£","$","%","^","&","*","(",")","{","}",":",";","@","~","#","|","<",">",".","?","/"]
  basic = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
  teacherFlag=True
  while teacherFlag==True:
    nameCheck=False
    position=0
    studentCount=0
    choice=input("Hello " + teacherName + ", welcome to the quiz admin. What would you like to do? \n 1.) Check what a student is struggling with\n 2.) Check a student's position on the leaderboard\n 3.) Reset a student's total answer score \n 4.) Check which tier a student is on \n 5.) Reset a student's tier\n 6.) Add a new student \n 7.) Remove a student \n 8.) Log out\n 9.) Stop the program\n\n ") 
    
    if choice=="1" or choice=="2" or choice=="3" or choice=="4" or choice=="5" or choice=="6" or choice=="7":
      name=input("What is the student's name? ")
      if len(name)==0: #factoring out erroneous data - an empty slot is present in all the student files so this checks if the input is an empty string
        print("This student is not registered in this quiz\n")
      else:
        login=open("loginInfo.txt","r") #reading from a file
        students=login.readlines()
        for entry in students:
          if name in entry:
            nameCheck=True #verifies that the student is part of the quiz. As most of the admin options involve searching for a student, this applies to all of those options, so the code does not need to be repeated in the other options
        if nameCheck==True and choice=="6":
          print("This student is already part of the quiz\n")
          login.close() #this is an exception as option 6 involves adding a student, so the student can't already be in the list
        elif nameCheck==False and choice!="6":
          print("This student is not registered in this quiz\n") #factors out erroneous inputs
          login.close() 
        elif nameCheck==True:
          tierAndStrugglesPosition() #the tier list and struggle position finder, as well as the leaderboard position finder, can be used by the teacher as well as students
          leaderboardPosition()
          login.close()

        
    if choice=="1":
      if nameCheck==True:
        struggles=open("studentStruggles.txt","r") #reading from a file
        students=struggles.readlines()
        if "perimeters" not in students[tierStrugglePos] and "areas" not in students[tierStrugglePos] and "Pythagoras" not in students[tierStrugglePos] and "sohcahtoa" not in students[tierStrugglePos] and "circles" not in students[tierStrugglePos]: #tierStrugglePos being used to skip another sequential search
          print("\n" + name + " is not struggling with anything at the moment\n")
        else:
          print(name + " is currently struggling with:\n")
          if "perimeters" in students[tierStrugglePos]:
            print("Perimeters\n")
          if "areas" in students[tierStrugglePos]:
            print("Areas\n")
          if "Pythagoras" in students[tierStrugglePos]:
            print("Pythagoras\n")
          if "sohcahtoa" in students[tierStrugglePos]:
            print("Sohcahtoa\n")
          if "circles" in students[tierStrugglePos]:
            print("Circles\n")
        struggles.close()
          
    elif choice=="2" or choice=="3":
      if nameCheck==True:
        leaderboard=open("leaderboard.txt","r") #reading from a file
        scores=leaderboard.readlines()
        if choice=="2":
          for entry in scores:
            print(entry)
          print("\n" + name + " is currently at position " + str(leaderboardPos) + " on the leaderboard with a score of " + leaderboardNum + "\n") #leaderboardPos being used to skip another sequential search through the leaderboard file
          leaderboard.close()
        elif choice=="3":
          scores[realLeaderboardPos]=scores[realLeaderboardPos].strip("\n")
          scores[realLeaderboardPos]=name+"="+"0"+"\n"
          leaderboard.close()
          leaderboard=open("leaderboard.txt","w")
          leaderboard.writelines(scores) #altering the contents of a file / writing to a file
          leaderboard.close()
          leaderboardFix() #a change to the leaderboard has been made so it needs to be readjusted
          print("\n" + name + "'s score has been reset to 0\n")
          
    elif choice=="4" or choice=="5":
      if nameCheck==True:
        tierAssignment()
        if choice=="4":
          print(name + " is currently at tier " + tier)
        elif choice=="5":
          studentTiers=open("studentTiers.txt","r") #reading from a file
          tiers=studentTiers.readlines()
          tiers[tierStrugglePos]=tiers[tierStrugglePos].strip("\n") #tierStrugglePos being used to skip a sequential search
          tiers[tierStrugglePos]=name + "=" + "1" + "\n"
          studentTiers.close()
          studentTiers=open("studentTiers.txt","w")
          studentTiers.writelines(tiers) #altering the contents of a file / writing to a file
          studentTiers.close()
          print("\n" + name + "'s tier has been reset to one\n")
          
    elif choice=="6":
      if nameCheck==False:
        nameCheck2=False
        while nameCheck2==False:
          nonLetterCount=0
          for i in name:
            if i not in capitals and i not in lowerLetters:
              nonLetterCount=nonLetterCount+1
          if nonLetterCount>0:
            name=input("This is not a valid name, please re enter the student's name \n ")
          else:
            nameCheck2=True
        loopCount=0
        length=0
        capCount=0
        specialCount=0
        numCount=0
        passwordFlag=True
        while passwordFlag==True:
          if loopCount==0:
            newPassword=input("What will this student's password be? It must be at least 8 characters long and contain at least one capital letter, one special character and one number \n") 
          elif loopCount>0:
            newPassword=input("Re enter the student's password \n")
          length=len(newPassword)
          for i in newPassword:
            if i in capitals:
              capCount=capCount+1
            if i in str(basic):
              numCount=numCount+1
            if i in symbols:
              specialCount=specialCount+1
          if length<8:
            print("Password must be 8 characters or longer")
          if capCount==0:
            print("Password must contain at least one capital letter")
          if numCount==0:
            print("Password must contain at least one number")
          if specialCount==0:
            print("Password must contain at least one special character")
          if length>=8 and capCount!=0 and numCount!=0 and specialCount!=0:
            loopCount=0
            break
          capCount=0
          numCount=0
          specialCount=0
          loopCount=loopCount+1
        login=open("loginInfo.txt","a") #reading from multiple files / writing to multiple files
        login.write(name + "\n")
        login.write(newPassword+"\n")
        login.close()
        leaderboard=open("leaderboard.txt","a") #as a new student is being added, they must be added to all the other files too
        leaderboard.write(name + "=0" + "\n")
        leaderboard.close()
        struggles=open("studentStruggles.txt","a")
        struggles.write(name + "=" + "\n")
        struggles.close()
        tiers=open("studentTiers.txt","a")
        tiers.write(name + "=1" + "\n")
        tiers.close()
        print("\n" + name + " has been added to the quiz" + "\n")

    elif choice=="7":
      if nameCheck==True:
        position=0
        studentCount=0
        login=open("loginInfo.txt","r+") #reading from multiple files / writing to multiple files
        students=login.readlines()
        for entry in students:
          if name in entry:
            position=studentCount
            del students[position]
            del students[position] #As the positions have now shifted, this deletes that student's password
          studentCount=studentCount+1
        login.close()
        login=open("loginInfo.txt","w")
        login.writelines(students)
        login.close()
        leaderboard=open("leaderboard.txt","r+")
        scores=leaderboard.readlines()
        del scores[realLeaderboardPos]
        leaderboard.close()
        leaderboard=open("leaderboard.txt","w")
        leaderboard.writelines(scores)
        leaderboard.close()
        struggles=open("studentStruggles.txt","r+")
        students=struggles.readlines()
        del students[tierStrugglePos]
        struggles.close()
        struggles=open("studentStruggles.txt","w")
        struggles.writelines(students)
        struggles.close()
        studentTiers=open("studentTiers.txt","r+")
        tiers=studentTiers.readlines()
        del tiers[tierStrugglePos]
        studentTiers.close()
        studentTiers=open("studentTiers.txt","w")
        studentTiers.writelines(tiers)
        studentTiers.close()
        print("\n" + name + " has been removed from the quiz\n")

    elif choice=="8":
      teacherFlag=False
      loginFunc()

    elif choice=="9":
      print("Goodbye")
      quit()
      
    else:
      print("Please choose an option from 1-9 \n") #factors out erroneous inputs


##############################################################################################################################################################

#general quiz functions. These functions are used across all quizzes. They cover important parts of the quizzes such as answering questions, re taking incorrect questions, and requesting examples. The functions for altering users tiers, the topics they struggle with and their leaderboard entries are also here

#Where the user enters their answers to the generated questions. As well as checking for the right answer, it also checks for the appropriate units

def answers(currentTierQs,currentTierTopic,quizTier):
  count=0
  points=0
  incorrectQs={} #dictionary
  for i in currentTierQs:
    userAns = input(currentTierQs[count][0])
    if userAns=="menu":
      menu()
    elif currentTierQs[count][1]=="true" or currentTierQs[count][1]=="false" or currentTierQs[count][1]=="A" or currentTierQs[count][1]=="B" or currentTierQs[count][1]=="C" or currentTierQs[count][1]=="D":
      if userAns == str(currentTierQs[count][1]):
        print("Correct, one point\n")
        points = points + 1
      else:
        print("Incorrect\n")
        incorrectQs[str(currentTierQs[count][0])] = str(currentTierQs[count][1])
        
    elif "Calculate the area" in currentTierQs[count][0]:
      if userAns == str(currentTierQs[count][1]) + "cm2" or userAns == str(currentTierQs[count][1]) + " cm2":
        print("Correct, one point\n")
        points = points + 1
      else:
        print("Incorrect\n")
        incorrectQs[str(currentTierQs[count][0])] = str(currentTierQs[count][1])

    elif quizTier==4:
      if userAns == str(currentTierQs[count][1]) or userAns == str(currentTierQs[count][1]) + " degrees":
        print("Correct, one point\n")
        points = points + 1
      else:
        print("Incorrect\n")
        incorrectQs[str(currentTierQs[count][0])] = str(currentTierQs[count][1])
    else:
      if userAns == str(currentTierQs[count][1]) + "cm" or userAns == str(currentTierQs[count][1]) + " cm":
        print("Correct, one point\n")
        points = points + 1
      else:
        print("Incorrect\n")
        incorrectQs[str(currentTierQs[count][0])] = str(currentTierQs[count][1])
    count=count+1
  incorrectQuiz(incorrectQs,points,quizTier) #these functions are always called next when the answer function finishes, so they are part of this function
  pointMessages(points,currentTierTopic,quizTier)
  

#incorrect questions quiz, where the user can have another attempt at their incorrect questions:

def incorrectQuiz(incorrectQs,points,quizTier): #the incorrect questions are stored in a dictionary, since they now don't need to be randomised
  if points < 10:
    print("Have another go at your incorrect questions\n")
    count=0
    incorrectPoints=0
    for i in incorrectQs:
      userAns = input(i)
      if userAns=="menu":
        menu()
      elif incorrectQs[i]=="true" or incorrectQs[i]=="false" or incorrectQs[i]=="A" or incorrectQs[i]=="B" or incorrectQs[i]=="C":
        if userAns == str(incorrectQs[i]):
          print("Correct, one point\n")
          incorrectPoints = incorrectPoints + 1
        else:
          print("Incorrect\n")
      elif "calculate the area" in incorrectQs[i]:
        if userAns == str(incorrectQs[i]) + "cm2" or userAns == str(incorrectQs[i]) + " cm2":
          print("Correct, one point\n")
          incorrectPoints = incorrectPoints + 1
        else:
          print("Incorrect\n")
      elif quizTier==4:
        if userAns == str(incorrectQs[i]) or userAns == str(incorrectQs[i]) + " degrees":
          print("Correct, one point\n")
          incorrectPoints = incorrectPoints + 1
        else:
          print("Incorrect\n")
      else:
        if userAns == str(incorrectQs[i]) + "cm" or userAns == str(incorrectQs[i]) + " cm":
          print("Correct, one point\n")
          incorrectPoints = incorrectPoints + 1
        else:
          print("Incorrect\n")
      count=count+1
    if incorrectPoints==len(incorrectQs):
      print("Well done, you got all your incorrect questions correct!\n")
    elif incorrectPoints==1:
      print("You scored " + str(incorrectPoints) + " more point. Remember, you can always look at some examples for questions to help\n")
    else:
      print("You scored " + str(incorrectPoints) + " more points. Remember, you can always look at some examples for questions to help\n")

#points messages, where the user discovers how many points they achieved. It's also where topics are added or removed from the struggling file, as well as where the user's tier is increased if they scored a perfect 10 

def pointMessages(points,currentTierTopic,quizTier):
  leaderboardAdd(points)
  print("\n")
  if points==1:  
    print("You achieved " + str(points) + " point on the first quiz, better luck next time.")
    strugglingPAAdd(currentTierTopic) 
    if tier==quizTier:
      print("Get a perfect 10 and you can advance to the next tier!")
  elif points < 5:  
    print("You achieved " + str(points) + " points on the first quiz, better luck next time.")
    strugglingPAAdd(currentTierTopic) 
    if tier==quizTier:
      print("Get a perfect 10 and you can advance to the next tier!")
  elif points == 10:
    print("Congratulations, you scored a perfect 10!")
    strugglingPARemove(currentTierTopic) #as the user has now scored a perfect 10, they can have the topic removed from their entry in the struggling file (if it was there)
    if quizTier==int(tier) and tier != "5": #if the user's tier is 5 there are no further quizzes so their tier cannot go any higher
      print("You can advance to the next tier!\n")
      tierIncrease(tier)
  elif points >= 5:
    print("Well done, you achieved " + str(points) + " points on the first quiz.")
    strugglingPARemove(currentTierTopic) #any score above 5 will also result in the topic being removed from a user's entry in the struggling file (if it was there)
    if tier==quizTier:
      print("Get a perfect 10 and you can advance to the next tier!")
  points=0
  print("\n")

#adding points to a user's total score in the leaderboard:

def leaderboardAdd(points):
  userScore=""
  leaderboard=open("leaderboard.txt","r+") #reading from a file
  scores=leaderboard.readlines()
  for i in scores[realLeaderboardPos]:
    if i in str(basic):
      userScore=userScore+i #takes the number part of the entry
  newScore=int(userScore)+points
  newScore=str(newScore)
  userScore=newScore
  scores[realLeaderboardPos]=name+"="+newScore+"\n" #altering a file/writing to a file
  leaderboard.close()
  leaderboard=open("leaderboard.txt","w")
  leaderboard.writelines(scores)
  leaderboard.close()
  leaderboardFix() #as the leaderboard always makes the necessary adjustments after having an entry changed, the leaderboardFix function is part of this one

#rearranging the leaderboard after the user's point total has been altered. This is also used in the teacher menu after they have reset a student's score to 0:
    
def leaderboardFix(): #natsort is used here to re arrange the file
  tempLeaderboard=[]
  userScore=""
  position=0
  leaderboard=open("leaderboard.txt","r+") #reading from a file
  scores=leaderboard.readlines()
  for entry in scores:
    for i in entry:
      if i in str(basic):
        userScore=userScore+i
    scores[position]=scores[position].replace(userScore,"") #the number part is taken out of the entry
    scores[position]=userScore+scores[position] #it is then placed at the front of the entry so the natsort will sort it by number instead of letter
    scores[position]=scores[position].strip("\n")
    tempLeaderboard.append(scores[position])
    userScore=""
    number=""
    position=position+1
  position=0
  number=""
  tempLeaderboard=natsorted(tempLeaderboard)
  tempLeaderboard.reverse() #as the natsort prints out the list in descending order, the list is reversed
  for entry in tempLeaderboard:
    for i in entry:
      if i in str(basic) or i=="0":
        number=number+i
    tempLeaderboard[position]=tempLeaderboard[position].replace(number,"") #as the numbers are currently at the front of the entry they are deleted and then placed at the back
    tempLeaderboard[position]=tempLeaderboard[position]+number 
    position=position+1
    number=""
  position=0
  for i in tempLeaderboard: 
    scores[position]=tempLeaderboard[position]+"\n" #the file entries are replaced with the updated scores
    position=position+1 
  leaderboard.close()
  leaderboard=open("leaderboard.txt","w")
  leaderboard.writelines(scores) #altering the contents of a file / writing to a file
  position=0


#Adding a topic to a user's entry in the struggles file

def strugglingPAAdd(currentTierTopic):
  studentStruggles=open("studentStruggles.txt","r+")
  struggles=studentStruggles.readlines()
  if currentTierTopic not in struggles[tierStrugglePos]: #tierStrugglePos variable used to skip another sequential search
    studentStruggles.close()
    studentStruggles=open("studentStruggles.txt","w")
    struggles[tierStrugglePos]=struggles[tierStrugglePos].strip("\n")
    struggles[tierStrugglePos]=struggles[tierStrugglePos] + currentTierTopic + "," + "\n"
    studentStruggles.writelines(struggles) #writing to a file
    studentStruggles.close()
  else:
    studentStruggles.close()


#Removing a topic from a user's entry in the struggles file

def strugglingPARemove(currentTierTopic):
  studentStruggles=open("studentStruggles.txt","r+") #reading from a file
  struggles=studentStruggles.readlines()
  if currentTierTopic in struggles[tierStrugglePos]: #tierStrugglePos variable used to skip another sequential search
    studentStruggles.close()
    studentStruggles=open("studentStruggles.txt","w")
    struggles[tierStrugglePos]=struggles[tierStrugglePos].replace((currentTierTopic + ","),"")
    studentStruggles.writelines(struggles) #writing to a file/altering the contents of a file
    studentStruggles.close()
  else:
    studentStruggles.close()

#increases a user's tier. This is done after they have achieved 10/10 on a quiz 


def tierIncrease(tier):
  studentTiers=open("studentTiers.txt","r")
  tiers=studentTiers.readlines()
  studentTiers.close()
  studentTiers=open("studentTiers.txt","w")
  newTier=int(tier)+1
  newTier=str(newTier)
  tiers[tierStrugglePos]=name + "=" + newTier +"\n" #tierStrugglePos variable used to skip another sequential search
  studentTiers.writelines(tiers)
  studentTiers.close()


#Explanations. The user is able to select which question they want explained, and the template that was generated in the quiz for that question will be outputted. This is also where the program will go if the user chooses to just see the examples for a tier:

def explanations(currentTierQs,currentTierEs):
  loopcount=0
  explanationsFlag = True
  count=0
  while explanationsFlag == True:
    if loopcount == 0:
      userExamplesChoice = input("Would you like to see some explanations of these questions?\n")
    elif loopcount > 0:
      userExamplesChoice = input("Would you like to see some more explanations?\n") #slight variation if the user has gone through the explanations more than once
    if userExamplesChoice == "yes":
      print("\n")
      for i in currentTierQs:
        print(currentTierQs[count][0])
        print("\n")
        count=count+1
      count=0
      userExampleNum = input("Which one would you like to see an explanation of? (1-10) \n")
      if userExampleNum=="menu":
        menu()
      elif userExampleNum not in str(basic) or userExampleNum=="0": #zero needs to be specified here as an invalid input, as 10 contains 0
        print("Please enter a number from 1-10") #factors out erroneous inputs
      elif userExampleNum in str(basic):
        userExampleNum = int(userExampleNum)
        listNum = userExampleNum - 1 #one is subtracted from the users request as the list entries start at 0
        print(currentTierEs[listNum])
        print("\n")
        loopcount = loopcount + 1
    elif userExamplesChoice == "no":
      print("\n")
      loopcount=0
      break
    elif userExamplesChoice=="menu":
      menu()
    elif userExamplesChoice != "yes" and userExamplesChoice != "no":
      print("Please enter either yes or no") #factors out erroneous inputs
      print("\n")

##############################################################################################################################################################


#Tier 1 and 2 quiz functions, which deals with the perimeters and areas of shapes. Mostly functions used to access the questions in the tier 1 and tier 2 files and replace the placeholders. The examples for the questions are also generated here. The questions vary between true or false questions and the user typing in the answer on their own. Which questions are true or false questions and whether the answer is true or false is random.

def tier12Quiz(tier1Qs,tier2Qs,tier1Es,tier2Es,quizTier,exampleCheck,random):
  listNums=[0,1,2,3,4,5,6,7,8,9] #one dimensional list - stores list positions
  Q12pos=0 #used to keep track of what entry of the file is being examined
  randomNum1=random.choice(listNums) #used to select what questions will be true or false questions. If this variable matches with a question's position in a file, that question is chosen to be a true or false question
  randomNum2=random.choice(listNums)
  while randomNum1==randomNum2:
    randomNum1=random.choice(listNums)
    randomNum2=random.choice(listNums)
  if quizTier==1:
    examplesOne=open("tier1Examples.txt","r+")
    questionsOne = open("tier1Questions.txt", "r+")
    examples=examplesOne.readlines()
    questions=questionsOne.readlines()
  elif quizTier==2:
    examplesTwo=open("tier2Examples.txt","r+") #reading from files
    questionsTwo = open("tier2Questions.txt", "r+")
    examples=examplesTwo.readlines()
    questions=questionsTwo.readlines()
  for i in questions:
    loopingPA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs,tier2Qs,tier1Es,tier2Es,listNums,quizTier,random)
    Q12pos=Q12pos+1
  if quizTier==1:
    examplesOne.close()
    questionsOne.close()
    currentTierQs=tier1Qs
    currentTierEs=tier1Es
    currentTierTopic="perimeters" #the topic of the current quiz is assigned here so that it can be easily removed from or added to a student's entry in the studentStruggles file
  elif quizTier==2:
    examplesTwo.close()
    questionsTwo.close()
    currentTierQs=tier2Qs
    currentTierEs=tier2Es
    currentTierTopic="areas"
  if exampleCheck==False: #if the user just requested to see examples, the answering part is not needed
    answers(currentTierQs,currentTierTopic,quizTier)
  explanations(currentTierQs,currentTierEs)


#Looks for the name of the shape in each question to determine what function should be used 

def loopingPA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs,tier2Qs,tier1Es,tier2Es,listNums,quizTier,random):
  if "square" in i: 
    squarePA(i,questions, examples, Q12pos,randomNum1,randomNum2, tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random)
  elif "isosceles" in i:
    isoscelesPA(i,questions, examples, Q12pos,randomNum1,randomNum2, tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random)
  elif "rectangle" in i:
    rectanglePA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random)
  elif "trapezium" in i:
    trapeziumPA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random)
  elif "scalene" in i:
    scalenePA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random)


#Decides what the answer to a true or false question will be and assigns them to the questions list

def trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random):
  TrueOrFalseAns=[] #one dimensional array - list used to randomly select between the right answer and the wrong answer. The one that is selected will determine whether the question is true or false
  TrueOrFalseAns.append(ans)
  TrueOrFalseAns.append(ans+(random.randint(1,10)))
  TrueOrFalseAns.append(ans-(random.randint(1,10)))
  tempAns=random.choice(TrueOrFalseAns)
  currentQuestion=currentQuestion.strip("\n")
  if quizTier==1:
    currentQuestion=currentQuestion + ". The answer to this is " + str(tempAns) + "cm. Is this true or false?" + "\n"
  elif quizTier==2:
    currentQuestion=currentQuestion + ". The answer to this is " + str(tempAns) + "cm2. Is this true or false?" + "\n"
  if tempAns==ans:
    currentTierQs[listPos][0]=currentQuestion
    currentTierQs[listPos][1]="true"
  elif tempAns!=ans:
    currentTierQs[listPos][0]=currentQuestion
    currentTierQs[listPos][1]="false"
  

#Deals with the questions and examples for square questions

def squarePA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random):  #this doubles up as the function for the perimeter and the area (tier 1 and tier 2)
  listPos=random.choice(listNums) #The random import is used to randomly select a number from a one dimensional list of list numbers. This number is then used to give a question and it's answer it's position in the two dimensional tier1Qs list
  listNums.remove(listPos)
  squareSide = random.choice(basic + teens) #The random import is also used here to randomly select a number from either the "basic" or "teens" one dimensional lists. This basic list covers 1-10 and the teens list covers 11-19
  squareQuestion=i
  squareQuestion = squareQuestion.replace("x", str(squareSide))
    #all the places in which the numbers go in the question are denoted with a unique character, allowing them to be easily replaced with a randomly selected number
  if quizTier==1:
    ans = squareSide * 4 #the answer is created from the randomly generated number
    currentQuestion=squareQuestion
    currentTierQs=tier1Qs #The current question and current questions list are converted into these variables. This allows the true or false function to be used across tier 1 and 2 on all questions
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier1Qs=currentTierQs
      squareExample=examples[Q12pos].replace("x",str(squareSide)) #Organised for sequential access - As both the examples and questions are in the same topic order in their files, the Q12pos variable (which keeps track of the questions positions in their file) can be used to immediately access the correct example template without having to sequentially search the file
      squareExample=squareExample.replace("/",str(ans))
      squareExample=squareExample.strip("\n")
      squareExample=squareExample + ". So it would be " + tier1Qs[listPos][1] + "\n"
      tier1Es[listPos]=squareExample
    else:
      tier1Qs[listPos][0]=squareQuestion
      tier1Qs[listPos][1]=ans
      squareExample=examples[Q12pos].replace("x",str(squareSide)) #the examples are also edited here
      squareExample=squareExample.replace("/",str(ans))
      tier1Es[listPos]=squareExample
  elif quizTier==2:
    ans = squareSide**2
    currentQuestion=squareQuestion
    currentTierQs=tier2Qs 
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier2Qs=currentTierQs
      squareExample=examples[Q12pos].replace("x",str(squareSide))
      squareExample=squareExample.replace("/",str(ans))
      squareExample=squareExample.strip("\n") 
      squareExample=squareExample + ". So it would be " + tier2Qs[listPos][1] + "\n"
      tier2Es[listPos]=squareExample
    else:
      tier2Qs[listPos][0]=squareQuestion
      tier2Qs[listPos][1]=ans
      squareExample=examples[Q12pos].replace("x",str(squareSide))
      squareExample=squareExample.replace("/",str(ans))
      tier2Es[listPos]=squareExample

#Deals with the questions and examples for isosceles questions

def isoscelesPA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random):
  listPos=random.choice(listNums)
  listNums.remove(listPos)
  isoscelesQuestion = i
  isoscelesBase = random.choice(basic + teens)
  isoscelesSides23 = random.choice(basic + teens)
  while isoscelesBase==isoscelesSides23: #as the base and the sides of an isosceles cannot be the same, this assignment is repeated until they are different. This is used in any event in which two assignments cannot be the same
    isoscelesBase = random.choice(basic + teens)
    isoscelesSides23 = random.choice(basic + teens)
  isoscelesHeight = random.choice(teens)
  isoscelesQuestion = isoscelesQuestion.replace("x", str(isoscelesHeight))
  isoscelesQuestion = isoscelesQuestion.replace("y", str(isoscelesBase))
  isoscelesQuestion = isoscelesQuestion.replace("z", str(isoscelesSides23))
  if quizTier==1:
    ans = (isoscelesSides23 * 2) + isoscelesBase
    currentQuestion=isoscelesQuestion
    currentTierQs=tier1Qs
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier1Qs=currentTierQs
      isoscelesExample=examples[Q12pos].replace("y",str(isoscelesBase))
      isoscelesExample=examples[Q12pos].replace("z",str(isoscelesSides23))
      isoscelesExample=isoscelesExample.replace("/",str(ans))
      isoscelesExample=isoscelesExample.strip("\n") 
      isoscelesExample=isoscelesExample + ". So it would be " + tier1Qs[listPos][1] + "\n"
      tier1Es[listPos]=isoscelesExample
    else:
      tier1Qs[listPos][0]=isoscelesQuestion
      tier1Qs[listPos][1]=ans
      isoscelesExample = examples[Q12pos].replace("y", str(isoscelesBase))
      isoscelesExample = isoscelesExample.replace("z", str(isoscelesSides23))
      isoscelesExample = isoscelesExample.replace("/", str(ans))
      tier1Es[listPos]=isoscelesExample
  elif quizTier==2:
    ans = (isoscelesBase * isoscelesHeight) / 2
    ans = round(ans, 1)
    currentQuestion=isoscelesQuestion
    currentTierQs=tier2Qs
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier2Qs=currentTierQs
      isoscelesExample=examples[Q12pos].replace("^",str(isoscelesBase))
      isoscelesExample=isoscelesExample.replace("x",str(isoscelesSides23))
      isoscelesExample=isoscelesExample.replace("/",str(ans))
      isoscelesExample=isoscelesExample.strip("\n") 
      isoscelesExample=isoscelesExample + ". So it would be " + tier2Qs[listPos][1] + "\n"
      tier2Es[listPos]=isoscelesExample
    else:
      tier2Qs[listPos][0]=isoscelesQuestion
      tier2Qs[listPos][1]=ans
      isoscelesExample=examples[Q12pos].replace("^",str(isoscelesBase))
      isoscelesExample=isoscelesExample.replace("x",str(isoscelesSides23))
      isoscelesExample=isoscelesExample.replace("/",str(ans))
      tier2Es[listPos]=isoscelesExample

    

#Deals with the questions and examples for rectangle questions

def rectanglePA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random):
  listPos=random.choice(listNums)
  listNums.remove(listPos)
  rectangleQuestion = i
  rectangleBase = random.choice(basic + teens)
  rectangleHeight = random.choice(basic + teens)
  while rectangleBase>=rectangleHeight:
    rectangleBase = random.choice(basic + teens)
    rectangleHeight = random.choice(basic + teens)
  rectangleQuestion = rectangleQuestion.replace("x", str(rectangleBase))
  rectangleQuestion = rectangleQuestion.replace("y", str(rectangleHeight))
  if quizTier==1:
    ans = (rectangleBase * 2) + (rectangleHeight * 2)
    currentQuestion=rectangleQuestion
    currentTierQs=tier1Qs
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier1Qs=currentTierQs
      rectangleExample=examples[Q12pos].replace("x",str(rectangleBase))
      rectangleExample = rectangleExample.replace("y", str(rectangleHeight))
      rectangleExample = rectangleExample.replace("/", str(ans))
      rectangleExample=rectangleExample.strip("\n")
      rectangleExample=rectangleExample + ". So it would be " + tier1Qs[listPos][1] + "\n"
      tier1Es[listPos]=rectangleExample
    else:
      tier1Qs[listPos][0]=rectangleQuestion
      tier1Qs[listPos][1]=ans
      rectangleExample = examples[Q12pos].replace("x", str(rectangleBase))
      rectangleExample = rectangleExample.replace("y", str(rectangleHeight))
      rectangleExample = rectangleExample.replace("/", str(ans))
      tier1Es[listPos]=rectangleExample
  elif quizTier==2:
    ans = rectangleBase * rectangleHeight
    currentQuestion=rectangleQuestion
    currentTierQs=tier2Qs
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier2Qs=currentTierQs
      rectangleExample=examples[Q12pos].replace("x",str(rectangleBase))
      rectangleExample = rectangleExample.replace("^", str(rectangleHeight))
      rectangleExample = rectangleExample.replace("/", str(ans))
      rectangleExample=rectangleExample.strip("\n") 
      rectangleExample=rectangleExample + ". So it would be " + tier2Qs[listPos][1] + "\n"
      tier2Es[listPos]=rectangleExample
    else:
      tier2Qs[listPos][0]=rectangleQuestion
      tier2Qs[listPos][1]=ans
      rectangleExample = examples[Q12pos].replace("x", str(rectangleBase))
      rectangleExample = rectangleExample.replace("^", str(rectangleHeight))
      rectangleExample = rectangleExample.replace("/", str(ans))
      tier2Es[listPos]=rectangleExample

#Deals with the questions and examples for trapezium questions

def trapeziumPA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random):
  listPos=random.choice(listNums)
  listNums.remove(listPos)
  trapeziumQuestion = i
  trapeziumHeight = random.choice(teens)
  trapeziumBase1 = random.choice(basic)
  trapeziumBase2 = random.choice(teens)
  trapeziumSides1 = random.choice(teens)
  trapeziumSides2 = random.choice(teens)
  while trapeziumBase2==trapeziumSides1 or trapeziumBase2==trapeziumSides2 or trapeziumSides1==trapeziumSides2:
    trapeziumBase2 = random.choice(teens)
    trapeziumSides1 = random.choice(teens)
    trapeziumSides2 = random.choice(teens)
  trapeziumQuestion = trapeziumQuestion.replace("x", str(trapeziumHeight))
  trapeziumQuestion = trapeziumQuestion.replace("y", str(trapeziumBase1))
  trapeziumQuestion = trapeziumQuestion.replace("k", str(trapeziumBase2))
  trapeziumQuestion = trapeziumQuestion.replace("?", str(trapeziumSides1))
  trapeziumQuestion = trapeziumQuestion.replace("!", str(trapeziumSides2))
  if quizTier==1:
    ans = trapeziumBase1 + trapeziumBase2 + trapeziumSides1 + trapeziumSides2
    currentQuestion=trapeziumQuestion
    currentTierQs=tier1Qs
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier1Qs=currentTierQs
      trapeziumExample = examples[Q12pos].replace("y", str(trapeziumBase1))
      trapeziumExample = trapeziumExample.replace("k", str(trapeziumBase2))
      trapeziumExample = trapeziumExample.replace("?", str(trapeziumSides1))
      trapeziumExample = trapeziumExample.replace("!", str(trapeziumSides2))
      trapeziumExample = trapeziumExample.replace("/", str(ans))
      trapeziumExample=trapeziumExample.strip("\n") 
      trapeziumExample=trapeziumExample + ". So it would be " + tier1Qs[listPos][1] + "\n"
      tier1Es[listPos]=trapeziumExample
    else:
      tier1Qs[listPos][0]=trapeziumQuestion
      tier1Qs[listPos][1]=ans
      trapeziumExample = examples[Q12pos].replace("y", str(trapeziumBase1))
      trapeziumExample = trapeziumExample.replace("k", str(trapeziumBase2))
      trapeziumExample = trapeziumExample.replace("?", str(trapeziumSides1))
      trapeziumExample = trapeziumExample.replace("!", str(trapeziumSides2))
      trapeziumExample = trapeziumExample.replace("/", str(ans))
      tier1Es[listPos]=trapeziumExample
  if quizTier==2:
    ans = ((trapeziumBase1 + trapeziumBase2) / 2) * trapeziumHeight
    ans = round(ans, 1)
    currentQuestion=trapeziumQuestion
    currentTierQs=tier2Qs
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier2Qs=currentTierQs
      trapeziumExample = examples[Q12pos].replace("^", str(trapeziumBase1))
      trapeziumExample = trapeziumExample.replace("k", str(trapeziumBase2))
      trapeziumExample = trapeziumExample.replace("x", str(trapeziumHeight))
      trapeziumExample = trapeziumExample.replace("/", str(ans))
      trapeziumExample=trapeziumExample.strip("\n") 
      trapeziumExample=trapeziumExample + ". So it would be " + tier2Qs[listPos][1] + "\n"
      tier2Es[listPos]=trapeziumExample
    else:
      tier2Qs[listPos][0]=trapeziumQuestion
      tier2Qs[listPos][1]=ans
      trapeziumExample = examples[Q12pos].replace("^", str(trapeziumBase1))
      trapeziumExample = trapeziumExample.replace("k", str(trapeziumBase2))
      trapeziumExample = trapeziumExample.replace("x", str(trapeziumHeight))
      trapeziumExample = trapeziumExample.replace("/", str(ans))
      tier2Es[listPos]=trapeziumExample

#Deals with the questions and examples for scalene questions


def scalenePA(i,questions, examples, Q12pos,randomNum1,randomNum2,tier1Qs, tier2Qs, tier1Es, tier2Es,listNums,quizTier,random):
  listPos=random.choice(listNums)
  listNums.remove(listPos)
  scaleneQuestion=i
  scaleneHeight = random.choice(teens)
  scaleneBase = random.choice(teens)
  scaleneSide1 = random.choice(basic)  
  scaleneSide2 = random.choice(basic)
  while scaleneSide1==scaleneSide2 or scaleneSide1==scaleneBase or scaleneBase==scaleneSide2 or scaleneHeight<scaleneBase or scaleneHeight<scaleneSide1 or scaleneHeight<scaleneSide2:
    scaleneHeight=random.choice(teens)
    scaleneBase=random.choice(basic + teens)
    scaleneSide1=random.choice(basic + teens)
    scaleneSide2=random.choice(basic + teens)
  scaleneQuestion = scaleneQuestion.replace("x", str(scaleneHeight))
  scaleneQuestion = scaleneQuestion.replace("y", str(scaleneBase))
  scaleneQuestion = scaleneQuestion.replace("z", str(scaleneSide1))
  scaleneQuestion = scaleneQuestion.replace("k", str(scaleneSide2))
  if quizTier==1:
    ans = scaleneBase + scaleneSide1 + scaleneSide2
    currentQuestion=scaleneQuestion
    currentTierQs=tier1Qs
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier1Qs=currentTierQs
      scaleneExample = examples[Q12pos].replace("y", str(scaleneBase))
      scaleneExample = scaleneExample.replace("z", str(scaleneSide1))
      scaleneExample = scaleneExample.replace("k", str(scaleneSide2))
      scaleneExample = scaleneExample.replace("/", str(ans))
      scaleneExample=scaleneExample.strip("\n") 
      scaleneExample=scaleneExample + ". So it would be " + tier1Qs[listPos][1] + "\n"
      tier1Es[listPos]=scaleneExample
    else:
      tier1Qs[listPos][0]=scaleneQuestion
      tier1Qs[listPos][1]=ans
      scaleneExample = examples[Q12pos].replace("y", str(scaleneBase))
      scaleneExample = scaleneExample.replace("z", str(scaleneSide1))
      scaleneExample = scaleneExample.replace("k", str(scaleneSide2))
      scaleneExample = scaleneExample.replace("/", str(ans))
      tier1Es[listPos]=scaleneExample
  elif quizTier==2:
    ans = (scaleneBase * scaleneHeight) / 2
    currentQuestion=scaleneQuestion
    currentTierQs=tier2Qs
    if Q12pos==randomNum1 or Q12pos==randomNum2:
      trueOrFalse(currentQuestion,currentTierQs,ans,listPos,quizTier,random)
      tier2Qs=currentTierQs
      scaleneExample=examples[Q12pos].replace("^",str(scaleneBase))
      scaleneExample=scaleneExample.replace("x",str(scaleneHeight))
      scaleneExample=scaleneExample.replace("/", str(ans))
      scaleneExample=scaleneExample.strip("\n") 
      scaleneExample=scaleneExample + ". So it would be " + tier2Qs[listPos][1] + "\n"
      tier2Es[listPos]=scaleneExample
    else:
      tier2Qs[listPos][0]=scaleneQuestion
      tier2Qs[listPos][1]=ans
      scaleneExample=examples[Q12pos].replace("^",str(scaleneBase))
      scaleneExample=scaleneExample.replace("x",str(scaleneHeight))
      scaleneExample=scaleneExample.replace("/", str(ans))
      tier2Es[listPos]=scaleneExample

##############################################################################################################################################################

#Tier 3 and 4 quiz functions, which deals with Pythagoras and finding the size of angles using sohcahtoa. This is mostly functions used to access the questions in the tier 3 and tier 4 files and replace the placeholders. The examples for the questions are also generated here. The questions vary between multiple choice questions and the user typing in the answer on their own. Which questions are multiple choice questions and what option is the correct one is random.

def tier34Quiz(tier3Qs, tier3Es, tier4Qs, tier4Es,quizTier, exampleCheck,random,math):
  randomNum1=random.randint(0,9) #random numbers are generated for the position of the multiple choice questions so they are in a different place each time the quiz is run
  randomNum2=random.randint(0,9)
  while randomNum1==randomNum2:
    randomNum1=random.randint(0,9)
    randomNum2=random.randint(0,9)
  Q34pos=0
  pi=math.pi #Use of math import
  pi=round(pi,3)
  listNums=[0,1,2,3,4,5,6,7,8,9]
  if quizTier==3:
    examplesThree = open("tier3Examples.txt", "r")
    questionsThree = open("tier3Questions.txt", "r+")
    examples=examplesThree.readlines()
    questions=questionsThree.readlines()
  if quizTier==4:
    examplesFour = open("tier4Examples.txt", "r")
    questionsFour = open("tier4Questions.txt", "r+")
    examples=examplesFour.readlines()
    questions=questionsFour.readlines()
  for i in questions:  
    loopingPS(i,Q34pos,questions,examples,randomNum1,randomNum2, tier3Qs, tier3Es, tier4Qs, tier4Es,listNums,quizTier,pi,random,math)
    Q34pos=Q34pos+1
  if quizTier==3:
    examplesThree.close()
    questionsThree.close()
    currentTierQs=tier3Qs
    currentTierEs=tier3Es
    currentTierTopic="Pythagoras"
  elif quizTier==4:
    examplesFour.close()
    questionsFour.close()
    currentTierQs=tier4Qs
    currentTierEs=tier4Es
    currentTierTopic="sohcahtoa"
  if exampleCheck==False:
    answers(currentTierQs,currentTierTopic,quizTier)
  explanations(currentTierQs,currentTierEs)

#As the differences in the questions are more subtle for this quiz, the entry positions are used to tell which functions should be used

def loopingPS(i,Q34pos,questions,examples,randomNum1,randomNum2, tier3Qs, tier3Es, tier4Qs, tier4Es,listNums,quizTier,pi,random,math):
  if Q34pos==0 or Q34pos==1 or Q34pos==2:
    hypotCalc(Q34pos,questions,examples,randomNum1, randomNum2, tier3Qs, tier3Es, tier4Qs, tier4Es,listNums,quizTier,pi,random,math)
  elif Q34pos==3 or Q34pos==4 or Q34pos==5:
    side1Calc(Q34pos,questions,examples,randomNum1,randomNum2, tier3Qs, tier3Es, tier4Qs, tier4Es,listNums,quizTier,pi,random,math)
  elif Q34pos==6 or Q34pos==7 or Q34pos==8 or Q34pos==9:
    side2Calc(Q34pos,questions,examples,randomNum1,randomNum2, tier3Qs, tier3Es, tier4Qs, tier4Es,listNums,quizTier,pi,random,math)

#Determines the answer to a multiple choice question and assigns this to the two dimensional questions list

def multipleChoice(currentQuestion, currentTierQs, ans, listPos,quizTier,random):
  multipleChoiceAns=[] #one dimensional list - similar to TrueOrFalseAns. Takes four variations of the answer. The answer is then randomly allocated to one of the letters and this letter is added to the questions list as the answer for the question
  multipleChoiceAns.append(ans)
  multipleChoiceAns.append(round(ans*random.randint(2,5),1))
  multipleChoiceAns.append(round(ans*random.randint(6,10),1))
  multipleChoiceAns.append(round(ans/random.randint(2,5),1))
  A=random.choice(multipleChoiceAns)
  multipleChoiceAns.remove(A)
  B=random.choice(multipleChoiceAns)
  multipleChoiceAns.remove(B)
  C=random.choice(multipleChoiceAns)
  multipleChoiceAns.remove(C)
  D=random.choice(multipleChoiceAns)
  currentQuestion=currentQuestion.strip("\n")
  if "Calculate the area" in currentQuestion: #ensuring the correct units are used
    currentQuestion=currentQuestion + ". Which one of these letters corresponds to the correct answer?: A.) " + str(A) + "cm2 / B.) " + str(B) + "cm2 / C.) " + str(C) + "cm2 / D.) " + str(D) + "cm2 \n"
  elif quizTier==3 or quizTier==5:
    currentQuestion=currentQuestion + ". Which one of these letters corresponds to the correct answer?: A.) " + str(A) + "cm / B.) " + str(B) + "cm / C.) " + str(C) + "cm / D.) " + str(D) + "cm \n"
  elif quizTier==4:
    currentQuestion=currentQuestion + ". Which one of these letters corresponds to the correct answer?: A.) " + str(A) + " / B.) " + str(B) + " / C.) " + str(C) + " / D.) " + str(D) + " \n"
  currentTierQs[listPos][0]=currentQuestion
  if A==ans:
    currentTierQs[listPos][1]="A"
  elif B==ans:
    currentTierQs[listPos][1]="B"
  elif C==ans:
    currentTierQs[listPos][1]="C"
  elif D==ans:
    currentTierQs[listPos][1]="D"

    
#Used for calculations in which side 1 and side 2 are given

def hypotCalc(Q34pos,questions,examples,randomNum1,randomNum2,tier3Qs, tier3Es, tier4Qs, tier4Es, listNums,quizTier,pi,random,math):
  listPos=random.choice(listNums)
  listNums.remove(listPos)
  side1=random.choice(twenties + thirties)
  side2=random.choice(twenties + thirties)
  if quizTier==3:
    ans=math.sqrt(side1**2 + side2**2) #maths calculations - the square root is calculated using the imported math function
    ans=round(ans,1)
    hypotQuestion=questions[Q34pos].replace("!",str(side1))
    hypotQuestion=hypotQuestion.replace("£",str(side2))
    currentQuestion=hypotQuestion
    currentTierQs=tier3Qs
    if Q34pos==randomNum1 or Q34pos==randomNum2:
      multipleChoice(currentQuestion, currentTierQs, ans, listPos,quizTier,random)
      tier3Qs=currentTierQs
      hypotExample=examples[Q34pos].replace("!",str(side1))
      hypotExample=hypotExample.replace("£",str(side2))
      hypotExample=hypotExample.replace("/",str(ans))
      hypotExample=hypotExample.strip("\n")
      hypotExample=hypotExample + ". So it would be " + tier3Qs[listPos][1] + "\n"
      tier3Es[listPos]=hypotExample
    else:
      tier3Qs[listPos][0]=hypotQuestion
      tier3Qs[listPos][1]=ans
      hypotExample=examples[Q34pos].replace("!",str(side1))
      hypotExample=hypotExample.replace("£",str(side2))
      hypotExample=hypotExample.replace("/",str(ans))
      tier3Es[listPos]=hypotExample
  if quizTier==4:
    if "angle A" in questions[Q34pos]:
      ans=((math.atan(side2/side1))*(180/pi)) #maths calculations
      ans=round(ans,1)
    elif "angle B" in questions[Q34pos]:
      ans=((math.atan(side1/side2))*(180/pi))
      ans=round(ans,1)
    side1BaseQuestion=questions[Q34pos].replace("!",str(side1))
    side1BaseQuestion=side1BaseQuestion.replace("£",str(side2))
    currentQuestion=side1BaseQuestion
    currentTierQs=tier4Qs
    if Q34pos==randomNum1 or Q34pos==randomNum2:
      multipleChoice(currentQuestion, currentTierQs, ans, listPos,quizTier,random)
      tier4Qs=currentTierQs
      side1BaseExample=examples[Q34pos].replace("!",str(side1))
      side1BaseExample=side1BaseExample.replace("£",str(side2))
      side1BaseExample=side1BaseExample.replace("/",str(ans))
      side1BaseExample=side1BaseExample.strip("\n")
      side1BaseExample=side1BaseExample + ". So it would be " + tier4Qs[listPos][1] + "\n"
      tier4Es[listPos]=side1BaseExample
    else:
      tier4Qs[listPos][0]=side1BaseQuestion
      tier4Qs[listPos][1]=ans
      side1BaseExample=examples[Q34pos].replace("!",str(side1))
      side1BaseExample=side1BaseExample.replace("£",str(side2))
      side1BaseExample=side1BaseExample.replace("/",str(ans))
      tier4Es[listPos]=side1BaseExample

#Used for calculations in which side 2 and the hypotenuse are given

def side1Calc(Q34pos,questions,examples,randomNum1,randomNum2,tier3Qs, tier3Es, tier4Qs, tier4Es, listNums,quizTier,pi,random,math):
  listPos=random.choice(listNums)
  listNums.remove(listPos)
  hypot=random.choice(twenties + thirties)
  side2=random.choice(twenties + thirties)
  while hypot<=side2:
    hypot=random.choice(twenties + thirties)
    side2=random.choice(twenties + thirties)
  if quizTier==3:
    ans=math.sqrt(hypot**2-side2**2) #maths calculations
    ans=round(ans,1)
    side1Question=questions[Q34pos].replace("!",str(hypot))
    side1Question=side1Question.replace("£",str(side2))
    currentQuestion=side1Question
    currentTierQs=tier3Qs
    if Q34pos==randomNum1 or Q34pos==randomNum2:
      multipleChoice(currentQuestion, currentTierQs, ans, listPos,quizTier,random)
      tier3Qs=currentTierQs
      side1Example=examples[Q34pos].replace("!",str(hypot))
      side1Example=side1Example.replace("£",str(side2))
      side1Example=side1Example.replace("/",str(ans))
      side1Example=side1Example.strip("\n")
      side1Example=side1Example + ". So it would be " + tier3Qs[listPos][1] + "\n"
      tier3Es[listPos]=side1Example
    else:
      tier3Qs[listPos][0]=side1Question
      tier3Qs[listPos][1]=ans
      side1Example=examples[Q34pos].replace("!",str(hypot))
      side1Example=side1Example.replace("£",str(side2))
      side1Example=side1Example.replace("/",str(ans))
      tier3Es[listPos]=side1Example
  elif quizTier==4:
    if "angle A" in questions[Q34pos]:
      ans=(math.asin(side2/hypot))*(180/pi)
      ans=round(ans,1)
    elif "angle B" in questions[Q34pos]:
      ans=(math.acos(side2/hypot))*(180/pi)
      ans=round(ans,1)
    side2HypotQuestion=questions[Q34pos].replace("!",str(hypot))
    side2HypotQuestion=side2HypotQuestion.replace("£",str(side2))
    currentQuestion=side2HypotQuestion
    currentTierQs=tier4Qs
    if Q34pos==randomNum1 or Q34pos==randomNum2:
      multipleChoice(currentQuestion, currentTierQs, ans, listPos,quizTier,random)
      tier4Qs=currentTierQs
      side2HypotExample=examples[Q34pos].replace("!",str(hypot))
      side2HypotExample=side2HypotExample.replace("£",str(side2))
      side2HypotExample=side2HypotExample.replace("/",str(ans))
      side2HypotExample=side2HypotExample.strip("\n")
      side2HypotExample=side2HypotExample + ". So it would be " + tier4Qs[listPos][1] + "\n"
      tier4Es[listPos]=side2HypotExample
    else:
      tier4Qs[listPos][0]=side2HypotQuestion
      tier4Qs[listPos][1]=ans
      side2HypotExample=examples[Q34pos].replace("!",str(hypot))
      side2HypotExample=side2HypotExample.replace("£",str(side2))
      side2HypotExample=side2HypotExample.replace("/",str(ans))
      tier4Es[listPos]=side2HypotExample

#Used for calculations in which side 1 and the hypotenuse are given

def side2Calc(Q34pos,questions,examples,randomNum1,randomNum2,tier3Qs, tier3Es, tier4Qs, tier4Es, listNums,quizTier,pi,random,math):
  listPos=random.choice(listNums)
  listNums.remove(listPos)
  hypot=random.choice(twenties + thirties)
  side1=random.choice(twenties + thirties)
  while hypot<=side1:
    hypot=random.choice(twenties + thirties)
    side1=random.choice(twenties + thirties)
  if quizTier==3:
    ans=math.sqrt(hypot**2-side1**2) #maths calculations
    ans=round(ans,1)
    side2Question=questions[Q34pos].replace("!",str(hypot))
    side2Question=side2Question.replace("£",str(side1))
    currentQuestion=side2Question
    currentTierQs=tier3Qs
    if Q34pos==randomNum1 or Q34pos==randomNum2:
      multipleChoice(currentQuestion, currentTierQs, ans, listPos,quizTier,random)
      tier3Qs=currentTierQs
      side2Example=examples[Q34pos].replace("!",str(hypot))
      side2Example=side2Example.replace("£",str(side1))
      side2Example=side2Example.replace("/",str(ans))
      side2Example=side2Example.strip("\n")
      side2Example=side2Example + ". So it would be " + tier3Qs[listPos][1] + "\n"
      tier3Es[listPos]=side2Example
    else:
      tier3Qs[listPos][0]=side2Question
      tier3Qs[listPos][1]=ans
      side2Example=examples[Q34pos].replace("!",str(hypot))
      side2Example=side2Example.replace("£",str(side1))
      side2Example=side2Example.replace("/",str(ans))
      tier3Es[listPos]=side2Example
  if quizTier==4:
    if "angle A" in questions[Q34pos]:
      ans=(math.acos(side1/hypot))*(180/pi) #maths calculations
      ans=round(ans,1)
    elif "angle B" in questions[Q34pos]:
      ans=(math.asin(side1/hypot))*(180/pi)
      ans=round(ans,1)
    side1HypotQuestion=questions[Q34pos].replace("!",str(hypot))
    side1HypotQuestion=side1HypotQuestion.replace("£",str(side1))
    currentQuestion=side1HypotQuestion
    currentTierQs=tier4Qs
    if Q34pos==randomNum1 or Q34pos==randomNum2:
      multipleChoice(currentQuestion, currentTierQs, ans, listPos,quizTier,random)
      tier4Qs=currentTierQs
      side1HypotExample=examples[Q34pos].replace("!",str(hypot))
      side1HypotExample=side1HypotExample.replace("£",str(side1))
      side1HypotExample=side1HypotExample.replace("/",str(ans))
      side1HypotExample=side1HypotExample.strip("\n")
      side1HypotExample=side1HypotExample + ". So it would be " + tier4Qs[listPos][1] + "\n"
      tier4Es[listPos]=side1HypotExample
    else:
      tier4Qs[listPos][0]=side1HypotQuestion
      tier4Qs[listPos][1]=ans
      side1HypotExample=examples[Q34pos].replace("!",str(hypot))
      side1HypotExample=side1HypotExample.replace("£",str(side1))
      side1HypotExample=side1HypotExample.replace("/",str(ans))
      tier4Es[listPos]=side1HypotExample

##############################################################################################################################################################

#Tier 5 quiz functions, which deals with circle calculations. This is mostly functions used to access the questions in the tier 5 file and replace the placeholders. The examples for the questions are also generated here. The questions vary between multiple choice questions and the user typing in the answer on their own (so the multiple choice function is also used here). Which questions are multiple choice questions and what option is the correct one are both random.

def tier5Quiz(tier5Qs, tier5Es,quizTier, exampleCheck,random,math):
  randomNum1=random.randint(0,9)
  randomNum2=random.randint(0,9)
  while randomNum1==randomNum2:
    randomNum1=random.randint(0,9)
    randomNum2=random.randint(0,9)
  Q5pos=0
  listNums=[0,1,2,3,4,5,6,7,8,9]
  questionsFive=open("tier5Questions.txt","r+")
  examplesFive=open("tier5Examples.txt","r+")
  questions=questionsFive.readlines()
  examples=examplesFive.readlines()
  for i in questions:
    loopingC(i,Q5pos,questions,examples,randomNum1,randomNum2,listNums,tier5Qs,tier5Es,quizTier,random,math)
    Q5pos=Q5pos+1
  questionsFive.close()
  examplesFive.close()
  currentTierQs=tier5Qs
  currentTierEs=tier5Es
  currentTierTopic="circles"
  if exampleCheck==False:
    answers(currentTierQs,currentTierTopic,quizTier)
  explanations(currentTierQs,currentTierEs)

#As the questions all use the same variables, there is no need to differentiate them at this stage

def loopingC(i,Q5pos,questions,examples,randomNum1,randomNum2,listNums,tier5Qs,tier5Es,quizTier,random,math):
  radius=random.choice(forties + fifties)
  theta=random.randint(180, 360)
  circ=random.choice(forties + fifties)
  circleCalc(i,Q5pos,questions,examples,randomNum1,randomNum2,theta,radius,circ,listNums,tier5Qs,tier5Es,quizTier,random,math)


#Used to generate questions and examples for questions about the area, diameter, circumference, and radius of a circle

def circleCalc(i,Q5pos,questions,examples,randomNum1,randomNum2,theta,radius,circ,listNums,tier5Qs,tier5Es,quizTier,random,math):
  pi=math.pi
  pi=round(pi,3) #use of maths import
  listPos=random.choice(listNums)
  listNums.remove(listPos)
  if Q5pos!=6 and Q5pos!=7 and Q5pos!=8 and Q5pos!=9:
    circleQuestion=questions[Q5pos].replace("!",str(theta))
    circleQuestion=circleQuestion.replace("£",str(radius))
  else:
    circleQuestion=questions[Q5pos].replace("!",str(theta))
    circleQuestion=circleQuestion.replace("£",str(circ))
  if Q5pos==0 or Q5pos==1:
    ans=(theta/360)*(pi)*(radius**2) #maths calculation
    ans=round(ans,1)
    circleExample=examples[listPos].replace("!",str(theta))
    circleExample=circleExample.replace("£",str(radius))
    circleExample=circleExample.replace("@",str(ans))
  elif Q5pos==2 or Q5pos==3:
    ans=(theta/360)*2*(radius) #maths calculation
    ans=round(ans,1)
    circleExample=examples[listPos].replace("!",str(theta))
    circleExample=circleExample.replace("£",str(radius))
    circleExample=circleExample.replace("@",str(ans))
  elif Q5pos==4 or Q5pos==5:
    ans=(theta/360)*(2)*(pi)*(radius) #maths calculation
    ans=round(ans,1)
    circleExample=examples[listPos].replace("!",str(theta))
    circleExample=circleExample.replace("£",str(radius))
    circleExample=circleExample.replace("@",str(ans))
  else:
    ans=(theta/360)*(circ/(2*pi)) #maths calculation
    ans=round(ans,1)
    circleExample=examples[listPos].replace("!",str(theta))
    circleExample=circleExample.replace("£",str(radius))
    circleExample=circleExample.replace("@",str(ans))
  currentQuestion=circleQuestion
  currentTierQs=tier5Qs
  if Q5pos==randomNum1 or Q5pos==randomNum2:
    multipleChoice(currentQuestion, currentTierQs, ans, listPos,quizTier,random)
    tier5Qs=currentTierQs
    circleExample=circleExample.strip("\n")
    circleExample=circleExample + ". So the answer to this is " + tier5Qs[listPos][1]
    tier5Es[listPos]=circleExample
  else:
    tier5Qs[listPos][0]=circleQuestion
    tier5Qs[listPos][1]=ans
    tier5Es[listPos]=circleExample
    
  
##############################################################################################################################################################
  
#main program
    
loginFunc()
