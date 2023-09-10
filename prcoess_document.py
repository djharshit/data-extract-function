from google.api_core.client_options import ClientOptions
from google.cloud import documentai
from os import environ

PROJECT_ID = environ.get("PROJECT_ID")
PROCESSOR_ID = environ.get("PROCESSOR_ID")
LOCATION = "us"

file_path = r"C:\Users\Harshit Music\Pictures\ticket-5.jpg"
mime_type = "image/jpeg"


def process_document() -> documentai.Document:
    client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(
            api_endpoint=f"{LOCATION}-documentai.googleapis.com"
        )
    )

    name = client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()

    # Configure the process request
    request = documentai.ProcessRequest(
        name=name,
        raw_document=documentai.RawDocument(content=image_content, mime_type=mime_type),
    )

    result = client.process_document(request=request)

    return result.document


def process_document_specialized_sample() -> None:
    document = process_document()

    print(f"Found {len(document.entities)} entities:")
    for entity in document.entities:
        print_entity(entity)
        for prop in entity.properties:
            print_entity(prop)


def print_entity(entity: documentai.Document.Entity) -> None:
    key = entity.type_

    text_value = entity.text_anchor.content
    confidence = entity.confidence
    normalized_value = entity.normalized_value.text
    print(f"    * {repr(key)}: {repr(text_value)}({confidence:.1%} confident)")

    if normalized_value:
        print(f"    * Normalized Value: {repr(normalized_value)}")


process_document_specialized_sample()
