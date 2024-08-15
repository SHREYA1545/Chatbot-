import random
import re

class SupportBot:
    negative_res = ("no", "nope", "nay", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "farewell")

    def __init__(self):
        self.support_responses = {
            'tuesday_timetable': r'.*\s*tuesday.*',
            'wednesday_timetable': r'.*\s*wednesday.*',
            'thursday_timetable': r'.*\s*thursday.*',
            'friday_timetable': r'.*\s*friday.*',
            'saturday_timetable': r'.*\s*saturday.*',
            'about_returns': r'.*\s*syllabus.*',
            'exam_schedule': r'.*exam.*details*'
        }
    
    def greet(self): 
        self.name = input("Hello! Welcome. What's your name? ")
        will_help = input(f"Hi {self.name}, can I help you? ").lower()
        if will_help in self.negative_res:
            print("Alright, have a great day.")
            return
        self.chat()

    def make_exit(self, reply):
        return any(command in reply for command in self.exit_commands)
  
    def chat(self):
        reply = input("I will help you find today's timetable, academic calendar, or answer any other queries. ").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply)).lower()
        print("Thanks for reaching out. Have a great day.")

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            if re.search(regex_pattern, reply):
                return getattr(self, intent)()
        return self.no_match_intent()

    def tuesday_timetable(self):
        responses = (
            "1. DBMS, 2. ADS, 3. DMS, 4. Batch A1-ADS Lab, 5. Batch A2-DBMS Lab",
            "1. DBMS, 2. ADS, 3. DMS, 4. Batch A1-ADS Lab, 5. Batch A2-DBMS Lab"
        )
        return random.choice(responses)
    
    def wednesday_timetable(self):
        responses = (
            "1. LA, 2. ADS, 3. T&P, 4. T&P, 5. Batch A1-DBMS Lab, 6. Batch A2-ADS Lab",
            "1. LA, 2. ADS, 3. T&P, 4. T&P, 5. Batch A1-DBMS Lab, 6. Batch A2-ADS Lab"
        )
        return random.choice(responses)
    
    def thursday_timetable(self):
        responses = (
            "1. DMS, 2. ADS, 3. DBMS, 4. PAIML, 5. LA, 6. LA",
            "1. DMS, 2. ADS, 3. DBMS, 4. PAIML, 5. LA, 6. LA"
        )
        return random.choice(responses)
    
    def friday_timetable(self):
        responses = (
            "1. DMS, 2. DBMS, 3. Batch A1-SST Lab, 4. Batch A2-DBMS, 5. Remedial, 6. MDM1",
            "1. DMS, 2. DBMS, 3. Batch A1-SST Lab, 4. Batch A2-DBMS, 5. Remedial, 6. MDM1"
        )
        return random.choice(responses)

    def saturday_timetable(self):
        responses = (
            "1. Batch A2-SST Lab, 2. Batch A1-MP Lab, 3. LA, 4. CI, 5. CI, 6. MDM1",
            "1. Batch A2-SST Lab, 2. Batch A1-MP Lab, 3. LA, 4. CI, 5. CI, 6. MDM1"
        )
        return random.choice(responses)

    def about_returns(self):
        responses = (
            "Your's syllabus accordind to your branch and year is avaliable on the offical website of college. visit it!",
            "Syllabus is avaliable on the website of college. Visit it!"
        )
        return random.choice(responses)

    
    def exam_schedule(self):
        responses = (
            "Exam details are in the academic calendar: Link- https://acrobat.adobe.com/id/urn:aaid:sc:AP:c07cdaa1-0b10-4c5c-8d6f-fc98643b232b",
            "Exam details are in the academic calendar: Link- https://acrobat.adobe.com/id/urn:aaid:sc:AP:c07cdaa1-0b10-4c5c-8d6f-fc98643b232b"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "I'm sorry, I didn't understand that.",
            "Sorry, I can't help with that request."
        )
        return random.choice(responses)
    
   
bot = SupportBot()
bot.greet()
