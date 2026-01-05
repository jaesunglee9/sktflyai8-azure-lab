import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

load_dotenv()

def upload_to_blob(local_file_path, container_name, blob_name):
    # 1. Connection String (Get this from the Azure Portal)
    # Recommended: Set as an environment variable
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    
    if not connect_str:
        print("Error: Please set the AZURE_STORAGE_CONNECTION_STRING environment variable.")
        return

    try:
        # 2. Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # 3. Get or Create a Container
        container_client = blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()
            print(f"Container '{container_name}' created.")

        # 4. Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        print(f"Uploading to Azure Storage as blob: {blob_name}")

        # 5. Upload the file
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            
        print("Upload completed successfully!")

    except Exception as ex:
        print(f"Exception occurred: {ex}")

# Usage
if __name__ == "__main__":
    # Replace these with your actual details
    LOCAL_PATH = "friends.jfif"
    CONTAINER = "image-data"
    BLOB_NAME = "friends.jfif"

    upload_to_blob(LOCAL_PATH, CONTAINER, BLOB_NAME)