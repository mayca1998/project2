#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2
import os

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


'''
    def get(self):
        template = jinja_environment.get_template('templates/main.html')
        # week1 = {
        # '1':'monday',
        # '2':'Tuesday',
        # '3':'Wenesday',
        # '4':'Thursday',
        # '5':'Friday'
        # }

        weekday = {'weekday'}


        if weekday == '1':
            variables = 'monday'
            self.response.write(template.render(variables))
        elif weekday == '2':
            variables = 'Tuesday'
            self.response.write(template.render(variables))


        variables = {'weekday': weekday}
        # self.response.write(template.render(variables))



        # template =
        # week1 = ['monday', 'tuesday']
        # week2 = ['monday', 'tuesday']
        #
        # week_dictionary = {'week_1': week1 , 'week2': week2}
        #
        # self.response.out.writse(template.render(week_dictionary))
        # self.response.write(week1['1'])
'''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
