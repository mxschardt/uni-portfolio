from flask import render_template


class UserView:

    @staticmethod
    def render_page(data):
        return render_template('extended_layout.html', name=data)


class IndexView:

    @staticmethod
    def render_page():
        return render_template('layout.html')
