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
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class MainHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("GET")
		logging.info(self.request.path)
		try:
			path = self.request.path
			template = JINJA_ENVIRONMENT.get_template('templates%s'%path)
			if path == '/home.html':
				self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'Home', 'Home':'HOME', 'Family': 'Family', 'School':'School', 'Login':'Login'}))
			elif path == '/family.html':
				self.response.write(template.render({'title': 'Family', 'pagetitle': 'Family', 'Home':'Home', 'Family': 'FAMILY', 'School':'School', 'Login':'Login'}))
			elif path == '/school.html':
				self.response.write(template.render({'title': 'School', 'pagetitle': 'School', 'Home':'Home', 'Family': 'Family', 'School':'SCHOOL', 'Login':'Login'}))
			else:
				self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'Home', 'Home':'HOME', 'Family': 'Family', 'School':'School', 'Login':'Login'}))
		except:
			template = JINJA_ENVIRONMENT.get_template('templates/home.html')
			self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'Home', 'Home':'HOME', 'Family': 'Family', 'School':'School', 'Login':'Login'}))
		#outstr = template.render(temp, {})
		#self.response.out.write(outstr)

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("GET")
		template = JINJA_ENVIRONMENT.get_template('templates/login.html')
		self.response.write(template.render({'title': 'Login', 'pagetitle': 'Login', 'Home':'Home', 'Family': 'Family', 'School':'School', 'Login':'LOGIN'}))
		
	def post(self):
		logging.info("POST")
		usernameinput = self.request.get('username')
		passwordinput = self.request.get('pw')
		if (usernameinput== 'Colleen' and passwordinput=='pass'):
			template = JINJA_ENVIRONMENT.get_template('templates/loginsuccess.html')
			self.response.write(template.render({'title': 'Logged in ...', 'pagetitle': 'Successful Login', 'Home':'Home', 'Family': 'Family', 'School':'School', 'Login':'LOGIN'}))
		else:
			logging.info("Error: Incorrect login credentials provided")
			template = JINJA_ENVIRONMENT.get_template('templates/login.html')
			self.response.write(template.render({'badcredentials': 'Bad Credentials. Try again.', 'title': 'Unsuccessful', 'pagetitle': 'Login', 'Home':'Home', 'Family': 'Family', 'School':'School', 'Login':'LOGIN'}))

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/home.html', MainHandler),
	('/family.html', MainHandler),
	('/school.html', MainHandler),
	('/login.html', LoginHandler),
], debug=True)
