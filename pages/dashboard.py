"""Student Dashboard page."""

import streamlit as st
from utils.session_manager import get_current_user, set_page, logout
from utils.ui_helpers import (
    apply_custom_css, show_welcome_message, show_project_card,
    show_info_box
)
from data.sample_data import SAMPLE_PROJECTS


def show_dashboard():
    """Display the student dashboard."""
    apply_custom_css()
    
    user = get_current_user()
    
    # Header with logout button
    col1, col2 = st.columns([4, 1])
    with col1:
        show_welcome_message(user["name"])
    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            logout()
            st.rerun()
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✨ Create New Project", use_container_width=True, 
                    key="create_project"):
            st.session_state.project_form_data = {}
            st.session_state.current_project = None
            set_page("project_submission")
            st.rerun()
    
    with col2:
        if st.button("📋 My Projects", use_container_width=True, 
                    key="view_projects"):
            set_page("my_projects")
            st.rerun()
    
    # Quick stats
    st.markdown("---")
    
    # Get user's projects
    user_projects = [p for p in SAMPLE_PROJECTS if p["student_id"] == user["id"]]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📊</div>
            <div style='color: #64748b; font-size: 0.9rem;'>Total Projects</div>
            <div style='font-size: 2rem; font-weight: 700; color: #2563eb;'>{len(user_projects)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        saved_projects = len([p for p in user_projects if p["status"] == "saved"])
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>✅</div>
            <div style='color: #64748b; font-size: 0.9rem;'>Completed</div>
            <div style='font-size: 2rem; font-weight: 700; color: #16a34a;'>{saved_projects}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        analyzed_projects = len([p for p in user_projects if p["status"] == "analyzed"])
        st.markdown(f"""
        <div class='card' style='text-align: center;'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🔍</div>
            <div style='color: #64748b; font-size: 0.9rem;'>Analyzed</div>
            <div style='font-size: 2rem; font-weight: 700; color: #ea580c;'>{analyzed_projects}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent projects section
    if user_projects:
        st.markdown("### 📌 Recent Projects")
        show_info_box(f"You have {len(user_projects)} project(s). Click 'My Projects' to view all details.")
        
        for project in sorted(user_projects, key=lambda x: x["created_date"], reverse=True)[:3]:
            show_project_card(project)
            if st.button("View Full Details", key=f"recent_details_{project['id']}"):
                st.session_state.current_project = project
                set_page("project_details")
                st.rerun()
    else:
        st.info("👋 No projects yet. Create your first project to get started!")
