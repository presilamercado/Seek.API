from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()



# echo "# Seek.API" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin https://github.com/presilamercado/Seek.API.git
# git push -u origin master