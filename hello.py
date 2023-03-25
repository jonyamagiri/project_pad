from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my_secret_key"

# create a form class
class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField('Submit')

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

# create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    # validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form Submitted successfully!")
    
    return render_template('name.html', name=name,form=form)




if __name__ == '__main__':
    app.run(debug=True)