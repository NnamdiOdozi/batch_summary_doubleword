## Document Metadata

**S/N:** 1  
**Title:** Evolution of economic scenario generators: a report by the Extreme Events Working Party members  
**Authors:** P. Jakhria, R. Frankland, S. Sharp, A. Smith, A. Rowe, T. Wilkins  
**Date of publication:** 2019-01-01 (as per journal volume; original presentation: 2018-02-22)  
**Topic:** Actuarial Science  
**Sub-topic:** Economic Scenario Generators (ESGs) and their historical evolution in insurance and pension modeling  
**URL:** https://doi.org/10.1017/S1357321718000181

---

## Summary

### 1. Modeling Techniques

The document traces the evolution of Economic Scenario Generators (ESGs) used in actuarial science, particularly in the UK insurance and pension industries. The modeling techniques discussed span multiple paradigms:

- **Random Walk Models**: Early stochastic models based on Brownian motion and geometric Brownian motion, inspired by Louis Bachelier’s 1900 thesis and later formalized by Norbert Wiener and Kiyoshi Ito. These models assume asset prices follow a random path with no memory, often used in early financial theory and option pricing.

- **Time Series Models**: Specifically, the Wilkie model (1984) is highlighted as the dominant actuarial ESG for decades. It is an ARMA (AutoRegressive Moving Average) model with a cascade structure linking inflation, equity returns, and interest rates. The model uses historical UK data (1919–1982) to estimate parameters and assumes stationarity and mean reversion in key variables.

- **Market-Consistent (MC) and Arbitrage-Free Models**: Introduced in the 1990s–2000s, these models are grounded in financial economics and option pricing theory (Black-Scholes, Merton). They ensure that asset prices are consistent with current market prices (no-arbitrage) and often use stochastic differential equations (SDEs) to model asset dynamics. Examples include Vasicek, Hull-White, and LIBOR market models for interest rates, and geometric Brownian motion with stochastic volatility or jumps for equities.

- **Value at Risk (VaR) Models**: Used primarily for regulatory capital calculations (e.g., Solvency II), these models focus on estimating the 99.5th percentile loss over a 1-year horizon. They often rely on historical data to estimate distributions and use copulas to model correlations between risk factors. Unlike full stochastic models, VaR models are typically calibrated to historical stress events rather than market prices.

The paper does not describe machine learning or deep learning techniques, as the focus is on historical evolution up to the early 2010s. The modeling approaches are primarily statistical and econometric, with increasing sophistication over time.

### 2. Code Availability

**Not available.** The document is a historical and conceptual review of ESG evolution. It does not provide implementation code, GitHub repositories, or software packages. While some models (e.g., Wilkie) were published with formulas and parameters, no executable code or open-source implementations are referenced. The paper notes that proprietary models (e.g., Towers Perrin’s system) were developed but not fully disclosed.

### 3. Learning Type

**Not applicable.** The document does not describe machine learning models trained on data. Instead, it discusses statistical and econometric models calibrated to historical data or market prices. The learning type (supervised, unsupervised, etc.) is not relevant to the techniques described, which are parametric and theory-driven rather than data-driven in the ML sense.

### 4. Dataset

The paper references several datasets and data sources, but does not provide direct access to them:

- **Historical UK economic data (1919–1982)**: Used by Wilkie to calibrate his model, including inflation, equity prices, and interest rates.
- **De Zoete equity index**: Used by the Maturity Guarantee Working Party (1980) to model equity prices.
- **ONS (Office for National Statistics) data**: Cited for UK inflation figures (Figure 5).
- **Historical market prices**: Used for calibrating arbitrage-free models (e.g., option prices for Black-Scholes).
- **Historical stress events**: Used for VaR models, though the paper notes limitations due to limited data (e.g., 10 years of falling interest rates may bias stress tests).

The datasets are real-world, not synthetic. Specific dataset names (e.g., “De Zoete index”) are mentioned, but no direct links or access instructions are provided. The paper emphasizes that data availability and quality have historically constrained model development, especially for extreme events.

### 5. Implementation Details

- **Programming language(s):** Not specified. The paper notes that the Wilkie model could be coded in spreadsheets, implying Excel or similar tools were used in practice. No specific languages (Python, R, MATLAB) are mentioned.
- **Key libraries/frameworks:** Not specified. The document predates modern ML frameworks (TensorFlow, PyTorch) and focuses on statistical methods (ARMA, GARCH, SDEs) implemented via custom code or spreadsheets. Libraries like scikit-learn or statsmodels are not referenced.

### 6. Model Architecture

The paper describes several model architectures, with the Wilkie model being the most detailed:

- **Wilkie Model (1984, updated 1995)**: A cascade-structured ARMA model with:
  - **Primary variables**: Inflation (entry point), equity returns.
  - **Secondary variables**: Long-term fixed interest yield, dividend yield.
  - **Structure**: Inflation drives equity returns and interest rates. Equity returns are modeled as a function of dividend payout (random walk) and dividend yield (mean-reverting). The Consol yield is a third-order autoregressive process.
  - **Extensions (1995)**: Added monthly time steps, full yield curve term structures, and parameter estimation error handling.

- **Arbitrage-Free Models**: Typically based on SDEs, e.g.:
  - **Black-Scholes PDE**: ∂V/∂t + ½σ²S²∂²V/∂S² + rS∂V/∂S − rV = 0, where V is option value, S is asset price, σ is volatility, r is risk-free rate.
  - **Interest rate models**: Vasicek (mean-reverting), Hull-White (extended Vasicek), Cox-Ingersoll-Ross (positive rates), LIBOR market model (for forward rates).
  - **Equity models**: Geometric Brownian motion with drift, stochastic volatility (e.g., Heston), or jumps (e.g., Merton).

- **VaR Models**: Not a single architecture but a methodology:
  - **Inputs**: Multiple risk factors (asset returns, liability stresses, correlations).
  - **Method**: Use historical data to estimate distributions, apply copulas for correlations, identify the 99.5th percentile stress (critical stress).
  - **Output**: Capital requirement to cover the worst 0.5% outcome over 1 year.

The paper notes that models are often composite, e.g., combining time series with arbitrage-free components, but does not provide architectural diagrams or code.

### 7. Technical Content

The paper provides a comprehensive historical review of Economic Scenario Generators (ESGs) in actuarial science, tracing their evolution from simple random walks to complex, regulation-driven models. The core narrative is that ESGs evolved in response to changing regulatory, technological, and economic environments, with key milestones driven by innovations in financial theory and computing power.

#### Origins and Motivation

The need for stochastic models in insurance arose from the complexity of long-dated liabilities, particularly with-profits policies, which required modeling surplus distribution. Early models were deterministic, relying on single-point estimates (e.g., best-estimate interest rates) and were adequate when insurers invested primarily in fixed-income assets with low volatility. However, as insurers began investing in equities and property (from 2% equity allocation in 1920 to 21% by 1952), the need for stochastic modeling increased to capture market risk.

The advent of electronic computers (ENIAC, 1945) and the Monte Carlo method (developed by Ulam, von Neumann, and Metropolis in the 1940s) enabled the practical simulation of stochastic paths. Monte Carlo methods rely on random number generation to simulate multiple scenarios, with early implementations using von Neumann’s “middle-square” generator. This laid the groundwork for modern ESGs, which simulate thousands of economic paths to assess risk.

#### Key Stages in ESG Evolution

The paper identifies four broad stages in ESG development:

1. **Random Walk Models (Early 20th Century)**: Based on Bachelier’s work on Brownian motion and Markowitz’s Modern Portfolio Theory (MPT). These models assumed asset prices follow a random path with no memory, capturing risk, return, and correlation. They were intuitive and easy to calibrate to historical data but failed to capture mean reversion or extreme events.

2. **Time Series Models (1980s–1990s)**: Dominated by the Wilkie model (1984), which introduced a cascade structure linking inflation, equity returns, and interest rates. Wilkie’s model was ARMA-based, with inflation as the entry point, and was designed for long-term actuarial use. It was widely adopted due to its transparency, practicality (could be coded in spreadsheets), and alignment with actuarial beliefs (e.g., mean reversion in equities). However, it was criticized for overemphasizing mean reversion and assuming normality, which limited its ability to model extreme events. The 1992 Geoghegan Working Party report highlighted these limitations, noting that actuaries without statistical training might misuse the model.

3. **Market-Consistent and Arbitrage-Free Models (1990s–2000s)**: Driven by the Black-Scholes option pricing model (1973) and the rise of financial economics. These models ensure that asset prices are consistent with current market prices (no-arbitrage) and are often used for valuing complex liabilities with embedded options (e.g., with-profits policies). Key models include Vasicek and Hull-White for interest rates, and geometric Brownian motion with stochastic volatility for equities. These models were initially slow to adopt in actuarial circles due to their complexity and the alien concept of no-arbitrage, but gained traction with regulatory changes (e.g., MC valuation requirements).

4. **VaR Models (2000s–Present)**: Introduced for regulatory capital calculations (e.g., Solvency II), these models focus on estimating the 99.5th percentile loss over 1 year. They use historical data to estimate distributions and copulas to model correlations, identifying the “critical stress” that maximizes capital requirements. While practical for regulation, they are criticized for ignoring contagion (e.g., 2008 crisis) and assuming constant volatility over time. The paper notes that VaR models are often “flat with respect to time” and may overstate risks based on limited historical data.

#### Technical Challenges and Limitations

The paper highlights several recurring challenges in ESG development:

- **Data Limitations**: Historical data is often insufficient, especially for extreme events. For example, calibrating interest rate stresses from 10 years of falling rates may overstate the risk of further declines and understate the risk of sharp rises. VaR models are particularly vulnerable to this, as they rely on historical data rather than market prices.

- **Model Complexity vs. Parsimony**: Wilkie’s model was praised for its simplicity but criticized for oversimplifying real-world behavior (e.g., ignoring jumps, negative rates). Arbitrage-free models are more sophisticated but harder to calibrate and require more judgment. The paper notes a trade-off between complexity and parsimony, with Occam’s razor often guiding model design.

- **Regulatory vs. Economic Reality**: Regulatory requirements (e.g., Solvency II’s 1-year VaR) often drive model development, but may not reflect economic reality. For example, 1-year VaR models ignore long-term risks and may not capture the true nature of liabilities. The paper suggests that ORSA (Own Risk and Solvency Assessment) may shift focus back to longer-term real-world modeling.

- **Social and Technical Criteria**: Model adoption is influenced by social factors (e.g., ease of use, auditability) as well as technical criteria (e.g., goodness of fit, back-testing). The paper notes that social criteria are rarely discussed in academic papers but are crucial in practice.

#### Current and Future Directions

The paper concludes with a discussion of future trends:

- **Regulatory Influence**: ORSA and MiFID II may drive a renewed focus on longer-term real-world modeling and greater transparency to customers. This could lead to more sophisticated ESGs that incorporate GDP growth (rather than inflation) as a key variable.

- **Technology**: Advances in cloud computing and big data may enable greater granularity, but complexity must be balanced with parsimony. Machine learning is mentioned as a potential disruptor, though constrained by the need for real-time data.

- **International Perspectives**: The paper notes differences in ESG use across countries, e.g., Canada’s regime-switching models (Mary Hardy), the US’s minimal profession-wide ESG, and Switzerland’s regulator-led development. These could inform future UK models.

- **Terminology**: The acronym “ESG” is noted to be at risk due to its association with Environmental, Social, and Governance factors. The paper suggests alternatives like CMM (Causal Capital Markets Model) or SAM (Stochastic Asset Model).

In summary, the paper provides a rich historical account of ESG evolution, emphasizing the interplay between theory, regulation, and practice. It highlights the ongoing tension between model sophistication and practicality, and suggests that future developments will be shaped by regulatory changes, technological advances, and a renewed focus on long-term economic reality.