"""Project submission page."""

import streamlit as st
from utils.session_manager import set_page, get_current_user
from utils.ui_helpers import apply_custom_css, show_header, show_info_box


def show_project_submission():
    """Display the project submission form."""
    apply_custom_css()
    
    show_header("Create New Project", "Submit your research project for novelty analysis")
    
    show_info_box(
        "Provide detailed information about your research project. "
        "This will be analyzed to identify its novelty and suggest improvements."
    )
    
    with st.form("project_form"):
        # Project title
        title = st.text_input(
            "Project Title *",
            value=st.session_state.project_form_data.get("title", ""),
            placeholder="e.g., AI-Powered Disease Detection System",
            help="A clear, descriptive title for your project"
        )
        
        # Problem statement
        problem_statement = st.text_area(
            "Problem Statement *",
            value=st.session_state.project_form_data.get("problem_statement", ""),
            placeholder="Describe the problem your project solves...",
            height=100,
            help="What problem does your project address?"
        )
        
        # Two columns for domain and dataset
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
                index=0 if st.session_state.project_form_data.get("domain") is None 
                else ["Natural Language Processing", "Computer Vision", "Medical AI", 
                      "Time Series Analysis", "Recommendation Systems", "Reinforcement Learning",
                      "Graph Neural Networks", "Other"].index(st.session_state.project_form_data.get("domain", "Natural Language Processing")),
                help="Select the primary domain of your project"
            )
        
        with col2:
            dataset = st.text_input(
                "Dataset *",
                value=st.session_state.project_form_data.get("dataset", ""),
                placeholder="e.g., ImageNet, MNIST, Custom Dataset",
                help="What dataset does your project use?"
            )
        
        # Method/Algorithm
        method = st.text_input(
            "Method/Algorithm *",
            value=st.session_state.project_form_data.get("method", ""),
            placeholder="e.g., CNN, BERT, Transformer, Federated Learning",
            help="What's the main method or algorithm used?"
        )
        
        # Technologies
        technologies_input = st.text_area(
            "Technologies Used *",
            value=st.session_state.project_form_data.get("technologies", ""),
            placeholder="e.g., Python, TensorFlow, PyTorch, Pandas (comma-separated)",
            height=80,
            help="List all technologies and frameworks used (comma-separated)"
        )
        
        # Additional details
        st.markdown("### Additional Details (Optional)")
        
        additional_info = st.text_area(
            "Additional Information",
            value=st.session_state.project_form_data.get("additional_info", ""),
            placeholder="Any other relevant information about your project...",
            height=80,
            help="Additional context or details about your project"
        )
        
        # Form submission
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.form_submit_button("← Back", use_container_width=True):
                set_page("dashboard")
                st.rerun()
        
        with col3:
            submitted = st.form_submit_button("Analyze Project →", 
                                            use_container_width=True,
                                            type="primary")
            
            if submitted:
                # Validate form
                if not all([title, problem_statement, domain, dataset, method, technologies_input]):
                    st.error("❌ Please fill in all required fields (marked with *)")
                else:
                    # Save form data to session
                    st.session_state.project_form_data = {
                        "title": title,
                        "problem_statement": problem_statement,
                        "domain": domain,
                        "dataset": dataset,
                        "method": method,
                        "technologies": [t.strip() for t in technologies_input.split(",")],
                        "additional_info": additional_info
                    }
                    
                    # Move to analysis page
                    set_page("analysis")
                    st.rerun()
