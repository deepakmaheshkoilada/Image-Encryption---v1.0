import h5py
import numpy as np

def load_matrix_from_hdf5(file_path):
    # Open the HDF5 file in read mode
    with h5py.File(file_path, "r") as f:
        # Retrieve the matrix data from the dataset named "matrix"
        matrix = f["matrix"][:]
    return matrix

# Example usage
if __name__ == "__main__":
    # Path to the HDF5 file
    hdf5_file = "image_matrix.h5"

    # Load the matrix from the HDF5 file
    matrix = load_matrix_from_hdf5(hdf5_file)

    # Display the matrix
    print("Retrieved Matrix:")
    for row in matrix:
        print(' '.join(map(str, row)))
