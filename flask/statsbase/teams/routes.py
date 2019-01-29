from flask import render_template, request, Blueprint, Flask
import os

app = Flask(__name__)

teams = Blueprint('teams', __name__, template_folder='teams')

@teams.route("/teams/fta", methods=['GET'])
def teamfta():
	return render_template('teams/index.html')



if __name__=='__main__':
	app.run(debug=True)