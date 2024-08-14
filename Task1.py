import random
import re

class SupportBot:
    negative_res = ("no", "nope", "nay", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "farewell")

    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\s*product.*',
            'technical_support': r'.*technical.*support.*',
            'about_returns': r'.*\s*returnpolicy.*',
            'general_query': r'.*how.*help.*' 
        }

    def greet(self):
        self.name = input("Hello! Welcome to our customer support. What's your name? ")
        will_help = input(f"Hi {self.name}, can I help you? ")
        if will_help.lower() in self.negative_res:
            print("Alright, have a great day.")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Thanks for reaching out. Have a great day.")
                return True
        return False

    def chat(self):
        reply = input("Please tell me your query: ").lower()
        while not self.make_exit(reply):
            response = self.match_reply(reply)
            print(response)
            reply = input("Anything else I can help with? ").lower()

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            if re.search(regex_pattern, reply):
                if intent ==  'ask_about_product':
                    return self.ask_about_product()
                elif intent == 'technical_support':
                    return self.technical_support()
                elif intent == 'about_returns':
                    return self.about_returns()
                elif intent == 'general_query':
                    return self.general_query()
                elif intent == 'exam_schedule':
                    return self.exam_schedule()
        return self.no_match_intent()

    def  ask_about_product(self):
        responses = ["Our product is top-notch and has excellent reviews! \n",
                 "You can find all prodct details on our website.\n"]
        return random.choice(responses)

    def technical_support(self):
        responses = ["Please visit our technical support page for detailed assistance.\n",
                     "Call our technical support page."]
        return random.choice(responses)

    def about_returns(self):
        responses = ["We have a 30-day return policy.\n",
                     "Please ensure the product is in original condition when returning.\n"]
        return random.choice(responses)

    def general_query(self):
        responses = ["How can I assist you further?\n",
                     "My apologies, can you provide more details?\n"]
        return random.choice(responses)

    def exam_schedule(self):
        responses = ["Our college exams are conducted offline.\n",
                     "Exams are based on the syllabus only."]
        return random.choice(responses)

    def no_match_intent(self):
        responses = ["I'm sorry, I didn't understand that.\n", "Sorry, I can't help with that."]
        return random.choice(responses)

bot = SupportBot()
bot.greet()
