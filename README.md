# 📩 Spam SMS Classifier

## 📌 About the Project

This project uses Machine Learning to classify SMS messages as **Spam** or **Ham (legitimate)**.

## 🎯 Objectives

* Detect unwanted spam messages.
* Classify messages automatically using machine learning.
* Evaluate model performance using test data.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorization
* Multinomial Naive Bayes
* Matplotlib
* Seaborn

## 📊 Dataset

The project uses an SMS dataset containing **5,572 messages**:

* 4,825 legitimate messages (Ham)
* 747 spam messages

## 🤖 Machine Learning Model

**Algorithm:** Multinomial Naive Bayes

**Accuracy:** 97.04%

The model converts text into numerical features using TF-IDF before classifying messages.

## 🧪 Example Predictions

| SMS Message                                           | Prediction |
| ----------------------------------------------------- | ---------- |
| Congratulations! You have won a free prize. Call now! | Spam       |
| Hey, are we meeting for lunch today?                  | Ham        |
| URGENT! Claim your cash reward now!                   | Spam       |

## ▶️ How to Run

1. Download or clone this repository.
2. Open `spam_classifier.ipynb` in Google Colab or Jupyter Notebook.
3. Install the required libraries using `requirements.txt`.
4. Run the notebook cells in order.

## 📁 Project Files

* `spam_classifier.ipynb` — Project code and model evaluation
* `requirements.txt` — Required Python libraries
* `README.md` — Project documentation

## ⚠️ Limitations

The model may occasionally misclassify messages. Its accuracy depends on the training data and the types of messages it encounters.

## 👩‍💻 Author

Vijaya Sri

