# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the model
model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Print some predictions and their corresponding true labels
print("\nSample Predictions vs True Labels:")
for i in range(5):
    print(f"Prediction: {iris.target_names[y_pred[i]]}, True Label: {iris.target_names[y_test[i]]}")

# Example new data point
new_data = [[5.1, 3.5, 1.4, 0.2]]  # A new sample with the same features as the Iris dataset

# Standardize the new data
new_data = scaler.transform(new_data)

# Predict the class of the new data point
prediction = model.predict(new_data)
print(f"\nPredicted class for new data point: {iris.target_names[prediction[0]]}")

# Print a classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Print a confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
