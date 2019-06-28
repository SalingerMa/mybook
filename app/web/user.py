# -*- coding: utf-8 -*-
from flask import request, redirect, url_for, render_template

from app.model.base import db
from app.model.user import User
from app.web import web
from app.form.user import RegisterForm


@web.route('/register', methods=['GET', 'POST'])
def register():
    ha = request.form
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
    return render_template('register.html', form=form)