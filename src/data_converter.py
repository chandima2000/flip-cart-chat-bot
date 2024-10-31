import os
import pandas as pd
from langchain_core.documents import Document

# Create a new document using required features from the dataset.

def dataConverter():

    # load the dataset
    try:
        dataset_path = os.path.join("..", "dataset", "dataset.csv")
        product_review_data = pd.read_csv(dataset_path)
    except FileNotFoundError:
        print("Error: Dataset is not found.")
        

    # get the required columns
    data_columns = product_review_data[["product_title", "review"]]


    product_list = []


    # Iterate over the rows of the DataFrame
    for _, row in data_columns.iterrows():

        review_entry = {
            "product_name": row["product_title"],
            "review": row["review"]
        }

        # Append each object into the product list
        product_list.append(review_entry)
    

    docs = []

     # Create Document instances
    for entry in product_list:

        metadata = {"product_name": entry['product_name']}
        doc = Document(page_content= entry['review'], metadata= metadata)
        docs.append(doc)   

    return docs