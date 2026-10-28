# Project Novelty Detector - Frontend

A clean, professional Streamlit application for analyzing research project novelty and suggesting improvements.

## 🚀 Features

- **Student Authentication**: Secure login with sample credentials
- **Project Dashboard**: Quick overview of submitted projects and statistics
- **Project Submission**: Comprehensive form to submit project details
- **Novelty Analysis**: AI-powered analysis of project novelty with sample results
- **Novelty Suggestions**: Get personalized recommendations to enhance your project
- **Project Management**: View and manage all submitted projects
- **Professional UI**: Clean, modern, responsive design

## 📋 Application Flow

1. **Login Page** - Student authentication
2. **Dashboard** - Project overview and navigation
3. **Project Submission** - Enter project details
4. **Analysis** - Backend analysis with loading state
5. **Novelty Results** - Main page showing analysis results (similar projects, suggestions, gaps)
6. **Select & Save** - Confirm project with selected novelty idea
7. **My Projects** - View all submitted projects
8. **Project Details** - Complete project information and analysis

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Installation Steps

1. **Navigate to the project directory:**
   ```bash
   cd project-novelty-detector
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Running the Application

```bash
streamlit run app.py
```

The application will start on `http://localhost:8501`

Both `app.py` and `app_single_file.py` use the demo accounts below without
connecting to MySQL. Email and username ignore surrounding spaces and
capitalization; passwords must match exactly. If these credentials are rejected,
restart Streamlit from this project directory and re-enter the password.

After login, use **Dashboard**, **My Projects**, or **Create New Project** in
the sidebar. **View Full Details** opens project information from the dashboard
or project list. The files under `pages/` are view helpers rendered by `app.py`;
launch the application with the command above, rather than running those files.
If an older sidebar is still displayed after updating, restart Streamlit and open
`http://localhost:8501` without a page suffix.

## 📝 Demo Credentials

### Student 1
- **Email:** john@university.edu
- **Username:** john_doe
- **Password:** password123

### Student 2
- **Email:** jane@university.edu
- **Username:** jane_smith
- **Password:** password123

## 📁 Project Structure

```
project-novelty-detector/
├── app.py                          # Main application entry point
├── requirements.txt                # Project dependencies
├── README.md                       # This file
│
├── pages/                          # Page components
│   ├── __init__.py
│   ├── login.py                    # Login page
│   ├── dashboard.py                # Student dashboard
│   ├── project_submission.py       # Project submission form
│   ├── analysis.py                 # Analysis page with loading
│   ├── novelty_results.py          # Main results page (MAIN PAGE)
│   ├── select_novelty.py           # Select & save page
│   ├── my_projects.py              # Projects list
│   └── project_details.py          # Project detail view
│
├── utils/                          # Utility modules
│   ├── __init__.py
│   ├── session_manager.py          # Session state management
│   └── ui_helpers.py               # UI styling and components
│
└── data/                           # Data and sample data
    ├── __init__.py
    └── sample_data.py              # Dummy/sample data
```

## 🎨 UI Features

- **Responsive Design**: Works on desktop and tablet
- **Professional Color Scheme**: Blue-based design with good contrast
- **Custom Styling**: CSS for cards, buttons, badges, and status indicators
- **Interactive Components**: Tabs, forms, buttons with smooth interactions
- **Status Indicators**: Visual badges for project status and metrics

## 💾 Data Management

Currently uses dummy/sample data stored in `data/sample_data.py`. The application is designed to easily connect to a backend:

### For Backend Integration:
1. Replace `authenticate_user()` in `utils/session_manager.py` with API calls
2. Replace sample data with database queries
3. Add API calls to `novelty_results.py` for analysis results
4. Implement project saving with database operations

## 🔄 Navigation

The application uses Streamlit's session state for navigation:
- `st.session_state.logged_in` - User authentication status
- `st.session_state.current_page` - Current page
- `st.session_state.project_form_data` - Form data during submission
- `st.session_state.analysis_results` - Analysis results
- `st.session_state.selected_novelty` - Selected novelty idea

## 📊 Sample Data Included

- **Students**: 2 sample students with login credentials
- **Projects**: Sample submitted projects with different statuses
- **Similar Projects**: Mock similarity analysis results
- **Novelty Ideas**: 5 different novelty suggestions
- **Technology Stack**: Common technologies used in ML/AI projects
- **Limitations & Gaps**: Common limitations and research gaps

## 🔐 Security Notes

⚠️ **Important**: This is a frontend prototype with hardcoded sample credentials. For production:
- Implement proper backend authentication (JWT, OAuth, etc.)
- Use secure password hashing
- Implement session management on the backend
- Add HTTPS/SSL encryption
- Validate all user inputs on the backend

## 🚀 Future Enhancements

- [ ] Backend API integration
- [ ] MySQL database connection
- [ ] Real similarity algorithm implementation
- [ ] User profile management
- [ ] Project editing and deletion
- [ ] Export project reports
- [ ] Email notifications
- [ ] Advanced search and filtering
- [ ] Collaborative features

## 📞 Support

For issues or questions, please refer to the code documentation or contact your development team.

## 📄 License

This project is part of the Research Project Novelty Detector system.

---

**Created**: September 2024
**Frontend Framework**: Streamlit
**Status**: Development/Prototype
