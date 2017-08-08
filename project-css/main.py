
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

weekday = {
'1':'monday',
'2':'Tuesday',
'3':'Wenesday',
'4':'Thursday',
'5':'Friday'
}


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/main.html')



        self.response.out.write(template.render())

    def post(self):
        template = jinja_environment.get_template('templates/result.html')

        day = self.request.get('number')
        #self.response.write(day)
        self.response.write(weekday[day])
        self.response.out.write(template.render())






app = webapp2.WSGIApplication([
    ('/', MainHandler)

], debug=True)
