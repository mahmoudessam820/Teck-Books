from flask import (Blueprint, render_template, abort,
                   request, redirect, flash, url_for)
from jinja2 import TemplateNotFound
from forms.new_book_form import NewBook
from models.model import Books, db


new_book_bp: Blueprint = Blueprint(
    'new_book_bp', __name__, template_folder='templates')


@new_book_bp.route('/newbook', methods=['GET', 'POST'])
def newbook() -> None:
    try:
        form = NewBook()

        if form.validate_on_submit and request.method == 'POST':

            new_book = Books(
                name=form.name.data,
                author=form.author.data,
                category=form.category.data,
                language=form.language.data,
                pages=form.pages.data,
                published=form.published.data,
                link=form.link.data
            )

            db.session.add(new_book)
            db.session.commit()
            flash(
                f"New Book Added successfully {new_book.name} 📕", 'success')
            return redirect(url_for('market_bp.market'))

        return render_template('forms/new_book.html', form=form)

    except TemplateNotFound:
        abort(404)