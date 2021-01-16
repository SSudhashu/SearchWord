from flask import Flask

app = Flask(__name__)


@ app.route('/')
def first():
    import SearchWord
    return '!Done'

# driver function
if __name__ == '__main__':

    app.run(debug=True)