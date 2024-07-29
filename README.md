# Flight Price Prediction

Welcome to the Flight Price Prediction project! This project demonstrates the end-to-end process of building, evaluating, and deploying a machine learning model to predict flight prices based on user inputs. The project combines frontend development, backend processing, and machine learning to create a fully functional web application.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

In this project, we develop a machine learning model to predict flight prices using historical data. The project is designed to provide a user-friendly interface where users can input flight details and receive price predictions. The backend processes these inputs and uses a pre-trained machine learning model to generate predictions.

## Features

- User-friendly web interface for inputting flight details.
- Backend processing using Flask to handle user inputs.
- Data preprocessing and feature engineering.
- Machine learning model training and evaluation.
- Model deployment using Google Cloud Platform (GCP).
- Version control and collaboration using GitHub.

## Project Structure

The project consists of the following main files and directories:

- `app.py`: The main Flask application file that sets up routes and handles backend processing.
- `templates/index.html`: The HTML file that contains the frontend form for user inputs.
- `static/s1.css`: The CSS file for styling the frontend interface.
- `notebook/`: Contains Jupyter Notebooks for data exploration, preprocessing, and model training.
- `model/`: Directory to save the trained machine learning models.
- `requirements.txt`: List of Python packages required to run the project.

## Setup and Installation

To set up and run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flight-price-prediction.git
    cd flight-price-prediction
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. Open your web browser and go to `http://localhost:5000` to use the application.

## Usage

1. Open the web application in your browser.
2. Enter the flight details such as departure date, arrival date, source, destination, and other relevant information.
3. Click the "Predict Price" button to get the predicted flight price.

## Model Training and Evaluation

The model training and evaluation process is documented in the Jupyter Notebook files in the `notebook/` directory. Follow the steps below to train and evaluate the model:

1. Load and preprocess the dataset.
2. Perform exploratory data analysis (EDA) to understand the data.
3. Generate new features and handle missing values.
4. Train multiple machine learning models (e.g., Linear Regression, Random Forest, Gradient Boosting).
5. Evaluate the models and select the best performing one based on RMSE and R² score.
6. Save the best model using the `joblib` library.

## Deployment

The project can be deployed to Google Cloud Platform (GCP) for online access. Follow these steps for deployment:

1. Create a GCP account and set up a new project.
2. Install the Google Cloud SDK and initialize it:
    ```bash
    gcloud init
    ```

3. App Engine setup:
    ```bash
    gcloud app create
    ```

4. Create an `app.yaml` file with the following content:
    ```yaml
    runtime: python39
    entrypoint: gunicorn -b :$PORT app:app

    handlers:
    - url: /static
      static_dir: static

    - url: /.*
      script: auto
    ```

5. Deploy the application:
    ```bash
    gcloud app deploy
    ```

6. Open the deployed application in your web browser:
    ```bash
    gcloud app browse
    ```

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss your changes.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact [jbiswajitlife@gmail.com].
