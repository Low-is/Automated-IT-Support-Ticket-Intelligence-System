## Automated IT Support Ticket Intelligence System

Live API: https://automated-it-support-ticket-intelligence.onrender.com/docs

# Overview
This project analyzes IT support tickets to identify operational patterns, understand high-priority incidents, and improve ticket triage through data analytics and machine learning.

At its current stage, the workflow is implemented as a series of analytical and modeling steps. While the project demonstrates the core components required for an automated ticket intelligence system (i.e., data processing, predictive modeling, and an API-based prediction UI), the pipeline is still under active development and has not yet been fully automated to be production ready.

By combining data analysis with predictive modeling, the project illustrates how support teams could proactively detect critical issues, improving ticket prioritization and supporting more efficient resource allocation within IT service operations. 

## ML Architecture Diagram
- Incoming Ticket
- Feature Encoding
- Trained Random Forest Model
- Priority Probability Score
- Flag Critical Tickets


Key objectives:

- Analyze IT support ticket metadata to understand operational patterns across ticket types, queues, and tags.
- Identify characteristics commonly associated with high-priority incidents.
- Visualize trends in ticket distribution to highlight recurring technical and operational issues.
- Develop a machine learning model that estimates the probability of a ticket requiring high-priority attention.
- Demonstrate how predictive analytics can support improved ticket triage, prioritization, and IT service workflow efficiency


## Languages & Libraries

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white) 
![Pandas](https://img.shields.io/badge/Pandas-1.5-lightgrey?logo=pandas&logoColor=black) 
![NumPy](https://img.shields.io/badge/NumPy-1.25-orange?logo=NumPy&logoColor=white) 
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-purple?logo=matplotlib&logoColor=white) 
![Seaborn](https://img.shields.io/badge/Seaborn-0.12-blueviolet?logo=seaborn&logoColor=white)

## Machine Learning

![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.2-ff69b4?logo=scikit-learn&logoColor=white)


## Model Deployment

![FastAPI](https://img.shields.io/badge/FastAPI-API%20Deployment-009688?logo=fastapi&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-Model%20Serialization-green)
