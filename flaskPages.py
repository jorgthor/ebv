from flask import Flask, render_template
import sankey
import sqlData

app = Flask(__name__)


@app.route('/')
def index():
    sankey.sampeFig()
    return 'Hello World!'


@app.route('SelectRamActivities')
def SelectRamActivities():
    return render_template('ramActivities.html')


@app.route('ramActivities')
def ramActivities():
    return render_template('ramActivities.html')


if __name__ == '__main__':
    app.run(debug=True)
