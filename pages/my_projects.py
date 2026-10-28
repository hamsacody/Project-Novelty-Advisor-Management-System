"""My Projects page - display all submitted projects."""

import streamlit as st
from utils.session_manager import set_page, get_current_user, logout
from utils.ui_helpers import apply_custom_css, show_header, show_info_box
from data.sample_data import SAMPLE_PROJECTS


def show_my_projects():
    """Display all projects submitted by the student."""
    apply_custom_css()
    
    show_header("My Projects", "View all your submitted projects")
    
    user = get_current_user()
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("← Dashboard", use_container_width=True):
            set_page("dashboard")
            st.rerun()
    
    with col3:
        if st.button("🚪 Logout", use_container_width=True):
            logout()
            st.rerun()
    
    st.markdown("---")
    
    # Get all user projects
    user_projects = [p for p in SAMPLE_PROJECTS if p["student_id"] == user["id"]]
    
    # Add any saved projects from current session
    if "saved_projects" in st.session_state and st.session_state.saved_projects:
        # Add session-saved projects (these would normally come from the database)
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
            set_page("project_submission")
            st.rerun()
    else:
        # Filter options
        col1, col2 = st.columns([2, 1])
        
        with col1:
            show_info_box(f"You have {len(user_projects)} project(s)")
        
        with col2:
            status_filter = st.selectbox(
                "Filter by Status",
                options=["All", "Saved", "Analyzed"],
                key="status_filter"
            )
        
        # Filter projects
        if status_filter != "All":
            filtered_projects = [p for p in user_projects if p["status"] == status_filter.lower()]
        else:
            filtered_projects = user_projects
        
        # Display projects
        for project in sorted(filtered_projects, key=lambda x: x["created_date"], reverse=True):
            with st.container():
                st.markdown(f"""
                <div class='project-card'>
                    <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                        <div style='flex: 1;'>
                            <h3 style='margin: 0 0 0.5rem 0; color: #1e293b;'>{project['title']}</h3>
                            <p style='color: #64748b; margin: 0 0 1rem 0; font-size: 0.95rem;'>{project['domain']}</p>
                            
                            <div style='display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;'>
                                <span class='metric-badge'>{project['status'].upper()}</span>
                                <span class='metric-badge'>{project['created_date']}</span>
                                <span class='metric-badge'>Method: {project['method']}</span>
                            </div>
                            
                            <p style='color: #475569; margin: 0; font-size: 0.9rem;'>
                                <strong>Dataset:</strong> {project['dataset']}
                            </p>
                            
                            {f"<p style='color: #16a34a; margin: 0.5rem 0 0 0; font-size: 0.9rem;'><strong>✓ Selected Novelty:</strong> {project['selected_novelty']}</p>" if project.get('selected_novelty') else ""}
                        </div>
                        
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Details button action
                if st.button("View Full Details", key=f"details_{project['id']}", 
                           use_container_width=False):
                    st.session_state.current_project = project
                    set_page("project_details")
                    st.rerun()
        
        st.markdown("---")
        
        if st.button("✨ Create New Project", use_container_width=True):
            st.session_state.project_form_data = {}
            set_page("project_submission")
            st.rerun()
