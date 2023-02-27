from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

from flask_app.controllers import users
from flask_app.controllers import recipes 

# from flask_app.controllers import users, recipes
# from flask import render_template, session, redirect, request

if __name__ == "__main__":
    app.run(debug = True)