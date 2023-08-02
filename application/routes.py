from application import app, db
from flask import request, jsonify, render_template, redirect, flash
from application.models import FootballPlayer
from application.forms import AddFootballerForm

def format_footballer(footballer):
    return {
        "name": footballer.name,
        "age": footballer.age,
        "position": footballer.position,
        "club": footballer.club,
        "shirt_number": footballer.shirt_number
    }

# GET ALL FOOTBALLERS AND ADD FOOTBALLER
@app.route("/", methods=["GET", "POST"])
def get_footballers():
    form = AddFootballerForm()
    if request.method == "POST":
        if form.validate_on_submit():
            footballer = FootballPlayer(form.name.data, form.age.data, form.position.data, form.club.data, form.shirt_number.data)
            db.session.add(footballer)
            db.session.commit()
            return redirect('/')
        
    else:
        footballers = FootballPlayer.query.all()
        footballers_list = []
        for footballer in footballers:
            footballers_list.append(format_footballer(footballer))
        
        if (len(footballers_list) == 0):
            return "Database is empty"
        else:
            return render_template('footballers.html', footballers=footballers_list, form=form)

# # ADD A FOOTBALLER
# @app.route("/footballers", methods=["POST"])
# def add_footballer():
#     form = AddFootballerForm()
#     if request.method == "POST":
#         if form.validate.on.submit():
#             footballer = FootballPlayer(form.name.data, form.age.data, form.position.data, form.club.data, form.shirt_number.data)
#             db.session.add(footballer)
#             db.session.commit()
            
#     return render_template('footballers.html', form=form)
#     # data = request.json
#     # footballer = FootballPlayer(data['name'], data['age'], data['position'], data['club'], data['shirt_number'])
#     # db.session.add(footballer)
#     # db.session.commit()
#     # return jsonify(id=footballer.id, name=footballer.name, age=footballer.age, position=footballer.position, club=footballer.club, shirt_number=footballer.shirt_number)

# GET FOOTBALLER BY ID
@app.route("/footballers/<id>")
def get_footballer(id):
    footballer = FootballPlayer.query.filter_by(id=id).first()
    return render_template('footballer.html', footballer=footballer)


# DELETE FOOTBALLER BY ID
@app.route("/footballers/<id>", methods=["DELETE"])
def delete_footballer(id):
    footballer = FootballPlayer.query.filter_by(id=id).first()
    db.session.delete(footballer)
    db.session.commit()
    return f"Football player {id} has been deleted"

# UPDATE FOOTBALLER
@app.route("/footballers/<id>", methods=["PATCH"])
def update_footballer(id):
    footballer = FootballPlayer.query.filter_by(id=id)
    data = request.json
    footballer.update(dict(name=data["name"], age=data["age"], position=data["position"], club=data["club"], shirt_number=data["shirt_number"]))
    db.session.commit()
    updatedFootballer = footballer.first()
    return jsonify(id=updatedFootballer.id, name=updatedFootballer.name, age=updatedFootballer.age, position=updatedFootballer.position, club=updatedFootballer.club, shirt_number=updatedFootballer.shirt_number)
