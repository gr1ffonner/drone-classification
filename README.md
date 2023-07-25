# Drone Classification with GUI
![image](https://github.com/gr1ffonner/drone_separation/assets/112549266/b1b25260-5b6b-4ede-b2c7-c277ca863699)

## Features
Classifies drones into 3 different categories (cargo, civil and military) based on the trained model.
Provides a user-friendly GUI for easy interaction and inference.
Uses Google Teachable Machine for training the classification model.

## Tech Stack
  - Google Teachable Machine: A web-based platform that simplifies the process of training machine learning models for image classification.
  - Keras: An open-source deep learning framework written in Python, built on top of TensorFlow, for creating and training deep neural networks.
  - Tkinter: The standard Python interface to the Tk GUI toolkit, used for building the graphical user interface.

## Installation

To use the Cigarette Detector, follow these installation steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/gr1ffonner/drone_separation.git
   cd drone_separation
2. Activate venv
   
   ```bash
   python -m venv venv
   source venv/bin/activate
3. Install dependencies
   
   ```bash
   pip install -r reqs.txt

## Usage 
```bash
   python gui.py
```
After this command all that you need is to specify two pathes for source data and the outpul folder and then click on the run button!!
