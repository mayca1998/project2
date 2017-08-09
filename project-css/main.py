
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
'5':{'1':'monday',
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



        self.response.out.write(template.render())

    def post(self):
        template = jinja_environment.get_template('templates/result.html')
        day = self.request.get('day')
        month = self.request.get('month')


        self.response.write(weekday[month][day])
        self.response.out.write(template.render())











app = webapp2.WSGIApplication([
    ('/', MainHandler)

], debug=True)
>>>>>>> 189fb20868602a572450143c1938470286e40a30
