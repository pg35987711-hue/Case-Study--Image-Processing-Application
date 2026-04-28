# image_advanced.py

import cv2
import logging
from pathlib import Path


class ImageEnhancer:
    """
    Professional Image Enhancement Tool:
    - Adjust brightness and contrast in real-time
    - Interactive UI using trackbars
    """

    def __init__(self, image_path: str):
        self.image_path = Path(image_path)
        self.original = None

        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    def load_image(self):
        """Load image from file"""
        if not self.image_path.exists():
            logging.error("Image file not found")
            raise FileNotFoundError

        self.original = cv2.imread(str(self.image_path))

        if self.original is None:
            raise ValueError("Failed to load image")

        logging.info("Image loaded successfully")

    def nothing(self, x):
        """Dummy function for trackbar"""
        pass

    def run(self):
        """Main UI loop"""
        self.load_image()

        cv2.namedWindow("Image Enhancer")

        # Create trackbars
        cv2.createTrackbar("Brightness", "Image Enhancer", 50, 100, self.nothing)
        cv2.createTrackbar("Contrast", "Image Enhancer", 10, 30, self.nothing)

        while True:
            # Get trackbar values
            brightness = cv2.getTrackbarPos("Brightness", "Image Enhancer") - 50
            contrast = cv2.getTrackbarPos("Contrast", "Image Enhancer") / 10

            # Apply brightness & contrast
            adjusted = cv2.convertScaleAbs(self.original, alpha=contrast, beta=brightness)

            # Display
            cv2.imshow("Image Enhancer", adjusted)

            # Exit on ESC
            if cv2.waitKey(10) & 0xFF == 27:
                break

        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = ImageEnhancer("input.jpg")
    app.run()