
# Human Activity Recognition Using Support Vector Machine

This project focuses on classifying human activities such as walking, sitting, standing, and running using sensor data collected from smartphones. The model utilizes the Support Vector Machine (SVM) algorithm to accurately detect and classify these activities, enabling applications in health monitoring, fitness tracking, and context-aware systems.

## 📂 Project Structure

```
Humanactivity_recoginition/
│
├── model/
│   └── trained_model.pkl       # Trained SVM model for activity classification
│
├── static/
│   └── style.css               # CSS file for styling the web interface
│
├── templates/
│   └── index.html              # HTML template for the web interface
│
├── Human_Activity_Recognition_Using_Smartphones_Data.csv  # Dataset containing sensor data
│
├── app.py                      # Flask application for deploying the model as a web service
└── model.training.ipynb         # Jupyter notebook for data preprocessing, model training, and evaluation
```

## 📊 Dataset Overview

The `Human_Activity_Recognition_Using_Smartphones_Data.csv` dataset includes the following features:

- **tBodyAcc-mean-X**: Mean of the body acceleration signal in the X direction
- **tBodyAcc-mean-Y**: Mean of the body acceleration signal in the Y direction
- **tBodyAcc-mean-Z**: Mean of the body acceleration signal in the Z direction
- **tGravityAcc-mean-X**: Mean of the gravity acceleration signal in the X direction
- **tGravityAcc-mean-Y**: Mean of the gravity acceleration signal in the Y direction
- **tGravityAcc-mean-Z**: Mean of the gravity acceleration signal in the Z direction
- **activity**: The activity label (walking, sitting, standing, running)

## ⚙️ Support Vector Machine (SVM)

The Support Vector Machine is a supervised machine learning algorithm used for classification tasks. It works by finding the hyperplane that best separates the data into different classes.

### Key Concepts:

- **Hyperplane**: A decision boundary that separates different classes in the feature space.
- **Support Vectors**: Data points that are closest to the hyperplane and influence its position.
- **Kernel Trick**: A method to transform data into a higher-dimensional space to make it linearly separable.

### Advantages:

- Effective in high-dimensional spaces.
- Robust to overfitting, especially in high-dimensional space.

### Disadvantages:

- Memory-intensive.
- Hard to interpret, especially with non-linear kernels.

## 🚀 Model Training

The model is trained using the following steps:

1. **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling features.
2. **Feature Extraction**: Selecting relevant features for the model.
3. **Model Training**: Using the SVM algorithm to train the model on the dataset.
4. **Model Evaluation**: Assessing the model's performance using metrics like accuracy, precision, recall, and F1-score.

## 🌐 Web Application

The `app.py` file contains a Flask application that serves the trained model as a web service. Users can input their sensor data through a web interface, and the model will predict the activity.

## 📈 Results

The SVM model achieved an accuracy of approximately 92% on the test set, demonstrating its effectiveness in classifying human activities.

## 📥 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Srinithimahalakshmi/Humanactivity_recoginition.git
   cd Humanactivity_recoginition
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000` to use the human activity recognition web service.

## 📚 References

- [UCI Machine Learning Repository: Human Activity Recognition Using Smartphones Dataset](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones)
- [Scikit-learn: Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html)
- [ResearchGate: Random Forest for Human Daily Activity Recognition](https://www.researchgate.net/publication/345315828_Random_Forest_for_Human_Daily_Activity_Recognition)
