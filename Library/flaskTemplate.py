from Flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/addUsers", methods=['POSt'])
def add_users():
    try:
        reqBody  = request.get_json()
        # process the request


    except Exception as e:
        # Logs the error
        return "400 Bad Request", 400
    

if __name__ == '__main__':
    app.run(port=5001, debug=True)

