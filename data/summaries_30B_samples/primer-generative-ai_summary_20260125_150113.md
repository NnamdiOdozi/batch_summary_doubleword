## Document Metadata

**S/N:** 1  
**Title:** A Primer on Generative AI for Actuaries  
**Authors:** Stephen Carlin, FIA; Stephan Mathys, FSA  
**Date of publication:** 2024-02  
**Topic:** Generative Artificial Intelligence  
**Sub-topic:** Applications and Practical Implementation for Actuaries  
**URL:** Not available  

---

## Summary

### 1. Modeling Techniques

The document provides a high-level overview of several foundational modeling techniques used in Generative AI, without delving into implementation specifics. The techniques discussed include:

- **Neural Networks and Deep Learning**: Used broadly as the backbone of most Generative AI systems. The document references Convolutional Neural Networks (CNNs) for image tasks and Recurrent Neural Networks (RNNs), including Long Short-Term Memory (LSTM) networks, for sequential data such as text or time series.

- **Transformer Models**: Highlighted as the dominant architecture for Large Language Models (LLMs). Transformers rely on self-attention mechanisms to process entire sequences of data simultaneously, enabling them to understand context more effectively than sequential models like RNNs. GPT models (Generative Pre-trained Transformer) are cited as examples.

- **Variational Autoencoders (VAEs)**: Described as probabilistic generative models that encode input data into a latent space (compressing it) and then decode it back to reconstruct the original data. VAEs are noted for their ability to generate new data by sampling from the learned latent distribution. They are particularly useful for anomaly detection, synthetic data generation, and dimensionality reduction.

- **Generative Adversarial Networks (GANs)**: Composed of two competing neural networks — a generator that creates synthetic data and a discriminator that tries to distinguish real from fake data. The adversarial training process improves both networks iteratively. GANs are used for image and video generation, style transfer, super-resolution, and data augmentation.

The document does not specify hybrid or composite model architectures beyond these foundational techniques. Instead, it emphasizes how these models are applied in actuarial contexts via platforms like ChatGPT, GitHub Copilot, and AWS Bedrock, which abstract away the underlying model complexity.

### 2. Code Availability

No implementation code is provided in the document. The paper is conceptual and explanatory, aimed at introducing actuaries to the capabilities and considerations of Generative AI. While it references tools such as GPT-4, GitHub Copilot, and Julius.ai, it does not link to GitHub repositories or provide code snippets for replication. The authors mention using GPT-4 to assist in drafting parts of the report, but no source code for the prompts or workflows is shared.

### 3. Learning Type

The document does not specify a single learning paradigm but implies a mix of approaches depending on context:

- **Supervised Learning**: Implicitly referenced in the context of training models on labeled datasets (e.g., for classification, code generation, or text summarization).

- **Self-Supervised Learning**: Suggested in the training of large language models like GPT, which are pre-trained on vast unlabeled text corpora using next-token prediction tasks.

- **Unsupervised Learning**: Mentioned in the context of anomaly detection using VAEs and clustering algorithms for model point compression.

The paper does not discuss reinforcement learning in depth, though it references Reinforcement Learning from Human Feedback (RLHF) as a technique used to refine models like Anthropic’s Claude.

### 4. Dataset

The document does not describe any specific dataset used for training or evaluation. It discusses:

- **Real-world data**: Used in actuarial applications such as claims processing, underwriting, and scenario analysis. Examples include policyholder data, economic scenario files, claims photos, and financial reports.

- **Synthetic data**: Generated via VAEs or GANs for testing, data augmentation, or privacy-preserving analysis. The authors note that synthetic data should not be used for experience analysis as it can misrepresent statistical reliability.

- **Training data for foundational models**: Referenced as large-scale, publicly available text corpora (e.g., hundreds of billions of words for GPT-3), though exact sources are not specified. The paper warns that such data may contain limited actuarial-specific content.

No named datasets (e.g., Kaggle, UCI, proprietary insurer datasets) are mentioned.

### 5. Implementation Details

- **Programming language(s):** Not explicitly specified. The document references tools that support multiple languages (e.g., GitHub Copilot for Python, R, SQL, etc.), but no single language is emphasized.

- **Key libraries/frameworks:** Not listed. The focus is on commercial platforms (ChatGPT, AWS Bedrock, Microsoft Azure AI Studio) rather than open-source libraries like TensorFlow or PyTorch. The paper assumes users interact with these platforms via APIs or web interfaces rather than coding directly with frameworks.

### 6. Model Architecture

The document does not describe custom or composite model architectures in technical detail. Instead, it outlines standard architectures used in Generative AI:

- **Transformer-based LLMs (e.g., GPT-4)**: Described as using self-attention to process entire input sequences in parallel. No layer counts, embedding dimensions, or parameter counts are provided.

- **VAEs**: Composed of an encoder (maps input to latent space parameters — mean and variance) and a decoder (reconstructs data from sampled latent points). The latent space is probabilistic, enabling diverse generation.

- **GANs**: Two-network adversarial system — generator creates data from noise; discriminator classifies real vs. fake. Training is iterative and competitive.

The paper emphasizes architectural choices in deployment (e.g., RAG vs. fine-tuning) rather than model internals. It notes that models can be accessed via APIs or integrated into platforms like Microsoft 365 or AWS Bedrock.

### 7. Technical Content

Generative AI (GenAI) represents a paradigm shift in how actuaries can approach tasks ranging from coding and documentation to claims processing and underwriting. Unlike traditional AI, which classifies or predicts based on input data, GenAI creates new content — text, code, images, or synthetic data — by learning patterns from vast training datasets. This capability stems from advanced neural network architectures, particularly Transformers, VAEs, and GANs, which enable systems like ChatGPT and DALL-E to generate human-like outputs.

The paper is structured to guide actuaries through the conceptual foundations, practical applications, and implementation considerations of GenAI. It begins by defining key terms and techniques, then explores use cases across actuarial workflows, and concludes with a checklist for responsible deployment.

#### Foundational Techniques

At the core of GenAI are deep learning models. **Transformers**, introduced in 2017, revolutionized natural language processing by replacing sequential RNNs with parallel processing and attention mechanisms. Attention allows the model to weigh the relevance of all input tokens when generating each output token, enabling superior context understanding. This architecture underpins LLMs like GPT-3 and GPT-4, which can summarize documents, generate code, and answer complex questions.

**VAEs** offer a probabilistic approach to generation. They compress input data into a latent space — a lower-dimensional representation capturing essential features — and then decode it back to reconstruct the original. By sampling from the latent distribution, VAEs generate new, similar data. This makes them ideal for anomaly detection: data points that reconstruct poorly (high reconstruction error) are likely outliers. In actuarial contexts, VAEs can validate datasets, detect fraudulent claims patterns, or generate synthetic test data for model validation.

**GANs** consist of two networks in competition: a generator that creates synthetic data from random noise, and a discriminator that tries to distinguish real from fake. Through adversarial training, both networks improve — the generator produces more realistic outputs, and the discriminator becomes better at detection. GANs are widely used in image generation (e.g., creating realistic faces) and can augment scarce datasets in insurance, such as generating additional claims images for training computer vision models.

#### Applications for Actuaries

The paper identifies seven key areas where GenAI can enhance actuarial work:

1. **General Productivity**: Tools like Fireflies.ai or Microsoft Teams AI can transcribe meetings, summarize discussions, and extract action items, saving time on note-taking. LLMs can also summarize lengthy regulatory documents or compare draft versions of policies, though users must verify outputs due to potential hallucinations.

2. **Coding and Software Development**: Copilot tools (GitHub Copilot, Amazon CodeWhisperer) suggest code, review syntax, generate comments, and write unit tests. These tools accelerate development for both experienced coders and those with limited programming skills. Code conversion (e.g., from legacy APL to Python) is also feasible, though human oversight is needed for efficiency and copyright compliance.

3. **Model Documentation and Governance**: GenAI can automatically generate technical documentation from code, translating complex logic into plain language. When integrated via APIs with Retrieval Augmented Generation (RAG), it can produce consistent, up-to-date documentation as models evolve. This addresses a common pain point in actuarial governance, where documentation often lags behind code changes.

4. **Data Enrichment and Analysis**: GenAI can generate synthetic datasets to test model scalability or validate assumptions. For example, it can expand a 10,000-row model point file to 100,000 rows. It can also manipulate data formats — e.g., reorganizing economic scenario files from long to wide format — using natural language prompts. For analysis, VAEs can flag anomalies in claims or policy data, while LLMs can automate report generation, though actuaries must validate outputs.

5. **Scenario Analysis**: Beyond traditional sensitivity testing (e.g., +/-10% mortality), GenAI can generate complex, multi-variable scenarios by learning from historical financial data, news, and external factors. It can also propose strategic responses to emerging scenarios and rank them by feasibility, helping actuaries understand not just impacts but likelihoods and trade-offs.

6. **Automation and Efficiency**: GenAI can automate repetitive tasks like summarizing financial results or documenting data lineage. For instance, it can trace upstream and downstream dependencies in spreadsheet chains, identify redundant calculations, and suggest streamlined workflows. This reduces manual effort and minimizes errors in complex reporting processes.

7. **Claims and Underwriting**: In claims, GenAI can analyze photos to estimate damage, validate policy coverage, connect to repair shops, and track claim progress. In underwriting, it can cross-reference applicant data with public records to detect inconsistencies (e.g., birth year errors) or synthesize risk profiles for unique coverages by learning from internal and external data. For group underwriting, it can evaluate new groups against existing portfolios and suggest targeted questions.

#### Practical Implementation

Deploying GenAI requires careful consideration of architecture, data, and governance. The paper distinguishes between:

- **Platforms** (e.g., ChatGPT, AWS Bedrock) that offer pre-trained models via APIs.
- **Specialist Applications** (e.g., GitHub Copilot for coding, Julius.ai for data manipulation).
- **Custom Solutions** built around foundational models.

Key implementation strategies include:

- **Prompt Engineering**: Crafting precise, context-rich prompts to guide LLM outputs. Small changes can significantly alter results, so testing and refinement are essential. For example, prompting GPT-4 to explain a Universal Life policy yields different outputs based on specificity and constraints.

- **Transfer Learning**: Fine-tuning a pre-trained model on domain-specific data (e.g., actuarial code or claims reports) to improve performance on specialized tasks. This requires additional training data and computational resources.

- **Retrieval Augmented Generation (RAG)**: Enhancing LLMs with external, task-specific data at query time. For instance, an actuarial documentation tool might retrieve function definitions from a code library before generating explanations. RAG is preferred for dynamic, data-sensitive applications over fine-tuning.

- **Chaining**: Combining multiple AI models or steps in sequence for complex tasks (e.g., first extracting data from a PDF, then summarizing it, then generating a report). This is necessary for end-to-end actuarial workflows.

#### Limitations and Risks

The paper emphasizes that GenAI is not a replacement for actuarial judgment. Key limitations include:

- **Hallucinations**: LLMs may generate plausible but incorrect outputs. Users must verify critical results.
- **Repeatability**: Outputs can vary for identical inputs due to randomness or model updates. This challenges auditability.
- **Data Privacy**: Uploading sensitive data to public platforms risks exposure. Private deployment or RAG with on-premises data is recommended.
- **Bias**: Models trained on biased data may perpetuate or amplify those biases, especially in underwriting or claims decisions.
- **Copyright**: Training on public data raises legal questions about ownership of generated content.
- **Prompt Engineering Skill**: Poorly crafted prompts yield poor results, requiring a learning curve.

Ethical considerations include job displacement, accountability for AI-generated errors, and regulatory compliance (e.g., EU AI Act).

#### Checklist for Deployment

The paper concludes with a practical checklist for organizations:

- Define the task, required data, and user interaction.
- Choose between third-party platforms or custom solutions.
- Assess if pretrained models suffice or if fine-tuning/RAG is needed.
- Evaluate data sensitivity and ensure compliance.
- Establish quality control, review processes, and governance.
- Secure stakeholder approvals and budget for costs (API tokens, licenses, infrastructure).

In summary, GenAI offers transformative potential for actuaries — from automating mundane tasks to enhancing complex modeling and decision-making. However, its successful adoption hinges on understanding its technical foundations, limitations, and ethical implications. Actuaries must act as stewards, combining AI’s computational power with their domain expertise to ensure responsible, effective, and auditable applications. The field is evolving rapidly, and this primer serves as a starting point for ongoing exploration and innovation.