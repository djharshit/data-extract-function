""" Program to convert given image to base64 string """

import base64


def image_to_base64(img_path: str) -> str:
    """Function to convert given image to base64 string

    Keyword arguments:
    img_path -- path of the image to be converted
    Return: The base64 string of the image
    """

    with open(img_path, "rb") as img_file:
        img_str = base64.b64encode(img_file.read()).decode()
    return img_str
