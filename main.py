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
			if path == '/':
				self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'Home', 'AboutMe':'ABOUT ME', 'Professional': 'Professional', 'PhotoGallery':'Photo Gallery', 'ThankYou':'Thank You'}))
			elif path == '/aboutme.html':
				self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'Home', 'AboutMe':'ABOUT ME', 'Professional': 'Professional', 'PhotoGallery':'Photo Gallery', 'ThankYou':'Thank You'}))
			elif path == '/professional.html':
				self.response.write(template.render({'title': 'Professional', 'pagetitle': 'Professional', 'AboutMe':'About Me', 'Professional': 'PROFESSIONAL', 'PhotoGallery':'Photo Gallery', 'ThankYou':'Thank You'}))
			elif path == '/photogallery.html':
				self.response.write(template.render({'title': 'Photo Gallery', 'pagetitle': 'Photo Gallery', 'AboutMe':'About Me', 'Professional': 'Professional', 'PhotoGallery':'PHOTO GALLERY', 'ThankYou':'Thank You'}))
			elif path == '/thankyou.html':
				self.response.write(template.render({'title': 'Connnect', 'pagetitle': 'Thank You', 'AboutMe':'About Me', 'Professional': 'Professional', 'PhotoGallery':'Photo Gallery', 'ThankYou':'THANK YOU'}))
			else:
				self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'Home', 'AboutMe':'ABOUT ME', 'Professional': 'Professional', 'PhotoGallery':'Photo Gallery', 'ThankYou':'Thank You'}))
		except:
			template = JINJA_ENVIRONMENT.get_template('templates/aboutme.html')
			self.response.write(template.render({'title': 'Nick Reitnour', 'pagetitle': 'Home', 'AboutMe':'ABOUT ME', 'Professional': 'Professional', 'PhotoGallery':'Photo Gallery', 'ThankYou':'Thank You'}))
		#outstr = template.render(temp, {})
		#self.response.out.write(outstr)

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/aboutme.html', MainHandler),
	('/professional.html', MainHandler),
	('/photogallery.html', MainHandler),
	('/thankyou.html', MainHandler),
], debug=True)
