from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load ML model and preprocessing tools
with open("model/health_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def recommend_healthcare(age, cluster, bmi, bp, sleep, stress, hydration, exercise, diet_score, cholesterol, heart_rate, medications):
    recommendations = []

    # 1️⃣ Age-based recommendations  
    if age > 50:
        recommendations.append("Prioritize balanced nutrition, regular checkups, and adequate rest.")
        if age > 80:
            recommendations.append("Engage in light activities like walking and stretching.")
    else:
        recommendations.append("Stay active and maintain a healthy lifestyle.")

    # 2️⃣ Hydration  
    if hydration < 5:
        recommendations.append("Drink more water to stay hydrated.")
    elif hydration > 8:
        recommendations.append("Your hydration is optimal; keep it up!")
    if hydration == 10:
        recommendations = [r for r in recommendations if "hydration" not in r]

    # 3️⃣ Stress Management  
    if stress > 6:
        recommendations.append("Engage in relaxing activities like playing games, music, or spending time with loved ones.")
        if stress > 8:
            recommendations.append("Try meditation or deep breathing exercises to manage stress effectively.")

    # 4️⃣ Blood Pressure  
    if bp < 60:
        recommendations.append("Monitor BP regularly; low BP can cause dizziness. Increase salt intake slightly if needed.")
    elif bp > 140:
        recommendations.append("Reduce salt intake, practice relaxation, and engage in light exercise.")

    # 5️⃣ Sleep Optimization  
    if sleep < 6:
        recommendations.append("Ensure at least 7-8 hours of sleep for proper recovery.")
    elif sleep > 9:
        recommendations.append("Avoid oversleeping; try engaging in morning exercise.")

    # 6️⃣ Exercise Recommendations  
    if age < 50:
        if exercise < 3:
            recommendations.append("Try to engage in at least 3-5 hours of exercise per week for better health.")
    elif age > 50 and exercise > 5:
        recommendations.append("Avoid excessive exercise; opt for light stretching and walking.")

    # 7️⃣ BMI and Weight Management  
    if bmi > 30:
        recommendations.append("Focus on a nutrient-dense diet and regular activity to manage weight.")
    elif bmi < 18.5:
        recommendations.append("Increase protein and healthy fats to maintain a healthy weight.")

    # 8️⃣ Cholesterol Levels  
    if cholesterol > 200:
        recommendations.append("Avoid fried foods and include fiber-rich foods in your diet.")
    elif cholesterol < 50:
        recommendations.append("Include healthy fats like nuts, avocados, and fish in your diet.")

    # 9️⃣ Heart Rate  
    if heart_rate < 50:
        recommendations.append("Ensure you are not overexerting yourself; monitor for dizziness or fatigue.")
    elif heart_rate > 100:
        recommendations.append("Reduce caffeine intake and engage in stress-reducing activities.")

    # 🔟 Diet Score  
    if diet_score < 5:
        recommendations.append("Improve your diet by eating more fruits, vegetables, and whole grains.")
    elif diet_score > 8:
        recommendations.append("Great job on maintaining a healthy diet!")

    # 1️⃣1️⃣ Medications Compliance  
    if medications:
        recommendations.append("Ensure medication compliance and follow doctor's advice.")

    # Return final recommendation  
    return " ".join(recommendations) if recommendations else "You're on track! Maintain your healthy habits. 🚀"


# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Validate input data
    try:
        features = np.array([[float(data["age"]), float(data["bmi"]), float(data["bp"]), 
                              float(data["sleep"]), float(data["stress"]),
                              float(data["exercise"]), float(data["cholesterol"]), 
                              float(data["heart_rate"]), float(data["diet_score"]), 
                              float(data["hydration_level"])]])
    except ValueError:
        return jsonify({"error": "Invalid input values. Please enter numerical values."}), 400

    # Scale features
    features_scaled = scaler.transform(features)

    # Predict cluster
    cluster = model.predict(features_scaled)[0]

    # Generate recommendation
    recommendation = recommend_healthcare(
        float(data["age"]), cluster, float(data["bmi"]), float(data["bp"]),
        float(data["sleep"]), float(data["stress"]), float(data["hydration_level"]),
        float(data["exercise"]), float(data["diet_score"]), float(data["cholesterol"]), 
        float(data["heart_rate"]), data["medications"] == "Yes"
    )

    return jsonify({"recommendation": recommendation})

if __name__ == "__main__":
    app.run(debug=True)
