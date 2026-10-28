"""Login page for student authentication."""

import streamlit as st
from utils.session_manager import authenticate_user, set_page
from utils.ui_helpers import apply_custom_css, show_header


def show_login_page():
    """Display the login page."""
    apply_custom_css()
    
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Logo/Title
        st.markdown("""
        <div style='text-align: center; margin-bottom: 3rem;'>
            <h1 style='border: none; color: #2563eb; font-size: 2.5rem;'>🚀</h1>
            <h2 style='color: inherit; margin: 0;'>Project Novelty Detector</h2>
            <p style='color: inherit; font-size: 1rem; margin-top: 0.5rem;'>
                Discover innovation in your research projects
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Login form
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
                    set_page("dashboard")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")
        
        # Demo credentials
        st.markdown("""
        <div style='background-color: #dbeafe; border-left: 4px solid #2563eb; 
                    padding: 1rem; border-radius: 4px; margin-top: 2rem;'>
            <p style='margin: 0; color: #1e40af; font-weight: 600;'>Demo Credentials</p>
            <p style='margin: 0.5rem 0 0 0; color: #475569; font-size: 0.9rem;'>
                <strong>Student 1:</strong><br>
                Email: john@university.edu<br>
                Password: password123
            </p>
            <p style='margin: 1rem 0 0 0; color: #475569; font-size: 0.9rem;'>
                <strong>Student 2:</strong><br>
                Email: jane@university.edu<br>
                Password: password123
            </p>
        </div>
        """, unsafe_allow_html=True)
