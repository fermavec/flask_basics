# FLASK Basics

## 1. Basics

### 1.1 Installation:

```sh
python3 -m venv venv
source ./venv/bin/activate
pip install flask
```

### 1.2 Setting up

- Create a directory called app
- Into directory create a file called app.py
- Create the file for a server
- Run

### 1.3 Running server:

```sh
python3 ./app/app.py
```

- To stop the server: ctrl + C

*Note: To understand how the file works please read the file app.py for more information*


### 1.4 Jinja2 and Templates for HTML files

- Create directory called templates into app directory and a file for a template.
- You can work with variable to send from your app to your html file with this format: '{{ variable }}'

*Note: jinja2 is a template engine used by flask and django which help us to renderize HTML documents and let us see them in our web*


### 1.5 Styles and Events

- Create a directory called static into the app directory, then you can create your css or javascript files.
- You can import any file from static directory using as this example: {{ url_for('static', filename='css/index.css') }} in the href parameter in HTML file.

### 1.6 Base template

- To better performance is a good practice to create a template for html files with the next sintaxis: {% block 'name' %} |content| {% endblock %}


### 1.7 Dinamism

- It is importan to define routes which can process parameters. e.g. See function "greeting" in app.py file.

### 1.8 Query string

- You can also send values through the query string in a HTTP request. e.g. See the function "data" in app.py file

### 1.9 Callbacks

- A callback is a method we can execute before and after some HTTP request.