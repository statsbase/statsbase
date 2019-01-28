from flask import render_template, request, Blueprint, Flask
import os

app = Flask(__name__)

players = Blueprint('players', __name__)

@players.route("/players/guards/fta", methods=['GET'])
def guardsfta():
	return render_template('guardsfta.html')





if __name__=='__main__':
	app.run(debug=True)