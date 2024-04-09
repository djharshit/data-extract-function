# Google Cloud Document AI Processing Script

This repository contains a Python script that demonstrates the use of Google Cloud's Document AI API to process documents and extract structured data from them. It's designed to process an image file, specifically extracting entities using a pre-configured Document AI processor.

## Features

- Configuration via environment variables for enhanced security and flexibility.
- Processing of document images with the support for the JPEG format.
- Extraction of entities from documents with confidence scores and normalized values.

## Requirements

- Google Cloud account
- Access to Google Cloud Document AI API
- A Document AI processor set up in your Google Cloud project
- Python 3.6 or later
- Google Cloud SDK and Python client library for Document AI

## Setup

### Google Cloud Configuration

1. Ensure that you have a Google Cloud account and have the Document AI API enabled.
2. Set up a Document AI processor in the Google Cloud Console and note down its `PROJECT_ID`, `PROCESSOR_ID`, and the `LOCATION`.

### Environment Variables

Set the following environment variables in your system:

- `PROJECT_ID`: Your Google Cloud project ID where the Document AI processor is set up.
- `PROCESSOR_ID`: The ID of your Document AI processor.
- `LOCATION`: The location where your Document AI processor is hosted (e.g., `us`).

### Dependencies Installation

Install the required Python packages by running:

```bash
pip install google-cloud-documentai
```

## Usage

1. Modify the `file_path` variable in the script to point to the image file you wish to process. The current setup assumes a JPEG image format.

2. Execute the script:

```bash
python document_ai_processing.py
```

The script will process the specified document image and output the extracted entities, along with their confidence scores and normalized values, to the console.

## Contributing

Contributions to this project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is provided as-is, with no warranties. It serves as a demonstration of using Google Cloud's Document AI API and might need adjustments to fit into your specific use case.

## Contact

If you have any questions or feedback, please feel free to open an issue in this repository.
