import streamlit as st
from vanilla_steel.config import logger, settings
from vanilla_steel.database.queries import fetch_stats

@st.cache_data
def fetch_all_stats():
    logger.info("Fetching stats ... ")
    all_stats = fetch_stats()
    return all_stats

def main():
    st.set_page_config(
        page_title="Vanilla Steel",
        page_icon=":rocket:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.header('Dashboard', divider='red')
    st.subheader(settings.DOCS.TITLE)
    st.sidebar.page_link("http://localhost:8000", label="Documentation", icon="📒", help="Sphinx Documentation - Please run the server separately as mentioned in the README.md file")
    st.sidebar.page_link("http://localhost:5000", label="Database", icon="📦", help="PG Admin")
    
    if 'stats' not in st.session_state:
        st.write("Basic statistics from all the materials present in the vanilla steel database")
        st.session_state['stats'] = fetch_all_stats()
    
    col1, col2, col3 = st.columns(3)

    with col1:
        col1.metric(label="Total Count", value=st.session_state['stats']['total_count'])
        col1.metric(label="Annealed", value=st.session_state['stats']['annealed'])
        col1.metric(label="Ductile", value=st.session_state['stats']['ductile'])

    with col2:
        col2.metric(label="Damaged", value=st.session_state['stats']['damaged'])
        col2.metric(label="Oiled", value=st.session_state['stats']['oiled'])
    
    with col3:
        col3.metric(label="Pickled", value=st.session_state['stats']['pickled'])
        col3.metric(label="Zinc Coated", value=st.session_state['stats']['zinc_coated'])

if __name__ == "__main__":
    main()