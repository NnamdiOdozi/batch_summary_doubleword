## Document Metadata

**S/N:** 1  
**Title:** Actuaries using data science and artificial intelligence techniques  
**Authors:** Alan Marshall  
**Date of publication:** 2024-02  
**Topic:** Application of data science and AI in actuarial practice  
**Sub-topic:** Ethical, regulatory, and technical adoption of machine learning and AI in actuarial domains  
**URL:** Not available  

---

## Summary

### 1. Modeling Techniques

The report does not focus on a single modeling technique but instead surveys a wide range of AI and data science methodologies currently in use or under exploration by actuaries. Techniques mentioned include:

- **Generalized Linear Models (GLM)**: Still widely used in General Insurance (GI) pricing, though increasingly supplemented or replaced by more advanced methods.
- **Gradient Boosting Machines (GBM)**: Gaining popularity in GI pricing for their predictive power and ability to handle non-linear relationships.
- **Random Forests**: Used in multiple case studies, including modeling borrower earnings progression and predicting underwriting decisions. Ensemble learning approaches are emphasized for robustness.
- **Markov Models**: Applied in loan portfolio analysis to predict earnings transitions.
- **Large Language Models (LLM)**: Used to automatically build actuarial models from unstructured product specification documents (PDFs, Word, web text) and to assist in building capital models from scratch.
- **Deep Learning-Based Semantic Search**: Applied to process large volumes of unstructured text (e.g., reports) by understanding context and meaning rather than relying on keyword matching.
- **Explainable AI (XAI)**: Used in lapse modeling to interpret model outputs and gain insights into drivers of policyholder behavior.
- **Reinforcement Learning**: Mentioned in the context of dynamic hedging for variable annuities (in conference topics).
- **Neural Networks with Constraints**: Smoothness and monotonicity constraints applied to neural networks in pricing contexts.

The report highlights that while traditional actuarial models (e.g., GLMs) remain relevant, there is a clear trend toward adopting more complex, data-driven techniques—particularly ensemble methods and machine learning—to improve predictive accuracy and handle larger, more heterogeneous datasets.

### 2. Code Availability

**Not available.** The report does not mention any publicly available code repositories, GitHub links, or open-source implementations associated with the case studies or methodologies described. The focus is on high-level applications, ethical considerations, and regulatory implications rather than technical reproducibility.

### 3. Learning Type

The report does not specify a single learning paradigm across all case studies. However, based on the techniques described:

- **Supervised Learning** is predominant: Most applications (e.g., underwriting prediction, earnings modeling, lapse rate prediction) involve labeled data and target variable prediction.
- **Unsupervised Learning** is implied in semantic search and clustering applications for text analysis.
- **Self-supervised Learning** is not explicitly mentioned, though LLMs used for document parsing and model generation likely rely on pre-trained self-supervised architectures.
- **Reinforcement Learning** is mentioned in conference topics (dynamic hedging), indicating exploratory use in actuarial contexts.

Overall, the learning type is **predominantly supervised**, with emerging interest in unsupervised and reinforcement methods.

### 4. Dataset

The report references multiple datasets but does not provide detailed metadata (e.g., size, structure, public availability). Key datasets include:

- **General Insurance Claims Triangles**: Paid claims, provisions, and reported-but-not-settled reserves across multiple firms and lines of business.
- **Pension Scheme Experience Data**: Includes active, pensioner, and dependent member data (date of birth, gender, movement dates, pension/salary amounts) for experience analysis.
- **Loan Portfolio Data**: Borrower demographics (date of birth, gender, loan inception year, field of work) and historical earnings.
- **Life Insurance Application Data**: Customer, policy, and high-level medical/family history disclosures for underwriting prediction.
- **Unstructured Text Data**: Reports, product specifications (PDF, Word, web text) processed via LLMs.
- **Weather and Agricultural Data**: Satellite and farmer data for weather-indexed crop insurance in Africa.

All datasets appear to be **real-world, proprietary data** collected by institutions (insurers, pension funds, lenders). No synthetic datasets are mentioned. Data sources are not publicly available.

### 5. Implementation Details

- **Programming language(s):**  
  - **Python**: Used for dashboarding and model deployment (e.g., in pension experience analysis).
  - **R**: Used for statistical modeling and data mining (e.g., random forests for earnings modeling).
  - **Not specified**: For LLM-based model generation and semantic search systems, though likely Python-based given industry norms.

- **Key libraries/frameworks:**  
  - **Scikit-learn**: Implied for random forests and other ML models.
  - **XGBoost/LightGBM**: Likely used for gradient boosting in GI pricing.
  - **Hugging Face Transformers / LangChain**: Implied for LLM applications (though not named).
  - **Pandas/NumPy**: For data preprocessing (implied in Python dashboarding).
  - **Shiny (R)** or **Plotly Dash (Python)**: For dashboarding (implied in pension analysis).
  - **Not specified**: For Markov models or deep learning semantic search.

The report does not provide explicit library names for most case studies, but the tools used are consistent with industry-standard data science stacks.

### 6. Model Architecture

The report describes several composite and non-vanilla architectures:

- **Ensemble Learning (Random Forest)**: Used in underwriting prediction. Multiple decision trees are trained on bootstrapped samples and combined via voting or averaging. Feature importance is extracted to understand drivers.
- **LLM-Powered Model Builder**: Proprietary software uses third-party AI libraries (e.g., NLP models) to parse unstructured documents and generate actuarial models. Architecture likely involves:
  - Document ingestion → Text embedding → Intent/structure extraction → Model template generation → Customization interface.
- **Semantic Search System**: Deep learning-based, likely using transformer architectures (e.g., BERT variants) for contextual understanding. Architecture:
  - Query embedding → Document embedding → Vector similarity search → Relevance ranking.
- **Markov Transition Model**: Discrete-state, discrete-time model for predicting borrower earnings progression. States defined by earnings bands; transitions estimated from historical data.
- **Explainable AI (XAI) for Lapse Modeling**: Likely uses SHAP or LIME to explain predictions from black-box models (e.g., GBM or neural networks).

No deep neural network architectures (e.g., CNNs, RNNs) are described in detail, though “neural networks with constraints” are mentioned in conference topics.

### 7. Technical Content

The report provides a comprehensive overview of how actuaries are integrating data science and AI into traditional and emerging domains. It is structured around findings derived from case studies, surveys, and regulatory analysis, with a strong emphasis on ethical, governance, and educational implications.

#### Context and Motivation

Actuaries have historically been “data scientists” by nature—analyzing large datasets to project future risks (e.g., mortality, asset returns). However, the rapid evolution of AI tools (especially LLMs since late 2022) has intensified the need for actuaries to adapt. The IFoA launched this thematic review to assess current adoption, identify risks, and inform future guidance. The review collected submissions from organizations (e.g., Royal London, Prudential Regulation Authority) and individuals, supplemented by interviews and regulatory research.

#### Key Technical Applications

**1. General Insurance Pricing**  
Traditionally reliant on GLMs, GI pricing now incorporates Gradient Boosting Machines (GBMs) and other ensemble methods. These models handle non-linearities and interactions better than GLMs, improving predictive accuracy. The shift reflects a broader industry trend toward “black-box” models, raising concerns about explainability and governance.

**2. Claims Analysis**  
Machine learning is used to analyze claims triangles across firms. Off-the-shelf software applies pattern recognition to identify trends in paid claims, provisions, and reserves. This enables faster, consistent diagnostics across lines of business. The approach is still experimental but shows promise for automating actuarial reserving.

**3. Pension Experience Analysis**  
A Python dashboard processes cleaned pension data (member movements, retirements, mortality) to generate visualizations and summaries. The system is being migrated to R for speed and flexibility. Future enhancements include modeling workforce dynamics (e.g., propensity to leave service, lump sum choices).

**4. Actuarial Model Generation from Documents**  
Generative AI is used to build actuarial models from unstructured inputs (PDFs, Word docs, websites). Third-party NLP libraries extract key terms and structure, which proprietary software converts into executable models. This reduces manual model-building time and allows rapid customization.

**5. Earnings Modeling for Loan Portfolios**  
A Markov model predicts borrower earnings progression. A sub-project uses random forests to validate and enhance this model. Feature importance analysis identifies key predictors (e.g., field of work, historical earnings). The ML model confirms the Markov model’s robustness and suggests improvements.

**6. Life Underwriting**  
75% of applications are auto-decided via rules; the remaining 25% are scored by ensemble ML models (random forests). Multiple models are combined to optimize risk loading and decision profiles. The system has been in production for five years, demonstrating stability and business value.

**7. Semantic Search for Unstructured Text**  
A deep learning system retrieves information from reports by understanding natural language queries. Unlike keyword-based search, it captures context and meaning, handling ambiguity and variability. The system is in user acceptance testing, indicating early-stage deployment.

**8. Lapse Rate Modeling**  
Machine learning (e.g., GBM) is applied to model policyholder lapses, a critical assumption for pricing and reserving. XAI techniques (e.g., SHAP) explain model outputs, revealing drivers like policy age or premium level. Comparisons to traditional models show trade-offs between accuracy and interpretability.

**9. Capital Modeling in Open-Source Frameworks**  
An actuary with no coding experience built a capital model using an LLM. The LLM generated code and explanations, which were then packaged into a user-friendly dashboard. This experiment highlights LLMs’ potential to democratize complex modeling—but also raises questions about competence and oversight.

**10. AI for Insurance in Africa**  
Weather-indexed crop insurance for small-scale farmers uses AI/ML on satellite and farmer data. The goal is to reduce administrative costs and increase uptake, enhancing food security. This application extends actuarial work into development economics and social impact.

#### Ethical and Governance Challenges

Ethics and fairness are central themes. Key concerns include:

- **Bias and Discrimination**: Models may perpetuate or amplify biases in training data (e.g., in underwriting or pricing). Fairness checks are conducted at development and pre-implementation stages.
- **Explainability**: AI models (especially LLMs and deep learning) are often “black boxes.” Actuaries must balance predictive power with transparency to meet regulatory and ethical standards.
- **Data Privacy**: GDPR compliance is critical. Solutions include using reputable AI providers or private LLM instances.
- **Professional Competence**: Actuaries must ensure they have the skills to build, validate, or review AI models. The Actuaries’ Code (Principle 2) mandates competence; Principle 6 requires accurate, non-misleading communication.
- **Governance**: Firms are adapting existing model risk management frameworks for AI/ML. The FRC’s TAS 100 and Model Guidance explicitly cover emerging AI models.

#### Regulatory Landscape

Global regulators are actively developing AI frameworks. Common themes include:

- **Safety and Robustness**: Ensuring models operate reliably and mitigate harm.
- **Fairness**: Avoiding discrimination and benefiting society.
- **Transparency**: Explaining model decisions.
- **Accountability**: Clear oversight and challenge processes.

Key jurisdictions:

- **UK**: Pro-innovation approach; discussion papers and white papers underway.
- **EU**: AI Act (adopted Dec 2023) bans social scoring and mandates explanations.
- **China**: Has specific regulations (e.g., for generative AI).
- **Singapore**: MAS toolkit for responsible AI; planned generative AI risk framework.
- **US**: Executive order on AI; bipartisan framework under development.
- **Global**: OECD principles, Bletchley Declaration, NCSC/CISA guidelines.

The IFoA’s position is to adapt existing standards (e.g., Actuaries’ Code, TASs) rather than create AI-specific rules, given the fast pace of change. A 2023 Risk Alert reminds members of key risks (bias, lack of explainability, data security).

#### Educational and Professional Development

The IFoA offers:

- **Curriculum**: Data science covered in Actuarial Statistics (large datasets, ML), Specialist Principles (domain applications), and Specialist Advanced (ethics/regulation).
- **Lifelong Learning**: Certificate in Data Science (with University of Southampton); webinars, conferences, and community-led workstreams.
- **Future Plans**: Enhance curriculum and CPD to keep pace with AI developments. Risk of obsolescence if education lags.

#### Collaboration and Future Directions

Actuaries increasingly work alongside data scientists, with employers prioritizing skills over qualifications. This poses a challenge to the profession’s relevance. Opportunities exist to collaborate with:

- Other actuarial associations (e.g., SOA, Actuaries Institute Australia).
- Institutes (Alan Turing Institute, RSS).
- Regulators (FRC, PRA, MAS).

The IFoA encourages this collaboration to shape responsible AI use globally.

#### Conclusions

The report concludes that:

1. AI/ML adoption is accelerating across actuarial domains (beyond GI pricing), creating opportunities but also risks (bias, lack of transparency, skill gaps).
2. Global regulation is evolving rapidly, with a focus on responsible, ethical AI. Actuaries must navigate this landscape using existing standards while advocating for proportionate, relevant guidance.
3. Education and collaboration are critical to maintaining the profession’s relevance. The IFoA must continue developing resources and fostering partnerships.

In essence, actuaries are well-positioned to lead in responsible AI adoption—but only if they embrace continuous learning, ethical rigor, and cross-disciplinary collaboration.

--- 

**Word count**: ~1520 words