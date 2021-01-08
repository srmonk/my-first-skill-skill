import time
from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_duration

class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
   
        
    @intent_handler('skill.study.intent')
    def handle_skill_study(self, message):
        blocks = self.get_response('skill.study')
        self.speak_dialog('skill.study.confirmation', {'time': str(blocks)})
# To convert  blocks to an int, itt first needs to be a  string. The variable must be of time int for us to be able to put it into a range for the  loop
        blocks = str(blocks)
        blocks = int(blocks)
        for i in range(blocks):
            time.sleep(25)
            if i <  blocks-1:
                self.speak_dialog('skill.breakbegin')
                time.sleep(5)
                self.speak_dialog('skill.breakend') 
            if i == blocks-1:
                break
        self.speak_dialog('skill.end') 



def create_skill():
    return MyFirstSkill()
