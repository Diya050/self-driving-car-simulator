# Self-Driving Car Simulator

A deep learning–based autonomous driving project using a **Convolutional Neural Network (CNN)** to predict steering angles from real-time road images.  
The system runs through a **Flask + Socket.IO** server and interacts with the **Udacity Self-Driving Car Simulator** to drive the vehicle autonomously.

---

## Features

- Real-time communication with Udacity Self-Driving Car Simulator  
- CNN-based steering angle prediction  
- Flask + Socket.IO integration for model control  
- Image preprocessing pipeline  
- Live telemetry monitoring (steering, throttle, speed)

---

## Model Architecture

This project implements the **NVIDIA End-to-End CNN architecture** for self-driving cars, designed to predict the **steering angle** directly from raw road images.

### Architecture Overview

The model consists of a series of **convolutional** and **fully connected layers** that extract spatial features and learn driving behavior patterns.

| Layer Type     | Filters/Units | Kernel Size | Strides | Activation | Description                                           |
| -------------- | ------------- | ----------- | ------- | ---------- | ----------------------------------------------------- |
| Conv2D         | 24            | 5×5         | 2×2     | ELU        | Extracts low-level road features like edges and lanes |
| Conv2D         | 36            | 5×5         | 2×2     | ELU        | Captures mid-level features such as curves            |
| Conv2D         | 48            | 5×5         | 2×2     | ELU        | Detects complex structures like lane intersections    |
| Conv2D         | 64            | 5×5         | —       | ELU        | Focuses on finer spatial patterns                     |
| Flatten        | —             | —           | —       | —          | Converts feature maps into a single vector            |
| Dense          | 100           | —           | —       | ELU        | Learns high-level driving decisions                   |
| Dense          | 50            | —           | —       | ELU        | Refines learned relationships                         |
| Dense          | 10            | —           | —       | ELU        | Narrowed decision representation                      |
| Dense (Output) | 1             | —           | —       | Linear     | Predicts final steering angle                         |

### Compilation

The model is compiled using:

```python
optimizer = Adam(learning_rate=1e-3)
loss = 'mse'  # Mean Squared Error
```
---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Diya050/self-driving-car-simulator.git
cd self-driving-car-simulator/
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Server

```bash
python drive.py
```

### 4. Launch the Simulator

* Open the **Udacity Self-Driving Car Simulator**
* Select **Autonomous Mode**
* The car should start driving automatically once connected

---

## Folder Structure

```
self-driving-car-simulator/
│
├── self_driving_car.ipynb    # Model training
├── drive.py                  # Flask + Socket.IO server
├── model
      └── model.h5            # Trained model weights 
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

## Sample Output

```python
print('{} {} {}'.format(steering_angle, throttle, speed))
```

```
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 53ms/step
-0.20981238782405853 0.7740466666666667 3.3893
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 54ms/step
-0.2079448252916336 0.7153933333333333 4.2691
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 51ms/step
-0.2124561071395874 0.6496933333333333 5.2546
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 41ms/step
-0.16783994436264038 0.5904266666666667 6.1436
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 54ms/step
-0.15334530174732208 0.5212866666666667 7.1807
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 51ms/step
```

---

## Requirements

* Python 3.8+
* TensorFlow / Keras
* Flask
* Socket.IO
* OpenCV
* NumPy

