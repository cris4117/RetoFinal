import pandas as pd

def preprocess_data(data, column_preprocessor, scaler):
    try:
        input_df = pd.DataFrame({
            "airline": [data["airline"]],
            "source_city": [data["source_city"]],
            "departure_time": ["Morning"],  # Valor por defecto
            "stops": [data["stops"]],
            "arrival_time": ["Afternoon"],  # Valor por defecto
            "destination_city": [data["destination_city"]],
            "days_left": [data["days_left"]],
            "duration": [0.0],  # Valor por defecto
            "price": [0.0]  # Valor por defecto
        })

        preprocessed_data = column_preprocessor.transform(input_df)

        expected_features = scaler.mean_.shape[0]
        actual_features = preprocessed_data.shape[1]

        if actual_features > expected_features:
            print(f"⚠️ Se detectaron más columnas ({actual_features}) de las esperadas ({expected_features}), recortando.")
            preprocessed_data = preprocessed_data[:, :expected_features]
        elif actual_features < expected_features:
            raise ValueError(f"⚠️ Faltan columnas: generadas {actual_features}, pero se esperaban {expected_features}.")

        scaled_data = scaler.transform(preprocessed_data)
        return scaled_data

    except Exception as e:
        raise ValueError(f"Error en el preprocesamiento: {str(e)}")