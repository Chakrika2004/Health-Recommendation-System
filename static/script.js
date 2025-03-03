document.getElementById("healthForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    // Get input values
    let age = parseInt(document.getElementById("age").value);
    let bmi = parseFloat(document.getElementById("bmi").value);
    let bp = parseFloat(document.getElementById("bp").value);
    let sleep = parseFloat(document.getElementById("sleep").value);
    let stress = parseInt(document.getElementById("stress").value);
    let exercise = parseFloat(document.getElementById("exercise").value);
    let cholesterol = parseFloat(document.getElementById("cholesterol").value);
    let heartRate = parseFloat(document.getElementById("heart_rate").value);
    let dietScore = parseFloat(document.getElementById("diet_score").value);
    let hydrationLevel = parseFloat(document.getElementById("hydration_level").value);
    let medications = document.getElementById("medications").value === "Yes"; // Convert to Boolean

    // Validation rules with real-time input feedback
    let errors = [];
    let resultElement = document.getElementById("result");
    resultElement.innerHTML = ""; // Clear previous messages

    function validate(field, condition, message) {
        if (condition) {
            errors.push(message);
            field.style.border = "2px solid red";
        } else {
            field.style.border = "1px solid #ccc";
        }
    }

    // Apply validation
    validate(document.getElementById("age"), age < 1 || age > 120, "Age must be between 1 and 120.");
    validate(document.getElementById("bmi"), bmi < 10 || bmi > 50, "BMI must be between 10 and 50.");
    validate(document.getElementById("bp"), bp < 50 || bp > 200, "Blood Pressure must be between 50 and 200.");
    validate(document.getElementById("sleep"), sleep < 1 || sleep > 12, "Sleep hours must be between 1 and 12.");
    validate(document.getElementById("stress"), stress < 1 || stress > 10, "Stress level must be between 1 and 10.");
    validate(document.getElementById("exercise"), exercise < 0 || exercise > 10, "Exercise hours should be between 0 and 10 per week.");
    validate(document.getElementById("diet_score"), dietScore < 1 || dietScore > 10, "Diet Score must be between 1 and 10.");
    validate(document.getElementById("hydration_level"), hydrationLevel < 1 || hydrationLevel > 10, "Hydration Level must be between 1 and 10.");
    validate(document.getElementById("cholesterol"), cholesterol < 50 || cholesterol > 300, "Cholesterol level must be between 50 and 300.");
    validate(document.getElementById("heart_rate"), heartRate < 40 || heartRate > 200, "Heart Rate must be between 40 and 200.");

    // Display error messages
    if (errors.length > 0) {
        resultElement.innerHTML = `<span style="color:red;">${errors.join("<br>")}</span>`;
        resultElement.scrollIntoView({ behavior: "smooth" }); // Bring error messages into view
        return; // Stop execution if there are errors
    }

    // Prepare data for sending
    let requestData = {
        age, bmi, bp, sleep, stress, exercise, cholesterol, 
        heart_rate: heartRate, diet_score: dietScore, hydration_level: hydrationLevel, medications
    };

    // Send request to Flask API
    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultElement.innerHTML = `<span style="color:red;">${data.error}</span>`;
        } else {
            resultElement.innerHTML = `<span style="color:green; font-weight:bold;">${data.recommendation}</span>`;
        }
        resultElement.scrollIntoView({ behavior: "smooth" });
    })
    .catch(error => {
        resultElement.innerHTML = `<span style="color:red;">Error: ${error.message}</span>`;
    });
});

// Real-time input validation to remove red border when user types
document.querySelectorAll("input").forEach(input => {
    input.addEventListener("input", function () {
        this.style.border = "1px solid #ccc"; // Reset border on valid input
    });
});
