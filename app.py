from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/jobs')
def jobs():
    return 'jobs'

@app.route('/companies')
def companies():
    return 'companies'


if __name__ == '__main__':
    app.run()
