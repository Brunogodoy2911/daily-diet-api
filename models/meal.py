from database import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    datetime = db.Column(db.DateTime, nullable=False)
    is_diet = db.Column(db.Boolean, nullable=False, default=False)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'datetime': self.datetime.isoformat(),
            'is_diet': self.is_diet
        }