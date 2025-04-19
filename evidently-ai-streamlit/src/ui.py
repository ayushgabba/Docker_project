import streamlit as st
import os

def display_sidebar_header():
    st.sidebar.title("🧭 Evidently Dashboard")
    st.sidebar.markdown("---")

def select_project():
    projects_path = "projects"
    projects = [p for p in os.listdir(projects_path) if os.path.isdir(os.path.join(projects_path, p))]
    return st.sidebar.selectbox("📁 Select Project", projects) if projects else None

def select_period(project):
    reports_path = os.path.join("projects", project, "reports")
    periods = [f for f in os.listdir(reports_path) if f.endswith(".html")]
    return st.sidebar.selectbox("🕒 Select Report", periods) if periods else None

def select_report(project, period):
    if project and period:
        return os.path.join("projects", project, "reports", period)
    return None

def display_report(report_path):
    with open(report_path, "r", encoding="utf-8") as f:
        report_html = f.read()
        st.components.v1.html(report_html, height=800, scrolling=True)
