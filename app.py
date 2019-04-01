from flask import (Flask, render_template,
                   url_for, flash, redirect)
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# random characters(eventually make dynamic)
app.config['SECRET_KEY'] = 'a3e4313c30d3b7e24f60d2f4f6f49493'

posts = [
    {
        'author': 'William Murphy',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Create a registration form"""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    """Create a registration form"""
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)









if __name__ == '__main__':
    app.run(debug=True)
