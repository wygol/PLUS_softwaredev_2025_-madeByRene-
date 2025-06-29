import numpy as np
from scipy.ndimage import convolve


def highPassFilter(raster: np.ndarray) -> np.ndarray:
    """
    Applies a high-pass filter to the input NDVI raster to enhance high-frequency features
    such as edges and abrupt changes in vegetation.

    Parameters:
    raster (np.ndarray): 2D NDVI raster data as a NumPy array.

    Returns:
    np.ndarray: High-pass filtered NDVI raster.
    """
    # High-pass filter kernel (Laplacian-like)
    kernel = np.array([
        [1, 0, 1],
        [1, 8, 1],
        [1, 0, 1]
    ])

    # Apply convolution
    filtered = convolve(raster, kernel, mode='reflect')

    return filtered


def lowPassFilter(raster: np.ndarray) -> np.ndarray:
    """
    Applies a low-pass filter (smoothing) to the input NDVI raster to reduce noise
    and emphasize broader features like large vegetation patches.

    Parameters:
    raster (np.ndarray): 2D NDVI raster data as a NumPy array.

    Returns:
    np.ndarray: Low-pass filtered NDVI raster.
    """
    # Low-pass filter kernel (average filter)
    kernel = np.ones((3, 3)) / 9.0

    # Apply convolution
    filtered = convolve(raster, kernel, mode='reflect')

    return filtered


def edgeDetectionFilter(raster: np.ndarray) -> np.ndarray:
    """
    Applies an edge detection filter (Sobel operator) to the input NDVI raster
    to highlight vegetation boundaries and changes in land cover.

    Parameters:
    raster (np.ndarray): 2D NDVI raster data as a NumPy array.

    Returns:
    np.ndarray: NDVI raster with edges detected.
    """
    # Sobel kernels for x and y direction
    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    sobel_y = np.array([
        [-1, -2, -1],
        [0,  0,  0],
        [1,  2,  1]
    ])

    # Apply Sobel filters
    gx = convolve(raster, sobel_x, mode='reflect')
    gy = convolve(raster, sobel_y, mode='reflect')

    # Compute edge magnitude
    edges = np.hypot(gx, gy)

    return edges
