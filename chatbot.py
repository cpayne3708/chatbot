# PyChat 2K17

import random
import datetime

def start():
    print("You are starting the chatbot at " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Ha",
                 "Wow",
                 "Ya think so?",
                 "You gotta be joking",
                 "That's awesome buddy",
                 "Dude, sick.",
                 "You ever eaten squirrel?",
                 "Who's yo daddy?",
                 "Huh?",
                 "yee yee bo!",
                 "Let's make this country great again buddy"
                 ]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    family_words = [" mother", " father", " brother", " sister", " mom", " dad"]
    school_words = [" class", " math", " homework", " school", " read"]
    computer_words = [" bot", " code", " computer", " program", " coding"]
    food_words = [" food", " dinner", " breakfast", " lunch", " eat", " cook", " drink"]
    dip_words = [" chaw", " lip"," dip"]
    thanks = ["thanks", "thank you"]

    
    if has_keyword(statement, family_words):
        response = "I love my family how bout you."
    elif has_keyword(statement, school_words):
        response = "You best not be failin your school boy you gon' end up like ol' " + name + " here."
    elif has_keyword(statement, dip_words):
        response = "Ye buddy I'll give you a fat chaw of only the finest Copenhagen"
    elif has_keyword(statement, thanks):
        response = "No problem buddy"
    elif has_keyword(statement, computer_words):
        response = "I have no clue what you are sayin buddy all that technical speak is over my bald head"
    elif has_keyword(statement, food_words):
        response = "I don't know bout all that but I went duck huntin' this mornin got me four juicy ones. We gonna be eatin them with our mountain dew for a week, yes sir."
    else:
        response = get_random_response()

    return response

name = "";
def play():
    talking = True

    rednecknames = ["Cletus","Billy Buck", "Ol' Randy", "Jack Willie", "Clyde",
                    "Floyd","Bubba", "Larry"]
    name = rednecknames[random.randint(0,7)];
    print("Howdy, " + name + " the Redneck Speakin")
    print("I love my family, eatin, dippin, and mountain dew")
    print("What do you want")

    while talking:
        statement = input(">> ")

        if statement.lower() == "goodbye" or statement.lower() == "bye":
            talking = False
        else:
            response = get_response(statement)
            print(response)

    print("Good talk now get back to work boy.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
