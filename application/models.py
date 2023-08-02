from application import db, app

app.app_context().push()

class FootballPlayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(100), nullable=False)
    club = db.Column(db.String(100), nullable=False)
    shirt_number = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age, position, club, shirt_number):
        self.name = name
        self.age = age
        self.position = position
        self.club = club
        self.shirt_number = shirt_number

    def __repr__(self):
        return f"My name is {self.name} and I play for {self.club}."
