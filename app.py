from flask import Flask, jsonify, request
from database import db
from models.meal import Meal
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:admin123@127.0.0.1:3306/daily_diet"

db.init_app(app)

@app.route("/api/meals", methods=["GET"])
def get_all_meals():
    all_meals = db.session.execute(db.select(Meal)).scalars().all()
    results = [meal.to_dict() for meal in all_meals]
    return jsonify(results)

@app.route("/api/meals/<int:meal_id>", methods=["GET"])
def get_meal_by_id(meal_id):
    meal = db.session.get(Meal, meal_id)

    if meal:
      return jsonify(
          meal.to_dict()
      )
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/api/meals", methods=["POST"])
def create_meal():
    data = request.json
  
    if not data or "name" not in data or "datetime" not in data or "is_diet" not in data:
        return jsonify({"message": "Dados inválidos ou faltando"}), 400
    
    try:
        meal_datetime = datetime.fromisoformat(data["datetime"])

        meal = Meal(
            name=data["name"],
            description=data.get("description"),
            datetime=meal_datetime,
            is_diet=data["is_diet"]
        )

        db.session.add(meal)
        db.session.commit()

        return jsonify(meal.to_dict()), 201
    
    except ValueError:
        return jsonify({"message": "Formato de 'datetime' inválido. Use ISO format (YYYY-MM-DDTHH:MM:SS)"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Erro ao criar refeição: {str(e)}"}), 500

@app.route("/api/meals/<int:meal_id>", methods=["PUT"])
def update_meal(meal_id):
    meal = db.session.get(Meal, meal_id)

    if not meal:
        return jsonify({"message": "Refeição não encontrada!"}), 404
    
    data = request.json
    if not data:
        return jsonify({"message": "Corpo da requisição inválidos ou ausentes"}), 400
    
    try:
        meal.name = data["name"]
        meal.description = data.get("description")
        meal.datetime = datetime.fromisoformat(data["datetime"])
        meal.is_diet = data["is_diet"]

        db.session.commit()

        return jsonify({"message": "Refeição atualizada com sucesso!"}), 200
    
    except KeyError as e:
        return jsonify({"message": f"Campo obrigatório ausente: {str(e)}"}), 400
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Erro interno ao atualizar: {str(e)}"}), 500
    
@app.route("/api/meals/<int:meal_id>", methods=["DELETE"])
def delete_meal(meal_id):
    meal = db.session.get(Meal, meal_id)

    if not meal:
        return jsonify({"message": "Refeição não encontrada!"}), 404
    
    db.session.delete(meal)
    db.session.commit()
    return jsonify({"message": "Refeição deletada com sucesso!"}), 204
    
if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)