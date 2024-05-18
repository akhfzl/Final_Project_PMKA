import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate using Kaggle API
api = KaggleApi()
api.authenticate()

# Download and unzip the dataset
api.dataset_download_files('tawsifurrahman/tuberculosis-tb-chest-xray-dataset', path='.', unzip=True)

print(f"Dataset downloaded to {download_path}")
