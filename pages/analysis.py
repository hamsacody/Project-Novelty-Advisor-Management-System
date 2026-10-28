"""Analysis page showing loading state."""

import streamlit as st
import time
from utils.session_manager import set_page
from utils.ui_helpers import apply_custom_css, show_header, show_loading_animation
from data.sample_data import (
    SAMPLE_SIMILAR_PROJECTS, COMMON_TECHNOLOGIES,
    COMMON_DATASETS, COMMON_METHODS, NOVELTY_IDEAS,
    EXISTING_LIMITATIONS, POSSIBLE_GAPS
)


def show_analysis_page():
    """Display the analysis page with loading animation."""
    apply_custom_css()
    
    show_header("Analyzing Your Project", "Please wait while we process your submission")
    
    # Show loading animation
    show_loading_animation("Analyzing your project...")
    
    # Simulate analysis progress
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
    
    # Generate analysis results
    analysis_results = {
        "similar_projects": SAMPLE_SIMILAR_PROJECTS,
        "common_technologies": COMMON_TECHNOLOGIES,
        "common_datasets": COMMON_DATASETS,
        "common_methods": COMMON_METHODS,
        "novelty_ideas": NOVELTY_IDEAS,
        "existing_limitations": EXISTING_LIMITATIONS,
        "possible_gaps": POSSIBLE_GAPS
    }
    
    # Save results to session
    st.session_state.analysis_results = analysis_results
    
    # Clear progress indicators
    progress_bar.empty()
    status_text.empty()
    
    # Show success message
    st.markdown("""
    <div class='success-box'>
        <strong>✓ Analysis Complete!</strong><br>
        Your project has been analyzed. Redirecting to results page...
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1)
    
    # Move to novelty results page
    set_page("novelty_results")
    st.rerun()
