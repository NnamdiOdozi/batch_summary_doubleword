## Document Metadata

**S/N:** 1  
**Title:** Evolution of economic scenario generators: a report by the Extreme Events Working Party members  
**Authors:** P. Jakhria, R. Frankland, S. Sharp, A. Smith, A. Rowe, T. Wilkins  
**Date of publication:** 2019-02-22 (presented); published in British Actuarial Journal, Vol. 24, e4, 2019  
**Topic:** Actuarial Science / Financial Modeling  
**Sub-topic:** Economic Scenario Generators (ESGs) in Insurance and Pension Fund Modeling  
**URL:** https://doi.org/10.1017/S1357321718000181  

---

## Summary

### 1. Modeling Techniques

The paper does not describe a single modeling technique but rather traces the historical evolution of modeling approaches used in economic scenario generation (ESG) for actuarial applications. The techniques discussed span several decades and include:

- **Random Walk Models**: Early stochastic models based on Brownian motion and geometric Brownian motion, pioneered by Louis Bachelier (1900) and later formalized by Norbert Wiener and Kiyoshi Ito. These models assume asset prices follow a path where future changes are independent of past changes and are normally distributed. They were foundational for modern portfolio theory (Markowitz, 1952) and later option pricing models.

- **Time Series Models**: Primarily represented by the Wilkie model (1984), which uses autoregressive moving average (ARMA) structures to model relationships between economic variables such as inflation, equity returns, and interest rates. The model employs a “cascade” structure where inflation drives other variables. Later extensions include multivariate ARMA, VAR (Vector Auto Regressive), and GARCH (Generalized Autoregressive Conditional Heteroskedasticity) models to capture volatility clustering and non-stationarity.

- **Market-Consistent (MC) and Arbitrage-Free Models**: Driven by financial economics and option pricing theory (Black-Scholes, 1973; Merton, 1973), these models are calibrated to market prices of traded instruments (e.g., options, bonds) and ensure no arbitrage opportunities exist. Examples include Vasicek, Hull-White, Cox-Ingersoll-Ross (CIR) for interest rates, and geometric Brownian motion with stochastic volatility or jumps for equities. These models are used for pricing and valuing liabilities with embedded options or guarantees.

- **Value at Risk (VaR) Models**: Used for capital adequacy calculations under regulatory regimes like ICAS and Solvency II. These are typically based on historical simulation or parametric distributions fitted to historical data (not market prices) and focus on extreme tail events (e.g., 99.5th percentile over 1 year). They often employ copulas to model correlations between risk factors.

The paper emphasizes that these modeling paradigms are not mutually exclusive but have coexisted and evolved in parallel, with different models being preferred for different purposes (e.g., strategic asset allocation vs. regulatory capital calculation).

### 2. Code Availability

**Not available.** The paper is a historical and conceptual review of modeling evolution and does not provide or reference any specific implementation code, GitHub repositories, or software packages. While some models (e.g., Wilkie model) were published with equations and parameters suitable for spreadsheet implementation, no open-source or downloadable code is mentioned.

### 3. Learning Type

**Not applicable.** The paper does not describe machine learning or statistical learning models trained on data in the modern ML sense. The modeling techniques discussed (random walks, time series, arbitrage-free pricing) are based on mathematical finance and econometric theory rather than supervised, unsupervised, or self-supervised learning algorithms. Parameter estimation in time series models (e.g., ARMA) may involve statistical inference, but this is not framed as “learning” in the ML context.

### 4. Dataset

The paper does not describe a single dataset used for model training or validation. Instead, it references:

- **Historical UK time series data** (1919–1982) used by Wilkie to calibrate his model.
- **Historical market data** (e.g., equity indices, interest rates, inflation) used for calibrating time series and VaR models.
- **Option prices and yield curves** used to calibrate market-consistent models.
- **Real-world data** from UK pension funds and insurers for asset allocation examples (e.g., Figure 2).

No specific dataset names (e.g., CRSP, FRED, Bloomberg) are provided. The focus is on the *type* of data used (historical, market-based, macroeconomic) rather than on specific sources or repositories.

### 5. Implementation Details

- **Programming language(s):** Not specified. The paper predates widespread use of Python/R for actuarial modeling. Wilkie’s original model was implemented in spreadsheets; later models may have used MATLAB, SAS, or proprietary software (e.g., Towers Perrin’s system).
- **Key libraries/frameworks:** Not specified. No mention of TensorFlow, PyTorch, scikit-learn, or similar ML libraries. Traditional statistical packages (e.g., R’s `forecast`, `tseries`, or SAS/ETS) may have been used for time series, but this is not stated.

### 6. Model Architecture

The paper does not describe a single composite model architecture but outlines the structure of key historical models:

- **Wilkie Model (1984, 1995)**: A cascade of time series equations. Inflation is the root variable, driving:
  - Equity returns (via dividend yield and payout)
  - Long-term interest rates (via consol yield, modeled as a 3rd-order AR process)
  - Short-term interest rates
  - Property returns
  - Wage inflation
  The model is parsimonious (few variables) but complex in its interdependencies. It was designed for long-term actuarial use, not short-term forecasting.

- **Market-Consistent Models**: Typically multi-factor, arbitrage-free models. For example:
  - **Interest rate models**: One-factor (Vasicek) or multi-factor (Hull-White) models that fit the initial yield curve and ensure no arbitrage.
  - **Equity models**: Geometric Brownian motion with drift, extended with stochastic volatility (Heston) or jumps (Merton).
  These models are often solved via PDEs (Black-Scholes) or Monte Carlo simulation.

- **VaR Models**: Not a single architecture but a methodology. Typically:
  - Simulate or estimate joint distribution of risk factors (interest rates, equities, inflation) using historical data or parametric assumptions.
  - Apply copulas to model dependence.
  - Calculate the 99.5th percentile loss over 1 year (Solvency II requirement).
  - The “critical stress” is the combination of factor movements that maximizes capital shortfall.

### 7. Technical Content

The paper provides a comprehensive historical account of how economic scenario generators (ESGs) have evolved in the UK actuarial profession over the past 50 years, driven by technical innovation, regulatory changes, and shifts in investment practice. The core narrative is that ESGs have progressed from simple random walk models to complex, multi-factor, market-consistent, and regulatory-driven frameworks, each addressing new challenges in modeling the uncertainty of capital markets for long-dated insurance and pension liabilities.

#### Origins of Stochastic Modeling in Actuarial Science

The need for stochastic models arose from the limitations of deterministic approaches, which assumed a single, fixed future (e.g., best-estimate interest rate). Early actuarial work focused on mortality and fixed-income investments, where deterministic models sufficed. However, as UK insurers began investing in equities and property from the 1920s onward (equity allocation rose from 2% in 1920 to 21% by 1952), the volatility and path-dependence of asset returns made deterministic models inadequate. The 1980 Maturity Guarantee Working Party (MGWP) report highlighted this: for maturity guarantees, investment risk cannot be matched, and policies are not independent, leading to high variability in claims. Thus, a distribution of outcomes — not just an expected value — was needed.

The advent of electronic computers (ENIAC, 1945) and the Monte Carlo method (Ulam, von Neumann, Metropolis, 1947–1949) enabled the practical simulation of stochastic paths. Monte Carlo relies on random number generation to simulate many possible future scenarios, allowing actuaries to assess tail risks and the full distribution of outcomes. Early random number generators (e.g., von Neumann’s “middle-square” method) were crude, but the principle — using randomness to explore uncertainty — became foundational.

#### The Challenge of Stochastic Asset Models (SAMs)

Modeling assets for insurers is uniquely challenging due to three factors:

1. **Global Asset Allocation**: UK pension funds and insurers have diversified geographically and across asset classes (equities, bonds, property, alternatives). This diversification improves risk-adjusted returns but complicates modeling, as each asset class has different risk-return characteristics and interdependencies. A truly accurate model would need to capture capital flows within and between asset classes and countries — a task of immense complexity.

2. **Long-Dated Liabilities**: Insurance and pension liabilities often span decades. Models must extrapolate scenarios far into the future, requiring not just accuracy but also stability over long horizons. The 2003 Prudential Sourcebook introduced the “Realistic Balance Sheet,” emphasizing that balance sheet volatility is driven by asset-side fluctuations. This forced insurers to model long-term asset behavior, not just short-term returns.

3. **Capital Regulations**: Regulations like ICAS (2004) and Solvency II (2016) require models to estimate extreme events (e.g., 1-in-200-year losses) that may lie far outside historical experience. This “extrapolation in probability” demands models that can simulate rare, severe scenarios — a challenge for data-driven models that rely on historical data.

#### Evolution of ESGs: Four Stages

The paper identifies four broad stages in ESG evolution:

1. **Random Walk Models (Pre-1980s)**: Based on Bachelier’s (1900) and Wiener’s (1920s) work, these models assume asset prices follow a random path with constant volatility. Markowitz’s (1952) portfolio theory showed how to optimize portfolios based on mean and variance, leading to the efficient frontier and CAPM. Advantages: intuitive, easy to calibrate to historical data, aligned with efficient market hypothesis. Disadvantages: no mean reversion, poor fit for long-term liabilities, ignores correlations between asset classes.

2. **Time Series Models (1980s–1990s)**: Dominated by the Wilkie model (1984), which used ARMA structures to model inflation, equity returns, and interest rates in a “cascade.” Wilkie’s model was designed for actuarial use — long-term, transparent, and practical (implementable in spreadsheets). It gained widespread adoption due to its publication, ease of use, and alignment with actuarial beliefs (e.g., mean reversion in equities). However, it had limitations: strong mean reversion could lead to unrealistic results (e.g., underestimating tail risk), and it was not arbitrage-free. The 1992 Geoghegan Working Party report critiqued its statistical foundations, warning against “enthroning” a single model without understanding its weaknesses.

3. **Market-Consistent (MC) and Arbitrage-Free Models (Late 1990s–2000s)**: Driven by financial economics (Black-Scholes, 1973) and regulatory demand for fair value accounting, these models are calibrated to market prices (e.g., option implied volatilities, yield curves) to ensure no arbitrage. They are used for pricing liabilities with embedded options (e.g., with-profits guarantees). Examples include Vasicek (interest rates) and geometric Brownian motion with stochastic volatility (equities). Advantages: consistent with market prices, suitable for valuation. Disadvantages: complex to calibrate, sensitive to parameter choices, may not reflect real-world probabilities (requires “risk premium” adjustments).

4. **VaR Models (2000s–Present)**: Required by ICAS and Solvency II for capital adequacy, these models focus on the 99.5th percentile loss over 1 year. They typically use historical simulation or parametric distributions fitted to historical data (not market prices) and employ copulas to model correlations. Advantages: regulatory compliance, focus on tail risk. Disadvantages: poor at modeling contagion (e.g., 2008 crisis), assumes constant volatility, may overfit to recent data (e.g., falling rates), and lacks economic plausibility in extreme scenarios.

#### Key Transitions and Drivers

The shift from one model type to another was rarely a clean replacement. Instead, models coexisted, each serving different purposes:

- **Wilkie to MC Models**: Driven by the need for market-consistent valuations (e.g., for with-profits liabilities) and regulatory changes (e.g., 2003 Prudential Sourcebook). MC models were not “better” but addressed different problems (valuation vs. strategic planning).

- **MC to VaR Models**: Driven by Solvency II’s 1-year VaR requirement. VaR models are not a replacement for MC models but a regulatory add-on for capital calculation. Interviewees noted that insurers often use MC models for business decisions and VaR models for compliance.

Key drivers of evolution include:

- **Regulation**: The largest driver historically (e.g., ICAS, Solvency II, Realistic Balance Sheet).
- **Technology**: Increased computing power enabled Monte Carlo simulation and complex models.
- **Investment Practice**: Globalization and diversification increased model complexity.
- **Academic Influence**: Financial economics (Black-Scholes, CAPM) gradually permeated actuarial thinking.
- **User and Developer Dissatisfaction**: Limitations in existing models (e.g., Wilkie’s mean reversion) spurred innovation.

#### Current State and Future Directions

As of 2019, the insurance industry uses a mix of models:

- **Strategic Asset Allocation**: Often uses time series or MC models for long-term projections.
- **Regulatory Capital**: Uses 1-year VaR models (Solvency II).
- **Product Pricing**: Uses MC models for liabilities with guarantees.

Interviewees emphasized the importance of understanding model limitations and communicating them to users. There is a growing need for:

- **Longer-Term Real-World Modeling**: Driven by ORSA (Own Risk and Solvency Assessment), which requires multi-year projections.
- **Greater Transparency**: To customers and regulators, requiring models that can explain portfolio outcomes.
- **Integration with Financial Planning**: Actuarial education may need to include lifetime financial planning.
- **Technological Advancements**: Cloud computing and big data enable more granular modeling, but Occam’s razor (simplicity) remains important. Machine learning is seen as a potential disruptor but is constrained by the need for real-time market data.

International perspectives vary: Canada uses regime-switching models (Hardy), the US has a minimal profession-wide ESG, and Switzerland has regulator-led ESG development. The paper suggests the term “ESG” may be confusing due to its use in “Environmental, Social, Governance” and proposes “CMM” (Causal Market Model) or “SAM” (Stochastic Asset Model) as alternatives.

In conclusion, the evolution of ESGs reflects a journey from simple, intuitive models to complex, regulatory-driven frameworks. The future will likely see a blend of real-world and market-consistent models, driven by both regulation and the need for better long-term decision-making in an increasingly uncertain world.