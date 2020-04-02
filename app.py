from flask import flask, render_template,request

app = flask(__name__)

@aa.route("/")
def index():
     return render_template('index.html')

@app.route('recomendations')
@app.route('recomendations/<string:man>')
def hello(man=''):
    user_name = user_name.capitalize()
    return render_template("recomendation.html", man = man )


@app.route("/all_drugs")
def add_drugs():
    drugs_list = [
        'Парацетамол',
        'Линкас',
        'Антигриппин',
        'Кавинтон',
        'Канефирон',
    ]
    return render_template("all_drugs.html", drugs_list = drugs_list)