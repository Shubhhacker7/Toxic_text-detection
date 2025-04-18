from flask import Flask, request, jsonify, render_template
import joblib  # or any other library you used to save your model

app = Flask(__name__)

# Load your model (make sure to replace 'path_to_your_model.pkl' with the actual path)
model, vectorizer = joblib.load("C:/Users/mrsau/OneDrive/Desktop/minorproject/toxic_detection_model.joblib")

@app.route('/')
def home():
    return render_template("index.html")
    

@app.route('/classify', methods=['POST'])
def classify_comment():
    data = request.get_json()
    comment = data['comment']
    
    # If you have a vectorizer, transform the comment before prediction
    comment_vectorized = vectorizer.transform([comment])  # This creates a 2D array
    prediction = model.predict(comment_vectorized)  # Use the model to predict
    
    # Convert the prediction to a standard Python int
    is_toxic = int(prediction[0])  # Assuming the model returns a single value
    
    return jsonify({'isToxic': is_toxic})
if __name__ == '__main__':
    app.run(debug=True)