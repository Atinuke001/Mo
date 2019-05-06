import logging.config

import os
from flask import Flask, Blueprint
from rest_api_demo import settings
from rest_api_demo.api.blog.endpoints.posts import ns as blog_posts_namespace
from rest_api_demo.api.blog.endpoints.categories import ns as blog_categories_namespace
from rest_api_demo.api.restplus import api
from rest_api_demo.database import db

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

@app.errorhandler(404)
def page_not_found(error):
    return 'This FERRIS route does not exist'




blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(blog_posts_namespace)
api.add_namespace(blog_categories_namespace)
app.register_blueprint(blueprint)

db.init_app(app)


# def main():
    # initialize_app(app)
    # log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    # app.run(host="0.0.0.0")  # Production Mode
    # app.run(debug=settings.FLASK_DEBUG)  # Dev Mode only


if __name__ == "__main__":
    #initialize_app(app)
    app.run()  # Production Mode

