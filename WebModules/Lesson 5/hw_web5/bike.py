from flask import Flask, request, render_template, redirect, url_for, session
from bike_data import insert_bike

app = Flask(__name__)

bike_data = [
    {
        # 'model': 'Honda',
        # 'fee': 100000,
        # 'image': 'https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjsibDSq9riAhVBPnAKHb-6AtQQjRx6BAgBEAU&url=https%3A%2F%2Fwww.drivespark.com%2Fcars%2Fhonda%2Famaze%2F1-2-e-i-vtec%2F&psig=AOvVaw161o4KJsUXPbataxsnnJZx&ust=1560098955677778',
        # 'year': 2013
    }
]

@app.route('/new_bike')
def new_bike():
    bike_model = request.form.get('model')
    bike_fee = request.form.get('fee')
    bike_image = request.form.get('image')
    bike_year = request.form.get('year')
    bike_data.append(
        {
            'model': bike_model,
            'fee': bike_fee,
            'image': bike_image,
            'year': bike_year
        }
    )
    # print(data)
    insert_bike(bike_model, bike_fee, bike_image, bike_year)
    return redirect(url_for('index'))
    # return render_template('bike.html', data = get_all())
    # return redirect(url_for('new_bike'))

# print(data)

@app.route('/')
def index():
    return render_template('bike.html', data = bike_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

# khong biet sai cho nao uhuhuhu