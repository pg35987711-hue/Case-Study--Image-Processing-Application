# image_professional.py

import cv2
import logging
from pathlib import Path


class EdgeDetector:
    """
    Edge Detection Pipeline:
    - Load image
    - Convert to grayscale
    - Apply Canny edge detection
    - Display results
    """

    def __init__(self, image_path: str):
        self.image_path = Path(image_path)
        self.image = None
        self.gray = None
        self.edges = None

        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    def load_image(self) -> None:
        """Load image from file"""
        if not self.image_path.exists():
            logging.error("Image file not found")
            raise FileNotFoundError("Invalid image path")

        self.image = cv2.imread(str(self.image_path))

        if self.image is None:
            raise ValueError("Failed to load image")

        logging.info("Image loaded successfully")

    def convert_to_grayscale(self) -> None:
        """Convert image to grayscale"""
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        logging.info("Converted to grayscale")

    def detect_edges(self) -> None:
        """Apply Canny edge detection"""
        # Thresholds can be tuned for better results
        self.edges = cv2.Canny(self.gray, 100, 200)
        logging.info("Canny edge detection applied")

    def display_results(self) -> None:
        """Display original and edge-detected images"""
        cv2.imshow("Original Image", self.image)
        cv2.imshow("Edge Detection (Canny)", self.edges)

        logging.info("Press any key to close windows")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self) -> None:
        """Execute pipeline"""
        self.load_image()
        self.convert_to_grayscale()
        self.detect_edges()
        self.display_results()


if __name__ == "__main__":
    detector = EdgeDetector("input.jpg")
    detector.run()