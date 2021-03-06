# -*- coding: utf-8 -*-
from . import db, AppModel

class Brand_info(AppModel):
    __tablename__ = 'brand_info'
    brand_name = db.Column(db.String(50), nullable= False)
    # telephone = db.Column(db.String(50))
    # brand_web = db.Column(db.String(100))
    # brand_logo = db.Column(db.String(100))
    brand_desc = db.Column(db.String(150))
    # brand_status = db.Column(db.Boolean)
    product_info = db.relationship('Product_info',backref = 'brand_info',lazy = 'dynamic')

    def __repr__(self):
        return '{}'.format(self.id)

    def __init__(self, brand_name, brand_desc):
        self.brand_name = brand_name
        self.brand_desc = brand_desc

