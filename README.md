SmartPrice AI



📌 Overview:

SmartPrice AI is an Autonomous Agentic AI Framework built to identify online deals, estimate fair prices, and notify users of special bargains in real time. The system leverages multi-agent collaboration, large language models (LLMs), and machine learning models to deliver a production-ready use case for intelligent deal discovery. It is designed as a scalable framework that demonstrates how next-generation agentic AI can be applied to real-world e-commerce problems.

🚀 Key Features:

SmartPrice AI integrates several capabilities into one pipeline. The system operates as an autonomous multi-agent workflow, where agents coordinate to scan for new items, retrieve contextual information, estimate product prices, and deliver notifications. A Retrieval-Augmented Generation (RAG) pipeline powered by ChromaDB and LLMs ensures contextual accuracy in pricing decisions. Price estimation is further refined using custom embeddings, Random Forest Regressors, and Ensemble Learning techniques. Once a potential bargain is identified, a dedicated messaging agent issues push notifications, keeping users informed in real time. The system has been benchmarked on 400K+ product records, providing both scale and robustness for experimentation.

🧠 Tech Stack and Tools:

The framework relies on a modern LLM and ML stack. For natural language understanding and embeddings, it employs OpenAI GPT-4o/GPT-4o-mini, Hugging Face Transformers, and SentenceTransformers, all running on a PyTorch backend. For vector storage and retrieval, ChromaDB is used as a persistent database capable of handling more than 400K product embeddings.

On the machine learning side, a Random Forest Regressor is trained to predict prices from product embeddings, and an Ensemble Model combines both ML predictions and LLM-based reasoning for improved accuracy. The Agentic AI framework coordinates tasks such as scanning, retrieval, planning, and messaging while maintaining memory and logging across sessions. For deployment, the project uses Modal for serverless model execution and the Hugging Face Hub for integration and model storage. Supporting utilities include Python 3.11, scikit-learn, joblib, and JSON-based memory management.

📂 Project Workflow:

The workflow begins with data ingestion, where more than 400K product descriptions and prices are loaded into the pipeline. These are vectorized using SentenceTransformers and stored in ChromaDB for efficient similarity search. A scanner agent continuously monitors for new items, while a retrieval and pricing process combines RAG with ML models such as the Random Forest Regressor and Ensemble predictors. A planning agent coordinates decision-making across agents, and finally, the messaging agent delivers push notifications when significant bargains are found.

💼 Business Use Case:

This project demonstrates the potential of Agentic AI for e-commerce and retail applications. By combining LLM-driven reasoning with statistical ML models, SmartPrice AI can automate the process of deal discovery, price estimation, and customer notification. Its modular design ensures that the system can scale across cloud environments, integrate with APIs such as Amazon or eBay, and extend into reinforcement learning for dynamic price optimization. This makes SmartPrice AI not just an academic prototype but a practical foundation for AI-powered commerce solutions
