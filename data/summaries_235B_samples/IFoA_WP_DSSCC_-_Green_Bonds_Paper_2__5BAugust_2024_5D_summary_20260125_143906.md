## Document Metadata

**S/N:** 1  
**Title:** Time series analysis of GSS bonds: Part 2 – Further univariate analysis of S&P Green Bond Index  
**Authors:** D Dey (on behalf of the IFoA Data Science, Sustainability & Climate Change Working Party)  
**Date of publication:** 2024-08  
**Topic:** Time series forecasting  
**Sub-topic:** Neural network architectures for green bond index prediction  
**URL:** Not available  

---

## Summary

### 1. Modeling Techniques

The study employs multiple neural network architectures for univariate time series forecasting of the S&P Green Bond Index. The primary models analyzed include:

- **N-BEATS (Neural Basis Expansion Analysis for interpretable Time Series forecasting)**: A deep feedforward architecture composed of stacks of blocks that use doubly residual stacking to iteratively refine backcasts and forecasts. The architecture includes fully connected layers and basis function layers to capture trends and seasonality without explicit feature engineering. The model was implemented with one stack (M=1), varying numbers of blocks per stack (2–30), and varying hidden layers per block (1–4). The authors opted for a generic configuration without explicit trend/seasonality decomposition.

- **Deep Neural Networks (DNNs)**: Feedforward networks with 1–3 hidden dense layers. Models labeled DNN0, DNN1, and DNN2 correspond to 1, 2, and 3 hidden layers respectively.

- **Convolutional Neural Networks (CNNs)**: 1D convolutional networks with one Conv1D layer, optionally followed by a dense layer (CNN0 and CNN1).

- **Long Short-Term Memory (LSTMs)**: Recurrent networks with one LSTM layer, return_sequences=False, with or without an additional dense layer (LSTM_0HL_F, LSTM_1HL_F).

- **Gated Recurrent Units (GRUs)**: Similar to LSTMs but with simpler gating mechanisms. Models GRU_0HL_F and GRU_1HL_F use one GRU layer with or without an additional dense layer.

All models were trained to predict the next day’s index value (horizon = 1 day) using input windows of 1, 2, or 5 prior days. The baseline model simply uses yesterday’s value as today’s prediction.

### 2. Code Availability

Code availability is **not explicitly stated** in the document. While the authors mention using Google Colab and open-source libraries (TensorFlow, Keras, Optuna, statsmodels), no public repository (e.g., GitHub) is provided. The implementation is based on code from the “Zero to Mastery TensorFlow for Deep Learning Book” (Bourke, 2023), but no direct link to the adapted code is given.

### 3. Learning Type

The approach uses **supervised learning**. The models are trained to predict the next day’s index value based on historical values. The training data consists of labeled sequences: input windows (past index values) paired with target outputs (next day’s index value). No self-supervised or unsupervised techniques are employed.

### 4. Dataset

- **Dataset name/source**: S&P Green Bond Index (Total Performance, USD), sourced from S&P Global’s website via a free subscription account.
- **Time range**: 31 January 2013 to 17 February 2023 (2,615 daily observations).
- **Data splits**: Chronological split into training (70%, 1,830 days: 2013-01-31 to 2020-02-16), validation (20%, 523 days: 2020-02-17 to 2022-02-16), and test (10%, 262 days: 2022-02-17 to 2023-02-17). This preserves temporal order for time series modeling.
- **Data type**: Real-world financial time series data.
- **Preprocessing**: No normalization, scaling, or log transformation was applied to the index values. The authors note this may be explored in future work.
- **Volatility**: The test set exhibits higher volatility (standard deviation = 8.04) compared to training (5.32) and validation (5.70) sets, posing a challenge for model generalization.

### 5. Implementation Details

- **Programming language(s)**: Python (implied by use of TensorFlow, Keras, Optuna, statsmodels, and Google Colab).
- **Key libraries/frameworks**:
  - **TensorFlow** and **Keras**: For building and training neural network models.
  - **Optuna**: For hyperparameter optimization using the Tree-structure Parzen Estimator (TPE) algorithm.
  - **statsmodels**: For generating ACF/PACF plots and seasonal decomposition.
  - **Matplotlib/Seaborn** (implied): For visualizing loss curves and model architectures (via Keras visualizer).
  - **NumPy/Pandas** (implied): For data manipulation and preprocessing.

### 6. Model Architecture

#### N-BEATS Architecture

The N-BEATS model is a deep feedforward network structured in stacks of blocks. Each block contains:

1. **Fully Connected Section**: Consists of 4 hidden layers (configurable in this study) with ReLU activation. The final layer projects to two sets of expansion coefficients: θ_b (backcast) and θ_f (forecast) via linear layers.

2. **Basis Layer Section**: Maps θ_b and θ_f to outputs using basis functions (g_b and g_f). In this study, no explicit basis functions (e.g., Fourier, polynomial) were used; the basis layer was implemented as a generalized dense layer.

3. **Doubly Residual Stacking**: Each block produces a backcast residual (x̂_l) and a partial forecast (ŷ_l). The residual x_l = x_{l-1} - x̂_{l-1} is passed to the next block, while ŷ_l is summed to form the global forecast ŷ = Σ ŷ_l. This allows iterative refinement of the forecast.

The overall architecture used in this study:
- **Stacks (M)**: Fixed at 1 (for computational efficiency; training took 3–4 hours).
- **Blocks per stack (K)**: Optimized between 2 and 30.
- **Hidden layers per block**: Optimized between 1 and 4.
- **Neurons per hidden layer**: Optimized between 4 and 512.
- **Output layer**: Dense layer with neurons equal to the combined length of input window and output horizon (e.g., 1+1=2 for window=1, horizon=1).

The model has over 4 million trainable parameters for the 1-day window case, vastly more than simpler DNNs (625 parameters) or LSTMs (47,629 parameters).

#### Other Architectures (from Appendix 3)

- **DNNs**: Simple feedforward networks with dense layers. DNN0 (1 layer), DNN1 (2 layers), DNN2 (3 layers).
- **CNNs**: 1D convolutional layer (Conv1D) followed by optional dense layers (CNN0: no dense, CNN1: one dense).
- **LSTMs/GRUs**: Single recurrent layer (LSTM or GRU) with return_sequences=False, optionally followed by a dense layer (e.g., LSTM_1HL_F has one LSTM layer + one dense layer).

All models used the same hyperparameter optimization framework (Optuna) and training setup (MAE loss, Adam optimizer, L2 regularization).

### 7. Technical Content

This paper extends a prior study (Dey, 2024) on forecasting the S&P Green Bond Index using neural networks. The goal is to evaluate whether more complex architectures (specifically N-BEATS) or wider input windows (2 or 5 days) can outperform a simple baseline (yesterday’s value = today’s value) or the simpler neural networks from the initial study. The analysis is strictly univariate and does not incorporate traditional methods like ARIMA or external variables.

#### N-BEATS Analysis (Section 3)

The N-BEATS architecture was chosen for its state-of-the-art performance in the M4 forecasting competition and its interpretability. The authors implemented a generic version (without explicit trend/seasonality blocks) to avoid biasing the model with prior assumptions. The model was trained with input windows of 1, 2, and 5 days, all predicting 1 day ahead.

Key implementation details:
- **Training**: 400 epochs, batch size 128, 30 Optuna trials.
- **Hyperparameters**: Optimized number of blocks (2–30), hidden layers per block (1–4), neurons per layer (4–512), L2 regularization (1e-5 to 1e-1), activation functions (elu, gelu, linear, relu, sigmoid, swish, tanh), and learning rate (1e-5 to 1e-1).
- **Loss**: MAE, optimized with Adam.
- **Architecture**: Single stack (M=1) to reduce training time (3–4 hours per run).

Results (Table 3):
- **MAE/MAPE**: All N-BEATS models performed worse than the baseline.
  - Window=1: MAE=0.620 (vs. baseline 0.610), MAPE=0.505% (vs. baseline 0.497%).
  - Window=2: MAE=0.662, MAPE=0.539%.
  - Window=5: MAE=0.657, MAPE=0.536%.
- **Conclusion**: No material outperformance. The 1-day window N-BEATS model performed best among N-BEATS variants but still worse than baseline. The authors note the baseline’s strong performance (MAPE ~0.5%) may reflect the index’s low volatility (coefficient of variation ~7.1%) or a random walk nature.

#### Widening the Window Analysis (Section 4)

This section re-evaluates the simpler models from the initial paper (DNNs, CNNs, LSTMs, GRUs) using 2-day and 5-day input windows, while keeping the 1-day prediction horizon. The goal was to see if more historical context improves forecasting.

Methodology:
- **Window Selection**: Based on ACF/PACF plots and prior literature (Peters et al., 2022), 2-day and 5-day windows were chosen. Longer windows (7, 148 days) were tested but performed worse.
- **Models**: Retrained models 1–12 from Appendix 3 (excluding return_sequences=True models and XGBoost).
- **Training**: Same as initial paper (Optuna, MAE loss, Adam, L2 regularization).

Results (Tables 4–6):
- **General Trend**: Expanding the window from 1 to 2 or 5 days generally degraded performance.
  - **MAPE**: Baseline MAPE=0.497%. Most models had MAPE >0.5%, with some exceeding 1% (e.g., DNN2 with 5-day window: MAPE=0.763%).
  - **Best Performer**: GRU_1HL_F with 2-day window (MAPE=0.507%, slightly worse than its 1-day version at 0.519% — a small improvement, but still worse than baseline).
- **Relative Performance** (Table 5):
  - **Green boxes**: Only GRU_1HL_F (2-day) outperformed its 1-day version (MAE decreased by 0.015, MAPE by 0.012%).
  - **Yellow boxes**: Some models (e.g., DNN2, LSTM_0HL_F, GRU_0HL_F) performed better with 5-day vs. 2-day windows, but still worse than 1-day.
  - **Pink boxes**: Most models performed worse with wider windows.
- **vs. Baseline** (Table 6): All models, regardless of window, performed worse than the baseline. Differences in MAPE ranged from +0.010% (GRU_1HL_F, 2-day) to +0.286% (CNN1, 5-day).

#### Overall Conclusions and Limitations

- **Inconclusive Results**: Neither N-BEATS nor wider windows improved performance over the baseline. The baseline’s simplicity and accuracy (MAPE ~0.5%) suggest the index may be hard to predict beyond a naive model, possibly due to its low volatility or random walk behavior.
- **Model Complexity vs. Performance**: More complex models (N-BEATS) did not yield better results. Simpler models (GRUs, LSTMs) performed better than DNNs/CNNs, but still not better than baseline.
- **Potential Reasons**:
  1. **Insufficient Information**: Univariate analysis may not capture enough signal. The authors suggest multivariate analysis (e.g., incorporating stock market or oil prices) may help, as shown in Wang et al. (2021) with CEEMDAN-LSTM.
  2. **Data Limitations**: The test set’s higher volatility may challenge generalization.
  3. **Architecture Choices**: Using only one stack in N-BEATS or not using ensemble techniques (as in the original paper) may have limited performance.
- **Future Work**:
  1. Expand to multivariate analysis.
  2. Test other architectures (e.g., TFT, GNNs).
  3. Broaden the prediction horizon (e.g., 1 week or 1 month).
  4. Explore data preprocessing (normalization, log transforms).
  5. Include ensemble methods for N-BEATS.

In summary, this study rigorously tests advanced neural architectures and wider input windows for green bond index forecasting but finds no significant improvement over a simple baseline. This highlights the challenge of forecasting financial time series, even with sophisticated deep learning models, and points to the need for richer data or different modeling approaches in future work.