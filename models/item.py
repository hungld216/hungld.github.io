from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    total = db.Column(db.Integer, unique=False, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    date_exprired = db.Column(db.String(80), unique=False, nullable=False)

    store_id = db.Column(
        db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False
    )
    store = db.relationship("StoreModel", back_populates="items")

    users = db.relationship("UserModel", back_populates="items", secondary="items_users")
