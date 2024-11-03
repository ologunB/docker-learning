import pandas as pd
from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('dataset/housing.csv')
X = data[['Area', 'Bedrooms', 'Bathrooms']]  # Features
y = data['Price']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Create a Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
