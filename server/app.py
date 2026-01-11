import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "title": e.title} for e in episodes])

# GET episode by ID
@app.route('/episode/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify({"id": episode.id, "title": episode.title})
    return jsonify({"error": "Episode not found"}), 404

# GET all guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{"id": g.id, "name": g.name} for g in guests])

# POST create appearance
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.json
    appearance = Appearance(guest_id=data['guest_id'], episode_id=data['episode_id'])
    db.session.add(appearance)
    db.session.commit()
    return jsonify({"id": appearance.id, "guest_id": appearance.guest_id, "episode_id": appearance.episode_id}), 201

# DELETE 
@app.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if episode:
        db.session.delete(episode)
        db.session.commit()
        return jsonify({"message": "Episode deleted"})
    return jsonify({"error": "Episode not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)