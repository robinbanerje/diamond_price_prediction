# Diamond Price Prediction

A machine learning project that predicts diamond prices based on various physical characteristics using advanced data science techniques.

## 🎯 Project Overview

This project implements an end-to-end machine learning pipeline for predicting diamond prices. It includes data ingestion, preprocessing, model training, and prediction capabilities.

## 🛠️ Tech Stack

- Python 3.x
- Scikit-learn
- Pandas
- NumPy
- MLflow (for experiment tracking)
- Streamlit (for web interface)

## 📁 Project Structure

```
diamond_price_prediction/
├── notebooks/
│   └── research.ipynb        # Data analysis and experimentation
├── src/
│   └── diamond_price_predict/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── preprocessing.py
│       │   └── model_training.py
│       └── pipeline/
│           └── training_pipeline.py
├── tests/                   # Unit tests
├── .github/
│   └── workflows/          # CI/CD pipelines
├── requirements.txt        # Project dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/diamond_price_prediction.git
cd diamond_price_prediction
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the training pipeline:
```bash
python src/diamond_price_predict/pipeline/training_pipeline.py
```

2. Start the web interface:
```bash
streamlit run src/diamond_price_predict/app.py
```

## 📊 Model Performance

The model's performance metrics are tracked using MLflow. Key metrics include:
- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Robin Banerjee - Initial work

## 🙏 Acknowledgments

- Special thanks to my mentors:
  - Krish Naik
  - Sunny Savita
- Dataset source: [Diamonds Price Dataset](https://www.kaggle.com/datasets/amirhosseinmirzaie/diamonds-price-dataset) from Kaggle
- Hitesh Choudhary - For sharing code community and best practices

