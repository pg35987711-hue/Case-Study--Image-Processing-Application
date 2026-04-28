# image_professional.py

import cv2
import logging
from pathlib import Path


class BlurProcessor:
    """
    Image Blurring Pipeline:
    - Load image
    - Apply Gaussian Blur
    - Apply Median Blur
    - Display results
    """

    def __init__(self, image_path: str):
        self.image_path = Path("D:\python labsheet\Case Study Image Processing Application\\input.jpg")
        self.image = None
        self.gaussian_blur = None
        self.median_blur = None

        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    def load_image(self) -> None:
        """Load image from file"""
        if not self.image_path.exists():
            logging.error("Image file not found")
            raise FileNotFoundError("Invalid path")

        self.image = cv2.imread(str(self.image_path))

        if self.image is None:
            raise ValueError("Failed to load image")

        logging.info("Image loaded successfully")

    def apply_gaussian_blur(self) -> None:
        """Apply Gaussian Blur (smooths image)"""
        self.gaussian_blur = cv2.GaussianBlur(self.image, (5, 5), 0)
        logging.info("Gaussian Blur applied")

    def apply_median_blur(self) -> None:
        """Apply Median Blur (removes salt-and-pepper noise)"""
        self.median_blur = cv2.medianBlur(self.image, 5)
        logging.info("Median Blur applied")

    def display_results(self) -> None:
        """Display all images"""
        cv2.imshow("Original Image", self.image)
        cv2.imshow("Gaussian Blur", self.gaussian_blur)
        cv2.imshow("Median Blur", self.median_blur)

        logging.info("Press any key to close windows")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self) -> None:
        """Execute full pipeline"""
        self.load_image()
        self.apply_gaussian_blur()
        self.apply_median_blur()
        self.display_results()


if __name__ == "__main__":
    processor = BlurProcessor("input.jpg")
    processor.run()