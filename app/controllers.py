# Import flask dependencies
from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for,
    jsonify,
)

from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models import Asset, asset_schema, item_schema, Item

mod_asset = Blueprint("assets", __name__, url_prefix="/api/assets")


# Set the route and accepted methods
@mod_asset.route("/", methods=["GET"])
def get_all():
    all_asset = Asset.query.all()
    data = asset_schema.dump(all_asset, many=True).data
    for asset in data:
        actual_items = []
        for item in asset['items']:
            actual_item = Item.query.get(item)
            actual_items.append(item_schema.dump(actual_item).data)
        asset['items'] = actual_items
    return jsonify({"data": data})


@mod_asset.route("/", methods=["POST"])
def create_asset():
    new_asset = asset_schema.load(request.get_json()).data
    
    db.session.add(new_asset)
    db.session.commit()
    return asset_schema.jsonify(new_asset)


@mod_asset.route("/<id>", methods=["PUT"])
def update_asset(id):
    found_item = Asset.query.get(id)
    if not found_item:
        return jsonify({"error": "Not found!"}), 404
    updated_asset_json = request.get_json()
    updated = Asset.query.filter_by(id=id).update(updated_asset_json)
    db.session.commit()
    return asset_schema.jsonify(updated)

@mod_asset.route("/<id>", methods=["DELETE"])
def delete_asset_by_id(id):
    found_item = Asset.query.get(id)
    if not found_item:
        return jsonify({"error": "Not found!"}), 404
    db.session.delete(found_item)
    db.session.commit()
    return asset_schema.jsonify(found_item)
