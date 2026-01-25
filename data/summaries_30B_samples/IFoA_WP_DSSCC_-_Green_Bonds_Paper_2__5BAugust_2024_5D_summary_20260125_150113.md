## Document Metadata

**S/N:** 1  
**Title:** Time series analysis of GSS bonds: Part 2 – Further univariate analysis of S&P Green Bond Index  
**Authors:** D Dey (on behalf of the IFoA Data Science, Sustainability & Climate Change Working Party)  
**Date of publication:** 2024-08  
**Topic:** Time series forecasting using neural networks  
**Sub-topic:** Univariate prediction of S&P Green Bond Index using N-BEATS and extended input windows  
**URL:** Not available  

---

## Summary

### 1. Modeling Techniques

The paper employs a suite of neural network architectures for univariate time series forecasting of the S&P Green Bond Index. The primary techniques include:

- **N-BEATS (Neural Basis Expansion Analysis for interpretable Time Series forecasting)**: A deep feedforward architecture composed of stacks of blocks that perform doubly residual stacking—producing both backcasts (residuals) and partial forecasts. Each block contains fully connected layers followed by basis function layers that map expansion coefficients to outputs. The architecture is designed to be interpretable and was originally shown to outperform M4 competition winners by 3% (Oreshkin et al., 2020). In this study, a generic (non-interpretable) variant was used with one stack (M=1), varying numbers of blocks (K=2–30), and hidden layers (1–4) per block.

- **Deep Neural Networks (DNNs)**: Feedforward networks with 1 to 3 hidden dense layers. These were retrained with input windows of 1, 2, and 5 days to assess the impact of longer historical context.

- **Convolutional Neural Networks (CNNs)**: 1D CNNs with one convolutional layer, optionally followed by one dense hidden layer. These were also retrained with 2- and 5-day input windows.

- **Long Short-Term Memory (LSTM) networks**: Recurrent networks with one LSTM layer (return_sequences=False) and optionally one additional dense layer. Variants include 0 or 1 hidden layer(s) after the LSTM.

- **Gated Recurrent Units (GRUs)**: Similar to LSTMs, with one GRU layer and optionally one dense layer. These were also retrained with extended input windows.

All models were trained to predict a 1-day-ahead horizon. The baseline model used for comparison is a naive persistence model: “today’s index value equals yesterday’s value.”

### 2. Code Availability

Implementation code is **not publicly available** in the document. The authors mention using Google Colab for training and reference code from the “Zero to Mastery TensorFlow for Deep Learning Book” (Bourke, 2023), but no GitHub repository or public code link is provided. Hyperparameter tuning was performed using Optuna, but no configuration files or scripts are shared.

### 3. Learning Type

All models use **supervised learning**. The task is framed as a regression problem: given a sequence of past index values (input window), predict the next day’s index value (output horizon). Labels are the actual daily index values from the S&P Green Bond Index dataset.

### 4. Dataset

- **Dataset name/source**: S&P Green Bond Index (Total Performance, USD)
- **Time range**: 31 January 2013 to 17 February 2023 (2,615 daily observations)
- **Data type**: Real-world financial time series data
- **Splits**: Chronologically ordered 70% training (31 Jan 2013–16 Feb 2020), 20% validation (17 Feb 2020–16 Feb 2022), 10% test (17 Feb 2022–17 Feb 2023)
- **Characteristics**: 
  - Index range: 109.80 to 158.99
  - Mean: 136.00, Std Dev: 9.65
  - Test set exhibits higher volatility (std dev 8.04) than training/validation sets (std dev ~5.3–5.7), making it a challenging out-of-sample prediction task.
- **Preprocessing**: No normalization or log transformation was applied, to preserve original scale and avoid assumptions about stationarity or seasonality.

### 5. Implementation Details

- **Programming language(s)**: Python
- **Key libraries/frameworks**:
  - TensorFlow and Keras (for model building and training)
  - Optuna (for hyperparameter optimization using TPE algorithm)
  - Statsmodels (for ACF/PACF and seasonal decomposition plots)
  - Matplotlib/Seaborn (for visualizations, though not explicitly named)
  - Google Colab (execution environment)

### 6. Model Architecture

#### N-BEATS Architecture (Generic Variant)

The N-BEATS model used in this study is a simplified version of the original architecture, configured as follows:

- **Stacks**: 1 stack (M=1) — the authors chose this to reduce training time (up to 4 hours) and complexity.
- **Blocks per stack**: 2 to 30 blocks (K), optimized via Optuna.
- **Block structure**:
  - **Fully connected section**: 1–4 hidden layers (each with 4–512 neurons), using ReLU (or other activation functions from a list: elu, gelu, linear, relu, sigmoid, swish, tanh). Each hidden layer is followed by a linear projection layer to generate expansion coefficients for backcast (θᵇ) and forecast (θᶠ).
  - **Basis layer**: Maps θᵇ and θᶠ to outputs via dense layers (no basis functions for trend/seasonality were used — generic mode). Output layer size equals input window + output horizon (e.g., 1+1=2 for 1-day window).
- **Doubly residual stacking**: Each block outputs a backcast residual (x̂ₗ = xₗ₋₁ - x̂ₗ₋₁) and a partial forecast (ŷₗ). The global forecast is the sum of all partial forecasts: ŷ = Σŷₗ.
- **Regularization**: L2 regularization applied to hidden layers (search space: 1e-5 to 1e-1).
- **Loss & Optimizer**: MAE loss with Adam optimizer (learning rate: 1e-5 to 1e-1).

#### DNN, CNN, LSTM, GRU Architectures (Extended Input Windows)

These models were retrained with 2-day and 5-day input windows (previously only 1-day). Architectures are identical to those in the initial paper (Dey, 2024):

- **DNN**: Feedforward networks with 1, 2, or 3 dense hidden layers (e.g., DNN0, DNN1, DNN2).
- **CNN**: 1D convolutional layer (kernel size=2 or 5) followed by optional dense layer (CNN0, CNN1).
- **LSTM/GRU**: Single LSTM or GRU layer (return_sequences=False) with optional dense layer (e.g., LSTM_0HL_F, LSTM_1HL_F, GRU_0HL_F, GRU_1HL_F).

All models use MAE loss, Adam optimizer, and L2 regularization. Hyperparameters (neurons, layers, activations, learning rate) were tuned via Optuna (30 trials, 400 epochs, batch size=128).

### 7. Technical Content

This paper extends prior work on forecasting the S&P Green Bond Index using neural networks by introducing the N-BEATS architecture and expanding input windows for existing models (DNN, CNN, LSTM, GRU). The goal is to improve prediction accuracy over a simple baseline (yesterday’s value = today’s value) for 1-day-ahead forecasts.

#### Background and Motivation

Green, Social, and Sustainability (GSS) bonds are a rapidly growing asset class (USD 939 billion issued in 2023), yet research on their time series behavior is limited. The authors aim to explore whether advanced neural architectures can capture patterns in this relatively new financial instrument. The study deliberately excludes traditional methods (e.g., ARIMA) and multivariate analysis to focus on pure neural network performance and interpretability. The S&P Green Bond Index (2013–2023) is used as the target variable, split chronologically into training (70%), validation (20%), and test (10%) sets to preserve temporal order.

#### N-BEATS Implementation and Results

N-BEATS was chosen for its state-of-the-art performance in time series forecasting (notably, 3% better than M4 winner) and its interpretable design. However, the authors implemented a “generic” variant without explicit trend/seasonality decomposition to maintain neutrality. The model was trained with input windows of 1, 2, and 5 days, predicting 1 day ahead.

Key implementation details:
- **Architecture**: 1 stack, 2–30 blocks, 1–4 hidden layers per block, 4–512 neurons per layer, ReLU or other activations, L2 regularization (1e-5 to 1e-1), MAE loss, Adam optimizer (lr 1e-5 to 1e-1).
- **Training**: 400 epochs, 30 Optuna trials, batch size 128, Google Colab environment.
- **Complexity**: The final model (1-day window) had over 4 million parameters — vastly more than DNNs (~625) or LSTMs (~47,629).

Results (Table 3):
- **MAE**: Baseline = 0.610; N-BEATS (1-day) = 0.620 (+0.010); N-BEATS (2-day) = 0.662 (+0.052); N-BEATS (5-day) = 0.657 (+0.047).
- **MAPE**: Baseline = 0.497%; N-BEATS (1-day) = 0.505% (+0.008%); N-BEATS (2-day) = 0.539% (+0.042%); N-BEATS (5-day) = 0.536% (+0.039%).

All N-BEATS variants underperformed the baseline. The 1-day window model was the best among N-BEATS, suggesting that adding more historical data did not help. The authors note that the baseline’s strong performance (MAPE ~0.5%) may reflect the index’s low volatility (coefficient of variation ~7.1%) or a “random walk” nature, making it hard to beat.

#### Extended Input Windows for DNN, CNN, LSTM, GRU

The authors retrained models from their initial paper with 2-day and 5-day input windows (previously only 1-day). This was motivated by ACF/PACF analysis (Section 4.2), which suggested potential 2-day lags, and prior literature suggesting 5-day lags. Seasonal decomposition of log returns showed weak trend/seasonality, supporting the use of longer windows.

Results (Tables 4–6):
- **Overall**: No model improved over the baseline (MAE 0.610, MAPE 0.497%) when using 2- or 5-day windows. In fact, most models performed worse.
- **Best performer**: GRU_1HL_F (Model 12) with 2-day window had MAE 0.623 (vs. 0.638 for 1-day) — a slight improvement, but still worse than baseline. Its MAPE was 0.507% (vs. 0.519% for 1-day), also better but not baseline-beating.
- **Worst performers**: DNN2 (Model 3) with 2-day window had MAE 1.320 (+0.700 over 1-day) and MAPE 1.085% (+0.580%).
- **Trends**: 
  - GRU and LSTM models generally outperformed DNN and CNN.
  - Extending to 5 days sometimes improved over 2 days (e.g., Models 3, 6, 10), but never over baseline.
  - The 5-day window often produced higher errors than 2-day, suggesting overfitting or noise amplification.

#### Interpretation and Limitations

The consistent failure to beat the baseline suggests that:
1. The S&P Green Bond Index may follow a near-random walk, where past values offer little predictive power beyond persistence.
2. Univariate analysis may be insufficient — the models lack external context (e.g., market indices, oil prices) that could provide meaningful signals.
3. The N-BEATS architecture, while powerful in general, may not be well-suited to this specific dataset or problem setup (e.g., generic mode without trend/seasonality, single stack).

The authors acknowledge that ensemble techniques (used by N-BEATS original authors) or multivariate inputs (e.g., as in Wang et al., 2021 with CEEMDAN-LSTM) could improve performance. They also note that longer windows (7 or 148 days) were tested but performed worse than 5 days.

#### Conclusions and Next Steps

The paper concludes that:
- N-BEATS and extended-window DNN/CNN/LSTM/GRU models did not materially outperform the naive baseline (differences up to +0.04% MAPE for N-BEATS, +0.3% for others).
- Results are inconclusive — the baseline’s simplicity and accuracy make it a tough benchmark.
- Future work will explore:
  1. Multivariate analysis (incorporating stock market, oil prices, etc.).
  2. Broader GSS bond indices and longer time ranges.
  3. Other architectures (e.g., TFT, Graph Neural Networks).
  4. Longer forecast horizons (1 week or 1 month).

In summary, while the paper rigorously tests advanced neural architectures on a novel financial time series, it finds no clear advantage over a simple persistence model. This highlights the challenge of forecasting GSS bond indices and suggests that future research should incorporate external variables or more sophisticated ensemble methods.

**Word count**: ~1500