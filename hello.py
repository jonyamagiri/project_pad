from flask import Flask, render_template


# create a Flask instance
app = Flask(__name__)

# create a route decorator
@app.route('/')
def index():
    first_name = "John"
    stuff = "This is bold text!"

    favorite_pizza = ["Pepperoni", "Cheese", "Meat-balls", 41]

    return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

# localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# create custom error handler
# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500




if __name__ == '__main__':
    app.run(debug=True)