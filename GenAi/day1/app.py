from flask import Flask, render_template, request, jsonify
from optimized import optimized_quick_sort

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/sort", methods=["POST"])
def sort():
    data = request.get_json()
    numbers = [float(num) for num in data["numbers"].split(",") if num.strip()]
    sorted_numbers = optimized_quick_sort(numbers)
    return jsonify({"sorted": sorted_numbers})


if __name__ == "__main__":
    app.run(debug=True)
