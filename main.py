import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__))
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def render_str(self, template, **params):
        return render_str(template, **params)

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class Movie(BHandler):
    def get(self):
        self.render('fresh_tomatoes.html')

app = webapp2.WSGIApplication([('/karthic-tomatoes', Movie)], debug=True)