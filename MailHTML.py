from jinja2 import Environment, FileSystemLoader
import os

class MailHTML():
    def __init__(self,name="",surname="",numberParcel="",pin="",link="",date=""):
        self.name=name
        self.surname=surname
        self.numberParcel=numberParcel
        self.pin=pin
        self.link=link
        self.date=date
    
    def generateHTML(self):
        env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))
        template = env.get_template('szablon.html')
        html = template.render(name=self.name,surname=self.surname,numberParcel=self.numberParcel,pin=self.pin,date=self.date,link=self.link)
        return html
