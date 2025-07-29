# 🥕 Fruit & Vegetable Classifier

This is a simple image classification app for fruits and vegetables built with **TensorFlow** and **Streamlit**.

## 💻 How to Run

1. Install the dependencies:

  pip install -r requirements.txt


2. Run the notebook first to download the model file:

  Open fruits-vegetables.ipynb

  Run all the cells
  
  (This will automatically download classify_Image3.h5 if it's not already present)

3. Then launch the Streamlit app :
  streamlit run App.py  

4. Once the app opens in your browser, you can upload any fruit or vegetable image to see the prediction and confidence score.



## 📷 Sample Images

You can try with:
- corn.jpg
- tomato.png

## 🔍 Output
The model will display the predicted class and the confidence score.

🧠 Model
The model was trained on a custom dataset and saved in Keras format as:

classify_Image3.h5

📌 Note: You don’t need to download the model manually.
Just run the notebook fruits-vegetables.ipynb and it will automatically download the model file for you if it's not already available.



📂 File Structure
```
├── App.py
├── classify_Image3.h5
├── fruits-vegetables.ipynb
├── requirements.txt
├── corn.jpg
├── tomato.png
└── README.md
```

Made with ❤️ by Ahmed AlMutaz


