from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify, abort
from statsbase import db
from statsbase.models import Census
from sqlalchemy import func

api = Blueprint('api', __name__)

@api.route("/api/census/name/<string:name>", methods=['GET', 'POST'])
def  retrieve_name(name):
    result = Census.query.filter(func.lower(Census.name).like("%" + name + "%")).all()
    return jsonify(census = [i.serialize for i in result])

@api.route("/api/census/id/<int:id>", methods=['GET', 'POST'])
def  retrieve_id(id):
    result = Census.query.filter_by(id=id).all()
    return jsonify(census = [i.serialize for i in result])
