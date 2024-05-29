#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, request, render_template, g
from flask_babel import Babel, _
from pytz import timezone, exceptions


class Config(object):
    """config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Returns user info if id is present"""
    return users.get(int(user_id))


@app.before_request
def before_request():
    """finds user in any"""
    user_id = request.args.get("login_as")
    if user_id:
        g.user = get_user(user_id)


def get_locale():
    lang = request.args.get("locale")
    user = g.get("user")

    if lang and lang in Config.LANGUAGES:
        return lang
    elif user and user.get("locale") in Config.LANGUAGES:
        return user.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone():
    """gets timezone information"""
    tz = request.args.get("timezone")
    user = getattr(g, "user", None)
    user_tz = user.get("timezone")
    try:
        if tz and timezone(tz):
            return tz
        elif user and user_tz and timezone(user_tz):
            return user_tz
        else:
            return "UTC"

    except exceptions.UnknownTimeZoneError:
        return "UTC"


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def index():
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(debug=True)
