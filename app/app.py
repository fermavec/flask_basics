from flask import Flask, render_template, request

app = Flask(__name__)


app.before_request
def callback_before(response):
    print('before request')
    return response


app.after_request
def callback_after():
    print('after request')


# This is a view
# @app.route('/')


def index():
    # To see a callback working
    print('login in')
    # return 'Fer Mavec'
    return render_template('index.html', title="Fer Mavec's Flask App")


@app.route('/contact')
def my_web_contact():
    data = {
        'contact_title': 'Contact',
        'c_header': 'Contact Me',
        'c_web': 'https://fermavec.com',
        'c_social': 'fermavec'
    }
    return render_template('contact.html', data=data)


@app.route('/extended')
def base_extended():
    return render_template('base_extends.html')


@app.route('/languages')
def languages():
    data = {
        'languages':['English', 'Español', 'Italiano']
    }

    return render_template('languages.html', data=data)


@app.route('/greeting/<name>/<int:age>')
def greeting(name, age):
    return 'Hello {0}, you are {1} years old'.format(name, age)


# Work with HTTP
# GET, POST, PUT and DELETE

@app.route('/data')
def get_data():
    # print(request.args)
    value_1 = request.args.get('value_1')
    # the query string: http://127.0.0.1:5005/data?value_1=%27Python%27
    b = request.args.get('value_2')
    # http://127.0.0.1:5005/data?value_1=python&value_2=25

    return 'this is the data {0} and {1}'.format(value_1, b)


if __name__ == '__main__':
    # Another way to create a view without the app decorator
    app.add_url_rule('/', view_func=index)

    # Mode debug=on to automatically update changes, also setting up port as 5005
    app.run(debug=True, port=5005)
