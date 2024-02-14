"""Flask app for Cupcakes"""
from flask import Flask, render_template, redirect, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import Cupcake, db, connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'password'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.app_context().push()
connect_db(app)
db.create_all()

@app.route('/api/cupcakes')
def get_cupcakes_data():
    """Gets data about all cupcakes in database as JSON"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake_data(cupcake_id):
    """Gets data about a single cupcake, returns with JSON"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def post_cupcake():
    """Creates a cupcake and responds with JSON"""
    new_cupcake = Cupcake(flavor=request.json['flavor'],
                          size=request.json['size'],
                          rating=request.json['rating'],
                          image=request.json['image']
                          )
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """ Updates a specific cupcake and responds with JSON of said cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    data = request.json 
    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.rating = data['rating']
    cupcake.image = data['image']
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Deletes a specific cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")

@app.route('/')
def show_home_page():
    """ Renders home page"""
    return render_template('home.html')