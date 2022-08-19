#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm BreachBot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook data breach!")


#Introduces breach

print("Would you like to learn about the Facebook 2019 data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Facebook faced a data breach from malicious actors in 2019 affecting 520 million users in 106 countries. The malicious actors had posted information from user profiles including phone numbers, full names, locations, some email addresses and other details to a hacking forum. They took the information from scraping the data in an old feature’s vulnerability that allowed users to find one another by phone number.")
  
  elif topic.lower() == "b":
    print("The social media company found and fixed the issue in August 2019 but did not inform users. Blog articles warned users to look out for email and phone scams.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, or (c) my advice (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("This data breach connects to confidentiality because hackers had access to data meant to be private.")
  
  elif topic.lower() == "b":
    print("I do not agree with the organization’s response because it is imperative to notify users that their information has been taken and can be used maliciously. Without this information, FB users are more vulnerable to scams and attacks.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by saying personal information can be used to steal their identity and makes them more susceptibile to phishing. My advice would be to change passwords and usernames, as well as be more suspicious of incoming messages and phone calls.")

  elif topic.lower() == "d":
    break
    
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")
  
#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")