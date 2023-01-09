import random
def generate():
    a = random.randrange(0, 3)
    if a == 0:
        print(generate_response())
    if a == 1:  
        print(generate_open())
    if a == 2:
        generate_question()

def generate_open():
    open_ended_question = [
        "What's the best thing that's happened to you today?",
        "What's your favorite thing to do?",
        "Do you like music?"
    ]
    return random.choice(open_ended_question)

def generate_response():
  responses = [
    "Interesting",
    "Neat",
    "That's Nice",
    "I love Ice Cream",
    "That sounds really cool!"
  ]
  return random.choice(responses)

def generate_question():
    questions = [
        Sport,
        Music,
    ]
    select = random.choice(questions)
    return select()

def Repeat():
    responses = [
        "I'm sorry I didn't quite catch that?",
        "Pardon?",
        "Say Again?",
        "Come Again?",
    ]
    return random.choice(responses)

def Name(): 
    name = input("What's yours? ")
    length = len(name)
    
    #Reduces to firstname
    try:
        name = name.split()[0]
    except:
        print(Repeat()) 
        Name() 

    if name.isalpha() != True: print("That's a very interesting name") #Checks for Non-Alphabetic Character's
          
    #Checks length
    elif length == 1: print("I've never met someone with just one letter for a first name") #Name Length
    elif length > 13: 
        print("You've got quite a long name!") #Name Length 13 or more
        if length > 20: print(f"I don't think I've ever met someone with {length} letters in their name before") #Name Length 20 or more
    return name.capitalize()

def Age():
    age = input("How old are you? ")
    try:
        age = int(age)
    except ValueError:
        print(Repeat)
        Age()

    if age <= 6: print("How did you get in here")
    elif age >= 7 and age <= 11: print("Have fun being a kid")
    elif age >= 12 and age <= 13: print("Middle Schools rough")
    elif age >= 14 and age <= 17: print("Happy High School")
    elif age >= 18 and age <= 60: print("I hope life is treating you well!")
    elif age >= 65:
        print("Any wise words for me?")
        input()

def Sport():
    sport = input("What's your favorite sport?: ")
    if sport.isalpha() == False:
        print(Repeat())
        Sport()
    else:
        sport = sport.lower()
        match sport:
            case "soccer": print("I really like soccer") 
            case "cricket": print("I've heard of it, but I've never played it")
            case "hockey": print("Fun to watch, can't skate though :/")
            case "tennis": print("Tennis is fun")
            case "rugby": print("I've heard of it, but I've never played it")
            case _: print("Never heard of it")
def Music():
    music = input("What's your favorite genre of music?: ")
    if music.isalpha() == False:
        print(Repeat())
        Music()
    else:
        music = music.lower()
        match music:
            case "rock": print("Rock on!") 
            case "classical": print("How fancy.")
            case "pop": print("Eh, depends on who it is")
            case "rap": print("Eh, depends on who it is")
            case "country": print("Gems in the mud, amiright partner?")
            case _: print("Never heard of it")


if __name__ == "__main__":
    exit = '/'
    user_input = 0
    print("Hello my name is, Chatbot.")
    name = Name()
    Age()
    print(f"Nice to meet you {name}")
    
    while user_input != exit:
        generate()
        user_input = input()
        
    