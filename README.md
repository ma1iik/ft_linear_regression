# Linear Regression from Scratch

A clean implementation of single-variable linear regression built from scratch in Python. Uses gradient descent to predict car prices based on mileage without using any external machine learning frameworks.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-11557c)
![42 Score](https://img.shields.io/badge/42_Score-125%2F100-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This project estimates the resale value of a car given its mileage ($km$). It implements the core linear regression algorithm, parameter normalization, cost function optimization via gradient descent, interactive inference, and model evaluation metrics.

### Key Capabilities
- **Gradient Descent Solver**: Iterative updates for bias ($\theta_0$) and slope ($\theta_1$) parameters.
- **Min-Max Feature Scaling**: Normalizes mileage values during training for numerical stability and scaling convergence.
- **Model Serialization**: Saves trained model parameters ($\theta_0, \theta_1$) to `thetas.json` for persistent inference.
- **Interactive Prediction**: Accepts user inputs for car mileage and outputs estimated prices in real time.
- **Visualization & Precision Metrics**: Plots data points against the fitted regression line and calculates Mean Absolute Error (MAE).

---

## Technical Architecture

### Hypothesis Function
$$\text{estimatePrice}(\text{mileage}) = \theta_0 + (\theta_1 \times \text{mileage})$$

### Gradient Descent Update Rules
For $m$ training examples and learning rate $\alpha$:

$$\theta_0 := \theta_0 - \alpha \frac{1}{m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)$$

$$\theta_1 := \theta_1 - \alpha \frac{1}{m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right) \cdot x^{(i)}$$

---

## File Structure

```
.
├── ft_training.py       # Trains model using gradient descent on dataset
├── ft_prediction.py     # Interactive CLI tool for predicting car prices
├── ft_bonus.py          # Precision evaluation (MAE) & Matplotlib plotting
├── classes.py           # LinearModel class encapsulating data & predictions
├── data.csv             # Training dataset (Mileage vs. Price)
└── Makefile             # Command shortcuts for training, prediction, and cleanup
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- Matplotlib (optional, for visualization)

```bash
pip install matplotlib
```

---

## Usage

You can manage the workflow using the provided `Makefile` or directly via Python scripts.

### Quickstart with Makefile
```bash
# Train the model
make train

# Run interactive prediction CLI
make predict

# Calculate precision metrics & display regression plot
make bonus

# Clean cached files and generated artifacts
make fclean
```

### Manual Execution

#### 1. Train the Model
Calculates parameters $\theta_0$ and $\theta_1$ over 10,000 iterations and exports them to `thetas.json`:
```bash
python3 ft_training.py
```

#### 2. Make Predictions
Run the interactive prompt:
```bash
python3 ft_prediction.py
# Prompt: Enter car mileage (km): 120000
# Estimated price: $5,240.15
```

#### 3. Evaluate & Plot (Bonus)
Calculate Mean Absolute Error (MAE) and output `visualisation.png`:
```bash
# Display regression graph and compute MAE
python3 ft_bonus.py

# Options:
python3 ft_bonus.py -p    # Print MAE precision only
python3 ft_bonus.py -v    # Plot and save regression graph only
```

---

## License

Distributed under the MIT License. See `LICENSE` for details.