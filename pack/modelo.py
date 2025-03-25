import tensorflow as tf
import joblib

# Cargar modelos y preprocesadores
business_model = tf.keras.models.load_model("model/model_business.keras")
economy_model = tf.keras.models.load_model("model/model_economy.keras")

business_feature_encoder = joblib.load("model/business_feature_encoder.pkl")
economy_feature_encoder = joblib.load("model/economy_feature_encoder.pkl")

business_scaler = joblib.load("model/scaler_business.pkl")
economy_scaler = joblib.load("model/scaler_economy.pkl")

def predict_price(data):
    """Predice el precio del vuelo basado en los datos de entrada."""
    try:
        class_type = data["class_type"]

        if class_type == "Business":
            model = business_model
            feature_encoder = business_feature_encoder
            scaler = business_scaler
        else:
            model = economy_model
            feature_encoder = economy_feature_encoder
            scaler = economy_scaler

        from pack.procesamiento import preprocess_data
        preprocessed_data = preprocess_data(data, feature_encoder, scaler)

        prediction = model.predict(preprocessed_data)
        return float(prediction[0][0])

    except Exception as e:
        return {"error": f"Error en la predicción: {str(e)}"}
