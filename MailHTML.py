class MailHTML():
    def __init__(self,name="",surname="",numberParcel="",pin="",link="",date=""):
        self.name=name
        self.surname=surname

        if date == "":
            self.date=""
        else:
            self.date="on "+date

        if numberParcel == "":
            self.numberParcel=""
        else:
            self.numberParcel="Your parcel number is: "+numberParcel+"<br><br>"
        
        if pin == "":
            self.pin=""
        else:
            self.pin="Here is your PIN to collect your parcel: "+pin+"<br><br>"

        if link == "":
            self.link=""
        else:
            self.link="<a href=\""+link+"\">Click here to track your parcel!</a><br><br>"
        
    
    def generateHTML(self):
        html = """\
            <html>
                <body>
                    <a href="https://ibb.co/420TdSS"><img src="https://i.ibb.co/jzjMRww/januszex.png" alt="januszex" border="0"></a><br>
                        <font size="4" color=#67595E>
                        Hello """+self.name+" "+self.surname+"""<br><br>
                        Your parcel has been <strong>succesfuly</strong> send """+self.date+""" and it is on the way! <br><br>
                        """+self.numberParcel+"""
                        """+self.pin+"""
                        """+self.link+"""
                        <br></font>
                        <font size="5" color=#900020>
                        Thank you for choosing the best courier company.<br>
                        JanuszeX Courier Company<br>
                    </font>
                </body>
            </html>
            """
        return html
