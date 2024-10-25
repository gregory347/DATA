import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import matplotlib.pyplot as plt 

gregory_path = r'C:\Users\User\OneDrive\Desktop\dataset\LINEAR REGRESSION\data\accidents-database-.csv'
gregory = pd.read_csv(gregory_path)


gregory['Gender'] = gregory['Gender'].fillna('UNKNOWN')
gregory['Age'] = gregory['Age'].fillna(gregory['Age'].median())  

bins = [0, 17, 30, 50, 100]
labels = ['0-17', '18-30', '31-50', '51+']
gregory['Age_band_of_driver'] = pd.cut(gregory['Age'], bins=bins, labels=labels, right=False)

gregory['Sex_of_driver'] = gregory['Gender']

gregory['Type_of_vehicle'] = gregory['MV INVOLVED'].apply(lambda x: x.split()[1] if isinstance(x, str) else 'UNKNOWN')

severity_mapping = {
    'Slight Injury': 1,
    'Serious Injury': 2,
    'Fatal Injury': 3
}
gregory['Accident_severity'] = gregory['Brief Accident Details'].apply(
    lambda x: 3 if 'FATAL' in x.upper() else 2 if 'SERIOUS' in x.upper() else 1
)

gregory = gregory.dropna(subset=['Accident_severity'])

gregory['Educational_level'] = gregory['Educational_level'].fillna(gregory['Educational_level'].mode()[0])
gregory['Driving_experience'] = gregory['Driving_experience'].fillna(gregory['Driving_experience'].mode()[0])
gregory['Type_of_vehicle'] = gregory['Type_of_vehicle'].fillna(gregory['Type_of_vehicle'].mode()[0])

categorical_features = ['Age_band_of_driver', 'Sex_of_driver', 'Educational_level',
                        'Driving_experience', 'Type_of_vehicle']

preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(), categorical_features)],
    remainder='passthrough'  
)

X = gregory[categorical_features]
y = gregory['Accident_severity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

model_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                 ('regressor', LinearRegression())])
model_pipeline.fit(X_train, y_train)

y_pred = model_pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

plt.figure(figsize=(10, 6))
severity_counts = gregory['Accident_severity'].value_counts().sort_index()
plt.bar(severity_counts.index, severity_counts.values, color='skyblue')
plt.xticks(severity_counts.index)
plt.xlabel('Accident Severity')
plt.ylabel('Count')
plt.title('Distribution of Accident Severity')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

model_filename = 'road_accident_severity_model.pkl'
joblib.dump(model_pipeline, model_filename)
print(f"Model saved to {model_filename}")

loaded_model_pipeline = joblib.load(model_filename)

hypothetical_data = pd.DataFrame({
    'Age_band_of_driver': ['18-30'],
    'Sex_of_driver': ['Male'],
    'Educational_level': ['Above high school'],
    'Driving_experience': ['1-2yr'],
    'Type_of_vehicle': ['Automobile']
})

hypothetical_data_processed = preprocessor.transform(hypothetical_data)

predicted_severity = loaded_model_pipeline.predict(hypothetical_data_processed)
print(f"Predicted accident severity: {predicted_severity[0]}")

