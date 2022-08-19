#CyHelp Starter Code
cybersecurityBirthYear = 1970

#Greets user
print("Hello! I'm CyHelp.\n")
username = input("What's your name?\n")
print("\nNice to meet you " + username)
#Recounts start of Cybersecurity
todaysYear = int(input("What year is it?\n"))
timePassed = todaysYear - cybersecurityBirthYear
print("Wow! That means it has been " + str(timePassed) + " years since Cybersecurity began!")
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")

input("Press enter to continue\n")
#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from cyber attacks.")
print("These people can be governments/nations, individuals, companies, community organizations, and hackers.\n")


#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and availability.")
print("Would you like to learn more about the CIA Triad?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains pillars of CIA Triad
while giveInfo.lower() == 'yes':
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) confidentiality, (b) integrity, (c) availability, or (d) none")
  topic = input()
  topic = topic.lower()
  
  if (topic == "a"):
    print("Confidentiality makes sure data is private.")
  elif (topic == "b"):
    print("Integrity makes sure data has not been tampered with and can be trusted.")
  elif (topic == "c"):
    print("Availability makes sure authorized people can access the data.")
  elif (topic == "d"):
    print("OK.")
    break
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")