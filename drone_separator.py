import os
import cv2
import numpy as np
from keras.models import load_model


def classify_drones(input_dir, output_dir):
    # Define the class labels
    class_labels = ["civil", "cargo", "military"]

    # Load the pre-trained Keras model
    model = load_model("keras_model.h5")

    # Set the output directories
    output_dirs = {}
    for label in class_labels:
        output_dirs[label] = os.path.join(output_dir, label)
        os.makedirs(output_dirs[label], exist_ok=True)

    # Loop through each image in the input directory and classify the drone
    for filename in os.listdir(input_dir):
        # Load the input image and preprocess it
        img = cv2.imread(os.path.join(input_dir, filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224, 224))
        img = img.astype("float32") / 255.0
        img = np.expand_dims(img, axis=0)

        # Use the model to classify the image
        predictions = model.predict(img)
        class_index = np.argmax(predictions[0])
        class_label = class_labels[class_index]

        # Save the image to the appropriate output directory
        output_path = os.path.join(output_dirs[class_label], filename)
        cv2.imwrite(
            output_path,
            cv2.cvtColor(
                cv2.imread(os.path.join(input_dir, filename)), cv2.COLOR_BGR2RGB
            ),
        )
