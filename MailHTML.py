from logging import raiseExceptions
from jinja2 import Environment, FileSystemLoader
import os

class MailHTML():
    def __init__(self,typeMessage):
        env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))
        self.template = env.get_template(typeMessage+'.html')

    def generateHTML(self,json):
        html = self.template.render(json=json)
        return html
