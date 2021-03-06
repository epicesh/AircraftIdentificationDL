import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from Site.db import get_db

views = Blueprint('views', __name__, url_prefix='/')

@views.route('about')
def about():
    render_template('')