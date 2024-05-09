import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import pandas as pd

# Load your pre-trained model
model = tf.keras.models.load_model('classify.h5')

# Define function to preprocess image
def preprocess_image(image):
    resized_image = image.resize((64, 64))
    img_array = np.array(resized_image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Create Streamlit app
st.title('Skin Cancer Classification')

# Allow user to upload an image
uploaded_image = st.file_uploader('Upload an image', type=['jpg', 'png'])

if uploaded_image is not None:
    # Display uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess image
    preprocessed_image = preprocess_image(image)

    # Make prediction
    result = model.predict(preprocessed_image)
    #st.write(result[0])

    # Get the index of the class with the highest probability
    predicted_class_index = np.argmax(result, axis=1)[0]

    # Map the index to the corresponding class label
    class_labels = [
        "Melanocytic nevi",
        "Melanoma",
        "Benign keratosis-like lesions",
        "Basal cell carcinoma",
        "Actinic keratoses",
        "Vascular lesions",
        "Dermatofibroma"
    ]
    

   # Create a DataFrame with class labels and their corresponding probabilities
    df = pd.DataFrame({'Class': class_labels, 'Probability': result[0]})

    # Plot the probabilities as a bar chart
    st.bar_chart(df.set_index('Class'))
    # Print the predicted class label
    predicted_class_label = class_labels[predicted_class_index]
    st.write("Predicted Class:", predicted_class_label)
