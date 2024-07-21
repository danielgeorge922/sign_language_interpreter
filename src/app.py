# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/translate', methods=['POST'])
# def translate_string():
#     data = request.get_json()
#     translated_string = data['string'][::-1]  # Reverse the string as a placeholder translation
#     return jsonify({'translated': translated_string})

# if __name__ == '__main__':
#     app.run(debug=True)
