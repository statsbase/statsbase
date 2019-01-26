from flask import render_template, request, Blueprint, Flask
import os
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'bokeh')
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates')

app = Flask(__name__, template_folder=TEMPLATE_PATH)

teams = Blueprint('teams', __name__)

@teams.route("/teams/fta", methods=['GET'])
def teamfta():
	return render_template('teamfta.html')





if __name__=='__main__':
	app.run(debug=True)