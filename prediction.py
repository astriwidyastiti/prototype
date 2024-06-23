import joblib
import os

dirname = os.path.dirname(__file__)

model_path = os.path.join(dirname,'model/rdf_model.joblib')
result_target_path = os.path.join(dirname, "model/encoder_target.joblib")

model = joblib.load(model_path)
result_target = joblib.load(result_target_path)

def prediction(data):

    result = model.predict(data.values)
    final_result = result_target.inverse_transform(result)[0]

    print(final_result)
    return final_result
    