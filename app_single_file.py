"""
Project Novelty Detector - SINGLE FILE APPLICATION
Complete Streamlit frontend for analyzing research project novelty.
All code consolidated into one file for simpler deployment.

Navigation Flow:
Login → Dashboard → Submit Project → Analyze → Novelty Results → Select Novelty → Save → My Projects
"""

import streamlit as st
import time
from datetime import datetime

# ============================================================================
# CONFIGURATION AND SETUP
# ============================================================================

st.set_page_config(
    page_title="Project Novelty Detector",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# SAMPLE DATA
# ============================================================================

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

COMMON_TECHNOLOGIES = [
    {"name": "Python", "usage_percent": 95},
    {"name": "TensorFlow", "usage_percent": 78},
    {"name": "PyTorch", "usage_percent": 72},
    {"name": "Pandas", "usage_percent": 85},
    {"name": "NumPy", "usage_percent": 88},
    {"name": "Scikit-learn", "usage_percent": 65}
]

COMMON_DATASETS = [
    {"name": "ImageNet", "usage_percent": 70},
    {"name": "MNIST", "usage_percent": 65},
    {"name": "CIFAR-10", "usage_percent": 58},
    {"name": "UCI ML Repository", "usage_percent": 72},
    {"name": "Kaggle Datasets", "usage_percent": 80}
]

COMMON_METHODS = [
    {"name": "CNN (Convolutional Neural Networks)", "usage_percent": 75},
    {"name": "RNN/LSTM", "usage_percent": 68},
    {"name": "Transfer Learning", "usage_percent": 70},
    {"name": "Random Forest", "usage_percent": 55},
    {"name": "Support Vector Machines (SVM)", "usage_percent": 48}
]

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

EXISTING_LIMITATIONS = [
    "Limited to small batch sizes due to memory constraints",
    "Training time exceeds 24 hours for large datasets",
    "Model performance degrades with domain shift",
    "Lack of real-time inference capabilities",
    "High computational requirements for deployment",
    "Limited cross-domain generalization",
    "Absence of uncertainty quantification"
]

POSSIBLE_GAPS = [
    "No standardized benchmarking framework for this domain",
    "Lack of interpretability in model decisions",
    "Limited focus on edge deployment and mobile optimization",
    "Missing privacy-preserving training methods",
    "No comprehensive comparison of recent architectures",
    "Insufficient real-world dataset diversity",
    "Limited multi-modal learning approaches"
]

# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================

def apply_custom_css():
    """Apply custom CSS styling to the application."""
    st.markdown("""
    <style>
        /* Main styling */
        :root {
            --primary-color: #2563eb;
            --secondary-color: #1e40af;
            --success-color: #16a34a;
            --danger-color: #dc2626;
            --warning-color: #ea580c;
            --light-bg: #f8fafc;
            --border-color: #e2e8f0;
        }
        
        /* Base text color - dark text by default */
        body, .main, p, span, div, a, li, label {
            color: #1e293b !important;
        }
        
        /* Light text on dark backgrounds */
        div[style*="color: #f8fafc"],
        div[style*="background: #2a2a2a"],
        div[style*="background: #1a1a1a"],
        div[style*="background: #0f0f0f"],
        div[style*="background: #111"],
        div[style*="background: #222"],
        div[style*="background-color: #2a2a2a"],
        div[style*="background-color: #1a1a1a"],
        div[style*="background-color: #0f0f0f"] {
            color: #ffffff !important;
        }
        
        /* Ensure text inside dark containers is light */
        div[style*="background-color: #2a2a2a"] *,
        div[style*="background-color: #1a1a1a"] *,
        div[style*="background-color: #0f0f0f"] *,
        div[style*="background: #2a2a2a"] *,
        div[style*="background: #1a1a1a"] *,
        div[style*="background: #0f0f0f"] * {
            color: #ffffff !important;
        }
        
        /* Page container */
        .main {
            padding: 2rem;
            color: #1e293b;
        }
        
        /* Headers */
        h1 {
            color: #1e293b !important;
            border-bottom: 3px solid #2563eb;
            padding-bottom: 1rem;
        }
        
        h2 {
            color: #1e293b !important;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }
        
        h3 {
            color: #1e293b !important;
        }
        
        /* Cards and containers */
        .card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        
        /* Form elements */
        .stTextInput > div > div > input,
        .stPasswordInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            border-radius: 6px;
            border: 1px solid #cbd5e1;
            padding: 0.75rem;
        }
        
        /* Buttons */
        .stButton > button {
            background-color: #2563eb;
            color: white !important;
            border-radius: 6px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #1e40af;
            box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
            color: white !important;
        }
        
        /* Success message */
        .success-box {
            background-color: #dcfce7;
            border-left: 4px solid #16a34a;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        
        /* Warning message */
        .warning-box {
            background-color: #fef08a;
            border-left: 4px solid #ea580c;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        
        /* Info message */
        .info-box {
            background-color: #dbeafe;
            border-left: 4px solid #2563eb;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        
        /* Project card */
        .project-card {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .project-card:hover {
            border-color: #2563eb;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.1);
        }
        
        /* Metric badge */
        .metric-badge {
            display: inline-block;
            background-color: #dbeafe;
            color: #1e40af !important;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }
        
        /* Ensure all text is readable regardless of background */
        p {
            color: #1e293b !important;
        }
        
        /* Handle streamlit components */
        .stMarkdown {
            color: #1e293b;
        }
        
        /* Light backgrounds with dark text */
        div, section, article {
            color: #1e293b;
        }
        
        /* Code blocks and pre-formatted text */
        code, pre {
            color: #1e293b !important;
            background-color: #f0f0f0;
        }
        
        /* Streamlit specific components */
        .stCode {
            color: #1e293b !important;
        }
        
        /* All text elements must be dark */
        span, li, td, th {
            color: #1e293b !important;
        }
        
        /* Override any light gray that might be in streamlit defaults */
        [data-testid] {
            color: #1e293b !important;
        }
        
        /* Ensure links are readable */
        a {
            color: #2563eb !important;
        }
        
        /* Button text always white */
        button {
            color: white !important;
        }
        
        button:hover {
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# UI HELPER FUNCTIONS
# ============================================================================

def show_header(title, subtitle=""):
    """Display a styled header."""
    st.markdown(f"# {title}")
    if subtitle:
        st.markdown(f"<p style='color: #1e293b; font-size: 1.1rem;'>{subtitle}</p>", 
                   unsafe_allow_html=True)

def show_welcome_message(name):
    """Display a welcome message."""
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%); 
                color: white; padding: 2rem; border-radius: 8px; text-align: center; 
                margin-bottom: 2rem;'>
        <h1 style='color: white; border: none; margin: 0;'>Welcome, {name}! 👋</h1>
        <p style='margin: 0.5rem 0 0 0;'>Discover the novelty in your research projects</p>
    </div>
    """, unsafe_allow_html=True)

def show_project_card(project):
    """Display a project card."""
    st.markdown(f"""
    <div class='project-card'>
        <div style='display: flex; justify-content: space-between; align-items: start;'>
            <div style='flex: 1;'>
                <h3 style='margin: 0 0 0.5rem 0;'>{project['title']}</h3>
                <p style='color: #334155; margin: 0 0 1rem 0; font-size: 0.95rem;'>{project['domain']}</p>
                <div style='margin-bottom: 1rem;'>
                    <span class='metric-badge'>{project['status'].upper()}</span>
                    <span class='metric-badge'>{project['created_date']}</span>
                </div>
                <p style='color: #1e293b; margin: 0; font-size: 0.9rem;'>
                    <strong>Method:</strong> {project['method']}<br>
                    <strong>Dataset:</strong> {project['dataset']}
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_info_box(message):
    """Display an info box."""
    st.markdown(f"""
    <div class='info-box'>
        <strong>ℹ️ Information:</strong><br>
        {message}
    </div>
    """, unsafe_allow_html=True)

def show_success_box(message):
    """Display a success box."""
    st.markdown(f"""
    <div class='success-box'>
        <strong>✓ Success:</strong><br>
        {message}
    </div>
    """, unsafe_allow_html=True)

def show_warning_box(message):
    """Display a warning box."""
    st.markdown(f"""
    <div class='warning-box'>
        <strong>⚠️ Warning:</strong><br>
        {message}
    </div>
    """, unsafe_allow_html=True)

def format_technologies(techs):
    """Format technologies as styled badges."""
    html = ""
    colors = {
        "Python": "#3776ab",
        "TensorFlow": "#ff6f00",
        "PyTorch": "#ee4c2c",
        "Transformers": "#7b68ee",
        "Pandas": "#150458",
        "NumPy": "#013243",
        "Keras": "#d00000",
        "Scikit-learn": "#f7931e"
    }
    
    for tech in techs:
        color = colors.get(tech, "#2563eb")
        html += f"""
        <span style='display: inline-block; background-color: {color}33; 
                     color: {color}; padding: 0.35rem 0.75rem; 
                     border-radius: 20px; margin-right: 0.5rem; 
                     margin-bottom: 0.5rem; font-size: 0.875rem; 
                     border: 1px solid {color};'>
            {tech}
        </span>
        """
    return html

def format_similarity_percentage(percentage):
    """Format similarity percentage with color coding."""
    if percentage >= 75:
        color = "#dc2626"
    elif percentage >= 60:
        color = "#ea580c"
    else:
        color = "#16a34a"
    
    return f"<span style='font-size: 1.5rem; font-weight: 700; color: {color};'>{percentage}%</span>"

def show_loading_animation(message="Loading..."):
    """Show a loading animation."""
    st.markdown(f"""
    <div style='text-align: center; padding: 2rem;'>
        <div style='font-size: 3rem; margin-bottom: 1rem;'>⏳</div>
        <h3>{message}</h3>
        <p style='color: #64748b;'>This may take a few moments...</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# SESSION MANAGEMENT
# ============================================================================

def initialize_session():
    """Initialize session state variables."""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "current_user" not in st.session_state:
        st.session_state.current_user = None
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"
    if "current_project" not in st.session_state:
        st.session_state.current_project = None
    if "project_form_data" not in st.session_state:
        st.session_state.project_form_data = {}
    if "analysis_results" not in st.session_state:
        st.session_state.analysis_results = None
    if "selected_novelty" not in st.session_state:
        st.session_state.selected_novelty = None
    if "saved_projects" not in st.session_state:
        st.session_state.saved_projects = []

def authenticate_user(username, password):
    """Authenticate user with dummy credentials."""
    username = username.strip().casefold()
    for student_id, student_data in SAMPLE_STUDENTS.items():
        if username in (student_data["username"].casefold(), student_data["email"].casefold()) \
           and student_data["password"] == password:
            st.session_state.logged_in = True
            st.session_state.current_user = {
                "id": student_id,
                "username": student_data["username"],
                "email": student_data["email"],
                "name": student_data["name"]
            }
            return True
    return False

def logout():
    """Clear session and logout user."""
    st.session_state.logged_in = False
    st.session_state.current_user = None
    st.session_state.current_page = "login"
    st.session_state.current_project = None
    st.session_state.project_form_data = {}
    st.session_state.analysis_results = None
    st.session_state.selected_novelty = None

# ============================================================================
# PAGE FUNCTIONS
# ============================================================================

def show_login_page():
    """Display the login page."""
    apply_custom_css()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 3rem;'>
            <h1 style='border: none; color: #2563eb; font-size: 2.5rem;'>🚀</h1>
            <h2 style='color: inherit; margin: 0;'>Project Novelty Detector</h2>
            <p style='color: inherit; font-size: 1rem; margin-top: 0.5rem;'>
                Discover innovation in your research projects
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Student Login")
        
        with st.form("login_form"):
            username = st.text_input(
                "Email or Username",
                placeholder="Enter your email or username",
                help="Use the sample credentials: john_doe / jane_smith"
            )
            
            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password",
                help="Sample password: password123"
            )
            
            submitted = st.form_submit_button("Login", use_container_width=True)
            
            if submitted:
                if not username.strip() or not password:
                    st.error("❌ Please enter both username and password")
                elif authenticate_user(username, password):
                    st.success("✓ Login successful! Redirecting...")
                    st.session_state.current_page = "dashboard"
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")
        
        st.markdown("""
        <div style='background-color: #dbeafe; border-left: 4px solid #2563eb; 
                    padding: 1rem; border-radius: 4px; margin-top: 2rem;'>
            <p style='margin: 0; color: #1e40af; font-weight: 600;'>Demo Credentials</p>
            <p style='margin: 0.5rem 0 0 0; color: #1e293b; font-size: 0.9rem;'>
                <strong>Student 1:</strong><br>
                Email: john@university.edu<br>
                Password: password123
            </p>
            <p style='margin: 1rem 0 0 0; color: #1e293b; font-size: 0.9rem;'>
                <strong>Student 2:</strong><br>
                Email: jane@university.edu<br>
                Password: password123
            </p>
        </div>
        """, unsafe_allow_html=True)

def show_dashboard():
    """Display the student dashboard."""
    apply_custom_css()
    
    user = st.session_state.current_user
    
    col1, col2 = st.columns([4, 1])
    with col1:
        show_welcome_message(user["name"])
    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            logout()
            st.rerun()
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✨ Create New Project", use_container_width=True, key="create_project"):
            st.session_state.project_form_data = {}
            st.session_state.current_project = None
            st.session_state.current_page = "project_submission"
            st.rerun()
    
    with col2:
        if st.button("📋 My Projects", use_container_width=True, key="view_projects"):
            st.session_state.current_page = "my_projects"
            st.rerun()
    
    st.markdown("---")
    
    user_projects = [p for p in SAMPLE_PROJECTS if p["student_id"] == user["id"]]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📊</div>
            <div style='color: #334155; font-size: 0.9rem;'>Total Projects</div>
            <div style='font-size: 2rem; font-weight: 700; color: #2563eb;'>{len(user_projects)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        saved_projects = len([p for p in user_projects if p["status"] == "saved"])
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>✅</div>
            <div style='color: #334155; font-size: 0.9rem;'>Completed</div>
            <div style='font-size: 2rem; font-weight: 700; color: #16a34a;'>{saved_projects}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        analyzed_projects = len([p for p in user_projects if p["status"] == "analyzed"])
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🔍</div>
            <div style='color: #334155; font-size: 0.9rem;'>Analyzed</div>
            <div style='font-size: 2rem; font-weight: 700; color: #ea580c;'>{analyzed_projects}</div>
        </div>
        """, unsafe_allow_html=True)
    
    if user_projects:
        st.markdown("### 📌 Recent Projects")
        show_info_box(f"You have {len(user_projects)} project(s). Click 'My Projects' to view all details.")
        
        for project in sorted(user_projects, key=lambda x: x["created_date"], reverse=True)[:3]:
            show_project_card(project)
            if st.button("View Full Details", key=f"recent_details_{project['id']}"):
                st.session_state.current_project = project
                st.session_state.current_page = "project_details"
                st.rerun()
    else:
        st.info("👋 No projects yet. Create your first project to get started!")

def show_project_submission():
    """Display the project submission form."""
    apply_custom_css()
    
    show_header("Create New Project", "Submit your research project for novelty analysis")
    
    show_info_box(
        "Provide detailed information about your research project. "
        "This will be analyzed to identify its novelty and suggest improvements."
    )
    
    with st.form("project_form"):
        title = st.text_input(
            "Project Title *",
            value=st.session_state.project_form_data.get("title", ""),
            placeholder="e.g., AI-Powered Disease Detection System"
        )
        
        problem_statement = st.text_area(
            "Problem Statement *",
            value=st.session_state.project_form_data.get("problem_statement", ""),
            placeholder="Describe the problem your project solves...",
            height=100
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            domain = st.selectbox(
                "Domain *",
                options=[
                    "Natural Language Processing",
                    "Computer Vision",
                    "Medical AI",
                    "Time Series Analysis",
                    "Recommendation Systems",
                    "Reinforcement Learning",
                    "Graph Neural Networks",
                    "Other"
                ],
                index=0
            )
        
        with col2:
            dataset = st.text_input(
                "Dataset *",
                value=st.session_state.project_form_data.get("dataset", ""),
                placeholder="e.g., ImageNet, MNIST, Custom Dataset"
            )
        
        method = st.text_input(
            "Method/Algorithm *",
            value=st.session_state.project_form_data.get("method", ""),
            placeholder="e.g., CNN, BERT, Transformer, Federated Learning"
        )
        
        technologies_input = st.text_area(
            "Technologies Used *",
            value=st.session_state.project_form_data.get("technologies", ""),
            placeholder="e.g., Python, TensorFlow, PyTorch, Pandas (comma-separated)",
            height=80
        )
        
        st.markdown("### Additional Details (Optional)")
        
        additional_info = st.text_area(
            "Additional Information",
            value=st.session_state.project_form_data.get("additional_info", ""),
            placeholder="Any other relevant information about your project...",
            height=80
        )
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.form_submit_button("← Back", use_container_width=True):
                st.session_state.current_page = "dashboard"
                st.rerun()
        
        with col3:
            submitted = st.form_submit_button("Analyze Project →", use_container_width=True, type="primary")
            
            if submitted:
                if not all([title, problem_statement, domain, dataset, method, technologies_input]):
                    st.error("❌ Please fill in all required fields (marked with *)")
                else:
                    st.session_state.project_form_data = {
                        "title": title,
                        "problem_statement": problem_statement,
                        "domain": domain,
                        "dataset": dataset,
                        "method": method,
                        "technologies": [t.strip() for t in technologies_input.split(",")],
                        "additional_info": additional_info
                    }
                    
                    st.session_state.current_page = "analysis"
                    st.rerun()

def show_analysis_page():
    """Display the analysis page with loading animation."""
    apply_custom_css()
    
    show_header("Analyzing Your Project", "Please wait while we process your submission")
    
    show_loading_animation("Analyzing your project...")
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    steps = [
        ("Extracting project features...", 0.2),
        ("Comparing with existing projects...", 0.4),
        ("Identifying similar methodologies...", 0.6),
        ("Analyzing technology stack...", 0.8),
        ("Generating novelty suggestions...", 0.95),
        ("Finalizing results...", 1.0)
    ]
    
    for step_text, progress in steps:
        status_text.info(step_text)
        progress_bar.progress(progress)
        time.sleep(0.5)
    
    analysis_results = {
        "similar_projects": SAMPLE_SIMILAR_PROJECTS,
        "common_technologies": COMMON_TECHNOLOGIES,
        "common_datasets": COMMON_DATASETS,
        "common_methods": COMMON_METHODS,
        "novelty_ideas": NOVELTY_IDEAS,
        "existing_limitations": EXISTING_LIMITATIONS,
        "possible_gaps": POSSIBLE_GAPS
    }
    
    st.session_state.analysis_results = analysis_results
    
    progress_bar.empty()
    status_text.empty()
    
    st.markdown("""
    <div class='success-box'>
        <strong>✓ Analysis Complete!</strong><br>
        Your project has been analyzed. Redirecting to results page...
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1)
    
    st.session_state.current_page = "novelty_results"
    st.rerun()

def show_novelty_results():
    """Display the novelty analysis results."""
    apply_custom_css()
    
    show_header("Novelty Analysis Results", "Review your project analysis and suggested improvements")
    
    project_data = st.session_state.project_form_data
    analysis_results = st.session_state.analysis_results
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.rerun()
    
    with col3:
        if st.button("Logout", use_container_width=True):
            logout()
            st.rerun()
    
    st.markdown("---")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Project Details",
        "🔍 Similar Projects",
        "💡 Novelty Ideas",
        "⚠️ Limitations & Gaps",
        "📊 Technology Analysis"
    ])
    
    with tab1:
        st.markdown("### Your Project")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class='card'>
                <h4 style='margin-top: 0;'>{project_data['title']}</h4>
                <p style='color: #1e293b; margin: 0.5rem 0;'><strong>Domain:</strong> {project_data['domain']}</p>
                <p style='color: #1e293b; margin: 0.5rem 0;'><strong>Method:</strong> {project_data['method']}</p>
                <p style='color: #1e293b; margin: 0.5rem 0;'><strong>Dataset:</strong> {project_data['dataset']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='card'>
                <h4 style='margin-top: 0;'>Technologies</h4>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(format_technologies(project_data['technologies']), unsafe_allow_html=True)
        
        st.markdown("#### Problem Statement")
        st.markdown(f"""
        <div class='card'>
            {project_data['problem_statement']}
        </div>
        """, unsafe_allow_html=True)
        
        if project_data.get('additional_info'):
            st.markdown("#### Additional Information")
            st.markdown(f"""
            <div class='card'>
                {project_data['additional_info']}
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Similar Existing Projects")
        show_info_box(
            "These are existing projects that share similar characteristics with yours. "
            "The similarity percentage indicates how closely they align with your project."
        )
        
        similar_projects = analysis_results['similar_projects']
        
        if similar_projects:
            for idx, project in enumerate(similar_projects, 1):
                with st.container():
                    st.markdown(f"""
                    <div class='card'>
                        <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                            <div>
                                <h4 style='margin: 0 0 0.5rem 0;'>{project['title']}</h4>
                                <p style='color: #334155; margin: 0; font-size: 0.9rem;'>
                                    {project['authors']} ({project['year']})
                                </p>
                            </div>
                            <div style='text-align: right;'>
                                <div style='margin-bottom: 0.5rem;'>Similarity</div>
                                {format_similarity_percentage(project['similarity'])}
                            </div>
                        </div>
                        <div style='background-color: #f8fafc; padding: 1rem; border-radius: 6px;'>
                            <p style='margin: 0.5rem 0; color: #475569; font-size: 0.9rem;'>
                                <strong>Domain:</strong> {project['domain']}<br>
                                <strong>Method:</strong> {project['method']}<br>
                            </p>
                            <div style='margin-top: 1rem;'>
                                <strong style='color: #475569; font-size: 0.9rem;'>Technologies:</strong><br>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(format_technologies(project['technologies']), unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### Suggested Novelty Ideas")
        show_info_box(
            "These suggestions are ways to add novelty and innovation to your project. "
            "Select one to proceed with your project submission."
        )
        
        novelty_ideas = analysis_results['novelty_ideas']
        
        for novelty in novelty_ideas:
            with st.container():
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    st.markdown(f"""
                    <div class='card'>
                        <h4 style='margin: 0 0 0.5rem 0;'>{novelty['title']}</h4>
                        <p style='color: #1e293b; margin: 0.5rem 0; font-size: 0.95rem;'>
                            {novelty['description']}
                        </p>
                        <div style='margin-top: 1rem;'>
                            <span class='metric-badge'>Impact: {novelty['impact']}</span>
                            <span class='metric-badge'>Feasibility: {novelty['feasibility']}</span>
                        </div>
                        <p style='color: #1e293b; margin: 1rem 0 0 0; font-size: 0.9rem;'>
                            <strong>Details:</strong> {novelty['details']}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    if st.button("Select", key=f"select_{novelty['id']}", use_container_width=True):
                        st.session_state.selected_novelty = novelty
                        st.session_state.current_page = "select_novelty"
                        st.rerun()
    
    with tab4:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Existing Limitations")
            st.markdown("Common limitations found in similar projects:")
            for limitation in analysis_results['existing_limitations']:
                st.markdown(f"• {limitation}")
        
        with col2:
            st.markdown("### Possible Gaps")
            st.markdown("Opportunities for innovation in this field:")
            for gap in analysis_results['possible_gaps']:
                st.markdown(f"• {gap}")
    
    with tab5:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Common Technologies")
            st.markdown("Frequently used technologies in your domain:")
            for tech in analysis_results['common_technologies']:
                st.markdown(f"**{tech['name']}** - {tech['usage_percent']}% usage")
        
        with col2:
            st.markdown("### Common Methods")
            st.markdown("Popular methods and algorithms in your domain:")
            for method in analysis_results['common_methods']:
                st.markdown(f"**{method['name']}** - {method['usage_percent']}% usage")
        
        st.markdown("### Common Datasets")
        st.markdown("Widely used datasets in your domain:")
        for dataset in analysis_results['common_datasets']:
            st.markdown(f"**{dataset['name']}** - {dataset['usage_percent']}% usage")

def show_select_novelty():
    """Display the select and save novelty page."""
    apply_custom_css()
    
    show_header("Review & Save Your Project", "Confirm your project with the selected novelty idea")
    
    project_data = st.session_state.project_form_data
    selected_novelty = st.session_state.selected_novelty
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("← Back to Results", use_container_width=True):
            st.session_state.current_page = "novelty_results"
            st.rerun()
    
    with col2:
        if st.button("Logout", use_container_width=True):
            logout()
            st.rerun()
    
    st.markdown("---")
    
    show_info_box(
        "Review your project and the selected novelty idea below. "
        "Once saved, you'll be able to view this project in your project list."
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📋 Original Project")
        
        st.markdown(f"""
        <div class='card'>
            <h4 style='margin-top: 0; color: #2563eb;'>{project_data['title']}</h4>
            
            <div style='background-color: #f8fafc; padding: 1rem; border-radius: 6px; margin: 1rem 0;'>
                <p style='margin: 0; color: #64748b;'><strong>Domain:</strong></p>
                <p style='margin: 0.25rem 0 1rem 0; color: #1e293b;'>{project_data['domain']}</p>
                
                <p style='margin: 0; color: #64748b;'><strong>Method/Algorithm:</strong></p>
                <p style='margin: 0.25rem 0 1rem 0; color: #1e293b;'>{project_data['method']}</p>
                
                <p style='margin: 0; color: #64748b;'><strong>Dataset:</strong></p>
                <p style='margin: 0.25rem 0; color: #1e293b;'>{project_data['dataset']}</p>
            </div>
            
            <p style='margin: 1rem 0 0.5rem 0;'><strong>Technologies:</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(format_technologies(project_data['technologies']), unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='card' style='margin-top: 1rem;'>
            <p style='margin: 0; color: #334155;'><strong>Problem Statement:</strong></p>
            <p style='margin: 0.5rem 0; color: #1e293b; line-height: 1.6;'>
                {project_data['problem_statement']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### ✨ Selected Novelty Idea")
        
        st.markdown(f"""
        <div class='card' style='border-left: 4px solid #16a34a;'>
            <h4 style='margin-top: 0; color: #16a34a;'>{selected_novelty['title']}</h4>
            
            <p style='margin: 1rem 0; color: #1e293b; line-height: 1.6;'>
                {selected_novelty['description']}
            </p>
            
            <div style='background-color: #f8fafc; padding: 1rem; border-radius: 6px; margin: 1rem 0;'>
                <p style='margin: 0; color: #334155;'><strong>Implementation Details:</strong></p>
                <p style='margin: 0.5rem 0; color: #1e293b;'>{selected_novelty['details']}</p>
            </div>
            
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin: 1rem 0 0 0;'>
                <div style='background-color: #dcfce7; padding: 0.75rem; border-radius: 6px;'>
                    <p style='margin: 0; color: #15803d; font-size: 0.85rem;'>Impact</p>
                    <p style='margin: 0.25rem 0 0 0; color: #166534; font-weight: 600;'>{selected_novelty['impact']}</p>
                </div>
                <div style='background-color: #dbeafe; padding: 0.75rem; border-radius: 6px;'>
                    <p style='margin: 0; color: #0c4a6e; font-size: 0.85rem;'>Feasibility</p>
                    <p style='margin: 0.25rem 0 0 0; color: #164e63; font-weight: 600;'>{selected_novelty['feasibility']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### Finalize Submission")
    
    notes = st.text_area(
        "Additional Notes (Optional)",
        placeholder="Add any additional notes or comments about your project and the selected novelty...",
        height=80
    )
    
    if st.button("💾 Save Project", use_container_width=True, type="primary"):
        final_project = {
            "title": project_data["title"],
            "problem_statement": project_data["problem_statement"],
            "domain": project_data["domain"],
            "dataset": project_data["dataset"],
            "method": project_data["method"],
            "technologies": project_data["technologies"],
            "selected_novelty": selected_novelty["title"],
            "novelty_id": selected_novelty["id"],
            "notes": notes,
            "status": "saved"
        }
        
        st.session_state.saved_projects.append(final_project)
        
        show_success_box(
            f"✓ Project '{project_data['title']}' has been saved successfully! "
            "Redirecting to your projects list..."
        )
        
        st.session_state.project_form_data = {}
        st.session_state.selected_novelty = None
        st.session_state.analysis_results = None
        
        time.sleep(2)
        
        st.session_state.current_page = "my_projects"
        st.rerun()

def show_my_projects():
    """Display all projects submitted by the student."""
    apply_custom_css()
    
    show_header("My Projects", "View all your submitted projects")
    
    user = st.session_state.current_user
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("← Dashboard", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.rerun()
    
    with col3:
        if st.button("🚪 Logout", use_container_width=True):
            logout()
            st.rerun()
    
    st.markdown("---")
    
    user_projects = [p for p in SAMPLE_PROJECTS if p["student_id"] == user["id"]]
    
    if st.session_state.saved_projects:
        for saved_proj in st.session_state.saved_projects:
            user_projects.append({
                "id": f"proj_{len(user_projects) + 1:03d}",
                "student_id": user["id"],
                "title": saved_proj["title"],
                "problem_statement": saved_proj["problem_statement"],
                "domain": saved_proj["domain"],
                "dataset": saved_proj["dataset"],
                "method": saved_proj["method"],
                "technologies": saved_proj["technologies"],
                "selected_novelty": saved_proj["selected_novelty"],
                "status": saved_proj["status"],
                "created_date": "Today",
                "notes": saved_proj.get("notes", "")
            })
    
    if not user_projects:
        st.info("👋 You haven't submitted any projects yet. Create your first project!")
        
        if st.button("✨ Create New Project", use_container_width=True):
            st.session_state.project_form_data = {}
            st.session_state.current_page = "project_submission"
            st.rerun()
    else:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            show_info_box(f"You have {len(user_projects)} project(s)")
        
        with col2:
            status_filter = st.selectbox(
                "Filter by Status",
                options=["All", "Saved", "Analyzed"],
                key="status_filter"
            )
        
        if status_filter != "All":
            filtered_projects = [p for p in user_projects if p["status"] == status_filter.lower()]
        else:
            filtered_projects = user_projects
        
        for project in sorted(filtered_projects, key=lambda x: x["created_date"], reverse=True):
            with st.container():
                st.markdown(f"""
                <div class='project-card'>
                    <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                        <div style='flex: 1;'>
                            <h3 style='margin: 0 0 0.5rem 0; color: #1e293b;'>{project['title']}</h3>
                            <p style='color: #334155; margin: 0 0 1rem 0; font-size: 0.95rem;'>{project['domain']}</p>
                            
                            <div style='display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;'>
                                <span class='metric-badge'>{project['status'].upper()}</span>
                                <span class='metric-badge'>{project['created_date']}</span>
                                <span class='metric-badge'>Method: {project['method']}</span>
                            </div>
                            
                            <p style='color: #1e293b; margin: 0; font-size: 0.9rem;'>
                                <strong>Dataset:</strong> {project['dataset']}
                            </p>
                            
                            {f"<p style='color: #16a34a; margin: 0.5rem 0 0 0; font-size: 0.9rem;'><strong>✓ Selected Novelty:</strong> {project['selected_novelty']}</p>" if project.get('selected_novelty') else ""}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("View Full Details", key=f"details_{project['id']}", use_container_width=False):
                    st.session_state.current_project = project
                    st.session_state.current_page = "project_details"
                    st.rerun()
        
        st.markdown("---")
        
        if st.button("✨ Create New Project", use_container_width=True):
            st.session_state.project_form_data = {}
            st.session_state.current_page = "project_submission"
            st.rerun()

def show_project_details():
    """Display complete project information."""
    apply_custom_css()
    
    project = st.session_state.current_project
    
    show_header(project["title"], f"Submitted for {project['domain']}")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("← My Projects", use_container_width=True):
            st.session_state.current_page = "my_projects"
            st.rerun()
    
    with col3:
        if st.button("🚪 Logout", use_container_width=True):
            logout()
            st.rerun()
    
    st.markdown("---")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Project Info",
        "💡 Novelty Suggestion",
        "🔍 Similar Projects",
        "📊 Analysis Summary"
    ])
    
    with tab1:
        st.markdown("### Project Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class='card'>
                <p style='margin: 0; color: #334155; font-size: 0.9rem;'><strong>Domain</strong></p>
                <p style='margin: 0.5rem 0; color: #1e293b; font-weight: 600;'>{project['domain']}</p>
                
                <p style='margin: 1rem 0 0 0; color: #334155; font-size: 0.9rem;'><strong>Method/Algorithm</strong></p>
                <p style='margin: 0.5rem 0; color: #1e293b; font-weight: 600;'>{project['method']}</p>
                
                <p style='margin: 1rem 0 0 0; color: #334155; font-size: 0.9rem;'><strong>Dataset</strong></p>
                <p style='margin: 0.5rem 0; color: #1e293b; font-weight: 600;'>{project['dataset']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='card'>
                <p style='margin: 0; color: #334155; font-size: 0.9rem;'><strong>Status</strong></p>
                <p style='margin: 0.5rem 0; color: #2563eb; font-weight: 600;'>{project['status'].upper()}</p>
                
                <p style='margin: 1rem 0 0 0; color: #334155; font-size: 0.9rem;'><strong>Submitted</strong></p>
                <p style='margin: 0.5rem 0; color: #1e293b; font-weight: 600;'>{project['created_date']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("#### Technologies Used")
        st.markdown(format_technologies(project['technologies']), unsafe_allow_html=True)
        
        st.markdown("#### Problem Statement")
        st.markdown(f"""
        <div class='card'>
            <p style='color: #475569; line-height: 1.6; margin: 0;'>
                {project['problem_statement']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        if project.get('selected_novelty'):
            st.markdown("### Selected Novelty Idea")
            st.markdown(f"""
            <div class='card' style='border-left: 4px solid #16a34a;'>
                <h4 style='margin-top: 0; color: #16a34a;'>{project['selected_novelty']}</h4>
                <p style='color: #475569; margin: 1rem 0;'>
                    This novelty suggestion was selected to enhance your research project.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            if project.get('notes'):
                st.markdown("#### Your Notes")
                st.markdown(f"""
                <div class='card'>
                    <p style='color: #475569; line-height: 1.6; margin: 0;'>
                        {project['notes']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No novelty idea selected for this project yet.")
    
    with tab3:
        st.markdown("### Similar Existing Projects")
        
        similar_projects = [
            {
                "title": "Deep Learning for Feature Analysis",
                "authors": "Smith et al.",
                "year": 2023,
                "similarity": 75
            },
            {
                "title": "Advanced Neural Network Architectures",
                "authors": "Johnson & Lee",
                "year": 2023,
                "similarity": 68
            },
            {
                "title": "Optimization Techniques for ML Models",
                "authors": "Chen et al.",
                "year": 2024,
                "similarity": 62
            }
        ]
        
        for proj in similar_projects:
            st.markdown(f"""
            <div class='card'>
                <div style='display: flex; justify-content: space-between; align-items: start;'>
                    <div style='flex: 1;'>
                        <h4 style='margin: 0 0 0.5rem 0;'>{proj['title']}</h4>
                        <p style='color: #64748b; margin: 0; font-size: 0.9rem;'>
                            {proj['authors']} ({proj['year']})
                        </p>
                    </div>
                    <div style='text-align: right;'>
                        <div style='color: #64748b; font-size: 0.9rem;'>Similarity</div>
                        {format_similarity_percentage(proj['similarity'])}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### Analysis Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Key Findings")
            st.markdown("""
            - Project addresses a relevant research problem
            - Comparable methodologies found in recent literature
            - Selected technologies are industry-standard
            - Novelty opportunity identified in implementation approach
            """)
        
        with col2:
            st.markdown("#### Recommendations")
            st.markdown("""
            1. Implement the selected novelty idea
            2. Review similar projects for best practices
            3. Consider adding explainability features
            4. Plan for comprehensive testing
            """)

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application entry point."""
    initialize_session()
    apply_custom_css()

    # Explicit navigation prevents helper modules in pages/ being run as scripts.
    st.navigation(
        [st.Page(show_current_page, title="Project Novelty Detector", default=True)],
        position="hidden",
    ).run()


def show_navigation():
    """Keep sidebar actions within the application's session-based router."""
    if not st.session_state.logged_in:
        return
    def navigate(page):
        if page == "project_submission":
            st.session_state.project_form_data = {}
            st.session_state.current_project = None
        st.session_state.current_page = page

    with st.sidebar:
        st.title("Project Novelty Detector")
        st.caption(st.session_state.current_user["name"])
        for label, page in (
            ("Dashboard", "dashboard"),
            ("My Projects", "my_projects"),
            ("Create New Project", "project_submission"),
        ):
            st.button(label, key=f"nav_{page}", use_container_width=True,
                      on_click=navigate, args=(page,))
        st.button("Logout", key="nav_logout", use_container_width=True,
                  on_click=logout)


def show_current_page():
    """Render the requested view through the authenticated application router."""
    show_navigation()
    
    # Route to appropriate page based on session state
    current_page = st.session_state.current_page
    
    if not st.session_state.logged_in:
        show_login_page()
    elif current_page == "dashboard":
        show_dashboard()
    elif current_page == "project_submission":
        show_project_submission()
    elif current_page == "analysis":
        show_analysis_page()
    elif current_page == "novelty_results":
        show_novelty_results()
    elif current_page == "select_novelty":
        show_select_novelty()
    elif current_page == "my_projects":
        show_my_projects()
    elif current_page == "project_details":
        show_project_details()
    else:
        show_dashboard()

if __name__ == "__main__":
    main()
