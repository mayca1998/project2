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

import webapp2
import jinja2
import os
from random import randint

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):

   def get(self):
       '''template = jinja_environment.get_template('templates/horoscop.html')
       self.response.write(template.render())'''
       self.response.write('WELCOME TO YOUR BIRTHDAY CLENDAR! <br>')
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
