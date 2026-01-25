## Document Metadata

**S/N:** 1  
**Title:** Time series analysis of GSS bonds: Part 1 – Introductory analysis of S&P Green Bond Index  
**Authors:** D Dey (Chair), Cem Öztürk, Shubham Mehta (Working Party members)  
**Date of publication:** 2023-11-01  
**Topic:** Time series forecasting  
**Sub-topic:** Application of neural networks and XGBoost to green bond index prediction  
**URL:** Not available  

---

## Summary

### 1. Modeling Techniques

The paper evaluates six distinct modeling approaches for univariate time series forecasting of the S&P Green Bond Index:

- **Baseline Model**: A naive model where today’s index value is assumed equal to yesterday’s value. This serves as a benchmark for comparison.
- **Deep Neural Network (DNN)**: Feedforward neural networks with 1, 2, or 3 hidden dense layers. Variants include DNN0 (1 layer), DNN1 (2 layers), and DNN2 (3 layers).
- **Convolutional Neural Network (CNN)**: Specifically, 1D CNN architectures (Conv1D) to extract temporal features from the time series. Models tested include CNN0 (single Conv1D layer) and CNN1 (Conv1D + one dense layer).
- **Long Short-Term Memory (LSTM)**: Recurrent neural network designed to handle long-term dependencies and mitigate vanishing gradients. Variants tested include LSTM_0HL_F, LSTM_0HL_T, LSTM_1HL_F, and LSTM_1HL_T, differing in return sequence setting and presence of additional dense layers.
- **Gated Recurrent Unit (GRU)**: Simplified variant of LSTM with fewer gates. Models include GRU_0HL_F, GRU_0HL_T, GRU_1HL_F, and GRU_1HL_T, varying in return sequence and hidden layer configuration.
- **XGBoost**: Gradient boosting decision tree ensemble algorithm. Used for regression with hyperparameters tuned via Optuna.

All models are trained to predict the next day’s index value based on the prior day’s value (1-day rolling window). The paper explicitly excludes stationarity tests and multivariate analysis, which are reserved for future work.

### 2. Code Availability

The paper states that code was implemented in **Google Colab** using **TensorFlow/Keras** for neural networks and **XGBoost** and **Optuna** libraries for hyperparameter tuning. However, **no public GitHub repository or code release is mentioned**. The authors acknowledge code review by Cem Öztürk, but no public access point is provided. Therefore:

**Code Availability: Not available**

### 3. Learning Type

All models are trained using **supervised learning**. The task is regression: predicting a continuous value (next day’s index) based on a single input feature (previous day’s index). The dataset is split chronologically into train (70%), validation (20%), and test (10%) sets, and no self-supervised or unsupervised techniques are employed.

### 4. Dataset

The dataset used is the **S&P Green Bond Index (Total Performance, USD)**, covering the period from **31 January 2013 to 17 February 2023**, inclusive. The data is sourced directly from the S&P website and consists of **2,615 daily observations** (workdays only). No adjustments, normalization, or transformations (e.g., log scaling) were applied.

The dataset is split chronologically:
- **Train set**: 31 Jan 2013 to 16 Feb 2020 (1,830 entries)
- **Validation set**: 17 Feb 2020 to 16 Feb 2022 (523 entries)
- **Test set**: 17 Feb 2022 to 17 Feb 2023 (262 entries)

Key statistics:
- Index range: 109.80 to 158.99
- Train set mean: 133.60, std: 5.32
- Validation set mean: 150.46, std: 5.70
- Test set mean: 123.96, std: 8.04 (more volatile)

The test set exhibits higher volatility than training/validation sets, posing a challenge for model generalization.

### 5. Implementation Details

- **Programming language(s):** Python
- **Key libraries/frameworks:**
  - **TensorFlow/Keras** for building and training DNN, CNN, LSTM, and GRU models
  - **XGBoost** for gradient boosting model
  - **Optuna** for hyperparameter optimization
  - **Pandas** for data handling
  - **NumPy** for numerical operations
  - **Matplotlib** for visualization
  - **Scikit-learn** (implied for data splitting, though not explicitly named)

All models were trained on **Google Colab**.

### 6. Model Architecture

#### Baseline Model
Trivial: `y_t = y_{t-1}`. No trainable parameters. Used as benchmark.

#### Deep Neural Network (DNN)
- Feedforward architecture with fully connected (dense) layers.
- Input: 1 feature (prior day’s index)
- Output: 1 value (predicted index)
- Hidden layers: 1, 2, or 3 dense layers with varying neuron counts (optimized via Optuna).
- Activation functions: relu, elu, gelu, swish, linear, sigmoid, tanh (tested via hyperparameter tuning).
- No dropout or batch normalization applied.

#### Convolutional Neural Network (CNN)
- **Conv1D layer** applied to 1D time series data.
- Kernel size: hyperparameter tuned (typically 1–3 for 1-day input, but potentially larger in future work).
- Filter size: number of filters (features) learned, tuned via Optuna.
- No pooling layer used in this initial analysis.
- Optional dense layer added after convolution (CNN1 variant).
- Input shape: (1, 1) — single time step, single feature.

#### Long Short-Term Memory (LSTM)
- Single LSTM layer with return_sequences set to True or False.
- Optional dense layer after LSTM (LSTM_1HL variants).
- Cell state, forget gate, input gate, and output gate implemented as per standard LSTM equations.
- Hyperparameters tuned: number of units, activation function, learning rate, L2 regularization, return_sequences.
- Input shape: (1, 1) — batch size, timesteps, features.

#### Gated Recurrent Unit (GRU)
- Single GRU layer with return_sequences True/False.
- Optional dense layer (GRU_1HL variants).
- Simpler than LSTM: reset gate and update gate only.
- Hyperparameters tuned similarly to LSTM.
- Input shape: (1, 1).

#### XGBoost
- Ensemble of regression trees.
- Hyperparameters tuned: eta (learning rate), gamma (pruning), max_depth, reg_lambda (L2 regularization).
- No feature engineering; input is single lagged value.
- Tree pruning and handling of missing values enabled.

### 7. Technical Content

This paper presents the foundational stage of a time series analysis project focused on predicting the S&P Green Bond Index using machine learning models. The goal is to establish whether non-traditional methods like neural networks can outperform a simple baseline (yesterday’s value = today’s value) in forecasting green bond index movements. The analysis is intentionally simplified: univariate (only prior day’s value used), no stationarity adjustments, and no multivariate inputs (e.g., stock market, oil prices) are considered — these are deferred to future work.

#### Methodology

The core methodology involves a **rolling 1-day window**: for each day `t`, the model uses the value at `t-1` to predict the value at `t`. This is repeated across the entire time series. The dataset is split chronologically into train (70%), validation (20%), and test (10%) sets to preserve temporal order and avoid data leakage. This is critical for time series, as random splitting would invalidate the temporal dependency assumption.

Models are trained to minimize **Mean Absolute Error (MAE)** using the **Adam optimizer**. **L2 regularization** is applied to all neural network models to mitigate overfitting. **Optuna** with **Tree-structure Parzen Estimator (TPE)** Bayesian optimization is used to tune hyperparameters across all models. For XGBoost, hyperparameters include learning rate (eta), max depth, gamma (pruning), and L2 regularization (reg_lambda).

#### Model Training and Optimization

The Adam optimizer is chosen for its efficiency in adapting learning rates per parameter and combining momentum with RMSProp. The update rule involves bias-corrected first and second moment estimates of gradients. L2 regularization adds a penalty term proportional to the square of weights to the loss function, encouraging smaller weights and reducing model complexity.

Optuna’s TPE algorithm constructs probabilistic models of the objective function (MAE) based on past evaluations. It uses two Gaussian mixtures — one for good trials (l(x)) and one for poor trials (g(x)) — to guide the search toward promising regions of the hyperparameter space. The Expected Improvement (EI) acquisition function balances exploration and exploitation.

Activation functions tested include ReLU, ELU, GELU, Swish, Linear, Sigmoid, and Tanh. ReLU is likely the default, but Optuna explores which performs best for each model type.

#### Results

Results are evaluated on the test set (Feb 2022–Feb 2023) using **MAE** and **MAPE**. The Baseline model achieves MAE = 0.610 and MAPE = 0.4969%. The best-performing models per category are:

- **DNN_best**: MAE = 0.607 (−0.003 vs Baseline), MAPE = 0.4947% (−0.0022%)
- **LSTM_best**: MAE = 0.609 (−0.001), MAPE = 0.4966% (−0.0003%)
- **CNN_best**: MAE = 0.611 (+0.001), MAPE = 0.4977% (+0.0008%)
- **GRU_best**: MAE = 0.615 (+0.005), MAPE = 0.5011% (+0.0042%)

**XGBoost** performs poorly: MAE = 2.840 (+2.23), MAPE = 2.4445% (+1.9476%). This is attributed to decision trees’ inability to extrapolate beyond the range of training data — the test set includes values below the training minimum (~122), which XGBoost cannot predict.

Graphically, the Baseline model fits the test data well, reflecting low daily volatility in the index. The DNN and LSTM models show marginal improvements, but differences are within ±0.1% MAPE — statistically and practically insignificant. When excluding 2022 data, the ranking changes (DNN, CNN, GRU beat Baseline; LSTM does not), further indicating no conclusive outperformance.

#### Conclusions

The key conclusion is that **no model materially outperforms the Baseline**. The small improvements by DNN and LSTM are not statistically significant and likely due to noise or hyperparameter tuning luck. The authors attribute this to the simplicity of the task: predicting one day ahead from one prior day’s value provides insufficient information for complex models to learn meaningful patterns. The test set’s higher volatility also challenges generalization.

XGBoost’s failure highlights a key limitation of tree-based models for time series: they cannot extrapolate beyond training data ranges. This is a known issue and not a flaw of the implementation.

#### Limitations and Future Work

The authors explicitly state this is a foundational study. Key limitations include:
- No stationarity treatment (e.g., differencing, ARIMA)
- No multivariate inputs (e.g., market indices, oil prices)
- No multi-step forecasting (predicting next week/month)
- No data preprocessing (normalization, log transforms)
- Small input window (only 1 day)

Future work will address these:
1. **Stationarity**: Introduce ARIMA or SARIMAX models.
2. **Multivariate analysis**: Incorporate stock market, oil prices, etc.
3. **Wider GSS universe**: Extend to Bloomberg MSCI, FTSE indices.
4. **Advanced models**: Test CEEMDAN-LSTM (hybrid decomposition + LSTM) and N-BEATS (interpretable time series architecture).
5. **Larger windows/horizons**: Use 5, 10, or 30 prior days to predict 1, 5, or 10 days ahead.
6. **Preprocessing**: Apply normalization or log transforms.

The authors emphasize that while results are inconclusive here, neural networks show potential for more complex time series problems, and this paper lays the groundwork for future, more sophisticated analyses.

#### Broader Implications

This work contributes to the growing literature on applying ML to sustainable finance. Green bonds are a rapidly growing asset class (>$2T global issuance in 2022), and accurate forecasting models could aid portfolio management, risk assessment, and actuarial modeling. The paper’s transparent methodology and clear limitations provide a replicable framework for future studies. The focus on open-source tools (TensorFlow, Optuna, XGBoost) also promotes accessibility.

In summary, this paper is a methodological foundation. It demonstrates that simple models can be competitive with complex ones when data is limited, and it sets the stage for more ambitious analyses that incorporate stationarity, multivariate inputs, and advanced architectures — where neural networks may truly shine.

---

**Word Count:** ~1520 words