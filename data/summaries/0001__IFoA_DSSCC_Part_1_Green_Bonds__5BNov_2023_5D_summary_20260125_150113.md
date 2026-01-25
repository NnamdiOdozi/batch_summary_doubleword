## Document Metadata

**S/N:** 1  
**Title:** Time series analysis of GSS bonds: Part 1 – Introductory analysis of S&P Green Bond Index  
**Authors:** D Dey (Chair), Cem Öztürk, Shubham Mehta (Working Party members)  
**Date of publication:** 2023-11-01  
**Topic:** Time series forecasting using machine learning  
**Sub-topic:** Application of neural networks and XGBoost to green bond index prediction  
**URL:** Not available  

---

## Summary

### 1. Modeling Techniques

The paper evaluates six distinct modeling approaches for univariate time series forecasting of the S&P Green Bond Index:

- **Baseline model**: A naive predictor where today’s index value equals yesterday’s value.
- **Deep Neural Network (DNN)**: Feedforward neural networks with 1, 2, or 3 hidden dense layers. The best-performing variant (DNN_best) used 3 hidden layers.
- **Convolutional Neural Network (CNN)**: 1D CNN architecture with a single Conv1D layer, designed to extract temporal features from sequential data without pooling layers.
- **Long Short-Term Memory (LSTM)**: Recurrent neural network with LSTM cells to capture long-term dependencies. Variants tested included return_sequence=True/False and with/without additional dense layers.
- **Gated Recurrent Unit (GRU)**: Simplified RNN variant with GRU cells. Tested configurations mirrored those of LSTM.
- **XGBoost**: Gradient boosting decision tree ensemble model, optimized for regression tasks.

All models were trained to predict the next day’s index value using only the prior day’s value (1-day rolling window). The study did not include stationarity transformations or multivariate inputs.

### 2. Code Availability

The paper states that the code was implemented in Google Colab using TensorFlow/Keras, XGBoost, and Optuna libraries. However, **no public repository or GitHub link is provided**. Code availability is therefore **not confirmed**.

### 3. Learning Type

All models were trained using **supervised learning**. The task was regression: predicting a continuous value (index level) based on a single prior observation. No self-supervised or unsupervised methods were employed.

### 4. Dataset

The dataset consists of daily values of the **S&P Green Bond Index (Total Performance, USD)** from **31 January 2013 to 17 February 2023**, totaling 2,615 observations. The data is real-world and publicly available via the S&P website.

The dataset was split chronologically (not randomly) into:
- **Training set**: 31 Jan 2013 – 16 Feb 2020 (1,830 entries)
- **Validation set**: 17 Feb 2020 – 16 Feb 2022 (523 entries)
- **Test set**: 17 Feb 2022 – 17 Feb 2023 (262 entries)

No normalization, log transformation, or stationarity adjustments were applied. The test set exhibited higher volatility (std dev 8.04) compared to training (std dev 5.32) and validation (std dev 5.70) sets.

### 5. Implementation Details

- **Programming language(s):** Python
- **Key libraries/frameworks:**
  - TensorFlow and Keras for neural network models
  - XGBoost for gradient boosting
  - Optuna for hyperparameter optimization
  - NumPy and Pandas for data handling
  - Matplotlib for visualization
  - Google Colab for execution environment

### 6. Model Architecture

#### Baseline Model
- Simple identity function: `y_t = y_{t-1}`

#### DNN Architecture
- Input layer → 1, 2, or 3 fully connected (dense) hidden layers → Output layer
- Each neuron applies weighted sum + bias + activation function
- Best model (DNN_best) used 3 hidden layers with optimized neuron counts, activation functions, and L2 regularization

#### CNN Architecture
- Input → Conv1D layer (kernel size = 1, filters = optimized) → Output
- No pooling layers used due to simplicity of 1-day window
- Designed to detect local temporal patterns

#### LSTM Architecture
- Single LSTM layer with internal gates:
  - Forget gate: `ft = σ(Wf · [ht-1, xt] + bf)`
  - Input gate: `it = σ(Wi · [ht-1, xt] + bi)`
  - Cell state: `Ct = ft ⊙ Ct-1 + it ⊙ tanh(Wc · [ht-1, xt] + bc)`
  - Output gate: `ot = σ(Wo · [ht-1, xt] + bo)`
  - Hidden state: `ht = ot ⊙ tanh(Ct)`
- Variants tested: return_sequence=True/False, with/without additional dense layer

#### GRU Architecture
- Single GRU layer with:
  - Reset gate: `rt = σ(Wr · [ht-1, xt] + br)`
  - Update gate: `zt = σ(Wz · [ht-1, xt] + bz)`
  - Candidate activation: `ℎ̃t = tanh(Wh · [rt ⊙ ht-1, xt] + bh)`
  - Hidden state: `ht = (1 - zt) ⊙ ht-1 + zt ⊙ ℎ̃t`
- Simpler than LSTM, with fewer gates

#### XGBoost Architecture
- Ensemble of regression trees
- Sequentially builds trees to correct residuals from prior trees
- Final prediction: `Fm(X) = Fm−1(X) + αm · hm(X, rm−1)`
- Hyperparameters optimized: eta (learning rate), gamma (pruning), max_depth, reg_lambda (L2 regularization)

### 7. Technical Content

This paper presents the foundational stage of a time series analysis project focused on predicting the S&P Green Bond Index using machine learning techniques. The primary objective is to establish whether neural networks and ensemble methods can outperform a simple baseline model (yesterday’s value = today’s value) in forecasting daily index levels. The study is explicitly limited to univariate analysis with a 1-day rolling window and excludes stationarity adjustments or multivariate inputs, which are reserved for future work.

The data spans from January 2013 to February 2023, covering a period that includes the COVID-19 market disruptions. The index shows a general upward trend until early 2021, followed by a decline through late 2022, reflecting broader market dynamics. The dataset was split chronologically into 70% training, 20% validation, and 10% test sets to preserve temporal dependencies. Notably, the test set (Feb 2022–Feb 2023) contains more volatile data than the training period, posing a challenge for generalization.

Five categories of neural network architectures were tested: DNN, CNN, LSTM, GRU, and XGBoost. Each model was optimized using Optuna’s Bayesian optimization (TPE algorithm) to tune hyperparameters including:
- Number of neurons per layer
- Activation functions (ReLU, ELU, GELU, Swish, Linear, Sigmoid, Tanh)
- Learning rate (Adam optimizer)
- L2 regularization strength
- For CNN: filter size
- For LSTM/GRU: return_sequence flag
- For XGBoost: eta, gamma, max_depth, reg_lambda

Training employed the Mean Absolute Error (MAE) loss function and the Adam optimizer with batch size 128. L2 regularization was applied to all non-baseline models to mitigate overfitting. The Adam optimizer combines momentum (exponential moving average of gradients) and RMSProp (exponential moving average of squared gradients) to adaptively adjust learning rates per parameter.

Results were evaluated on the test set using MAE and Mean Absolute Percentage Error (MAPE). The baseline model achieved MAE = 0.610 and MAPE = 0.4969%. The best-performing models were:
- **DNN_best**: MAE = 0.607 (−0.003 vs baseline), MAPE = 0.4947% (−0.0022%)
- **LSTM_best**: MAE = 0.609 (−0.001), MAPE = 0.4966% (−0.0003%)

These represent marginal improvements over the baseline. The CNN_best model performed slightly worse (MAE = 0.611, MAPE = 0.4977%), while GRU_best performed worst among neural networks (MAE = 0.615, MAPE = 0.5011%). The XGBoost model failed catastrophically, with MAE = 2.840 and MAPE = 2.4445%, primarily because decision trees cannot extrapolate beyond the range of training data (minimum training value ~122, but test data dropped to ~110).

The paper concludes that, given the 1-day window constraint, the models do not materially outperform the baseline. This is attributed to insufficient historical context being provided to the models—each prediction uses only one prior value, limiting the ability to learn complex temporal patterns. The authors hypothesize that expanding the input window (e.g., using 5 or 10 prior days) and output horizon (predicting multiple days ahead), introducing stationarity (e.g., via ARIMA or differencing), and incorporating multivariate inputs (e.g., oil prices, stock indices) will yield more significant improvements.

Future work will explore:
1. **Stationary models**: ARIMA, SARIMAX, and hybrid models like SARIMAX-LSTM.
2. **Advanced architectures**: CEEMDAN-LSTM (decomposes signal before LSTM) and N-BEATS (designed specifically for interpretable time series forecasting).
3. **Multivariate analysis**: Correlations with commodities, equity markets, and macroeconomic indicators.
4. **Broader GSS bond universe**: Extending analysis to Bloomberg MSCI Green Bond Index and other social/sustainability bonds.
5. **Greenium analysis**: Studying the yield premium of green bonds pre- and post-COVID.

The study serves as a methodological foundation, demonstrating the feasibility of applying modern ML techniques to green bond forecasting. While initial results are inconclusive, the authors argue that neural networks offer potential for complex time series problems where traditional statistical models may fall short. The paper emphasizes that the choice of architecture (CNN, LSTM, etc.) may become more impactful once richer input windows and multivariate features are incorporated.

In summary, this work provides a rigorous, reproducible framework for time series forecasting in sustainable finance. It highlights the importance of data preprocessing, hyperparameter tuning, and model selection in financial applications. The modest performance gains underscore the challenge of predicting financial time series with minimal input, while the planned extensions promise more meaningful insights in subsequent papers.

**Word count: ~1,500**