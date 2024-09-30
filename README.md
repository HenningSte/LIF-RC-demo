# LIF-RC Demo Project

## Overview

The LIF-RC Demo Project is designed to introduce into the topic of leaky integrate and fire neurons and how they can be used in Reservoir networks. It covers the theory behind both concepts and includes some code which shows how the theory is implemented. The notebook is designed as an addition to the course "Neurodynamics" therefore a familiarity with base concepts of neurodynamics is expected.

## Installation

To get started with the demo, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/HenningSte/LIF-RC-demo.git
    ```
2. Navigate to the project directory:
    ```bash
    cd LIF-RC-demo
    ```
3. Create a Python virtual environment:
    ```bash
    python -m venv .venv
    ```
4. Install dependencies (we used Python version 3.11.9, to be sure use a version between 3.9 - 3.11):
    ```
    pip install -r requirements.txt
    ```

## Usage

The theoretical and practical content can be found in the SnnRcNotebook.ipynb file. Once the Python environment is set up, read through the notebook and play around with the parameters in the demos. If you are interested in how the plots are generated, that code can be found in the `utils.py` file in the utils folder.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more details.
