import machine
import time
import config

class SSTV:
    def __init__(self):
        # Initialize the buzzer with PWM
        self.buzzer = machine.PWM(machine.Pin(config.BUZZER_PIN), freq=config.SSTV_FREQUENCY)

    def send_signal(self, data):
        """Send SSTV signal based on the provided data."""
        for byte in data:
            for i in range(8):  # 8 bits per byte
                bit = (byte >> (7 - i)) & 1  # Get the bit
                self.buzzer.duty(512 if bit else 0)  # Set duty cycle
                time.sleep(config.SSTV_DURATION)  # Wait for the duration of the bit
        self.buzzer.duty(0)  # Turn off the buzzer after sending

    def encode_image_to_sstv(self, image_path):
        """Read the image file and send its data as SSTV signal."""
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
        
        # Here you would implement the SSTV encoding logic
        # For simplicity, we will just send the raw image data
        self.send_signal(img_data)
