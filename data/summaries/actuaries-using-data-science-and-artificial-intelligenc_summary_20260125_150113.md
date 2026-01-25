## Document Metadata

**S/N:** 1  
**Title:** Actuaries using data science and artificial intelligence techniques  
**Authors:** Alan Marshall  
**Date of publication:** 2024-02  
**Topic:** Actuarial science and artificial intelligence  
**Sub-topic:** Application of data science and AI techniques in actuarial practice, regulatory considerations, and professional development  
**URL:** Not available  

---

## Summary

### 1. Modeling Techniques

The document does not focus on specific algorithmic implementations or model architectures in the technical sense, but rather surveys the *types* of modeling techniques actuaries are adopting or experimenting with across various domains. The following techniques are mentioned:

- **Generalized Linear Models (GLM)**: Traditionally dominant in actuarial pricing, especially in General Insurance (GI), now considered one among many regression/forecasting tools.
- **Gradient Boosting Machines (GBM)**: Increasingly adopted in GI pricing due to superior predictive performance over GLMs.
- **Random Forests**: Used in multiple case studies including earnings progression modeling and life underwriting decision prediction. Ensemble learning approaches are highlighted.
- **Markov Models**: Applied in loan portfolio analysis to predict borrower earnings transitions.
- **Large Language Models (LLMs)**: Used experimentally to parse product specification documents (PDF, Word, web) and auto-generate actuarial models. Also used to build capital models from scratch via prompting.
- **Deep Learning-based Semantic Search**: Applied to process unstructured text (reports, documents) by understanding context rather than keyword matching.
- **Explainable AI (XAI)**: Explicitly mentioned in the context of lapse modeling to interpret model outputs and gain insights beyond traditional assumptions.
- **Neural Networks**: Mentioned in the context of constraints (smoothness, monotonicity) for model behavior, though no specific architecture is detailed.
- **Reinforcement Learning**: Cited in a conference topic for dynamic hedging of variable annuities, indicating exploratory use.

The report emphasizes that actuaries are moving beyond “vanilla” statistical models toward more complex, often ensemble or machine learning-based techniques, particularly where predictive accuracy or automation is valued. However, the report does not delve into hyperparameter tuning, loss functions, or training procedures — it remains at a conceptual and applied level.

### 2. Code Availability

**Not available.** The document does not mention any publicly available code repositories, GitHub links, or open-source implementations of the models or techniques described. Case studies are presented as organizational or individual applications without code sharing. The report focuses on governance, ethics, and professional practice rather than technical reproducibility.

### 3. Learning Type

The document does not specify the learning paradigms (supervised, unsupervised, self-supervised) for the models described. However, based on the applications:

- **Supervised Learning** is implied in most cases: pricing models (predicting premiums), underwriting models (predicting approval/rejection), lapse modeling (predicting policy termination), and earnings prediction (regression task).
- **Unsupervised or Self-supervised Learning** is not explicitly mentioned, though semantic search systems may leverage self-supervised pre-training (e.g., via LLMs), this is not elaborated.
- **Reinforcement Learning** is referenced as a topic for dynamic hedging, which is inherently an online, reward-based learning paradigm.

In summary, the dominant learning type inferred from use cases is **supervised learning**, though the report does not classify models by learning type.

### 4. Dataset

The datasets referenced are primarily **real-world, proprietary, and industry-specific**. No public datasets are named. Examples include:

- **GI Claims Triangles**: Paid claims, provisions, reported but unsettled reserves across firms and lines of business.
- **Pension Scheme Data**: Active, pensioner, and dependent member data including date of birth, gender, movement dates, pension/salary amounts.
- **Loan Portfolio Data**: Borrower demographics (date of birth, gender, loan inception year), historical earnings, field of work.
- **Life Insurance Applications**: Customer, policy, medical, and family history data collected at application.
- **Unstructured Text Data**: Reports and documents requiring semantic search.
- **Weather and Agricultural Data**: Satellite and farmer data for weather-indexed crop insurance in Africa.
- **Product Specification Documents**: PDFs, Word files, web pages used as input for LLM-based model generation.

Datasets are typically internal to the organizations involved and not publicly accessible. The report emphasizes data quality, bias, and GDPR compliance as key concerns, but does not provide dataset statistics (size, features, time periods).

### 5. Implementation Details

- **Programming language(s):**  
  - **Python**: Used for dashboarding and visualization in pension experience analysis.  
  - **R**: Used for data mining/analysis in earnings progression modeling (random forests), and planned migration for pension experience analysis.  
  - **Proprietary Software**: Mentioned for GI claims triangle analysis and actuarial model building (via LLMs).  
  - **Open-source frameworks**: Referenced in the context of building capital models, though no specific language is named.

- **Key libraries/frameworks:**  
  - **R packages**: Specifically mentioned for data mining and random forests (e.g., `randomForest`, `caret`, or similar — though not named).  
  - **Python libraries**: Not explicitly listed, but implied for dashboarding (e.g., `Dash`, `Streamlit`, `Plotly`) and machine learning (e.g., `scikit-learn`, `XGBoost`).  
  - **Third-party AI libraries**: Used to analyze documents for model generation (e.g., likely Hugging Face, spaCy, or proprietary NLP tools).  
  - **LLM APIs**: Implied for document parsing and capital model generation (e.g., OpenAI GPT, Anthropic Claude, or internal LLMs).

No specific versions or dependencies are provided. The focus is on functional outcomes rather than technical stack.

### 6. Model Architecture

The report does not provide detailed architectural diagrams or component breakdowns of composite models. However, the following architectural patterns are implied:

- **Ensemble Models**: In life underwriting, multiple random forest models are combined to predict decisions — this suggests a voting or stacking ensemble.
- **Pipeline Architecture**: In pension experience analysis, a two-stage pipeline: (1) data cleaning and exposure-to-risk derivation, (2) dashboard visualization in Python.
- **LLM-Powered Model Generation**: A hybrid system where LLMs parse unstructured inputs (documents) → output structured data → proprietary software builds actuarial models. This is a “prompt-to-model” architecture.
- **Semantic Search System**: Likely based on transformer-based embeddings (e.g., BERT, Sentence-BERT) for vector retrieval, paired with a vector database (e.g., FAISS, Pinecone) and possibly a reranker.
- **Markov Transition Models**: Used for earnings progression, implying a state-space model with transition probabilities between earnings bands.

No neural network architectures (e.g., CNN, LSTM, Transformer layers) are detailed beyond the mention of “neural networks” in the context of constraints. The report avoids technical depth on architecture, favoring functional descriptions.

### 7. Technical Content

The report “Actuaries using data science and artificial intelligence techniques” by Alan Marshall, published by the Institute and Faculty of Actuaries (IFoA) in February 2024, is a thematic review examining the evolving role of actuaries in the age of data science and AI. It is not a technical paper presenting novel algorithms or empirical results, but rather a comprehensive survey of industry practices, regulatory landscapes, ethical considerations, and professional development needs. The document synthesizes insights from case studies, regulatory research, conference proceedings, and stakeholder interviews to provide a holistic view of how actuaries are engaging with AI/ML technologies across traditional and emerging domains.

#### Context and Motivation

The report opens with a recognition that while actuaries have historically been “data scientists” in spirit — analyzing large datasets to infer future risks — the modern tools of AI and machine learning offer unprecedented capabilities. The rapid proliferation of generative AI (especially LLMs) since late 2022 has accelerated adoption and raised new ethical, governance, and transparency challenges. The IFoA’s Regulatory Board, which commissioned the review, is particularly concerned with ensuring that AI applications in actuarial work balance commercial interests with consumer fairness and public interest.

#### Key Findings and Case Studies

The review identifies eight key findings, supported by a range of case studies that illustrate practical applications:

1. **Rapidly Changing Environment**: The increasing capacity and accessibility of AI tools, coupled with growing data volumes, are transforming actuarial work. This introduces new risks (bias, lack of explainability, reputational damage) alongside opportunities (better risk modeling, product innovation).

2. **Growing Actuarial Involvement**: Actuaries are increasingly involved in AI/ML across domains beyond traditional GI pricing — including pensions, life underwriting, claims analysis, capital modeling, and even non-traditional areas like African agriculture insurance. Many organizations report plans to expand usage further.

3. **Broadening Application Scope**: Applications now span risk management, reporting, retention, marketing, and model validation. For example, a case study describes using ML to analyze GI claims triangles for trend detection across firms — a task previously done manually or with basic statistical methods.

4. **Collaboration with Data Scientists**: Actuaries often work alongside data scientists and other experts. Organizations prioritize skills over professional qualifications, which may challenge the traditional actuarial value proposition. This necessitates continuous upskilling.

5. **Global Regulatory Activity**: There is significant and accelerating regulatory activity worldwide, with jurisdictions like the EU (AI Act), China (specific regulations), and the UK (pro-innovation white paper) taking divergent approaches. Common themes include fairness, transparency, accountability, and safety.

6. **Existing Standards Are Relevant**: The IFoA’s Actuaries’ Code (especially Principles 2 and 6 on competence and communication) and existing Technical Actuarial Standards (TASs) provide a foundation for ethical AI use. However, there is a tension between creating specific AI standards (which may become obsolete) and adapting existing guidance.

7. **Education and Lifelong Learning**: The IFoA curriculum includes data science elements in Actuarial Statistics, Specialist Principles, and Specialist Advanced modules. The IFoA Data Science Certificate (with University of Southampton) offers upskilling for qualified members. Plans are underway to expand both pathways.

8. **Opportunities for Collaboration**: The IFoA has a strong track record of collaboration with bodies like the Royal Statistical Society and the Alan Turing Institute. There are opportunities to engage with global actuarial associations and regulators to shape responsible AI practices.

#### Technical Case Studies in Detail

- **GI Personal Lines Pricing**: Gradient Boosting Machines (e.g., XGBoost, LightGBM) are replacing GLMs due to better handling of non-linear relationships and interactions. This reflects a broader industry shift toward ensemble methods for pricing accuracy.

- **GI Claims Triangle Analysis**: An off-the-shelf ML software package uses pattern recognition to identify trends in claims development triangles. The output is consistent and rapid, though validation and ranking of trends are still underway. This highlights the move toward automation in reserving.

- **Pension Experience Analysis**: A two-stage pipeline: first, data is cleaned and exposure-to-risk is calculated; second, outputs are visualized in a Python dashboard. The intention is to migrate to R for faster processing and enhanced modeling (e.g., workforce dynamics, lump sum propensity).

- **Model Build from Documents**: Generative AI (LLMs) parses product specs (PDF, Word, web) and feeds into proprietary software to auto-generate actuarial models. This reduces manual model-building time and allows for rapid iteration, though human review is still required.

- **Loan Portfolio Earnings Modeling**: A Markov model predicts earnings transitions. A sub-project uses random forests to validate and improve the model. Feature importance from random forests identifies key predictors (e.g., field of work, historical earnings), affirming the Markov model’s robustness while suggesting enhancements.

- **Life Underwriting**: An ensemble of random forest models predicts underwriting decisions for 25% of applications (the 75% are handled by rules). The model optimizes risk cost loading and has been in production for five years, demonstrating long-term operational viability.

- **Semantic Search for Unstructured Text**: A deep learning system (likely transformer-based) enables context-aware retrieval from reports. This moves beyond keyword search to understand user intent, handling ambiguity and complexity in natural language. It is in user acceptance testing.

- **Lapse Modeling with XAI**: Machine learning models (likely tree-based or neural) are applied to lapse rates, with explainable AI techniques used to interpret outputs. Comparisons with traditional models reveal trade-offs between accuracy and interpretability.

- **Capital Model in Open-Source Framework**: An actuary with no coding experience built a capital model using an LLM by asking questions. The model was then showcased in a dashboard. This demonstrates the potential of LLMs as “co-pilots” for complex actuarial tasks, though reproducibility and governance remain concerns.

- **AI for African Crop Insurance**: Weather-indexed insurance for small-scale farmers uses satellite and farm data with ML algorithms to reduce costs and increase uptake. This is an example of AI for social good, enhancing food security and resilience.

#### Ethical and Regulatory Considerations

Ethics and fairness are central to the report. Key challenges include:

- **Bias and Discrimination**: Models may perpetuate or amplify biases in training data. Solutions include fairness testing at development and pre-implementation stages, and redeveloping models if bias is found.
- **Data Privacy and GDPR**: Organizations are advised to use reputable AI providers or private LLM instances to ensure compliance.
- **Explainability**: AI/ML models are often less explainable than traditional actuarial models, posing a challenge for governance and stakeholder communication. Explainable AI (XAI) techniques are being explored.
- **Professional Competence**: Actuaries must ensure they have the necessary skills (Principle 2 of the Code). Organizations are encouraged to demonstrate competence via accreditation (e.g., IFoA’s Quality Assurance Scheme).

The report notes that ethical considerations are often discussed at the team level, with a need for standardized definitions and internal policies. Actuaries’ existing ethical code provides a strong foundation, but firms with mixed professional teams need consistent internal frameworks.

#### Global Regulatory Landscape

The report provides a snapshot of global AI regulation as of end-2023:

- **EU**: AI Act (provisional agreement Dec 2023) — strict, with bans on social scoring, biometric ID by law enforcement, and requirements for consumer explanations.
- **UK**: Pro-innovation approach, with discussion papers and a white paper. Focus on principles rather than prescriptive rules.
- **China**: Already has specific regulations (Ethical Norms, Generative AI Measures) — one of the few jurisdictions with enforceable rules.
- **US**: Mix of executive orders (White House), bipartisan frameworks, and NAIC principles. Regulatory activity is fragmented across agencies.
- **Singapore**: MAS toolkit for responsible AI, with a planned generative AI risk framework.
- **Australia**: AI Ethics Principles (non-binding).
- **Global**: OECD AI Principles, Bletchley Declaration, and NCSC/CISA guidelines for secure AI development.

Common themes across jurisdictions include **fairness, transparency, accountability, robustness, and safety**. The report notes that while principles are converging, implementation may vary, creating challenges for multinational firms.

#### Professional Development and Education

The IFoA’s education pathway includes data science in:

- **Actuarial Statistics**: Introduction to large datasets, ML, and software tools.
- **Specialist Principles**: Domain-specific applications (e.g., GI, Life).
- **Specialist Advanced**: Ethical and regulatory aspects.

Lifelong learning is supported via the Data Science Certificate and ongoing CPD. The report acknowledges a risk to the profession’s relevance if learning resources do not keep pace with technological change. Plans are underway to enhance both curriculum and CPD offerings.

#### Conclusion and Future Directions

The report concludes that the increasing use of data science and AI presents both opportunities and risks for actuaries. To remain competitive, actuaries need evolving resources for professional development and standards that support them as both builders and users of AI systems. The IFoA Regulatory Board supports a review of ethical guidance and continued development of professional skills material. Collaboration with global actuarial associations and other agencies is encouraged to drive responsible and ethical use of AI.

The report does not prescribe specific technical solutions but emphasizes the need for:

- **Ethical frameworks** tailored to actuarial practice.
- **Governance processes** that ensure model explainability and fairness.
- **Education** that keeps pace with technological change.
- **Collaboration** across professions and borders.

In essence, the report serves as a call to action for the actuarial profession to proactively engage with AI/ML technologies, ensuring that their application is safe, transparent, and in the public interest — while preserving the profession’s core values of competence, integrity, and public trust.

--- 

**Word Count:** ~1520 words