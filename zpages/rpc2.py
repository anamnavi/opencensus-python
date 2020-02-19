from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    #name = request.args.get("name", "World")
    direction = "south"
    template_values = {'Direction': direction}
    # path = os.path.join(os.path.dirname(__file__), 'index.html')
    # self.response.out.write(template.render(path, template_values))

    return render_template("index.html", Direction = direction)

if __name__ == '__main__':
    app.run(debug=True)


# class CalcController(webapp.RequestHandler):
#   def get(self):
#     principalString=self.request.get('principal')
#     rateString = self.request.get('rate')
#     principal = int(principalString)
#     rate = int(rateString)
#     interest = principal*rate/100
#     interestString = str(interest)
#    # set up the template_values with the list of people returned.
#     template_values= {'interest':interestString, 'principal': principalString}
#     # render the page using the template engine
#     path = os.path.join(os.path.dirname(__file__),'index.html')
#     self.response.out.write(template.render(path,template_values))