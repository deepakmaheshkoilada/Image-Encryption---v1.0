import numpy as np
from PIL import Image

def image_to_matrix(image_path):

    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to a numpy array
        matrix = np.array(img)
    return matrix

def display_matrix(matrix):

    for row in matrix:
        print(' '.join(map(str, row)))

# Example usage
if __name__ == "__main__":
    image_path = "C:/Users/deepa/OneDrive/Pictures/Screenshots/empty.png"
    matrix = image_to_matrix(image_path)
    print("Image Matrix:")
    display_matrix(matrix)
