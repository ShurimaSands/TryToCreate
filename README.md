# TryToCreate


# GPT-J Local Inference

This repository contains scripts to run GPT-J for local inference. Follow the steps below to download the model and set up the environment.

## Requirements

Ensure you have the following installed on your system:

- Python 3.8 or later
- pip

## Setup

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/ShurimaSands/TryToCreate.git
    cd TryToCreate
    ```

2. Create a virtual environment and activate it.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies.

    ```bash
    pip install -r requirements.txt
    ```

## Downloading the Model

Run "descargar.py" This will save the model to a default path on your C drive.


2. Run the script:

    ```bash
    python descargar.py
    ```

## Running the GPT-J Model


2. Run the script:

    ```bash
    python main-j.py
    ```

## Notes

- Replace `your_username` in the paths with your actual username.
- This setup assumes the use of CPU for inference. Make sure your machine has enough RAM to handle the model.
- If you encounter any issues or have questions, feel free to open an issue on this repository.



