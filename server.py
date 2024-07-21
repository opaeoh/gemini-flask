import google.generativeai as genai
from flask import Flask, request, jsonify, abort


from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


api_key = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=api_key)


@app.route("/generate_text", methods=["POST"])
def generate_text():
    if request.method == "POST":
        prompt = request.json.get("prompt")
        if prompt is None:
            abort(400, message="Missing required field: 'prompt'")

        try:
            response = genai.text(prompt=prompt)
            return jsonify({"text": response.text})
        except Exception as e:
            abort(500, message=f"Error generating text: {str(e)}")

    return abort(405, message="Method not allowed")


if __name__ == "__main__":
    app.run(debug=True)
