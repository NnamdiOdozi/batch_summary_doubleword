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

The document explores the application of **Large Language Models (LLMs)** — specifically **GPT-3.5 and GPT-4** from OpenAI — across multiple domains in actuarial and insurance work. These models are not trained from scratch for specific actuarial tasks but are leveraged via **prompt engineering**, **few-shot learning**, and **API-based integration** to perform tasks such as:

- **Text summarization** (e.g., summarizing claims descriptions, medical reports, police reports)
- **Sentiment and emotion analysis** (e.g., detecting policyholder anger or distress)
- **Named Entity Recognition (NER)** (e.g., extracting dates, locations, parties from free-text claims)
- **Information extraction and structuring** (e.g., parsing reinsurance treaties into JSON, extracting inconsistencies in claims)
- **Regulatory compliance assistance** (via vector databases for context-aware querying)
- **Emerging risk identification** (e.g., summarizing news articles on cyber risks)
- **Code generation and debugging** (e.g., assisting actuaries with IBNR reserving code in Python)
- **Scenario analysis and stress testing** (e.g., generating economic impact assessments for geopolitical events)

The paper does not describe training custom neural architectures but focuses on **zero-shot and few-shot prompting** of pre-trained LLMs to perform domain-specific tasks. The LLMs are treated as **black-box assistants** or **automation engines** rather than models trained on actuarial datasets.

### 2. Code Availability

**Yes**, implementation code is available. The paper references a **GitHub repository** containing Python scripts for all case studies:

- **Repository URL:** https://github.com/cbalona/actuarygpt-code
- The repository includes code for:
  - Parsing claims descriptions (Case Study 1)
  - Automating reinsurance treaty extraction (Case Study 4)
  - Regulatory knowledgebase construction (Case Study 3 — partial code referenced)
  - Example scripts for news scraping and summarization (Case Study 2)

The code uses the **OpenAI API** to interact with GPT-3.5 and GPT-4, and includes utilities for PDF text extraction (PyPDF2), JSON schema enforcement, and vector database integration (Pinecone).

### 3. Learning Type

The approach primarily uses **zero-shot and few-shot learning** — meaning the LLMs are **not fine-tuned** on actuarial datasets. Instead, they are prompted with instructions, examples, or schemas to perform tasks on-demand.

- **Zero-shot**: The model is given a task without prior examples (e.g., “Summarize this claim”).
- **Few-shot**: The model is shown 2–3 examples of desired input-output pairs before being asked to generalize (e.g., demonstrating how to format economic impact scenarios before asking for a new one).

This is **not supervised learning** in the traditional sense (no labeled training data is used to update model weights). It is **prompt-based inference** using pre-trained models.

### 4. Dataset

The datasets used are **synthetic or illustrative**, generated for demonstration purposes:

- **Claims data**: Fictional JSON structures containing claim IDs, policyholder IDs, incident descriptions, communication logs (phone/email transcripts), medical reports, and police reports.
- **Reinsurance treaties**: Simplified, fabricated PDF documents used to demonstrate structured data extraction.
- **Regulatory documents**: Real documents from the **South African Solvency Assessment and Management (SAM)** framework (FSI and GOI standards), embedded into a vector database.
- **News articles**: Scraped results from Google searches on cyber risks (simulated for the case study).

No real-world, proprietary insurance datasets are used. The paper emphasizes that LLMs can handle **unstructured data** (free text, PDFs, emails) and convert them into **structured formats** (JSON, databases) — a key value proposition.

### 5. Implementation Details

- **Programming language(s):** Python
- **Key libraries/frameworks:**
  - `openai` (for API access to GPT-3.5/GPT-4)
  - `PyPDF2` (for extracting text from PDFs in Case Study 4)
  - `pandas` (for data manipulation)
  - `json` (for schema validation and output formatting)
  - `requests` (for web scraping in Case Study 2)
  - `pinecone` (for vector database in Case Study 3 — referenced but not fully implemented in repo)
  - `chainladder` (used in Appendix C for IBNR reserving example)

The paper also references **GitHub Copilot** (a code-specific LLM) and **ChatGPT plugins** (like Code Interpreter) as auxiliary tools for data cleaning and code generation.

### 6. Model Architecture

The paper does not describe custom model architectures. Instead, it leverages **off-the-shelf LLMs**:

- **GPT-3.5 and GPT-4** (OpenAI): These are **decoder-only transformer models** with billions of parameters, trained on massive web corpora. They are accessed via API and used as black boxes.
- **No fine-tuning** is performed. The models are used in their **base, pre-trained form**.
- **Composite systems** are built around the LLMs:
  - **Vector database + LLM** (Case Study 3): Pinecone stores embeddings of regulatory documents; queries are matched to relevant context before being passed to GPT-4.
  - **Prompt + Schema + LLM** (Case Study 4): A JSON schema is provided to GPT-3.5 to enforce structured output.
  - **Few-shot prompt + LLM** (Appendix C.3): Examples are provided to guide output format.

The architecture is **modular**: LLMs are embedded in workflows (e.g., claims processing pipeline, regulatory compliance tool) rather than being end-to-end models.

### 7. Technical Content

The paper presents a comprehensive exploration of how Large Language Models (LLMs) — particularly OpenAI’s GPT-3.5 and GPT-4 — can be integrated into actuarial and insurance workflows. The core thesis is that LLMs are not replacements for actuaries but powerful **assistants and automation tools** that can handle unstructured data, reduce manual labor, and enhance decision-making — provided they are used responsibly and with appropriate safeguards.

#### Direct Applications in Claims Processing

The paper details a **7-step claims management process** (Reporting → Adjusting → Investigating → Negotiating → Agreements → Payments → Compliance) and maps LLM applications to each stage:

- **Reporting**: LLMs extract structured data (date, location, incident type) from free-text inputs (emails, call transcripts). They also perform **sentiment analysis** to detect anger or distress, which may indicate fraud or need for customer support. **Entity recognition** identifies key people, places, and events. The output is stored in a **NoSQL database** (e.g., MongoDB) for flexibility in handling unstructured data.
  
- **Adjusting**: LLMs summarize information from multiple sources (call logs, emails, reports) into a structured report for adjusters. They can also **classify claims by severity** (low/medium/high) based on descriptions (e.g., “bumper bashing” vs. “high-impact collision”) to prioritize investigations.

- **Investigating**: LLMs identify **inconsistencies** across documents (e.g., police report vs. claimant statement) to flag potential fraud. They can also be given policy terms to assess whether claims violate conditions (e.g., speeding in motor claims).

- **Negotiating, Agreements, Payments**: LLMs are less directly involved here, but insights from earlier stages (e.g., sentiment, severity, fraud risk) inform negotiations and automate payment triggers.

- **Compliance**: LLMs ingest regulatory documents (via vector databases) and answer queries about compliance (e.g., “Does this claim comply with GOI Section 5.2?”). This automates a traditionally manual, time-consuming task.

The paper emphasizes that LLMs **add value by automating labor-intensive tasks** (e.g., data entry, document summarization) and **providing new insights** (e.g., detecting fraud patterns, identifying emotional cues) that would be too costly to gather manually.

#### High-Level Applications in Other Insurance Functions

Beyond claims, the paper explores LLM applications in:

- **Emerging Risk Identification**: LLMs analyze scraped news articles to identify trends (e.g., rising cyber risks, climate-related litigation) and generate **actionable summaries and project plans**. For example, after summarizing cyber risks, the LLM generates “Action Points” and then creates detailed “Project Plans” for each point — demonstrating **recursive prompting**.

- **Commercial Underwriting**: LLMs extract key information from technical reports (e.g., engineering assessments) and output it in structured formats (e.g., JSON) for underwriting systems. This streamlines the review of complex documents.

- **Compliance**: LLMs can answer queries against internal policy documents or regulatory texts. The paper demonstrates this using a **vector database** (Pinecone) to overcome the LLM’s context length limitation. For example, when asked “How should a real estate investment be stressed on the balance sheet?”, the LLM returns a generic answer without context, but with the SAM regulatory knowledgebase, it returns a precise, regulation-specific answer.

#### Decision Framework for LLM Suitability

The paper introduces a **two-part decision framework** to evaluate whether an LLM is suitable for a given task:

1. **Technical Assessment Tree**:
   - Is the data structured/numeric? → If yes, traditional methods may suffice.
   - Does the task require generating new content or complex pattern recognition? → If yes, LLMs may be suitable.
   - Do the benefits (accuracy, efficiency) outweigh costs (API fees, maintenance)?
   - Do you have the resources (data, expertise, compute)?

2. **Risk Assessment Tree**:
   - Could bias negatively impact the task?
   - Are there ethical concerns (e.g., using social media data)?
   - Is interpretability required? (Critical for actuaries who must attest to results.)
   - Is there a risk of data leakage or memorization?
   - Is output variability acceptable?
   - Are adversarial conditions likely?
   - Are the consequences of errors acceptable?

The framework is applied to a real-world example: **extracting structured data from reinsurance treaties**. The technical assessment concludes LLMs are suitable (complex pattern recognition needed, benefits outweigh costs). The risk assessment identifies minimal risk (no content generation, low variability, data leakage mitigated via ring-fenced models).

#### Assistance Applications: LLMs as Actuarial Assistants

The paper dedicates a section to **indirect, assistant-style applications** of LLMs:

- **Coding Assistant**: LLMs help write, debug, and optimize code (e.g., Python for IBNR reserving). The paper includes a transcript where ChatGPT explains Python concepts (e.g., “dot notation”, “random seeds”) and generates working code using the `chainladder` library.

- **Problem Solving**: LLMs help actuaries articulate problems, explore solutions, and refine ideas. For example, when asked to price a policy for LLM-generated misinformation, ChatGPT advises on risk quantification, scenario analysis, and expert judgment — demonstrating **collaborative problem-solving**.

- **Drafting Reports and Summarization**: LLMs can generate executive summaries, translate technical findings into layman’s terms, and even create visualizations (charts, infographics) to accompany reports. The key is providing **detailed prompts** (e.g., “Summarize this report in 3 bullet points, tone: formal, focus on financial impact”).

- **Education**: LLMs serve as tutors, explaining concepts (e.g., hyperparameter tuning), providing analogies, and simulating business scenarios for training.

- **Data Cleaning and Preparation**: Using ChatGPT’s Code Interpreter plugin, users can upload datasets and ask the LLM to clean, analyze, or visualize data — accelerating the EDA phase.

- **Model Development and Interpretation**: LLMs help explain model assumptions, suggest hyperparameter search spaces, and translate complex model outputs for non-technical stakeholders.

#### Case Studies

The paper includes four detailed case studies with code:

1. **Parsing Claims Descriptions (Case Study 1)**: GPT-4 analyzes a claim (including call logs, medical, and police reports) to extract claim ID, policy ID, inconsistencies, claimant emotion, and summary. Output is in JSON for system integration. Example: Detects that a claimant’s description of “horrifying accident” contradicts a police report stating “no serious injuries”.

2. **Identifying Emerging Risks (Case Study 2)**: GPT-4 summarizes scraped news on cyber risks, generates “Action Points”, and then creates “Project Plans” for each action — demonstrating **multi-step prompting**.

3. **Regulatory Knowledgebase (Case Study 3)**: Uses Pinecone to store embeddings of SAM regulatory documents. When asked “How should a real estate investment be stressed?”, the LLM returns a regulation-specific answer, unlike the generic response without context.

4. **Parsing Reinsurance Documents (Case Study 4)**: GPT-3.5 extracts structured data (treaty type, reinsurer, loss layers, exclusions) from a PDF reinsurance treaty and outputs it in JSON. The schema is provided to ensure consistent formatting.

#### Impact on the Actuarial Profession

The paper argues that LLMs will **augment, not replace**, actuaries. They free actuaries from manual, repetitive tasks (e.g., data extraction) so they can focus on **high-value activities** requiring judgment, creativity, and strategic thinking. However, actuaries must:

- Understand LLM limitations (bias, hallucination, context limits).
- Manage risks (data privacy, ethical use, output validation).
- Collaborate with data scientists, ethicists, and IT professionals.
- Adapt to new workflows and continuously learn.

The paper also highlights **risks**: LLMs can produce incorrect or biased outputs, hallucinate facts, or leak sensitive data. Actuaries must **review and validate** all LLM outputs, especially for high-stakes decisions.

#### Conclusion

LLMs offer significant potential to **enhance efficiency, reduce errors, and unlock insights** in actuarial work — particularly in handling unstructured data and automating routine tasks. The paper provides a practical framework for evaluating LLM suitability and demonstrates real-world applications via case studies. However, it stresses that LLMs are tools, not oracles — their outputs require **human oversight, ethical consideration, and professional accountability**. The future of actuarial science lies in **human-AI collaboration**, where actuaries leverage LLMs to amplify their expertise, not outsource it.

---

**Word Count**: ~1500 words (excluding metadata and headers)