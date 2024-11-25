import os
from sstv import SSTV
import config

def main():
    # Path to your BMP image
    image_path = 'image.bmp'
    
    if os.path.exists(image_path):
        print("Sending SSTV signal...")
        sstv = SSTV()
        sstv.encode_image_to_sstv(image_path)
        print("SSTV signal sent.")
    else:
        print("Image file not found.")

# Run the main function
if __name__ == "__main__":
    main()
