from flask import Flask, jsonify, request

app = Flask(__name__)

# Ejemplo de datos para carros y usuarios
cars = [
    {"id": 1, "brand": "Chevrolet", "model": 2009},
    {"id": 2, "brand": "Renault", "model": 2002}
]

users = [
    {"id": 1, "name": "Juan Santacruz", "email": "juan@gmail.com"},
    {"id": 2, "name": "Mario Santacruz", "email": "mario@gmail.com"}
]


# Endpoints para carros
@app.route("/cars", methods=["GET"])
def get_cars():
    return jsonify(cars)


@app.route("/cars", methods=["POST"])
def create_car():
    new_car = request.get_json()
    cars.append(new_car)
    return jsonify({"message": "Nuevo carro creado"}), 201


@app.route("/cars/<int:car_id>", methods=["PUT"])
def update_car(car_id):
    updated_car = request.get_json()
    for index, car in enumerate(cars):
        if car["id"] == car_id:
            cars[index] = updated_car
            return jsonify({"message": "Información del carro actualizada"})
    return jsonify({"message": "Carro no encontrado"}), 404


@app.route("/cars/<int:car_id>", methods=["DELETE"])
def delete_car(car_id):
    global cars
    cars = [car for car in cars if car["id"] != car_id]
    return jsonify({"message": f"El carro con ID: {car_id} ha sido eliminado"}), 200


# Endpoints para usuarios
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify({"message": "Nuevo usuario creado"}), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    updated_user = request.get_json()
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users[index] = updated_user
            return jsonify({"message": "Información del usuario actualizada"})
    return jsonify({"message": "Usuario no encontrado"}), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": f"El usuario con ID: {user_id} ha sido eliminado"}), 200


if __name__ == "__main__":
    app.run(debug=True)
