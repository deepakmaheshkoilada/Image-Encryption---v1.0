import h5py
from PIL import Image
import numpy as np

def load_matrix_from_hdf5(file_path):
    # Open the HDF5 file in read mode
    with h5py.File(file_path, "r") as f:
        # Retrieve the matrix data from the dataset named "matrix"
        matrix = f["matrix"][:]
    return matrix

def matrix_to_image(matrix, output_path):
    # Convert the numpy array to an image
    image = Image.fromarray(matrix.astype('uint8'))
    
    # Save the image
    image.save(output_path)
    print(f"Image saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Path to the HDF5 file
    hdf5_file = "image_matrix.h5"

    # Load the matrix from the HDF5 file
    matrix = load_matrix_from_hdf5(hdf5_file)

    # Convert the matrix to an image
    output_image_path = "output_image.png"
    matrix_to_image(matrix, output_image_path)
