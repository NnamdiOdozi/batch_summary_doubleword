## Document Metadata

**S/N:** 1  
**Title:** Treasury Committee Inquiry: AI in Financial Services — IFoA Response  
**Authors:** Institute and Faculty of Actuaries (IFoA), Steven Graham (Technical Policy Manager)  
**Date of publication:** 2025-04-11  
**Topic:** Artificial Intelligence in Financial Services  
**Sub-topic:** Regulatory, Ethical, and Operational Implications of AI Adoption in Insurance, Pensions, Investment, and Risk Management  
**URL:** Not available (document provided as text; original source likely actuaries.org.uk)

---

## Summary

### 1. Modeling Techniques

The document does not describe specific machine learning or AI algorithms (e.g., CNNs, LSTMs, XGBoost) in technical detail. Instead, it broadly references **narrow AI** (primarily data science and machine learning) and **Generative AI (GenAI)** as the two main categories of AI currently in use within financial services. The focus is on *application domains* rather than model architectures.

Examples of AI applications mentioned include:
- **Predictive analytics** for underwriting, pricing, and customer segmentation in general and life insurance.
- **Fraud detection models** using anomaly detection techniques.
- **Personalized disease management programs** in health insurance.
- **Sentiment analysis** of unstructured data (news, social media, earnings calls) for investment decisions.
- **Climate risk modeling** and ESG impact analysis using AI-enhanced catastrophe models.
- **RegTech applications** for automated compliance, contract analysis, and real-time risk monitoring.
- **Chatbots and voice assistants** for customer service (with human oversight for complex queries).
- **Retrieval Augmented Generation (RAG)** and **prompt engineering** to mitigate hallucinations in GenAI outputs.

No specific neural network architectures, ensemble methods, or deep learning frameworks are detailed. The emphasis is on *functional use cases* rather than algorithmic implementation.

### 2. Code Availability

**Not available.** The document does not mention any publicly available code repositories, GitHub links, or open-source implementations of the AI systems discussed. The IFoA’s work is policy-oriented and focuses on guidance, ethics, and governance rather than technical code sharing.

### 3. Learning Type

The document does not specify whether the AI applications described use **supervised, unsupervised, or self-supervised learning**. However, based on the context of use cases (e.g., fraud detection, underwriting, pricing), it is reasonable to infer that most applications rely on **supervised learning**, where models are trained on labeled historical data (e.g., claims outcomes, customer churn, market movements).

Generative AI (e.g., chatbots, document summarization) likely employs **self-supervised or foundation models** (like LLMs), but this is not explicitly stated.

### 4. Dataset

The document references **real-world data** used in financial services, including:
- Customer transaction records
- Claims data
- Health and mortality records
- Market data (news, earnings calls, social media)
- Environmental and climate risk datasets
- Pension fund performance data

No specific dataset names or public sources (e.g., Kaggle, UCI, FRED) are provided. The IFoA mentions **Federated Learning** as a technique to train models without sharing raw data across insurers, implying that data is proprietary and not publicly available.

The document also highlights **data quality** and **bias in training data** as critical concerns, particularly when datasets are historic, incomplete, or unrepresentative of protected groups.

### 5. Implementation Details

- **Programming language(s):** Not specified.
- **Key libraries/frameworks:** Not specified.

The document does not discuss technical implementation tools. Instead, it references **cloud-based systems** (used by Fintech firms) and **legacy systems** (used by traditional insurers, often Excel-based). It also mentions **proprietary third-party AI tools** from large tech firms (e.g., ChatGPT), but does not name specific frameworks like TensorFlow or PyTorch.

### 6. Model Architecture

No detailed model architectures are provided. The document refers to:
- **“Black-box” AI models** — implying complex, non-interpretable models (e.g., deep neural networks or ensemble models) whose internal logic is not transparent.
- **Autonomous AI agents** — mentioned as a future trend, but not defined technically.
- **Reinforcement Learning from Human Feedback (RLHF)** — referenced as a technique to mitigate herding behavior in financial models, but no architecture details are given.

The focus is on *functional outcomes* (e.g., “AI improves pricing accuracy”) rather than *technical design*.

### 7. Technical Content

The IFoA’s response to the UK Treasury Committee’s inquiry on AI in financial services is a comprehensive, policy-oriented analysis of the opportunities, risks, and governance challenges associated with AI adoption. It is written from the perspective of the actuarial profession, which the IFoA positions as uniquely qualified to navigate the ethical, technical, and regulatory complexities of AI due to its long-standing expertise in risk modeling, data analysis, and ethical decision-making.

#### AI Adoption Across Financial Services

AI is already embedded across multiple domains within financial services, with actuaries playing a central role in its application. Key areas include:

- **General Insurance**: AI enhances underwriting by analyzing granular datasets to improve risk segmentation and pricing. It also automates claims processing and detects fraud through pattern recognition. Customer segmentation and targeted marketing are optimized using predictive analytics.
  
- **Health & Care Insurance**: AI enables personalized disease management programs, helping both patients and insurers by improving health outcomes and reducing claims costs.

- **Life Insurance**: AI refines mortality and longevity predictions, allowing for more accurate pricing. Underwriting triage systems speed up the application process by flagging high-risk cases for human review.

- **Pensions**: AI analyzes investment performance, assesses long-term risk scenarios, and improves member engagement by providing personalized retirement planning insights.

- **Investments**: AI processes vast amounts of unstructured data (news, social media, earnings calls) to detect market trends, optimize asset allocation, and personalize investment strategies.

- **Risk Management**: AI monitors news and data feeds to identify emerging risks, helping risk managers adjust strategies proactively.

- **Environmental Risk Analysis**: AI models assess climate risks, perform catastrophe modeling, and evaluate ESG impacts, aiding firms in managing sustainability-related exposures.

Additionally, AI is used to automate financial reporting, audit trails, and compliance processes, reducing manual effort and improving consistency.

#### Productivity Gains and Use Cases

AI has significant potential to improve productivity by automating routine, low-risk tasks such as:
- Generating meeting minutes and model documentation
- Processing claims and underwriting applications
- Cleansing and assembling data
- Performing compliance checks and reserving calculations
- Providing 24/7 customer service via chatbots (with human oversight for complex issues)
- Detecting fraud and anomalies in transactions
- Personalizing user interfaces and financial advice
- Improving risk assessment and capital modeling

The IFoA emphasizes that while AI can automate repetitive tasks, it also creates opportunities for employees to focus on higher-value activities, such as interpreting AI outputs, managing model governance, and ensuring ethical compliance.

#### Barriers to Adoption

Despite its potential, AI adoption faces several barriers:
- **Cost**: AI transformation requires significant investment in infrastructure, consultancy, and training.
- **Workforce Training**: Financial professionals need upskilling to work effectively with AI tools.
- **Data Quality**: AI models depend on high-quality, unbiased data; poor data leads to flawed outputs.
- **Regulatory Uncertainty**: Firms are cautious due to unclear governance frameworks and the risk of regulatory lag.
- **Cultural Resistance**: Some firms are hesitant due to fear of cyber threats, data leaks, or ethical concerns.
- **Legacy Systems**: Many insurers still rely on Excel spreadsheets and non-cloud systems, making AI integration difficult.
- **Explainability**: “Black-box” models lack transparency, complicating regulatory approval.
- **GenAI Hallucinations**: Generative AI can produce plausible but incorrect outputs, requiring safeguards like RAG and prompt engineering.

#### Job Displacement and Reskilling

AI is likely to displace administrative and manual processing roles, particularly in claims, underwriting, and data entry. However, the IFoA highlights opportunities for reskilling into roles focused on:
- Interpreting AI outputs
- Model governance and risk management
- AI ethics and bias mitigation
- Data quality and explainability

New roles will require multidisciplinary expertise in algorithms, governance, and ethics.

#### Risks to Financial Stability

AI introduces several systemic risks:
- **Cybersecurity**: AI-driven attacks can exploit vulnerabilities at scale, amplified by interconnected systems. Open-source AI models may contain hidden vulnerabilities.
- **Third-Party Dependencies**: Reliance on a few large tech firms (e.g., for LLMs) creates systemic risk. Firms may lack clarity on model complexity or data usage.
- **Model Complexity**: “Black-box” models are hard to audit, increasing the risk of unintended consequences.
- **Herding Behavior**: Financial models trained on similar data may lead to market instability. RLHF is proposed as a mitigation.
- **GenAI Hallucinations**: Outputs that are plausible but incorrect can undermine trust and require costly verification.

Mitigations include:
- Upgrading cyber resilience
- Performing independent AI audits
- Stress testing models
- Requiring explainability
- Diversifying AI providers

#### Consumer Benefits and Risks

AI offers consumers:
- More accurate risk assessments (potentially lowering premiums for low-risk individuals)
- Personalized financial products and advice
- Improved fraud detection
- Better engagement with pensions and investments
- Identification of vulnerabilities through real-time data analysis

However, risks include:
- **Bias and Discrimination**: AI may replicate or amplify existing biases, particularly if trained on historic, unrepresentative data. For example, using postcode as a proxy for ethnicity can lead to unfair pricing.
- **Financial Exclusion**: Overly accurate risk assessment may render products unaffordable for high-risk individuals.
- **Lack of Transparency**: Consumers may not understand or challenge AI-driven decisions.
- **Mis-selling**: AI-driven sales processes may target vulnerable consumers without adequate safeguards.

The IFoA recommends:
- **Ethics by Design**: Embedding ethical principles into model development.
- **Bias Testing**: Mandatory testing for discrimination, even if using third-party tools.
- **Transparency**: Clear communication of AI decisions to consumers.
- **Redress Mechanisms**: Easy avenues for consumers to challenge AI outcomes.
- **Federated Learning**: Training models on pooled data without sharing raw data, preserving privacy.

#### Regulatory Approach

The IFoA advocates for a **principles-based, rather than rules-based**, regulatory framework to keep pace with AI’s rapid evolution. Key recommendations include:
- Adapting existing conduct and prudential regulations to cover AI, avoiding duplication.
- Focusing on how AI is used in context (e.g., consumer fairness, financial inclusion).
- Balancing risk management with innovation to maintain trust.
- Using regulatory sandboxes to test AI innovations responsibly.
- Aligning with global standards to ensure a level playing field.

The IFoA also emphasizes the need for:
- **Firm Governance**: Ensuring AI governance is embedded in second and third lines of defense.
- **Staff Training**: Equipping employees with knowledge of AI ethics and limitations.
- **Multidisciplinary Collaboration**: Engaging academia, industry, and regulators to develop best practices.

#### Energy and Climate Impact

AI’s energy consumption is a growing concern. The International Energy Agency predicts global data center energy use could double by 2030, conflicting with climate goals. The IFoA calls for solutions like:
- Locational flexibility (placing data centers near renewable sources)
- Operational flexibility (adjusting usage based on energy availability)
- Increased use of renewables

#### Conclusion

The IFoA positions actuaries as essential stakeholders in the responsible adoption of AI in financial services. Their skills in critical thinking, ethics, and risk management are crucial for navigating AI’s complexities. The document concludes that while AI offers transformative benefits, its risks — including bias, opacity, and systemic fragility — require proactive governance, ethical oversight, and global collaboration. The UK, with its strong Fintech ecosystem and AI research, is well-placed to lead in responsible AI adoption, provided regulation balances innovation with consumer protection.

The IFoA invites further engagement with policymakers to ensure AI evolves in a way that serves the public interest, promotes financial stability, and enhances consumer welfare.