import uuid
from app import db, ma


class Asset(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    display_name = db.Column(db.String(), nullable=False)
    reusable = db.Column(db.Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<Asset %r>" % self.display_name


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    material = db.Column(db.String(), nullable=False, default="Unknown")
    name = db.Column(db.String(), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey("asset.id"))
    asset = db.relationship("Asset", backref="items")

    def __repr__(self):
        return "<Item %r>" % self.id


class AssetSchema(ma.ModelSchema):
    class Meta:
        model = Asset


class ItemSchema(ma.ModelSchema):
    class Meta:
        model = Item


asset_schema = AssetSchema()
item_schema = ItemSchema()


def seed_db():
    """
    Create a mock db
    """

    item1 = Item(id=3, material="Wood", name="Table")
    item2 = Item(id=4, material="Metal", name="Pipe")
    item3 = Item(id=5, material="Rubber", name="Tire")

    oil_rig = Asset(id=1, display_name="OilRig")
    drilling_plat = Asset(id=2, display_name="DrillingPlatform")
    oil_rig.items.append(item1)
    oil_rig.items.append(item2)
    drilling_plat.items.append(item3)
    found_item = Asset.query.get(oil_rig.id)
    if not found_item:
        db.session.add(oil_rig)
    found_item = Asset.query.get(drilling_plat.id)
    if not found_item:
        db.session.add(drilling_plat)
    
    db.session.commit()

