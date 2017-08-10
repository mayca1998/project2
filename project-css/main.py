import webapp2
import jinja2
import os
import calendar
from random import randint

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

weekday = {
#31
'1':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#29
'2':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#31
'3':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#30
'4':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'So yesterday is the day that happened before today',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#31
'5':{'1':'Tim McGraw',
     '2':'Baron Von Richtofen',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'George Clooney',
     '7':'Wenesday',
     '8':'Harry S. Truman - 33rd U.S President (1945-1953)',
     '9':'Wass up',
     '10':'John Wilkes Booth',
     '11':'',
     '12':'',
     '13':'Stevie Wonder - Singer, Musician',
     '14':'George Lucas - filmmaker',
     '15':'',
     '16':'',
     '17':'',
     '18':'',
     '19':'Malcolm X',
     '20':'',
     '21':'',
     '22':'',
     '23':'',
     '24':'Bob Dylan',
     '25':'',
     '26':'',
     '27':'',
     '28':'',
     '29':'John F. Kennedy - 35th U.S. President',
     '30':'',
     '31':'Clint Eastwood'
},
#30
'6':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#31
'7':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#31
'8':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#30
'9':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#31
'10':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#30
'11':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
#31
'12':{'1':'monday',
     '2':'Tueday',
     '3':'Wenesday',
     '4':'Thursday',
     '5':'Wass up',
     '6':'Tueday',
     '7':'Wenesday',
     '8':'Thursday',
     '9':'Wass up',
     '10':'HI'
},
}

class MainHandler(webapp2.RequestHandler):

    def get(self):

        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render())


    def post(self):
        template = jinja_environment.get_template('templates/result.html')
        day1 = self.request.get('day')
        month1 = self.request.get('month')

        if month1 == '2':
            if day1 == ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']:
              self.response.write(weekday[month1][day1])
            else:
              self.response.write('<br><a href="/">Back</a>')
        elif month1 == ['4','6','9','11']:
            if day1 == ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']:
                self.response.write(weekday[month1][day1])
            else:
                self.response.write('<br><a href="/">Back</a>')
        elif month1 == ['1','5','7','8','10','12']:
            if day1 == ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']:
                self.response.write('<br><a href="/">Back</a>')
            else:
                self.response.write('<br><a href="/">Back</a>')
        else:
            self.response.write('<br><a href="/">Back</a>')





        # self.response.write(weekday[month1][day1])
        self.response.out.write(template.render())

        #month1 = self.request.get('r_month')
        #day1 = self.request.get('r_day')
        #self.response.write(day)

        if((int(month1)==3 and int(day1)>= 21)or (int(month1)==4 and int(day1)<=19)):
            self.response.write('<strong> Zodiac Sign: Aries </strong>')
        if((int(month1)==4 and int(day1)>=20 )or (int(month1)==5 and int(day1)<=20)):
            self.response.write('<strong> Zodiac Sign: Taurus </strong>')
        if((int(month1)==5 and int(day1)>=21 )or (int(month1)==6 and int(day1)<=20)):
            self.response.write('<strong> Zodiac Sign: Gemini </strong>')
        if((int(month1)==6 and int(day1)>=21 )or (int(month1)==7 and int(day1)<=22)):
            self.response.write('<strong> Zodiac Sign: Cancer </strong>')
        if((int(month1)==7 and int(day1)>=22 )or (int(month1)==8 and int(day1)<=22)):
            self.response.write('<strong> Zodiac Sign: Leo </strong>')
        if((int(month1)==8 and int(day1)>=23 )or (int(month1)==9 and int(day1)<=22)):
            self.response.write('<strong> Zodiac Sign: Virgo </strong>')
        if((int(month1)==9 and int(day1)>=23 )or (int(month1)==10 and int(day1)<=22)):
            self.response.write('<strong> Zodiac Sign: Libra </strong>')
        if((int(month1)==10 and int(day1)>=23 )or (int(month1)==11 and int(day1)<=21)):
            self.response.write('<strong> Zodiac Sign: Scorpio </strong>')
        if((int(month1)==11 and int(day1)>=22 )or (int(month1)==12 and int(day1)<=21)):
            self.response.write('<strong> Zodiac Sign: Sagittarius </strong>')
        if((int(month1)==12 and int(day1)>=22 )or (int(month1)==1 and int(day1)<=19)):
            self.response.write('<strong> Zodiac Sign: Capricorn </strong>')
        if((int(month1)==1 and int(day1)>=20 )or (int(month1)==2 and int(day1)<=18)):
            self.response.write('<strong> Zodiac Sign: Aquarius </strong>')
        if((int(month1)==2 and int(day1)>=19 )or (int(month1)==3 and int(day1)<=20)):
            self.response.write('<strong> Zodiac Sign: Pisces </strong>')

        horoscope=['Today will be a great day to start something new.' ,
            'Nothing is too hard if you set your mind to it.',
            'Everything will work out as long as you keep your goals in mind.',
            'Remember that the best success comes from the hardest work.',
            'Failure is in your future, everything  you think you know will turn out to be lies.',
            'Nothing is the way that it seems.',
            "Remember that it's not about the destination, but the adventure.",
            'All good things are worth waiting for.',
            'Success is in your future.',
            'Nothing lasts forever, be ready to let go.',
            "Dreams show one's true desire.",
            "Don't be afraid to be yourself.",
            "Don't take things for granted, your may regret it",
            "There's no such thing as imposssible.",
            "If you're too comfortable, maybe its time for a change.",
            "Change doesn't always have to be hard."]

        horoscope[randint(0,15)]

        self.response.write(horoscope[randint(0,15)])
        self.response.write('<br><a href="/">Back</a>')


app = webapp2.WSGIApplication([
    ('/', MainHandler)

], debug=True)
