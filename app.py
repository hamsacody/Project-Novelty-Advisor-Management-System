"""
Project Novelty Detector - Frontend Application
A Streamlit application for analyzing research project novelty.

Navigation Flow:
Login → Dashboard → Submit Project → Analyze → Novelty Results → Select Novelty → Save → My Projects
"""

import streamlit as st
from utils.session_manager import initialize_session, is_logged_in, get_current_page
from utils.ui_helpers import apply_custom_css, show_navigation
from utils.session_manager import logout

# Import all page modules
from pages import (
    login,
    dashboard,
    project_submission,
    analysis,
    novelty_results,
    select_novelty,
    my_projects,
    project_details
)


def main():
    """Main application entry point."""
    # Configure page
    st.set_page_config(
        page_title="Project Novelty Detector",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session()
    
    # Apply custom CSS
    apply_custom_css()

    # Explicit navigation prevents helper modules in pages/ being run as scripts.
    st.navigation(
        [st.Page(show_current_page, title="Project Novelty Detector", default=True)],
        position="hidden",
    ).run()


def show_current_page():
    """Render the requested view through the authenticated application router."""
    show_navigation(logout)
    
    # Route to appropriate page based on session state
    if not is_logged_in():
        # Show login page
        login.show_login_page()
    else:
        # Logged-in user - show current page
        current_page = get_current_page()
        
        if current_page == "dashboard":
            dashboard.show_dashboard()
        elif current_page == "project_submission":
            project_submission.show_project_submission()
        elif current_page == "analysis":
            analysis.show_analysis_page()
        elif current_page == "novelty_results":
            novelty_results.show_novelty_results()
        elif current_page == "select_novelty":
            select_novelty.show_select_novelty()
        elif current_page == "my_projects":
            my_projects.show_my_projects()
        elif current_page == "project_details":
            project_details.show_project_details()
        else:
            # Default to dashboard
            dashboard.show_dashboard()


if __name__ == "__main__":
    main()
