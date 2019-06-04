from flask import Flask, request, render_template, redirect, url_for
from garan import get_all,insert_food,get_food_by_id,update_food_by_id
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

@app.route('/edit_food/,<food_id>', methods = ['POST'])
def put_food(food_id):
    dish_name = request.form.get('name')
    dish_price = int(request.form.get('price'))
    update_food_by_id(food_id,dish_name,dish_price)
    return redirect(url_for('index'))

@app.route('/edit_food/,<food_id>')
def func_name(food_id):
    print(food_id)
    dish = get_food_by_id(food_id)
    return render_template('edit_food.html', food = menu_data)

@app.route('/', methods=['POST'])
def post_dish():
    dish_name = request.form.get('name')
    dish_price = int(request.form.get('price'))
    menu_data.append({
        'name': dish_name,
        'price': dish_price
    })
    insert_food(dish_name, dish_price)

    return redirect(url_for('index'))
    return render_template("menu_copy.html", menu_data=get_all)

# @app.route('/edit_food/<id>')
# def func_name(food_id):
#     print(food_id)
#     dish = get_food_by_id(food_id)

#     return render_template('edit_food.html', food = dish)
@app.route('/')
def index():
    # for k, v in menu_data:
    #     menu_data['price']='xu ly them dau , vao price'
    return render_template('menu_copy.html', menu_data=get_all)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
