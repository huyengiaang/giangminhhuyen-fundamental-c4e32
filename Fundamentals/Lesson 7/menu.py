from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
menu_data = [
    {
        'name': 'Com Rang Dua Bo',
        'price': 10
    },
    {   
        'name': 'Bun Bo Nam Bo',
        'price': 20
    },
    {
        'name': 'Nem Ran',
        'price': 50
    }
]


@app.route('/')
def index():
    # for k, v in menu_data:
    #     menu_data['price']='xu ly them dau , vao price'
    return render_template('menu.html', menu_data=menu_data)


@app.route('/', methods=['POST'])
def post_dish():
    dish_name = request.form.get('name')
    dish_price = int(request.form.get('price'))
    menu_data.append({
        'name': dish_name,
        'price': dish_price
    })
    return redirect(url_for('index'))
    return render_template("menu.html", menu_data=menu_data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
