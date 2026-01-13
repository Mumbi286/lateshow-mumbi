from . import db
from .models import Episode, Guest, Appearance

def seed_database():
    episodes_df = pd.read_csv('episodes.csv')
    guests_df = pd.read_csv('guests.csv')
    appearances_df = pd.read_csv('appearances.csv')

    for _, row in episodes_df.iterrows():
        db.session.add(Episode(id=row['id'], title=row['title']))
    for _, row in guests_df.iterrows():
        db.session.add(Guest(id=row['id'], name=row['name']))
    for _, row in appearances_df.iterrows():
        db.session.add(Appearance(id=row['id'], guest_id=row['guest_id'], episode_id=row['episode_id'], rating=row['rating']))

    db.session.commit()

if __name__ == '__main__':
    from app import create_app, db
    app = create_app()
    with app.app_context():
        seed_database()