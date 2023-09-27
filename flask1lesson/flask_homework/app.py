from flask import Flask, render_template

app = Flask(__name__)



foods = [
    {"number":"1","name":"Маргарита", "description":"Томатний соус, моцарела, базилік", "price":"10.99"},
    {"number":"2","name":"Пепероні", "description":"Томатний соус, пепероні, моцарела", "price":"12.99"},
    {"number":"3","name":"Гавайська", "description":"Томатний соус, шинка, ананаси, моцарела", "price":"11.99"},
    {"number":"4","name":"BBQ Цезар", "description":"BBQ соус, куряче філе, салат, моцарела", "price":"13.99"},
    {"number":"5","name":"Мексиканська", "description":"Томатний соус, ковбаски, паперчі, моцарела", "price":"14.99"},
    {"number":"6","name":"Вегетаріанська", "description":"Томатний соус, броколі, гриби, моцарела", "price":"11.99"},
    {"number":"7","name":"Фреш салямі", "description":"Томатний соус, салямі, моцарела", "price":"12.99"},
    {"number":"8","name":"Піца з морепродуктами", "description":"Томатний соус, морські гребінці, креветки, моцарела", "price":"15.99"},
    {"number":"9","name":"Чотири сири", "description":"Томатний соус, моцарела, дор-блю, пармезан, фета", "price":"12.99"},
    {"number":"10","name":"Піца Одерман", "description":"Томатний соус, пепероні, гриби, моцарела, оливки, салат, помідори", "price":"14.99"}
]




@app.route("/")
def index():
    return render_template('index.html', title1="Oderman - Піцерія", title2="PizzaMondo", title3="Меню")



@app.route("/menu/")
def menu_page():
    return render_template('menu.html', title1="Меню", foods=foods)

if __name__ == '__main__':
    app.run(debug=True)