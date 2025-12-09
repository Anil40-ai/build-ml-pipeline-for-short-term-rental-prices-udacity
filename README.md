NYC Airbnb ML Pipeline Project

This repository contains my implementation of the Udacity Project: Build an ML Pipeline for Short-Term Rental Prices.

🔗 Required Links

W&B Project (Public):
https://wandb.ai/anilavadhanula-none/nyc_airbnb

GitHub Repository (Public):
[Anil40-aibuild-ml-pipeline-for-short-term-rental-prices-udacity](https://github.com/Anil40-ai/build-ml-pipeline-for-short-term-rental-prices-udacity)

📦 Final Pipeline Release

The final working release used for production runs:
Release: 1.0.1
This release includes:

Data boundaries fix

Full ML pipeline

Hyperparameter-optimized Random Forest

Reproducible MLflow runs

📂 Project Overview

This project implements a full reproducible ML pipeline using:

MLflow

Hydra

Weights & Biases

Random Forest modeling

Data validation tests

Multi-step artifact-driven workflow

Pipeline steps:

download

basic_cleaning

data_check

data_split

train_random_forest

test_regression_model (manual after tagging model prod)

🚀 How to Run the Pipeline (from release)
mlflow run https://github.com/Anil40-ai/build-ml-pipeline-for-short-term-rental-prices-udacity.git \
    -v 1.0.1 \
    -P hydra_options="etl.sample='sample2.csv'"


🏷 Model Promotion

The best model from W&B HPO was promoted to prod and used in:

mlflow run . -P steps=test_regression_model
