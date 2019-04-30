from rest_api_demo.database import db
from rest_api_demo.database.models import Idea, Category


def create_research_idea(data):
    title = data.get('title')
    body = data.get('body')
    category_id = data.get('category_id')
    category = Category.query.filter(Category.id == category_id).one()
    post = Idea(title, body, category)
    db.session.add(idea)
    db.session.commit()


def update_idea(idea_id, data):
    idea = Idea.query.filter(Idea.id == idea_id).one()
    idea.title = data.get('title')
    idea.body = data.get('body')
    category_id = data.get('category_id')
    idea.category = Category.query.filter(Category.id == category_id).one()
    db.session.add(idea)
    db.session.commit()


def delete_idea(idea_id):
    idea = Idea.query.filter(Idea.id == idea_id).one()
    db.session.delete(idea)
    db.session.commit()


def create_category(data):
    name = data.get('name')
    category_id = data.get('id')

    category = Category(name)
    if category_id:
        category.id = category_id

    db.session.add(category)
    db.session.commit()


def update_category(category_id, data):
    category = Category.query.filter(Category.id == category_id).one()
    category.name = data.get('name')
    db.session.add(category)
    db.session.commit()


def delete_category(category_id):
    category = Category.query.filter(Category.id == category_id).one()
    db.session.delete(category)
    db.session.commit()
