"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cupcake(db.Model):
    """Cupcake"""

    def __repr__(self):
        c = self
        return f"<Cupcake id={c.id} flavor={c.flavor} size={c.size} rating={c.rating}>"
    
    id=db.Column(db.Integer,
                 primary_key=True,
                 autoincrement=True)
    flavor=db.Column(db.Text,
                     nullable=False)
    size=db.Column(db.Text,
                   nullable=False)
    rating=db.Column(db.Float,
                     nullable=False)
    image=db.Column(db.Text,
                    nullable=False,
                    default="https://tinyurl.com/demo-cupcake")
    
    def serialize(self):
        """Returns a dict representation of cupcake which can be turned into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
    
    
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    db.create_all()

