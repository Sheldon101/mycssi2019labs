import webapp2
import jinja2
import os
from models import Meme


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class EnterInfoHandler(webapp2.RequestHandler):

    def post(self):
        self.response.write("A post request to the EnterInfoHandler")


class ShowLoginHandler(webapp2.RequestHandler):
    def post(self):

        results_template = the_jinja_env.get_template('templates/login.html')
        username_first_line = self.request.get('user-first-ln')
        password_second_line = self.request.get('user-second-ln')



        user_Info = Info(first_line = username_first_line,
                         second_line = password_second_line,

                                        )
        user_Info.put()
        the_variable_dict = {"line1": username_first_line,
                             "line2": password_second_line,

                                                    }
        self.response.write(results_template.render(the_variable_dict))


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/loginresult', ShowLoginHandler)
], debug=True)
