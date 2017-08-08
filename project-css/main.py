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
import random

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('WELCOME TO YOUR BIRTHDAY CLENDAR! <br>')
        horoscope=['Today will be a great day to start something new.' ,
         'Nothing is too hard if you set your mind to it.',
         'Everything will work out as long as you keep your goals in mind.',
         'Remember that the best success comes from the hardest work.',
         'Failure is in your future, everything  you think you know will turn out to be lies.',
         'Nothing is the way that it seems.']
         print str(random.choice(horoscope))
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
