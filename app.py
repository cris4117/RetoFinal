from flask import Flask, render_template, request, jsonify
from pack.modelo import predict_price

app = Flask(__name__)

@app.route("/")
def index():
    source_cities = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Hyderabad', 'Kolkata']
    destination_cities = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Hyderabad', 'Kolkata']

    return render_template("index.html", source_cities=source_cities, destination_cities=destination_cities)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()
            data["days_left"] = int(data["days_left"])  # Convertir a número

        predicted_price = round(predict_price(data))  # 🔹 Ahora es un entero

        return jsonify({
            "airline": data["airline"], 
            "class_type": data["class_type"], 
            "stops": data["stops"], 
            "predicted_price": predicted_price
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
