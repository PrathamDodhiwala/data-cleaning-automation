# 🧹 Data Cleaning Automation Tool (Streamlit UI)

A simple and powerful **Data Cleaning Automation Web App** built using **Python** and **Streamlit**. This tool allows users to upload raw CSV files, clean the data automatically, and download a processed version — all through an interactive UI.


## 🚀 Features

* 📂 Upload any CSV dataset
* 🧼 Handle missing values (Mean / Median / Zero)
* 🔁 Remove duplicate rows
* 🔤 Strip unwanted whitespace from text columns
* 🔄 Auto-detect and convert column data types
* 📉 Remove outliers using Z-score method
* 👀 Preview original and cleaned data
* 📥 Download cleaned dataset instantly
* 🎛️ User-friendly sidebar controls


## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **SciPy**


## 📁 Project Structure

```
Data-Cleaning-App/
│
├── Data cleaning.py      # Main Streamlit app
├── requirements.txt     # Required dependencies
└── README.md            # Project documentation
```


## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/data-cleaning-app.git
cd data-cleaning-app
```


### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Run the Application

```bash
streamlit run "Data cleaning.py"
```


## 📦 Requirements.txt

Create a `requirements.txt` file and paste this:

```
streamlit
pandas
numpy
scipy
```


## 🧑‍💻 How to Use

1. Run the app using Streamlit
2. Upload your CSV file
3. Select cleaning options from the sidebar:

   * Missing value strategy
   * Remove duplicates
   * Strip whitespace
   * Fix data types
   * Remove outliers
4. Click **"Clean Data"**
5. Preview cleaned dataset
6. Download cleaned CSV



## 🌟 Future Improvements

* 📊 Data visualization dashboard
* 🤖 Smart AI-based cleaning suggestions
* 📈 Column-wise outlier handling
* 📄 Support for Excel files
* ☁️ Deployment on Streamlit Cloud / AWS


## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.


## 📄 License

This project is open-source and available under the **MIT License**.


## 🙌 Acknowledgements

* Streamlit for amazing UI framework
* Open-source Python community


## 💡 Author

Pratham Dodhiwala
GitHub: https://github.com/PrathamDodhiwala


⭐ If you like this project, don’t forget to star the repo!
