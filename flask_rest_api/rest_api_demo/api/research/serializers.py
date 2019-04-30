from flask_restplus import fields
from rest_api_demo.api.restplus import api

research_idea = api.model('Research Idea', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a research idea'),
    'title': fields.String(required=True, description='Research article title'),
    'body': fields.String(required=True, description='Research article content'),
    'pub_date': fields.DateTime,
    'category_id': fields.Integer(attribute='category.id'),
    'category': fields.String(attribute='category.name'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_research_ideas = api.inherit('Page of research ideas', pagination, {
    'items': fields.List(fields.Nested(research_idea))
})

category = api.model('Research category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a research category'),
    'name': fields.String(required=True, description='Category name'),
})

category_with_ideas = api.inherit('Research category with investment ideas', category, {
    'ideas': fields.List(fields.Nested(research_idea))
})
