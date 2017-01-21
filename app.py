from flask import Flask

api = Flask(__name__)


@api.route('/')
def stylishly():
    return "Stay stylish!"


if __name__ == '__main__':
    api.run(debug=True)
