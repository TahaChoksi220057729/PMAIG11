# PMAI CW Project:

### Group 11:
Weng Chan - 220029635
Kateryna - 220053500
Taha - 220057729
Andrew - 220019030

## Overview
This project involves implementing neural networks for classification tasks using both custom Numpy-based neural network code and PyTorch. It demonstrates fundamental machine learning concepts and techniques, including activation functions, dropout, optimization methods, and hyperparameter tuning.

## Set up virtual environment
1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install Dependencies**:
   Install the required libraries using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Dataset Setup
### Required Datasets
1. **CiFAKE Dataset** (for classification tasks)
2. **Fashion MNIST Dataset** (for additional experimentation)

### Instructions for Downloading
- Download the datasets from the provided links:
  - **Fashion MNIST Dataset**: [Link to download](https://www.kaggle.com/datasets/zalando-research/fashionmnist).
  - **CiFAKE Dataset**: [Link to download](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images).


## Project structure
```
Root
|
├── Dataset
│   ├── cifake
│   │   ├── test
│   │   └── train
│   └── fashion_data
│       ├── fashion-mnist_test.csv
│       ├── fashion-mnist_train.csv
│       ├── t10k-images-idx3-ubyte
│       ├── t10k-labels-idx1-ubyte
│       ├── train-images-idx3-ubyte
│       └── train-labels-idx1-ubyte
|
|── final_code
│   ├── final_task_1.ipynb
│   └── final_task_2.ipynb
```

To avoid file errors during execution, please make sure that you follow the instruction above.

- The final code for task 1 is named "final_task_1.ipynb"
- The final code for task 2 is named "final_task_2.ipynb"
- Final code for both tasks are located in the "final_code" folder.

## How to Run the Project
1. **Open the Jupyter Notebook**:
   - Launch Jupyter Notebook in the project root directory.
   - Open the provided `.ipynb` files for each task.

2. **Task Execution**:
   - Run the code after installing required packages

3. **Modify Parameters**:
   - Update hyperparameters, model architecture, or other settings in the cells as necessary for experimentation.

4. **View Results**:
   - Results, graphs, and metrics will be displayed in the notebook cells.