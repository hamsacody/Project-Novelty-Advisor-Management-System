"""Select & Save Page - showing selected novelty and project idea."""

import streamlit as st
from utils.session_manager import set_page, get_current_user
from utils.ui_helpers import (
    apply_custom_css, show_header, show_success_box,
    show_info_box, format_technologies
)


def show_select_novelty():
    """Display the select and save novelty page."""
    apply_custom_css()
    
    show_header("Review & Save Your Project", "Confirm your project with the selected novelty idea")
    
    project_data = st.session_state.project_form_data
    selected_novelty = st.session_state.selected_novelty
    
    # Navigation buttons
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("← Back to Results", use_container_width=True):
            set_page("novelty_results")
            st.rerun()
    
    with col2:
        if st.button("Logout", use_container_width=True):
            from utils.session_manager import logout
            logout()
            st.rerun()
    
    st.markdown("---")
    
    show_info_box(
        "Review your project and the selected novelty idea below. "
        "Once saved, you'll be able to view this project in your project list."
    )
    
    # Main content
    col1, col2 = st.columns(2)
    
    # Original Project (Left Column)
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
            <p style='margin: 0; color: #64748b;'><strong>Problem Statement:</strong></p>
            <p style='margin: 0.5rem 0; color: #475569; line-height: 1.6;'>
                {project_data['problem_statement']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Selected Novelty Idea (Right Column)
    with col2:
        st.markdown("### ✨ Selected Novelty Idea")
        
        st.markdown(f"""
        <div class='card' style='border-left: 4px solid #16a34a;'>
            <h4 style='margin-top: 0; color: #16a34a;'>{selected_novelty['title']}</h4>
            
            <p style='margin: 1rem 0; color: #475569; line-height: 1.6;'>
                {selected_novelty['description']}
            </p>
            
            <div style='background-color: #f8fafc; padding: 1rem; border-radius: 6px; margin: 1rem 0;'>
                <p style='margin: 0; color: #64748b;'><strong>Implementation Details:</strong></p>
                <p style='margin: 0.5rem 0; color: #475569;'>{selected_novelty['details']}</p>
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
    
    # Save button section
    st.markdown("---")
    
    st.markdown("### Finalize Submission")
    
    # Add optional notes
    notes = st.text_area(
        "Additional Notes (Optional)",
        placeholder="Add any additional notes or comments about your project and the selected novelty...",
        height=80
    )
    
    # Save button
    if st.button("💾 Save Project", use_container_width=True, type="primary"):
        # Create the final project data
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
        
        # Save to session (in real app, would save to database)
        if "saved_projects" not in st.session_state:
            st.session_state.saved_projects = []
        
        st.session_state.saved_projects.append(final_project)
        
        # Show success message
        show_success_box(
            f"✓ Project '{project_data['title']}' has been saved successfully! "
            "Redirecting to your projects list..."
        )
        
        # Reset form
        st.session_state.project_form_data = {}
        st.session_state.selected_novelty = None
        st.session_state.analysis_results = None
        
        import time
        time.sleep(2)
        
        # Go to my projects
        set_page("my_projects")
        st.rerun()
