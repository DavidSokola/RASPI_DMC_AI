# RASPI_DMC_AI

Raspberry pi 5 + raspebery AI kit plus 26TOPS 



To create a new virtual environment named `DMC_Code_Reader` and install the required libraries specified in your DMC_test.json

 configuration file, follow these steps:

1. **Create the Virtual Environment**:
    ```bash
    python3 -m venv DMC_Code_Reader
    ```

2. **Activate the Virtual Environment**:
    ```bash
    source DMC_Code_Reader/bin/activate
    ```

3. **Install the Required Libraries**:
    ```bash
    pip install pylibdmtx picamera opencv-python
    ```

### Summary of Steps
1. **Create the Virtual Environment**:
    ```bash
    python3 -m venv DMC_Code_Reader
    ```

2. **Activate the Virtual Environment**:
    ```bash
    source DMC_Code_Reader/bin/activate
    ```

3. **Install the Required Libraries**:
    ```bash
    pip install pylibdmtx picamera opencv-python
    ```

### Verify the Installation
To verify that the libraries are installed correctly, you can list the installed packages:
```bash
pip list
```

This will show you a list of installed packages, including `pylibdmtx`, `picamera`, and `opencv-python`.

### Example Script (`capture_and_decode.py`)
Here is an example script that captures an image and decodes the DMC code:

```python
from picamera import PiCamera
from time import sleep
from pylibdmtx.pylibdmtx import decode
import cv2

def capture_image(file_path):
    camera = PiCamera()
    camera.start_preview()
    sleep(2)  # Give the camera some time to adjust
    camera.capture(file_path)
    camera.stop_preview()
    camera.close()
    print(f"Image captured and saved to {file_path}")

def decode_dmc(file_path):
    img = cv2.imread(file_path)
    if img is None:
        print("Failed to load image.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Converted image to grayscale.")

    decoded_objects = decode(gray)
    if not decoded_objects:
        print("No Data Matrix Code detected.")
    else:
        for obj in decoded_objects:
            print(f"Decoded Data Matrix Code: {obj.data.decode('utf-8')}")

if __name__ == "__main__":
    image_path = "/home/david/Documents/dmc_test.jpg"
    capture_image(image_path)
    decode_dmc(image_path)
```

### Running the Script
To run the script, use the following command:

```bash
python capture_and_decode.py
```

This will capture an image using the Raspberry Pi camera, save it to `/home/david/Documents/dmc_test.jpg`, and then decode any Data Matrix Codes in the image, printing the decoded data to the console.
