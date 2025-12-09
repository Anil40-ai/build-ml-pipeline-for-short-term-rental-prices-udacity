#!/usr/bin/env python
"""
Performs basic cleaning on the data and saves the results in W&B
"""
import argparse
import logging

import pandas as pd
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(vars(args))

    logger.info("Downloading input artifact...")
    artifact = run.use_artifact(args.input_artifact)
    artifact_path = artifact.file()

    logger.info("Reading dataset...")
    df = pd.read_csv(artifact_path)

    # Drop outliers based on price
    logger.info("Filtering price between %s and %s", args.min_price, args.max_price)
    idx = df["price"].between(args.min_price, args.max_price)
    df = df[idx].copy()

    # Convert last_review to datetime
    logger.info("Converting last_review to datetime")
    df["last_review"] = pd.to_datetime(df["last_review"])

    # Save cleaned data
    output_file = "clean_sample.csv"
    logger.info("Saving cleaned data to %s", output_file)
    df.to_csv(output_file, index=False)

    # Log cleaned artifact to W&B
    logger.info("Logging cleaned artifact to W&B")
    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(output_file)
    run.log_artifact(artifact)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This step cleans the data")

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Name of the raw input data artifact (e.g. sample.csv:latest)",
        required=True,
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="Name for the cleaned data artifact (e.g. clean_sample.csv)",
        required=True,
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="Type for the cleaned artifact (e.g. clean_sample)",
        required=True,
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="Description for the cleaned data artifact",
        required=True,
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="Minimum nightly price to keep",
        required=True,
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="Maximum nightly price to keep",
        required=True,
    )

    args = parser.parse_args()

    go(args)
