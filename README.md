# Health-Recommendation-System

📌 Problem Statement

Women have diverse health needs that are often not adequately addressed by generic healthcare approaches. This lack of personalization can lead to suboptimal health outcomes and limited access to relevant services.

🚀 Solution

This project uses Hierarchical Clustering and Gaussian Mixture Models (GMM) to segment women based on their health needs and preferences. By leveraging machine learning, it provides personalized healthcare recommendations, improving accessibility to healthcare services and promoting better health outcomes.

📌 Technologies Used

🎯 Machine Learning & Data Science:
      Hierarchical Clustering, Gaussian Mixture Model (GMM)
      Random Forest Classifier for prediction
      SHAP for explainability

🎯 Backend: Flask (Python)
🎯 Frontend: React (JavaScript)
🎯 Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, SHAP

📌 Machine Learning Pipeline

1. Data Preprocessing:
         Encode categorical features (e.g., Medications, Ethnicity)
         Scale numerical features (e.g., BMI, BP, Sleep)
   
2. Clustering:
         Hierarchical Clustering for initial segmentation
         GMM (Gaussian Mixture Model) for optimal clustering

3. Recommendation Engine:
         Personalized healthcare advice based on cluster, BMI, BP, stress levels, and medications

4. Classification Model:
         Random Forest model predicts clusters for new users

5. Explainability:
         SHAP values provide feature importance insights

📌 Future Enhancements
         🎯 Improve Recommendation Logic using more real-world medical datasets
         🎯 Add More Features (e.g., family history, genetic factors, mental health indicators)
         🎯 Deploy on Cloud for real-world accessibility



Video demo of the app - https://github.com/user-attachments/assets/782160ab-32fb-4c56-8291-91fdcd788cb4

ML model graphs - 
![303876ba-b4f8-4d86-ac9a-96b3b06b0e74](https://github.com/user-attachments/assets/5bd92c1e-995c-4280-8456-34c8ab058ece)
![441196aa-b544-4670-895f-9bcf56e9b11a](https://github.com/user-attachments/assets/699035a5-d91d-4029-9747-454e53869bbf)
