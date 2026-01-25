## Document Metadata

**S/N:** 1  
**Title:** A Primer on Generative AI for Actuaries  
**Authors:** Stephen Carlin, FIA; Stephan Mathys, FSA  
**Date of publication:** 2024-02  
**Topic:** Generative Artificial Intelligence  
**Sub-topic:** Applications and practical implementation for actuaries in insurance and risk modeling  
**URL:** Not available  

---

## Summary

### 1. Modeling Techniques

The document provides a high-level overview of key modeling techniques used in Generative AI, without detailing specific implementations or custom architectures. The primary techniques discussed include:

- **Large Language Models (LLMs)**: Specifically, Transformer-based models such as GPT (Generative Pre-trained Transformer), which are trained to predict the next word in a sequence. These are used for text generation, summarization, translation, and code generation.
- **Transformer Models**: The dominant architecture for modern LLMs, utilizing self-attention mechanisms to process entire sequences in parallel, enabling superior context understanding compared to sequential models like RNNs.
- **Variational Autoencoders (VAEs)**: Probabilistic generative models that encode input data into a latent space (represented by mean and variance distributions) and decode it back to reconstruct or generate new data. VAEs are highlighted for their use in anomaly detection, synthetic data generation, and data validation.
- **Generative Adversarial Networks (GANs)**: Consist of two competing neural networks — a generator that creates synthetic data and a discriminator that evaluates its authenticity. GANs are used for image generation, style transfer, and data augmentation.
- **Convolutional Neural Networks (CNNs)**: Primarily used in image-related tasks such as damage assessment in claims processing.
- **Recurrent Neural Networks (RNNs) and LSTMs**: Used for sequential data tasks like text generation and time-series modeling, though largely superseded by Transformers in modern LLMs.

The paper does not describe novel or hybrid architectures but focuses on how these established techniques can be applied to actuarial tasks such as model documentation, data enrichment, and scenario generation.

### 2. Code Availability

No implementation code is provided in the document. The paper references tools and platforms (e.g., ChatGPT, GitHub Copilot, AWS Bedrock, Julius.ai) but does not include source code repositories, GitHub links, or downloadable scripts. Code examples are mentioned conceptually (e.g., generating Python code via prompts) but are not reproduced or made available for replication.

### 3. Learning Type

The document discusses applications of both **supervised** and **self-supervised** learning paradigms:

- **Supervised Learning**: Implicitly referenced in contexts like fine-tuning models on labeled datasets (e.g., training a model on historical financial data to predict deviations).
- **Self-supervised Learning**: The dominant paradigm for training foundational LLMs like GPT, which learn from vast unlabeled text corpora by predicting masked or next tokens.
- **Unsupervised Learning**: Mentioned in the context of anomaly detection using VAEs, which learn data distributions without explicit labels.
- **Reinforcement Learning from Human Feedback (RLHF)**: Referenced as a technique used by models like Claude to refine outputs based on human feedback.

The paper does not discuss reinforcement learning in depth but acknowledges its role in model refinement.

### 4. Dataset

The document does not specify any particular dataset used for training or evaluation. Instead, it discusses general principles:

- **Real-world data**: Emphasized for training models in actuarial contexts (e.g., historical financial results, claims data, policyholder information).
- **Synthetic data**: Generated via VAEs or GANs for testing, data augmentation, or privacy-preserving analysis.
- **Public vs. proprietary data**: Highlights the trade-offs between using public datasets (which may lack actuarial specificity) and internal company data (which offers domain relevance but raises privacy concerns).
- **Training data volume**: Notes that models like GPT-3 were trained on hundreds of billions of words, while smaller models (e.g., Llama 2) can be fine-tuned on smaller, domain-specific datasets.

No dataset names or sources are provided. The focus is on data quality, representativeness, and ethical sourcing rather than specific benchmarks.

### 5. Implementation Details

- **Programming language(s):** Not explicitly specified. However, Python is implied as the primary language for data manipulation and model interaction (e.g., via APIs or tools like Julius.ai). Other languages like R, SQL, and legacy systems (e.g., APL) are mentioned in the context of code conversion.
- **Key libraries/frameworks:** Not listed. The paper references platforms (e.g., OpenAI’s API, AWS Bedrock, Microsoft Azure AI Studio) rather than specific libraries. Frameworks like TensorFlow or PyTorch are not mentioned, though they underpin many of the models discussed.

### 6. Model Architecture

The document does not describe custom or composite model architectures. Instead, it outlines standard architectures:

- **Transformer Architecture**: Composed of encoder-decoder layers with self-attention mechanisms. Used in LLMs like GPT for text generation.
- **VAE Architecture**: Consists of an encoder (maps input to latent space) and a decoder (reconstructs input from latent space). Uses probabilistic sampling for generation.
- **GAN Architecture**: Two adversarial networks — generator (creates data from noise) and discriminator (classifies real vs. fake). Trained in tandem.
- **CNN Architecture**: Hierarchical layers for feature extraction in images, used in claims processing for damage assessment.
- **RNN/LSTM Architecture**: Sequential processing with memory cells, used for text and time-series tasks.

No novel combinations or modifications are presented. The focus is on how these architectures can be applied via existing platforms (e.g., using RAG with a Transformer model).

### 7. Technical Content

Generative AI (GenAI) represents a paradigm shift in how actuaries can approach modeling, documentation, data analysis, and automation. Unlike traditional AI, which classifies or predicts based on existing data, GenAI creates new content — text, code, images, or synthetic datasets — by learning patterns from vast training corpora. This capability stems from advances in deep learning, particularly Transformer models, which process entire sequences in parallel using attention mechanisms, enabling context-aware generation. The document positions GenAI not as a replacement for actuarial judgment but as a powerful augmentative tool that can handle repetitive, data-intensive, or creative tasks, freeing actuaries to focus on high-value analysis and decision-making.

One of the most immediate applications is in **general productivity**. Actuaries spend significant time on administrative tasks like meeting notes, document summarization, and drafting reports. GenAI tools like Fireflies.ai or Microsoft Teams’ built-in transcription can automatically generate meeting summaries, capturing key points and action items with high accuracy. Similarly, LLMs can summarize lengthy regulatory documents or compare draft versions, saving hours of manual review. However, the document cautions that these tools are not substitutes for deep reading; they are best used for initial scans or to recall specific sections. The quality of output is highly sensitive to prompt engineering — small changes in phrasing can yield vastly different results. For example, asking an LLM to “explain a Universal Life policy” versus “explain a Universal Life policy to a 10-year-old” produces outputs tailored to different audiences, demonstrating the importance of specificity and context in prompts.

In **coding and software development**, GenAI offers transformative potential. Tools like GitHub Copilot, Amazon Code Whisperer, and GPT-4 can generate code from natural language prompts, review and debug existing code, write unit tests, and add documentation comments. This is particularly valuable for actuaries with limited coding skills, as it lowers the barrier to automating tasks traditionally done in Excel. For experienced coders, these tools accelerate development by providing starting points and suggesting optimizations. Code conversion is another strength — GenAI can translate code from one language to another (e.g., Python to Go), which is crucial for insurers migrating legacy systems. However, the document notes that syntax conversion alone is insufficient; human intervention is needed to refactor for efficiency, handle proprietary functions, and address copyright issues. Building actuarial models from scratch via GenAI (e.g., generating a term life reserving model) is still nascent. While GPT-4 can produce a simplified, textbook-style model, it lacks the nuance and rigor required for production use. The real value lies in generating first drafts or baseline models that actuaries can refine, provided prompts are carefully engineered and augmented with domain-specific data.

**Model documentation and governance** is a critical area where GenAI can deliver immediate ROI. Actuarial models are often poorly documented, and maintaining documentation is a low-priority task. GenAI can automatically generate technical documentation by interpreting code — translating it into human-readable explanations. For instance, feeding a term life model’s code to GPT-4 can yield a summary of its inputs, outputs, and limitations. To achieve consistent, high-quality outputs, the document recommends integrating GenAI via APIs with Retrieval-Augmented Generation (RAG). RAG enhances LLMs by retrieving relevant context (e.g., internal documentation or function libraries) at query time, ensuring outputs are accurate and tailored. An example given is an actuarial platform using AWS Bedrock to scan its function library and auto-generate/update documentation as code changes, embedding this into CI/CD pipelines. This ensures documentation is always current, reducing the risk of divergence between code and documentation. GenAI can also compare model versions, summarizing changes (e.g., adding a TPD rider) and highlighting implications, which is invaluable for audit trails and governance.

In **data enrichment and manipulation**, GenAI can create synthetic datasets that mimic real data, useful for testing model capacity or augmenting sparse datasets (e.g., claims data). However, the document warns against using synthetic claims data for experience analysis, as it inflates statistical reliability. For data manipulation, tools like Julius.ai can reformat files (e.g., pivoting economic scenario data from long to wide format) based on natural language prompts, saving time for non-technical users. While Python or SQL might be more efficient for recurring tasks, GenAI can prototype solutions or generate the initial code. For **data analysis**, VAEs are highlighted for anomaly detection — they learn normal data distributions and flag outliers (e.g., policy inception dates before product launch). This is applicable to fraud detection in claims or transactions. Automated report generation is also possible, though the document notes early frustrations with the verbosity of natural language for mathematical concepts. The real value may lie in democratizing advanced analytics, allowing non-experts to perform basic predictive modeling.

**Scenario analysis** is another high-impact area. Traditional sensitivity analyses (e.g., ±10% mortality) are linear and isolated. GenAI can generate multi-dimensional scenarios by training on historical data (financial results, news, economic indicators) and predicting future outcomes with associated likelihoods. For example, an insurer could ask a GenAI model to forecast impacts of demographic shifts or market consolidation, then generate strategic responses ranked by effectiveness. This moves beyond “what-if” to “what’s likely and how should we respond?” The document emphasizes that these are not precise predictions but explorations of plausible futures, helping companies prepare for uncertainty.

**Automation and efficiency** extend to understanding data lineage. Actuaries often work with complex spreadsheet chains, where errors propagate silently. GenAI can map upstream and downstream dependencies, identifying the minimum inputs needed for a report and documenting impacts of changes. This can streamline processes, reduce manual copying, and minimize errors. Similarly, GenAI can review spreadsheets for hard-coded values or inconsistent macros, allowing actuaries to focus on validating logic rather than syntax.

In **claims processing**, GenAI can automate assessments using photographic evidence. For auto claims, it can verify vehicle coverage, estimate damage, calculate repair costs, connect to repair shops, and coordinate scheduling — all while communicating with the insured. It can also flag anomalies (e.g., inconsistent damage patterns) for fraud detection and notify actuaries of deviations from estimates, triggering experience studies. Beyond auto, this applies to medical, disability, and life insurance (e.g., photo of a death certificate to initiate claims).

For **underwriting**, GenAI can automate data validation (e.g., cross-referencing birth dates with public records) and handle unique coverages by synthesizing data from internal and external sources to generate risk scores. For group coverages, it can evaluate new groups against historical data, suggest questions to uncover risk drivers, and estimate impacts on the insurer’s portfolio. The key advantage is real-time, connected data — no lag between historical and current information — enabling more accurate reserve and capital allocation.

The document also addresses **limitations and practical considerations**. Key concerns include:

- **Hallucinations**: GenAI can generate plausible but false outputs. Mitigation requires human review and choosing reliable models.
- **Repeatability**: Outputs may vary for the same prompt due to randomness or model drift. Guardrails and consistent prompting are needed.
- **Data privacy**: Sensitive data should not be uploaded to public platforms. Private deployments (e.g., on AWS Bedrock) are recommended.
- **Auditability**: Complex models are “black boxes,” making it hard to explain decisions — a challenge for regulatory compliance.
- **Copyright**: Models trained on public data may infringe on copyrighted material. Ownership of AI-generated content is unclear.
- **Prompt engineering**: A critical skill requiring experimentation to craft effective prompts. Poor prompting leads to low-quality outputs.
- **Bias**: Models reflect biases in training data, which can perpetuate discrimination in underwriting or claims.
- **Ethics and regulation**: Concerns about job displacement and accountability. The EU AI Act is cited as an emerging regulatory framework.

Architecturally, the document distinguishes between **platforms** (e.g., ChatGPT, which offers APIs and plugins), **foundation models** (e.g., GPT-4, Llama 2), and **specialist applications** (e.g., GitHub Copilot for coding, Dall-E for images). Deployment choices depend on data sensitivity, task specificity, and required customization. Techniques like **transfer learning** (fine-tuning a pre-trained model on domain data) and **RAG** (augmenting prompts with external context) are recommended to tailor models without full retraining. **Chaining** — linking multiple models or steps — is essential for complex tasks.

Finally, the paper provides a **checklist** for adopting GenAI, covering task definition, solution selection (pretrained vs. custom), data handling (sensitivity, leakage), quality requirements, costs, and stakeholder approvals. It concludes that GenAI will profoundly impact actuarial work — from automating documentation to enhancing scenario planning — but success requires careful consideration of technical, ethical, and operational factors. The field is rapidly evolving, and actuaries must stay informed to harness its potential responsibly.

*(Word count: 1,502)*