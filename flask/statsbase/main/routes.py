from flask import render_template, request, Blueprint
from statsbase.models import Post

main = Blueprint('main', __name__)


@main.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/teams")
def teams():
	return render_template('teams/index.html', title='Teams')

@main.route("/guards")
def guards():
	return render_template('guards/index.html', title='Teams')