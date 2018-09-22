from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/') # route to page - home page
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)

@app.route("/shopping")
def shopping():
	food = ["Cheese","Tuna","Beef","Toothpaste"]
	return render_template("shopping.html", food=food)
	
# @app.route('/') # route to page - home page
# def home():
#     return 'Method used: %s' % request.method

# @app.route("/profile/<name>") # profile page with dynamic name 
# def profile(name):
#     return render_template("profile.html", name=name)

# @app.route('/bacon', methods=['GET','POST']) # page can both GET and POST
# def bacon():
# 	if request.method == 'POST':
# 		return "You are using POST"
# 	else:
# 		return "You are probably using GET"

# @app.route('/tuna') # another directory within homepage
# def tuna():
# 	return '<h2> Tuna is good </h2>'

# @app.route('/profile/<username>') # passes what the url is to username var
# def profile(username):
# 	return "Hey there %s" % username

# @app.route('/post/<int:post_id>') # how to pass an int through url
# def post(post_id):
# 	return "Post ID is %s" % post_id

if __name__ == "__main__": # Start server
    app.run()
    