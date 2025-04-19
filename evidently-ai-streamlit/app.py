import streamlit as st
from src.ui import display_sidebar_header, select_project, select_period, select_report, display_report

# Set page config
st.set_page_config(
    page_title="Evidently AI Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar UI
display_sidebar_header()

# Main App Logic
st.title("📊 Evidently AI Streamlit Dashboard")

# Step 1: Select a project
project = select_project()

if project:
    # Step 2: Select a report period
    period = select_period(project)

    # Step 3: Select a report
    report_path = select_report(project, period)

    # Step 4: Display the report
    if report_path:
        display_report(report_path)
    else:
        st.warning("⚠️ No reports found in this project.")
else:
    st.info("📁 Please select a valid project to continue.")
