from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


app = create_app()


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    position = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.position}"


@app.route('/employees')
def get_employees():
    employees = Employee.query.all()
    output = [{'name': employee.name, 'position': employee.position} for employee in employees]
    return {"employees": output}


@app.route('/employees/<int:id>')
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify({"name": employee.name, "position": employee.position})


@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    employee = Employee(name=data['name'], position=data['position'])
    db.session.add(employee)
    db.session.commit()
    return {'id': employee.id}


@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee_name(id):
    employee = Employee.query.get_or_404(id)
    if 'name' in request.json:
        employee.name = request.json['name']
        db.session.commit()
        return jsonify({"message": "Name updated successfully"})
    else:
        return jsonify({"error": "Name field missing in the request"}), 400


@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return {"message": "successful"}


if __name__ == "__main__":
    app.run(debug=True)
