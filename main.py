from flask import Flask, redirect
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Your API routes
@app.route('/api/hello', methods=['GET'])
def hello():
    """
    A sample endpoint that returns a greeting message.
    ---
    responses:
      200:
        description: A successful response
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Hello, world!
    """
    return {'message': 'Hello, world!'}

# Route for the root URL ("/") to redirect to the Swagger UI page
@app.route('/')
def index():
    return redirect('/apidocs')

if __name__ == '__main__':
    app.run(debug=True)
