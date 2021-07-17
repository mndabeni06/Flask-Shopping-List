from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return render_template('/shopping_list.html')


@app.route('/showitems', methods=['POST'])
def showitems():
    item_name = request.form['Name']
    item_id = request.form['id']
    quantity = request.form['Quantity']
    price = request.form['Price']
    total_price = int(price)*int(quantity)
    return render_template('/showitems.html',
                           item_name=item_name,
                           item_id=item_id,
                           quantity=quantity,
                           price=price,
                           total=total_price
                           )


if __name__ == '__main__':
    app.run(debug=True)
