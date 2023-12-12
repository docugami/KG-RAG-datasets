import pandas as pd
import requests
import os
from urllib.parse import urlparse

# The path to your CSV file - update this as needed
csv_file_path = "download.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)


def download_study_documents(df):
    """
    This function downloads all study documents from the provided DataFrame.
    Each document is saved locally using the NCT number as the file name.
    """

    # Create a directory to store the downloaded documents
    download_dir = "docs"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract NCT number and study documents
        nct_number = row["NCT Number"]
        study_documents = str(row["Study Documents"])

        # Split the study documents string into individual documents
        documents = study_documents.split("|")

        for doc in documents:
            # Split each document into name and URL
            parts = doc.split(", ")
            if len(parts) == 2:
                doc_name, doc_url = parts
                try:
                    # Download the document
                    response = requests.get(doc_url)
                    response.raise_for_status()

                    # Extract the file name from the URL
                    parsed_url = urlparse(doc_url)
                    file_name = os.path.basename(parsed_url.path)

                    # Save the document
                    save_path = os.path.join(download_dir, f"{nct_number}_{file_name}")
                    with open(save_path, "wb") as file:
                        file.write(response.content)

                    print(f"Downloaded {doc_name} for {nct_number} to {save_path}")
                except Exception as e:
                    print(f"Error downloading {doc_name} for {nct_number}: {e}")
            else:
                print(f"No valid URL for {doc} in {nct_number}")


# Call the function to download study documents
download_study_documents(df)
