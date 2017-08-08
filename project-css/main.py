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

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
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
        elif weekday == '2':
            variables = 'Tuesday'


        variables = {'weekday': weekday}
        self.response.write(template.render(variables))



        # template =
        # week1 = ['monday', 'tuesday']
        # week2 = ['monday', 'tuesday']
        #
        # week_dictionary = {'week_1': week1 , 'week2': week2}
        #
        # self.response.out.writse(template.render(week_dictionary))
        # self.response.write(week1['1'])


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
