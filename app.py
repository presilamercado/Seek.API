from flask import Flask

app = Flask(__name__)


@app.route('/jobs')
def jobs():
    return 'jobs'

@app.route('/companies')
def companies():
    return 'companies'


if __name__ == '__main__':
    app.run()
