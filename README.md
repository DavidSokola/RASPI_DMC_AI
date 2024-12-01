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
#!/home/david/Documents/DMC_Code_Reader/bin/python3.11
from __future__ import print_function

import argparse
import sys

import pylibdmtx
from pylibdmtx.pylibdmtx import decode


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description='Reads datamatrix barcodes in images'
    )
    parser.add_argument('image', nargs='+')
    parser.add_argument(
        '-v', '--version', action='version',
        version='%(prog)s ' + pylibdmtx.__version__
    )
    args = parser.parse_args(args)

    from PIL import Image

    for image in args.image:
        for barcode in decode(Image.open(image)):
            print(barcode.data)


if __name__ == '__main__':
    main()


```

### Running the Script
To run the script, use the following command:

```bash
python read_datamatrix.py /path/to/your/image.jpg
```

