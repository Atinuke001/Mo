import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.research.business import create_research_idea, update_idea, delete_idea
from rest_api_demo.api.research.serializers import research_idea, page_of_research_ideas
from rest_api_demo.api.research.parsers import pagination_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Idea

log = logging.getLogger(__name__)

ns = api.namespace('research/ideas', description='Operations related to research ideas')


@ns.route('/')
class IdeasCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_research_ideas)
    def get(self):
        """
        Returns list of research ideas.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        ideas_query = Ideas.query
        ideas_page = ideas_query.paginate(page, per_page, error_out=False)

        return ideas_page

    @api.expect(research_idea)
    def post(self):
        """
        Creates a new research idea.
        """
        create_research_idea(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Idea not found.')
class IdeaItem(Resource):

    @api.marshal_with(research_idea)
    def get(self, id):
        """
        Returns a research idea.
        """
        return Idea.query.filter(Idea.id == id).one()

    @api.expect(research_idea)
    @api.response(204, 'Idea successfully updated.')
    def put(self, id):
        """
        Updates a research idea.
        """
        data = request.json
        update_idea(id, data)
        return None, 204

    @api.response(204, 'Idea successfully deleted.')
    def delete(self, id):
        """
        Deletes research idea.
        """
        delete_idea(id)
        return None, 204


@ns.route('/archive/<int:year>/')
@ns.route('/archive/<int:year>/<int:month>/')
@ns.route('/archive/<int:year>/<int:month>/<int:day>/')
class IdeasArchiveCollection(Resource):

    @api.expect(pagination_arguments, validate=True)
    @api.marshal_with(page_of_research_ideas)
    def get(self, year, month=None, day=None):
        """
        Returns list of research ideas from a specified time period.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
        end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
        ideas_query = Idea.query.filter(Idea.pub_date >= start_date).filter(Idea.pub_date <= end_date)

        ideas_page = ideas_query.paginate(page, per_page, error_out=False)

        return ideas_page
