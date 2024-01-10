import uuid
from flask import render_template, request, redirect, url_for, flash

from . import newbook
from ..forms.new_book import NewBookForm
from app import db, login_required, current_user
from models.model import Books


@newbook.route('/newbook', methods=["POST", "GET"])
@login_required
def newbook():
    if not current_user.is_admin:
        flash("You do not have permission to access this page.", 'error')
        return redirect(url_for('market.market'))

    form = NewBookForm()

    if request.method == 'POST' and form.validate_on_submit():

        new_book = Books(
            id=str(uuid.uuid4()),
            title=form.title.data,
            author=form.author.data,
            category=form.category.data,
            language=form.language.data,
            pages=form.pages.data,
            year=form.year.data,
            link=form.link.data
        )

        try:
            db.session.add(new_book)
            db.session.commit()

            form.title.data = ''
            form.author.data = ''
            form.category.data = ''
            form.language.data = ''
            form.pages.data = ''
            form.year.data = ''
            form.link.data = ''

            flash(
                f"New Book Added successfully {new_book.title} 📕", 'success')

            return redirect(url_for('market.market'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error {str(e)} occurred while adding the book. Please try again.", 'error')

    return render_template('forms/new_book.html', form=form)