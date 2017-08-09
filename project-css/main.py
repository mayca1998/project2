import os
import webapp2
import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/horoscop.html')
        self.response.write(template.render())

    def post(self):
        month = self.request.get('r_month')
        day = self.request.get('r_day')
        #self.response.write(day)

        if((int(month)==3 and int(day)>= 21)or (int(month)==4 and int(day)<=19)):
            self.response.write('<strong> Zodiac Sign: Aries </strong>')
        if((int(month)==4 and int(day)>=20 )or (int(month)==5 and int(day)<=20)):
            self.response.write('<strong> Zodiac Sign: Taurus </strong>')
        if((int(month)==5 and int(day)>=21 )or (int(month)==6 and int(day)<=20)):
            self.response.write('<strong> Zodiac Sign: Gemini </strong>')
        if((int(month)==6 and int(day)>=21 )or (int(month)==7 and int(day)<=22)):
            self.response.write('<strong> Zodiac Sign: Cancer </strong>')
        if((int(month)==7 and int(day)>=22 )or (int(month)==8 and int(day)<=22)):
            self.response.write('<strong> Zodiac Sign: Leo </strong>')
        if((int(month)==8 and int(day)>=23 )or (int(month)==9 and int(day)<=22)):
            self.response.write('<strong> Zodiac Sign: Virgo </strong>')
        if((int(month)==9 and int(day)>=23 )or (int(month)==10 and int(day)<=22)):
            self.response.write('<strong> Zodiac Sign: Libra </strong>')
        if((int(month)==10 and int(day)>=23 )or (int(month)==11 and int(day)<=21)):
            self.response.write('<strong> Zodiac Sign: Scorpio </strong>')
        if((int(month)==11 and int(day)>=22 )or (int(month)==12 and int(day)<=21)):
            self.response.write('<strong> Zodiac Sign: Sagittarius </strong>')
        if((int(month)==12 and int(day)>=22 )or (int(month)==1 and int(day)<=19)):
            self.response.write('<strong> Zodiac Sign: Capricorn </strong>')
        if((int(month)==1 and int(day)>=20 )or (int(month)==2 and int(day)<=18)):
            self.response.write('<strong> Zodiac Sign: Aquarius </strong>')
        if((int(month)==2 and int(day)>=19 )or (int(month)==3 and int(day)<=20)):
            self.response.write('<strong> Zodiac Sign: Pisces </strong>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
