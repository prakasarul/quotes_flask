from flask import Flask, render_template, request, redirect, url_for
from models import db, Favquotes
from config import BaseConfig, BaseConfigLocal


def create_app():
    app = Flask(__name__)
    config_container = BaseConfig()
    config_local = BaseConfigLocal()  # Initialize config object
    app.config.from_object(config_container)
    db.init_app(app)  # Add this line Before migrate line

    with app.app_context():
        db.create_all()  # Ensure all database tables are created

    @app.route("/")
    def index():
        result = Favquotes.query.all()
        return render_template("index.html", result=result)

    @app.route("/quotes")
    def quotes():
        return render_template("quotes.html")

    @app.route("/process", methods=["POST"])
    def process():
        author = request.form["author"]
        quote = request.form["quote"]
        quotedata = Favquotes(author=author, quote=quote)
        db.session.add(quotedata)
        db.session.commit()
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
