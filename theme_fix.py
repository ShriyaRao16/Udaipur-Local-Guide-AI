# Quick fix for the theme toggle
# Copy this code and replace the sidebar section in your streamlit_standalone.py

# Sidebar with information
with st.sidebar:
    st.header("🎨 Theme Settings")
    
    # Theme toggle
    theme_choice = st.radio(
        "Choose Theme:",
        ["🌞 Light Mode", "🌙 Dark Mode"],
        index=1 if st.session_state.dark_mode else 0,
        key="theme_toggle"
    )
    
    # Update theme state and reapply if changed
    new_dark_mode = (theme_choice == "🌙 Dark Mode")
    if new_dark_mode != st.session_state.dark_mode:
        st.session_state.dark_mode = new_dark_mode
        apply_theme()
        st.rerun()
    
    st.header("🎯 What I Can Help With")
    st.markdown("""
    **🗣️ Language & Culture**
    - Local greetings like "Khamma Ghani"
    - Hindi-Mewari phrases
    - Cultural etiquette
    
    **🍽️ Food & Dining**
    - Authentic local dishes
    - Best food areas (Surajpole, Hathipole)
    - Restaurant recommendations
    
    **🏛️ Tourism & Travel**
    - Crowd timing at attractions
    - Transportation advice
    - Best visit times
    
    **🎭 Cultural Guidance**
    - Temple etiquette
    - Local customs
    - Respectful interactions
    """)
    
    st.header("📍 Popular Locations")
    st.markdown("""
    - **City Palace** - Royal architecture
    - **Lake Pichola** - Scenic boat rides
    - **Fateh Sagar** - Evening walks
    - **Sajjangarh** - Sunset views
    - **Surajpole** - Food street
    - **Hathipole** - Local markets
    """)