from jinja2 import Environment, PackageLoader, select_autoescape

from controller.html_controller import HTMLController


def main():
    env = Environment(loader=PackageLoader("calculator"),
                      autoescape=select_autoescape())
    template = env.get_template("calculator.html")
    print(template.render(the="variables", go="here"))


def main1():
    from jinja2 import Template

    html = open('templates/calculator.html').read()
    template = Template(html)
    print(template.render(name=u'Петя'))


class Logger:

    def log(self, message):
        print(message)


def create_flask():
    from flask import Flask

    app = Flask(__name__)

    logger = Logger()

    HTMLController(app, logger)

    return app


if __name__ == '__main__':
    app = create_flask()
    app.run(host="0.0.0.0", debug=True)
    # main1()
