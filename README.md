
#  Human Activity Recognition (HAR) with SVM

##  Overview
This project utilizes a **Support Vector Machine (SVM)** classifier to recognize everyday human activities—such as **walking**, **sitting**, **standing**, and **running**—using sensor data features. The workflow encompasses data preprocessing, feature extraction, model training, evaluation, and a user-friendly Flask web interface for live predictions.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation

```bash
git clone https://github.com/Srinithimahalakshmi/Humanactivity_recoginition.git
cd Humanactivity_recoginition

python3 -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

### 1. Explore & Train via Jupyter Notebook

Open the notebook to walk through preprocessing, training, and evaluation:

```bash
jupyter notebook model.training.ipynb
```

### 2. Launch the Flask App

Start the web interface to try live activity recognition:

```bash
python app.py
```

Open your browser and go to **[http://127.0.0.1:5000](http://127.0.0.1:5000)** to input sensor values and see real-time activity predictions.

---

## Project Structure

```
Humanactivity_recoginition/
├── Human_Activity_Recognition_Using_Smartphones_Data.csv  # Dataset
├── model.training.ipynb                                   # Notebook for data prep & model training
├── app.py                                                 # Flask web application
├── model/                                                 # Folder containing trained model file
│    └── [model file].pkl
├── templates/
│    └── index.html                                        # Web UI template
├── static/
│    └── [CSS/JS files]                                    # Frontend assets
├── requirements.txt                                       # Project dependencies
└── README.md                                              # Project documentation
```

---

## Results

* **Model Accuracy**: `XX%`
* Includes evaluation metrics such as **confusion matrix**, **classification report**, and performance visualizations—accessible via the notebook or app.

*(Feel free to update with actual metrics and visual references.)*

---

## Contributing

Contributions are welcome! You could help by:

* Tuning hyperparameters or testing additional models (e.g., Random Forest, Neural Networks)
* Adding feature engineering improvements or new sensors
* Enhancing model interpretability using SHAP or LIME
* Polishing the frontend interface or adding more interactive features

To contribute:

1. Fork the repository
2. Create a branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add feature XYZ"`
4. Push and open a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If you found this project valuable, a star would be much appreciated!*

