from app import db,fsqla

class Role(db.Model, fsqla.FsRoleMixin):
    pass
class User(db.Model,fsqla.FsUserMixin):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(16),
        unique=True,
    )
    email = db.Column(
        db.String(20),
        unique=True
    )
    admin = db.Column(
        db.Boolean
    )
    active = db.Column(
        db.Boolean
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    password = db.Column(db.String(255))
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(20),
        unique=False,
        nullable=False
    )
    color = db.Column(
        db.String(20),
        unique=False,
        nullable=False
    )
    weight = db.Column(
        db.FLOAT,
        nullable=True
    )
    price = db.Column(
        db.FLOAT,
        nullable=False
    )
    numbers = db.Column(
        db.Integer
    )
    def __repr__(self):
        return self.name

class Address(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'),nullable=False,unique=False)
    product = db.relationship('Product', backref=db.backref('address',lazy=True))
    country = db.Column(
        db.String(20),
        unique=False,
        nullable=False
    )
    city = db.Column(
        db.String(20),
        unique=False,
        nullable=False
    )
    street = db.Column(
        db.String(20),
        unique=False,
        nullable=False
    )
    number_of_building = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )