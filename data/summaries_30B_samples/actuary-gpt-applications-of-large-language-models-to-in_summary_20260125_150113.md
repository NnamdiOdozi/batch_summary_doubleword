## Document Metadata

**S/N:** 1  
**Title:** ACTUARYGPT: APPLICATIONS OF LARGE LANGUAGE MODELS TO INSURANCE AND ACTUARIAL WORK  
**Authors:** Caesar Balona  
**Date of publication:** 2023-08-17  
**Topic:** Artificial Intelligence in Actuarial Science  
**Sub-topic:** Large Language Models for Insurance Claims, Underwriting, Compliance, and Workflow Automation  
**URL:** https://ssrn.com/abstract=4543652  

---

## Summary

### 1. Modeling Techniques

The document primarily employs **Large Language Models (LLMs)**, specifically **GPT-4** and **GPT-3.5** from OpenAI, as the core AI technique. These models are transformer-based architectures trained on massive text corpora and are used for:

- **Natural Language Processing (NLP)** tasks including sentiment analysis, named entity recognition, text summarization, and classification.
- **Structured data extraction** from unstructured text (e.g., claims descriptions, reinsurance treaties, medical reports).
- **Prompt engineering** and **few-shot learning** to guide model outputs toward domain-specific tasks.
- **Context-aware querying** via vector databases to overcome context-length limitations of LLMs for regulatory compliance tasks.

No traditional machine learning models (e.g., decision trees, SVMs, random forests) are used as primary modeling tools. The focus is on leveraging pre-trained LLMs via API calls rather than training or fine-tuning models from scratch.

### 2. Code Availability

**Yes**, implementation code is available.

- **GitHub Repository:** https://github.com/cbalona/actuarygpt-code
- The repository contains Python scripts for:
  - Parsing claims descriptions (Case Study 1)
  - Extracting structured data from reinsurance treaties (Case Study 4)
  - Automating regulatory compliance via vector databases (Case Study 3)
  - Demonstrating prompt engineering and few-shot learning (Appendix C)

Code is provided for educational and demonstrative purposes and is not production-grade. It relies on the OpenAI API and libraries like `PyPDF2`, `chainladder`, and `pandas`.

### 3. Learning Type

The approach uses **supervised learning** in a narrow sense — the LLMs are pre-trained on massive datasets (unsupervised pre-training) and then **prompted or fine-tuned via instructions** (supervised fine-tuning via prompt design) to perform specific tasks.

However, the document does **not** describe traditional supervised training with labeled datasets. Instead, it relies on **in-context learning** (zero-shot or few-shot) where the model is guided by example inputs and desired output formats within the prompt.

Thus, the learning type is best described as:  
> **Prompt-based supervised inference using pre-trained LLMs**

### 4. Dataset

The datasets used are **synthetic or fictional**, generated for demonstration purposes:

- **Claims data** (JSON format) with policyholder interactions, medical reports, and police reports (Case Study 1).
- **Reinsurance treaties** (PDFs converted to text) for structured extraction (Case Study 4).
- **Regulatory documents** (FSI and GOI standards under SAM framework) for compliance querying (Case Study 3).
- **Automatically scraped news snippets** related to cyber risks (Case Study 2).

No real-world, proprietary, or public datasets are used. All data is fabricated to illustrate LLM capabilities without exposing sensitive information.

### 5. Implementation Details

- **Programming language(s):** Python
- **Key libraries/frameworks:**
  - `openai` (for API access to GPT-4 and GPT-3.5)
  - `PyPDF2` (for extracting text from PDFs)
  - `pandas` (for data manipulation)
  - `chainladder` (for IBNR reserving examples in Appendix C)
  - `json` (for structured output formatting)
  - `pinecone` (for vector database in regulatory knowledgebase — mentioned but not fully implemented in code)
  - `requests` (for API calls in some examples)

No custom model training frameworks (e.g., TensorFlow, PyTorch) are used. The implementation is entirely API-driven with minimal local computation.

### 6. Model Architecture

The document does not describe custom model architectures. It uses **off-the-shelf, pre-trained LLMs**:

- **GPT-4** and **GPT-3.5** (OpenAI models)
- These are **decoder-only transformer models** with billions of parameters, trained on internet-scale text data.

In Case Study 3, a **hybrid architecture** is proposed:

- **Vector Database (Pinecone)** stores embeddings of regulatory documents.
- **LLM (GPT-4)** queries the vector DB to retrieve relevant context before generating a response.
- This forms a **Retrieval-Augmented Generation (RAG)** pipeline, though not explicitly named.

No ensemble models, custom neural networks, or fine-tuned variants are implemented. The focus is on leveraging existing LLMs via API with prompt engineering.

### 7. Technical Content

The paper explores how Large Language Models (LLMs) can be integrated into actuarial and insurance workflows, both as direct automation tools and as assistance aids. The author, Caesar Balona, presents a structured framework for evaluating LLM suitability and demonstrates practical applications through four case studies.

#### Background and Motivation

Actuarial work traditionally relies on structured, numerical data. However, modern insurance operations generate vast amounts of unstructured text — claims descriptions, medical reports, emails, regulatory documents — which are difficult to process manually. LLMs offer a solution by enabling:

- **Natural Language Understanding (NLU)**: Extracting entities, sentiments, and inconsistencies from text.
- **Structured Output Generation**: Converting free-form text into JSON, tables, or summaries.
- **Workflow Automation**: Reducing manual labor in claims processing, underwriting, and compliance.

The paper emphasizes that LLMs are not replacements for actuaries but **augmentation tools** that enhance efficiency, reduce error, and free actuaries to focus on high-value reasoning tasks.

#### Direct Applications: Claims Process

The claims management process is broken down into 7 stages (Reporting, Adjusting, Investigating, Negotiating, Agreements, Payments, Compliance). LLMs can be embedded at each stage:

- **Reporting**: Extract incident details (date, location, type) from phone call transcripts or emails. Perform sentiment analysis to detect fraud signals (e.g., angry policyholders may exaggerate claims).
- **Adjusting**: Summarize all collected documents (medical, police, witness statements) for adjusters. Classify claims by severity (low/medium/high) to prioritize investigations.
- **Investigating**: Identify inconsistencies across documents (e.g., claimant says “stationary” but police report mentions “brake marks”). Flag potential fraud based on emotional tone or factual contradictions.
- **Compliance**: Query regulatory documents (e.g., SAM framework) to ensure claims handling meets legal requirements — using a vector database to overcome context-length limits.

A key innovation is the use of **NoSQL databases** to store flexible, unstructured claim data (e.g., sentiment scores, extracted entities, summaries) for cross-referencing and trend analysis over time.

#### Direct Applications: Other Insurance Functions

Beyond claims, LLMs can assist in:

- **Emerging Risk Identification**: Scrape news articles and summarize trends (e.g., cyber risks, climate change impacts) for risk committees. Generate action points and project plans from summaries.
- **Commercial Underwriting**: Extract key terms from technical reports (e.g., engineering safety assessments) and output them in structured formats (JSON) for underwriting systems.
- **Regulatory Compliance**: Build a “regulatory knowledgebase” using vector embeddings to answer queries about specific regulations (e.g., “How should real estate investments be stressed under SAM?”).

#### Decision Framework for LLM Suitability

The paper introduces a two-part decision tree to evaluate whether an LLM is appropriate for a given task:

1. **Technical Assessment Tree**:
   - Is the data unstructured or requires context/pattern recognition? → LLM suitable.
   - Does the task require generating new content or restructuring existing content? → LLM suitable.
   - Do benefits (automation, accuracy) outweigh costs (API fees, maintenance)? → Proceed if yes.
   - Do you have resources (data, expertise, compute)? → Proceed if yes.

2. **Risk Assessment Tree**:
   - Could bias affect outcomes? → Mitigate or avoid.
   - Is interpretability required? → Consider if LLM can explain outputs.
   - Is data leakage a risk? → Use private or ring-fenced models.
   - Is output variability acceptable? → Use low-temperature parameters.
   - Are adversarial inputs likely? → Validate outputs.
   - Are error consequences severe? → Implement human oversight.

An example application — extracting data from reinsurance treaties — passes both trees, making it a viable LLM use case.

#### Assistance Applications

LLMs can also serve as “assistants” to actuaries:

- **Coding Assistant**: Help write, debug, and optimize Python code (e.g., IBNR reserving using `chainladder` library). The paper includes a conversation where ChatGPT explains Python syntax and generates working code.
- **Problem Solving**: Actuaries can describe complex problems (e.g., pricing insurance for LLM-generated misinformation) and receive structured feedback, including scenario analysis and expert judgment suggestions.
- **Drafting Reports**: Summarize technical findings, generate executive summaries, or translate actuarial jargon into layman’s terms. Can also suggest visualizations or improve grammar.
- **Education**: Teach new statistical methods or programming concepts via interactive Q&A, analogies, and exercises.
- **Data Cleaning**: Use ChatGPT’s Code Interpreter plugin to upload datasets and generate cleaning code.
- **Model Interpretation**: Explain hyperparameters, validate assumptions, or translate model outputs for non-technical stakeholders.

#### Case Studies

**Case Study 1: Parsing Claims Descriptions**  
- Input: JSON with claim details, phone/email transcripts, medical/police reports.
- Prompt: Instructs GPT-4 to extract claim ID, policy ID, inconsistencies, claimant emotion, summary, and whether further assessment is needed.
- Output: Structured JSON with reasoning (e.g., “claimant is angry because they described the accident as ‘horrifying’”).
- Result: Demonstrates LLM’s ability to synthesize multi-source text and flag potential fraud.

**Case Study 2: Identifying Emerging Risks**  
- Input: Automatically scraped Google News results on cyber risks.
- Process: GPT-4 summarizes trends, generates action points, then creates project plans for each action.
- Output: Detailed project plan for “Cybersecurity Strategy and Continuous Monitoring” with phases, timeline, resources.
- Result: Shows LLMs can turn raw data into actionable business intelligence.

**Case Study 3: Regulatory Knowledgebase**  
- Problem: LLMs have limited context (e.g., GPT-4 handles ~12k words; IFRS 17 is 102 pages).
- Solution: Use Pinecone vector DB to store embeddings of regulatory docs (FSI, GOI).
- Query: “How should real estate investments be stressed?” → LLM retrieves relevant sections and answers precisely.
- Result: More accurate, domain-specific answers than generic ChatGPT responses.

**Case Study 4: Parsing Reinsurance Treaties**  
- Input: PDF reinsurance treaty.
- Process: Extract text → Prompt GPT-3.5 to output JSON with treaty details (type, reinsurer, layers, exclusions, etc.).
- Output: Structured JSON with loss layers, commissions, currency, arbitration clauses.
- Result: Automates a tedious manual task; useful for complex, variable contracts.

#### Ethical and Professional Considerations

The paper acknowledges significant risks:

- **Bias**: LLMs trained on internet data may reflect societal biases. Actuaries must validate outputs and avoid using LLMs in sensitive areas (e.g., pricing, underwriting) without oversight.
- **Hallucinations**: LLMs may invent facts or use non-existent libraries. Outputs must be reviewed.
- **Data Privacy**: Using public LLMs (e.g., ChatGPT) risks leaking confidential data. Solutions: Use private APIs, local LLMs, or ring-fenced models.
- **Professional Responsibility**: Actuaries remain accountable for LLM outputs. LLMs are tools, not decision-makers.
- **Interpretability**: LLMs are “black boxes.” Actuaries must ensure they can explain results to stakeholders.

The author stresses that LLMs should complement, not replace, human judgment. Actuaries must continuously monitor, validate, and understand LLM limitations.

#### Impact on the Actuarial Profession

LLMs will not replace actuaries but will transform their roles:

- **Efficiency Gains**: Automate routine tasks (data extraction, report drafting) to free time for strategic analysis.
- **Skill Shift**: Actuaries need to learn prompt engineering, AI ethics, and model validation.
- **Interdisciplinary Collaboration**: Work with data scientists, ethicists, and software engineers.
- **Communication**: Translate LLM outputs for non-technical stakeholders while acknowledging uncertainties.

The paper concludes that LLMs are powerful tools for enhancing actuarial work — if used responsibly, ethically, and with professional oversight.

#### Limitations and Future Work

- **No Fine-Tuning**: The paper uses only API-based LLMs without domain-specific fine-tuning.
- **Synthetic Data**: All case studies use fictional data; real-world validation is needed.
- **Cost**: API usage can become expensive at scale.
- **Context Limits**: Even with vector DBs, handling very long documents remains challenging.
- **Regulatory Uncertainty**: AI regulations are evolving; actuaries must stay informed.

Future research should explore fine-tuning LLMs on actuarial corpora, integrating LLMs with traditional actuarial models, and developing validation frameworks for LLM outputs.

---

**Word Count**: ~1500 words (excluding metadata and headers)