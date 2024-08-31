import random
import re

class RuleBot:
    ##response
    negative_res = ("no","nope","nah","naw","not a chance","sorry")
    exit_commands = ("I'll, chat you later","quit","pause","exit","goodbye","later")
    
    
    random_question = (
        "Are there many humans like you?",
        "what do you consume for sustence?",
        "Is there Intelligent life on this planet?"
    )
    
    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipaat': r'.*\s*intellipaat.*'
        }
    
    def greet(self):
        self.name = input("what is your name ?\n")
        will_help = input(
            f"Hi {self.name}, I am your bot. Will you help me learn about your planet?\n")
        if will_help in self.negative_res:
            print("have nice earth day!")
            return  
        self.chat()
        
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("It's good to chat with you. Have a nice day!")
                return True

    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
            
    
    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipaat':
                return self.about_intellipaat()
        
        if not found_match:
            return self.no_match_intent() 
    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organism\n",
                    "I heard the coffee is goood \n")
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses = ("I come in peace \n","I am here to collect data on your planet and its inhabitants\n",
                      "I heard the coffee is good \n")
        return random.choice(responses)
    
    def about_intellipaat(self):
        responses = ("Intelligent is world largest professional; educational company \n", "Intelligent will make you learn concept in the way never less\n",
                      "Intelligent is where your career and skill grows\n")
        return random.choice(responses)
    

    def no_match_intent(self):
        responses = ( "Please tell me more.\n","tell me more!\n","I see.Can you elaborate\n",
                        "Interesting.can you tell me more ?\n")
        return random.choice(responses)

bot = RuleBot()
bot.greet()