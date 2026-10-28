"""Session management for user authentication and state tracking."""

import streamlit as st
from data.sample_data import SAMPLE_STUDENTS


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
    if "analyzing" not in st.session_state:
        st.session_state.analyzing = False


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


def is_logged_in():
    """Check if user is logged in."""
    return st.session_state.logged_in


def get_current_user():
    """Get current logged-in user."""
    return st.session_state.current_user


def set_page(page_name):
    """Set the current page."""
    st.session_state.current_page = page_name


def get_current_page():
    """Get the current page."""
    return st.session_state.current_page
