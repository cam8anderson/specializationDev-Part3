from flask import Flask, render_template, redirect, flash, request, session
import jinja2
from melons import Melon
from forms import LoginForm
import customers


app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined
app.secret_key = 'dev'


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/melons')
def all_melons_route():
    melon_list = Melon.all_melons()
    return render_template('all_melons.html', melon_list=melon_list)

@app.route('/melons/<melon_id>')
def one_melon_route(melon_id):
    melon = Melon.get_with_id(melon_id)
    return render_template('melon_details.html', melon=melon)

@app.route('/add_to_cart/<melon_id>')
def add_to_cart(melon_id):
    if 'username' not in session:
        return redirect('/login')

    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    
    cart[melon_id] = cart.get(melon_id, 0) + 1
    session.modified = True
    flash(f'{melon_id} added to the cart')
    print(cart)
    return redirect('/melons')

@app.route('/cart')
def cart():
    if 'username' not in session:
        return redirect('/login')

    order_total = 0
    cart_melons = []

    cart = session.get('cart', {})

    for melon_id, quantity in cart.items():
        melon = Melon.get_with_id(melon_id)

        total_cost = quantity * melon.price
        order_total += total_cost

        melon.quantity = quantity
        melon.total_cost = total_cost

        cart_melons.append(melon)
    return render_template('cart.html', cart_melons=cart_melons, order_total=order_total)

@app.route('/empty-cart')
def empty_cart():
    session['cart'] = {}

    return redirect('/cart')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = customers.get_with_username(username)

        if not user or user['password'] != password:
            flash('Invalid password or username')
            return redirect('/login')

        session['username'] = user['username']
        flash('Logged in')
        return redirect('/melons')
    
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    del session['username']
    flash('Logged out')
    return redirect('/login')

app.errorhandler(404)
def error_404(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.env = 'development'
    app.run(port= 8000, host= 'localhost')