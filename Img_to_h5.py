import numpy as np
from PIL import Image
import h5py

def image_to_matrix(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to a numpy array
        matrix = np.array(img)
    return matrix

# Example usage
if __name__ == "__main__":
    # Path to the image file
    image_path = "C:/Users/deepa/OneDrive/Desktop/IMP DOCS/deepak.jpeg"
    
    # Convert the image to a matrix
    matrix = image_to_matrix(image_path)
    
    # Display the matrix
    print("Image Matrix:")
    for row in matrix:
        print(' '.join(map(str, row)))

    # Store the matrix in HDF5 format
    hdf5_file = "image_matrix.h5"
    with h5py.File(hdf5_file, "w") as f:
        f.create_dataset("matrix", data=matrix)

    print(f"Matrix stored in {hdf5_file}")