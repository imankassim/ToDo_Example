from flask import redirect, url_for, render_template, request
from flask_testing import TestCase

#import stuff
from application import app, db
from application.models import ToDos
from application.forms import TaskForm

#class
class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY="shhh it's a secret",
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    #setup
    def setUp(self):
        db.create_all()
        sample1 = ToDos(task="Barbara")
        db.session.add(sample1)
        db.session.commit()

    #to end
    def tearDown(self):
        db.session.remove()
        db.drop_all()

# Read
class TestView(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Barbara', response.data)

    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is the about page', response.data)

# Create

class TestCreate(TestBase):
    def test_create(self):
        response = self.client.post(
            url_for('addtask'),
            data = Todos(task="Ryan", completed=True)
            )
        self.assertIn(b'Ryan', response.data)
