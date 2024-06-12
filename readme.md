# Sendy API Project

This project is a machine learning API for predicting delivery times using a linear regression model. The API is built with FastAPI and the frontend is implemented with Streamlit.


## Installation

To get started with this project, follow the steps below:

1. **Clone the repository**:

    ```
    git clone https://github.com/Manuams99/ML_project.git
    
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv .venv
    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force  # On Windows use: .venv\Scripts\activate
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Ensure you have the machine learning model file** in the `assets/ml_components/` directory:

    ```plaintext
    assets/
    └── ml_components/
        └── RegressionLinear_model.sav
    ```

## Usage

### Running the API

To start the FastAPI server, use the following command:

```sh
uvicorn src.api:app

### Running the streamlit app

streamlit run frontend.py
