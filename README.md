# E-commerce Product Recommendation Chatbot

This repository contains an E-commerce chatbot capable of providing product recommendations based on user queries and customer reviews. It leverages a Retrieval-Augmented Generation (RAG) system that combines vector retrieval with a language model for enhanced conversational and contextual responses. The application is deployed on AWS EC2.


## Features

- **E-commerce Product Recommendations:** Provides personalized product suggestions based on user preferences and historical customer reviews.
- **Retrieval-Augmented Generation (RAG):** Utilizes a vector store for retrieval-based search and a language model for generating responses.
- **Session-based Conversations:** Maintains unique sessions per user to enable consistent and context-aware recommendations.
- **Scalable and Cloud-Ready:** Deployed on AWS EC2 for scalability, enabling a global reach for e-commerce users.

## Architecture

The architecture is built using Python, Flask, and LangChain, with integration to AWS EC2 for deployment.

1. **Data Ingestion:** Reads and processes customer reviews for each product.
2. **Vector Store Generation:** Embeds and stores data in a vector format for efficient retrieval. Use Astra DB as the Vector DB.
3. **Conversational Chain:** Combines a retriever, language model, and conversational memory for continuous context-aware responses.
4. **Flask API:** Exposes endpoints for chatbot interactions, serving as the application's backend.

---

## Setup and Installation

### Prerequisites

- **Python**: 3.10 or later
- **AWS CLI**: Installed and configured
- **Docker**: For containerized deployment

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/chandima2000/flip-cart-chat-bot
   cd flip-cart-chat-bot
   ```

2. **Set up a Virtual Environment**

   ```bash
   python -m venv venv
   venv/Scripts/activate.ps1
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a .env File**

   ```bash
   GROQ_API_KEY=<your_groq_api_key>
   AWS_ACCESS_KEY_ID=<your_aws_access_key>
   AWS_SECRET_ACCESS_KEY=<your_aws_secret_key>
   ASTRA_DB_API_ENDPOINT=<your_astra_db_api_key>
   ASTRA_DB_APPLICATION_TOKEN=<your_astra_db_token>
   ASTRA_DB_KEYSPACE=<your_astra_db_keyspace>
   HUGGING_FACE_TOKEN=<your_hugging_face_token>
   ```
## Running the Application

### 1. Data Ingestion
   ```bash
   python src/data_ingestion.py
   ```

### 2. Start the Flask Application
   ```bash
   python app.py
   ```

### 3. Access the Chatbot
   ```bash
   http://localhost:5000
   ```

## Docker Deployment

### 1. Build the Docker Image
   ```bash
   docker build -t chatbot .
   ```

### 2. Run the Docker Container
   ```bash
   docker run -p 5000:5000 chatbot
   ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.