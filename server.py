from flask import Flask
import article_collection

FLASK_APP = Flask(__name__)
@FLASK_APP.route('/')

def main():
    """ Used for health check """
    return 'OK'

@FLASK_APP.route('/output')
def output():
    """ Main rest function """
    return(article_collection())

if __name__ == '__main__':
    FLASK_APP.run(host='0.0.0.0', port='8080')


