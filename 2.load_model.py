import pickle

# Open the file in read mode (rb = read binary)
with open("clf.pkl", "rb") as file:
    model = pickle.load(file)  # Load the trained model

print("Model loaded successfully!")
