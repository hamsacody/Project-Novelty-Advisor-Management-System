"""Sample/dummy data for the project novelty detector."""

# Sample student data
SAMPLE_STUDENTS = {
    "student1": {
        "username": "john_doe",
        "email": "john@university.edu",
        "password": "password123",
        "name": "John Doe"
    },
    "student2": {
        "username": "jane_smith",
        "email": "jane@university.edu",
        "password": "password123",
        "name": "Jane Smith"
    }
}

# Sample projects submitted by students
SAMPLE_PROJECTS = [
    {
        "id": "proj_001",
        "student_id": "student1",
        "title": "AI-Powered Sentiment Analysis for Social Media",
        "problem_statement": "Analyze public sentiment in real-time social media posts",
        "domain": "Natural Language Processing",
        "dataset": "Twitter/X Dataset",
        "method": "BERT-based Transfer Learning",
        "technologies": ["Python", "BERT", "Transformers", "TensorFlow"],
        "status": "analyzed",
        "created_date": "2024-09-01",
        "selected_novelty": "Implement multi-language sentiment detection"
    },
    {
        "id": "proj_002",
        "student_id": "student1",
        "title": "ECG Anomaly Detection using CNN",
        "problem_statement": "Detect cardiac anomalies from ECG signals",
        "domain": "Medical AI",
        "dataset": "MIT-BIH ECG Database",
        "method": "Convolutional Neural Networks",
        "technologies": ["Python", "TensorFlow", "Keras", "Pandas"],
        "status": "saved",
        "created_date": "2024-08-15",
        "selected_novelty": "Add attention mechanism for explainability"
    }
]

# Sample similar projects (for novelty results)
SAMPLE_SIMILAR_PROJECTS = [
    {
        "title": "Deep Learning for Stock Price Prediction",
        "authors": "Smith et al.",
        "year": 2023,
        "similarity": 72,
        "domain": "Time Series Analysis",
        "method": "LSTM Networks",
        "technologies": ["Python", "TensorFlow", "NumPy"]
    },
    {
        "title": "Recurrent Neural Networks for Sequence Modeling",
        "authors": "Johnson & Lee",
        "year": 2023,
        "similarity": 68,
        "domain": "Deep Learning",
        "method": "RNN/LSTM",
        "technologies": ["PyTorch", "Python"]
    },
    {
        "title": "Transformer Models for Time Series Forecasting",
        "authors": "Chen et al.",
        "year": 2024,
        "similarity": 65,
        "domain": "Deep Learning",
        "method": "Transformer Architecture",
        "technologies": ["Python", "Transformers", "PyTorch"]
    }
]

# Common/overused technologies in the domain
COMMON_TECHNOLOGIES = [
    {"name": "Python", "usage_percent": 95},
    {"name": "TensorFlow", "usage_percent": 78},
    {"name": "PyTorch", "usage_percent": 72},
    {"name": "Pandas", "usage_percent": 85},
    {"name": "NumPy", "usage_percent": 88},
    {"name": "Scikit-learn", "usage_percent": 65}
]

# Common datasets in the domain
COMMON_DATASETS = [
    {"name": "ImageNet", "usage_percent": 70},
    {"name": "MNIST", "usage_percent": 65},
    {"name": "CIFAR-10", "usage_percent": 58},
    {"name": "UCI ML Repository", "usage_percent": 72},
    {"name": "Kaggle Datasets", "usage_percent": 80}
]

# Common methods/algorithms
COMMON_METHODS = [
    {"name": "CNN (Convolutional Neural Networks)", "usage_percent": 75},
    {"name": "RNN/LSTM", "usage_percent": 68},
    {"name": "Transfer Learning", "usage_percent": 70},
    {"name": "Random Forest", "usage_percent": 55},
    {"name": "Support Vector Machines (SVM)", "usage_percent": 48}
]

# Suggested novelty ideas
NOVELTY_IDEAS = [
    {
        "id": "novelty_001",
        "title": "Implement Federated Learning",
        "description": "Add federated learning capabilities to train the model across distributed devices while maintaining data privacy.",
        "impact": "High",
        "feasibility": "Medium",
        "details": "Distribute model training across multiple devices without centralizing data"
    },
    {
        "id": "novelty_002",
        "title": "Add Explainability with SHAP",
        "description": "Integrate SHAP (SHapley Additive exPlanations) to make model predictions interpretable and trustworthy.",
        "impact": "High",
        "feasibility": "High",
        "details": "Provide feature importance and decision explanations for each prediction"
    },
    {
        "id": "novelty_003",
        "title": "Implement Adversarial Robustness",
        "description": "Add adversarial training and robustness testing to make the model resilient against adversarial attacks.",
        "impact": "Medium",
        "feasibility": "Medium",
        "details": "Train and test against adversarial examples to improve model robustness"
    },
    {
        "id": "novelty_004",
        "title": "Multi-Modal Learning Approach",
        "description": "Combine multiple data modalities (text, images, audio) for improved predictions.",
        "impact": "High",
        "feasibility": "Low",
        "details": "Fuse different data types with ensemble methods"
    },
    {
        "id": "novelty_005",
        "title": "Real-time Inference Optimization",
        "description": "Optimize the model for edge deployment with quantization and pruning techniques.",
        "impact": "Medium",
        "feasibility": "High",
        "details": "Deploy lightweight models for mobile and IoT devices"
    }
]

# Existing limitations (commonly found in similar projects)
EXISTING_LIMITATIONS = [
    "Limited to small batch sizes due to memory constraints",
    "Training time exceeds 24 hours for large datasets",
    "Model performance degrades with domain shift",
    "Lack of real-time inference capabilities",
    "High computational requirements for deployment",
    "Limited cross-domain generalization",
    "Absence of uncertainty quantification"
]

# Possible gaps in the field
POSSIBLE_GAPS = [
    "No standardized benchmarking framework for this domain",
    "Lack of interpretability in model decisions",
    "Limited focus on edge deployment and mobile optimization",
    "Missing privacy-preserving training methods",
    "No comprehensive comparison of recent architectures",
    "Insufficient real-world dataset diversity",
    "Limited multi-modal learning approaches"
]
