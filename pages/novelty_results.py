"""Novelty Results page - MAIN PAGE showing analysis results."""

import streamlit as st
from utils.session_manager import set_page, get_current_user
from utils.ui_helpers import (
    apply_custom_css, show_header, format_technologies,
    format_similarity_percentage, show_info_box
)


def show_novelty_results():
    """Display the novelty analysis results."""
    apply_custom_css()
    
    show_header("Novelty Analysis Results", "Review your project analysis and suggested improvements")
    
    project_data = st.session_state.project_form_data
    analysis_results = st.session_state.analysis_results
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("← Back", use_container_width=True):
            set_page("dashboard")
            st.rerun()
    
    with col3:
        if st.button("Logout", use_container_width=True):
            from utils.session_manager import logout
            logout()
            st.rerun()
    
    st.markdown("---")
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Project Details",
        "🔍 Similar Projects",
        "💡 Novelty Ideas",
        "⚠️ Limitations & Gaps",
        "📊 Technology Analysis"
    ])
    
    # Tab 1: Project Details
    with tab1:
        st.markdown("### Your Project")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class='card'>
                <h4 style='margin-top: 0;'>{project_data['title']}</h4>
                <p style='color: #64748b; margin: 0.5rem 0;'><strong>Domain:</strong> {project_data['domain']}</p>
                <p style='color: #64748b; margin: 0.5rem 0;'><strong>Method:</strong> {project_data['method']}</p>
                <p style='color: #64748b; margin: 0.5rem 0;'><strong>Dataset:</strong> {project_data['dataset']}</p>
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
    
    # Tab 2: Similar Projects
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
                                <p style='color: #64748b; margin: 0; font-size: 0.9rem;'>
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
    
    # Tab 3: Novelty Ideas
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
                        <p style='color: #64748b; margin: 0.5rem 0; font-size: 0.95rem;'>
                            {novelty['description']}
                        </p>
                        <div style='margin-top: 1rem;'>
                            <span class='metric-badge'>Impact: {novelty['impact']}</span>
                            <span class='metric-badge'>Feasibility: {novelty['feasibility']}</span>
                        </div>
                        <p style='color: #475569; margin: 1rem 0 0 0; font-size: 0.9rem;'>
                            <strong>Details:</strong> {novelty['details']}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    if st.button("Select", key=f"select_{novelty['id']}", use_container_width=True):
                        st.session_state.selected_novelty = novelty
                        set_page("select_novelty")
                        st.rerun()
    
    # Tab 4: Limitations & Gaps
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
    
    # Tab 5: Technology Analysis
    with tab5:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Common Technologies")
            st.markdown("Frequently used technologies in your domain:")
            for tech in analysis_results['common_technologies']:
                st.markdown(f"""
                **{tech['name']}** - {tech['usage_percent']}% usage
                """)
        
        with col2:
            st.markdown("### Common Methods")
            st.markdown("Popular methods and algorithms in your domain:")
            for method in analysis_results['common_methods']:
                st.markdown(f"""
                **{method['name']}** - {method['usage_percent']}% usage
                """)
        
        st.markdown("### Common Datasets")
        st.markdown("Widely used datasets in your domain:")
        for dataset in analysis_results['common_datasets']:
            st.markdown(f"""
            **{dataset['name']}** - {dataset['usage_percent']}% usage
            """)
