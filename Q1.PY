# image_professional.py

import cv2
import logging
from pathlib import Path


class ImageProcessor:
    """
    Professional Image Processing Pipeline:
    - Read image
    - Convert to grayscale
    - Display results
    """

    def __init__(self, image_path: str):
        self.image_path = Path("D:\python labsheet\Case Study Image Processing Application\\input.jpg")
        self.image = None
        self.gray_image = None

        # Setup logging
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    def load_image(self) -> None:
        """Load image from disk"""
        if not self.image_path.exists():
            logging.error(f"Image not found: {self.image_path}")
            raise FileNotFoundError("Invalid image path")

        self.image = cv2.imread(str(self.image_path))

        if self.image is None:
            raise ValueError("Failed to read image")

        logging.info("Image loaded successfully")

    def convert_to_grayscale(self) -> None:
        """Convert loaded image to grayscale"""
        if self.image is None:
            raise RuntimeError("Image not loaded")

        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        logging.info("Converted to grayscale")

    def display_images(self) -> None:
        """Display original and grayscale images"""
        cv2.imshow("Original Image", self.image)
        cv2.imshow("Grayscale Image", self.gray_image)

        logging.info("Press any key to close windows")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self) -> None:
        """Execute full pipeline"""
        self.load_image()
        self.convert_to_grayscale()
        self.display_images()


if __name__ == "__main__":
    # Change path as needed
    processor = ImageProcessor("input.jpg")
    processor.run()