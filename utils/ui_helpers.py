"""UI helper functions and styling utilities."""

import streamlit as st
from datetime import datetime


def show_navigation(logout_callback):
    """Keep sidebar actions within the application's session-based router."""
    if not st.session_state.logged_in:
        return
    def navigate(page):
        if page == "project_submission":
            st.session_state.project_form_data = {}
            st.session_state.current_project = None
        st.session_state.current_page = page

    with st.sidebar:
        st.title("Project Novelty Detector")
        st.caption(st.session_state.current_user["name"])
        for label, page in (
            ("Dashboard", "dashboard"),
            ("My Projects", "my_projects"),
            ("Create New Project", "project_submission"),
        ):
            st.button(label, key=f"nav_{page}", use_container_width=True,
                      on_click=navigate, args=(page,))
        st.button("Logout", key="nav_logout", use_container_width=True,
                  on_click=logout_callback)


def apply_custom_css():
    """Apply custom CSS styling to the application."""
    st.markdown("""
    <style>
        /* Main styling */
        :root {
            --primary-color: #2563eb;
            --secondary-color: #1e40af;
            --success-color: #16a34a;
            --danger-color: #dc2626;
            --warning-color: #ea580c;
            --light-bg: #f8fafc;
            --border-color: #e2e8f0;
        }
        
        /* Page container */
        .main {
            padding: 2rem;
        }
        
        /* Headers */
        h1 {
            color: #1e293b;
            border-bottom: 3px solid #2563eb;
            padding-bottom: 1rem;
        }
        
        h2 {
            color: #334155;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }
        
        h3 {
            color: #475569;
        }
        
        /* Cards and containers */
        .card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        
        /* Form elements */
        .stTextInput > div > div > input,
        .stPasswordInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {
            border-radius: 6px;
            border: 1px solid #cbd5e1;
            padding: 0.75rem;
        }
        
        /* Buttons */
        .stButton > button {
            background-color: #2563eb;
            color: white;
            border-radius: 6px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #1e40af;
            box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
        }
        
        /* Success message */
        .success-box {
            background-color: #dcfce7;
            border-left: 4px solid #16a34a;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        
        /* Warning message */
        .warning-box {
            background-color: #fef08a;
            border-left: 4px solid #ea580c;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        
        /* Info message */
        .info-box {
            background-color: #dbeafe;
            border-left: 4px solid #2563eb;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        
        /* Project card */
        .project-card {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .project-card:hover {
            border-color: #2563eb;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.1);
        }
        
        /* Metric badge */
        .metric-badge {
            display: inline-block;
            background-color: #dbeafe;
            color: #1e40af;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }
        
        /* Table styling */
        .dataframe {
            width: 100% !important;
        }
        
        /* Status badge */
        .status-active {
            color: #16a34a;
            font-weight: 600;
        }
        
        .status-pending {
            color: #ea580c;
            font-weight: 600;
        }
        
        .status-saved {
            color: #2563eb;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)


def show_header(title, subtitle=""):
    """Display a styled header."""
    st.markdown(f"# {title}")
    if subtitle:
        st.markdown(f"<p style='color: #64748b; font-size: 1.1rem;'>{subtitle}</p>", 
                   unsafe_allow_html=True)


def show_welcome_message(name):
    """Display a welcome message."""
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%); 
                color: white; padding: 2rem; border-radius: 8px; text-align: center; 
                margin-bottom: 2rem;'>
        <h1 style='color: white; border: none; margin: 0;'>Welcome, {name}! 👋</h1>
        <p style='margin: 0.5rem 0 0 0;'>Discover the novelty in your research projects</p>
    </div>
    """, unsafe_allow_html=True)


def show_project_card(project):
    """Display a project card."""
    st.markdown(f"""
    <div class='project-card'>
        <div style='display: flex; justify-content: space-between; align-items: start;'>
            <div style='flex: 1;'>
                <h3 style='margin: 0 0 0.5rem 0;'>{project['title']}</h3>
                <p style='color: #64748b; margin: 0 0 1rem 0; font-size: 0.95rem;'>{project['domain']}</p>
                <div style='margin-bottom: 1rem;'>
                    <span class='metric-badge'>{project['status'].upper()}</span>
                    <span class='metric-badge'>{project['created_date']}</span>
                </div>
                <p style='color: #475569; margin: 0; font-size: 0.9rem;'>
                    <strong>Method:</strong> {project['method']}<br>
                    <strong>Dataset:</strong> {project['dataset']}
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_info_box(message):
    """Display an info box."""
    st.markdown(f"""
    <div class='info-box'>
        <strong>ℹ️ Information:</strong><br>
        {message}
    </div>
    """, unsafe_allow_html=True)


def show_success_box(message):
    """Display a success box."""
    st.markdown(f"""
    <div class='success-box'>
        <strong>✓ Success:</strong><br>
        {message}
    </div>
    """, unsafe_allow_html=True)


def show_warning_box(message):
    """Display a warning box."""
    st.markdown(f"""
    <div class='warning-box'>
        <strong>⚠️ Warning:</strong><br>
        {message}
    </div>
    """, unsafe_allow_html=True)


def format_technologies(techs):
    """Format technologies as styled badges."""
    html = ""
    colors = {
        "Python": "#3776ab",
        "TensorFlow": "#ff6f00",
        "PyTorch": "#ee4c2c",
        "Transformers": "#7b68ee",
        "Pandas": "#150458",
        "NumPy": "#013243",
        "Keras": "#d00000",
        "Scikit-learn": "#f7931e"
    }
    
    for tech in techs:
        color = colors.get(tech, "#2563eb")
        html += f"""
        <span style='display: inline-block; background-color: {color}33; 
                     color: {color}; padding: 0.35rem 0.75rem; 
                     border-radius: 20px; margin-right: 0.5rem; 
                     margin-bottom: 0.5rem; font-size: 0.875rem; 
                     border: 1px solid {color};'>
            {tech}
        </span>
        """
    return html


def format_similarity_percentage(percentage):
    """Format similarity percentage with color coding."""
    if percentage >= 75:
        color = "#dc2626"
    elif percentage >= 60:
        color = "#ea580c"
    else:
        color = "#16a34a"
    
    return f"<span style='font-size: 1.5rem; font-weight: 700; color: {color};'>{percentage}%</span>"


def show_loading_animation(message="Loading..."):
    """Show a loading animation."""
    st.markdown(f"""
    <div style='text-align: center; padding: 2rem;'>
        <div style='font-size: 3rem; margin-bottom: 1rem;'>⏳</div>
        <h3>{message}</h3>
        <p style='color: #64748b;'>This may take a few moments...</p>
    </div>
    """, unsafe_allow_html=True)


def show_metric_row(label, value, unit=""):
    """Display a metric row."""
    st.markdown(f"""
    <div style='padding: 1rem; background-color: #f8fafc; border-radius: 6px; 
                margin-bottom: 0.5rem; border-left: 4px solid #2563eb;'>
        <div style='color: #64748b; font-size: 0.9rem;'>{label}</div>
        <div style='color: #1e293b; font-size: 1.25rem; font-weight: 600;'>{value} {unit}</div>
    </div>
    """, unsafe_allow_html=True)
