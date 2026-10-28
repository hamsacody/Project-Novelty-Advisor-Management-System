"""Project Details page - complete project information."""

import streamlit as st
from utils.session_manager import set_page, logout
from utils.ui_helpers import (
    apply_custom_css, show_header, format_technologies,
    format_similarity_percentage, show_info_box
)


def show_project_details():
    """Display complete project information."""
    apply_custom_css()
    
    project = st.session_state.current_project
    
    show_header(project["title"], f"Submitted for {project['domain']}")
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("← My Projects", use_container_width=True):
            set_page("my_projects")
            st.rerun()
    
    with col3:
        if st.button("🚪 Logout", use_container_width=True):
            logout()
            st.rerun()
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Project Info",
        "💡 Novelty Suggestion",
        "🔍 Similar Projects",
        "📊 Analysis Summary"
    ])
    
    # Tab 1: Project Information
    with tab1:
        st.markdown("### Project Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class='card'>
                <p style='margin: 0; color: #64748b; font-size: 0.9rem;'><strong>Domain</strong></p>
                <p style='margin: 0.5rem 0; color: #1e293b; font-weight: 600;'>{project['domain']}</p>
                
                <p style='margin: 1rem 0 0 0; color: #64748b; font-size: 0.9rem;'><strong>Method/Algorithm</strong></p>
                <p style='margin: 0.5rem 0; color: #1e293b; font-weight: 600;'>{project['method']}</p>
                
                <p style='margin: 1rem 0 0 0; color: #64748b; font-size: 0.9rem;'><strong>Dataset</strong></p>
                <p style='margin: 0.5rem 0; color: #1e293b; font-weight: 600;'>{project['dataset']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='card'>
                <p style='margin: 0; color: #64748b; font-size: 0.9rem;'><strong>Status</strong></p>
                <p style='margin: 0.5rem 0; color: #2563eb; font-weight: 600;'>{project['status'].upper()}</p>
                
                <p style='margin: 1rem 0 0 0; color: #64748b; font-size: 0.9rem;'><strong>Submitted</strong></p>
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
    
    # Tab 2: Selected Novelty
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
    
    # Tab 3: Similar Projects
    with tab3:
        st.markdown("### Similar Existing Projects")
        
        # Mock similar projects data
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
    
    # Tab 4: Analysis Summary
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
