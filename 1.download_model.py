# Download the pickle file (clf.pkl)

import gdown

# Google Drive file ID (from your link)
file_id = "1ARKgJT67wd7K7oe8BRjyRV0zeRVqCeE7"

# Output file name
output = "clf.pkl"

# Download the file
gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)

print("Download completed successfully!")
