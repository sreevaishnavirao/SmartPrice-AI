SmartPrice AI

SmartPrice AI is an Autonomous Agentic AI Framework designed to identify online deals, estimate fair prices, and notify users of special bargains in real time. The system leverages multi-agent collaboration, LLMs, and machine learning models to build a production-ready business use case for intelligent deal discovery.

🚀 Key Features

Autonomous Multi-Agent Workflow – Scanner, Planner, Ensemble, Specialist, and Messaging agents collaborate to process data and estimate prices.

RAG-based Price Estimation – Retrieval-Augmented Generation pipeline with ChromaDB vector store and LLMs.

Fine-Tuned Models – Custom embeddings and price prediction with Random Forest Regressor and Ensemble Learning.

Push Notifications – Automated messaging agent alerts users when new deals or significant bargains are found.

400K+ Products Processed – Large-scale dataset used to build embeddings and benchmark the system.

🧠 Tech Stack & Tools

LLM & NLP Frameworks:

OpenAI GPT-4o / GPT-4o-mini for reasoning and RAG queries

Hugging Face Transformers & SentenceTransformers for embeddings

PyTorch backend for deep learning

Vector Databases:

ChromaDB persistent store for product embeddings (~400K+ docs)

Machine Learning Models:

Random Forest Regressor for supervised price prediction

Ensemble Models combining RAG outputs and ML estimates

Agentic AI:

Multi-agent framework coordinating scanning, retrieval, planning, and messaging

Logging, memory, and planning workflows for autonomous execution

Deployment:

Modal for serverless LLM hosting

Hugging Face Hub for model storage and integration

Utilities:

Python 3.11, scikit-learn, joblib for ML pipeline persistence

JSON for memory state management

Visualization & UI:

Minimal UI (Gradio prototype during dev)

Workflow diagrams

📂 Project Workflow

Data Ingestion – Load 400K+ product descriptions and prices

Vectorization – Encode using SentenceTransformers → store in ChromaDB

Deal Scanning – Agents scan for new items and candidate bargains

Price Estimation – RAG pricer + Random Forest + Ensemble output

Decision & Planning – Multi-agent planner coordinates responses

Notification – Messaging agent pushes bargain alerts

💼 Business Use Case

This project demonstrates how Agentic AI systems can:

Automate e-commerce deal discovery

Estimate market-fair prices using both LLM reasoning and statistical ML models

Deploy scalable AI pipelines with Modal, Hugging Face, and cloud-ready architectures
