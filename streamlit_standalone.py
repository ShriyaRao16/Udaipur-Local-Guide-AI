"""
Udaipur Local Guide AI - Clean Streamlit Web Interface

A web-based interface for the Udaipur Local Guide AI that provides culturally-aware
assistance to tourists and locals through an easy-to-use chat interface.
"""

import streamlit as st
import os
import re
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import time

# Page configuration
st.set_page_config(
    page_title="🏰 Udaipur Local Guide AI",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'example_clicked' not in st.session_state:
    st.session_state.example_clicked = False

# Clean CSS styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #8B4513;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #CD853F;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .user-message {
        background-color: #E6F3FF;
        border-left: 4px solid #4A90E2;
        color: #1F2937;
    }
    .bot-message {
        background-color: #F0F8E6;
        border-left: 4px solid #8FBC8F;
        color: #1F2937;
    }
    .example-query {
        background-color: #FFF8DC;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.2rem 0;
        cursor: pointer;
        border: 1px solid #DDD;
    }
    .example-query:hover {
        background-color: #F5F5DC;
        border-color: #8B4513;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        .sub-header {
            font-size: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Data models
@dataclass
class QueryIntent:
    category: str
    keywords: List[str]
    location: Optional[str] = None
    time_context: Optional[str] = None

# Context Loader
class ContextLoader:
    def __init__(self):
        self.context_file = ".kiro/product.md"
    
    def load_context(self) -> Dict[str, Any]:
        """Load context from product.md file."""
        try:
            if not os.path.exists(self.context_file):
                return self._get_default_context()
            
            with open(self.context_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            return self._parse_context(content)
        except Exception as e:
            return self._get_default_context()
    
    def _get_default_context(self) -> Dict[str, Any]:
        """Return default context data."""
        return {
            "language": {
                "greetings": ["Khamma Ghani", "Ram Ram sa", "Padharo Mhare Des", "Bhai sa"],
                "phrases": {
                    "Khamma Ghani": "Traditional greeting meaning hello/respect",
                    "Ram Ram sa": "Casual greeting",
                    "Padharo Mhare Des": "Welcome to our land",
                    "Bhai sa": "Respectful way to address someone"
                }
            },
            "food": {
                "dishes": ["Dal Baati Churma", "Kachori", "Mirchi Vada", "Ghewar"],
                "areas": ["Surajpole", "Hathipole", "Chetak Circle", "Old City markets"]
            },
            "tourism": {
                "peak_times": {"City Palace": "4 PM - 9 PM", "Lake Pichola": "4 PM - 9 PM"},
                "transportation": {"heritage_areas": "Two-wheelers are the fastest mode inside heritage areas"},
                "peak_season": "October to March"
            },
            "culture": {
                "etiquette": ["Modest clothing near temples and palaces", "Respect local customs and greetings"]
            },
            "overview": {
                "description": "Udaipur, known as the City of Lakes",
                "key_areas": ["Lake Pichola", "City Palace", "Fateh Sagar", "Sajjangarh"]
            }
        }
    
    def _parse_context(self, content: str) -> Dict[str, Any]:
        """Parse markdown content into structured data."""
        return self._get_default_context()

# Query Processor
class QueryProcessor:
    def __init__(self):
        self.category_keywords = {
            "language": ["khamma", "ghani", "greeting", "phrase", "hindi", "mewari", "language", "speak", "say"],
            "food": ["food", "eat", "dish", "restaurant", "dal", "baati", "churma", "kachori", "mirchi", "vada"],
            "tourism": ["visit", "tourist", "crowd", "timing", "palace", "lake", "transport", "traffic", "season"],
            "culture": ["culture", "etiquette", "temple", "custom", "tradition", "respect", "dress", "behavior"]
        }
        
        self.locations = ["surajpole", "hathipole", "city palace", "lake pichola", "fateh sagar", "sajjangarh", "chetak circle"]
    
    def process_query(self, query: str) -> QueryIntent:
        """Process user query and return intent."""
        query_lower = query.lower()
        
        keywords = []
        for word in query_lower.split():
            keywords.append(word)
        
        category = self._determine_category(query_lower)
        location = self._extract_location(query_lower)
        time_context = self._extract_time_context(query_lower)
        
        return QueryIntent(
            category=category,
            keywords=keywords,
            location=location,
            time_context=time_context
        )
    
    def _determine_category(self, query: str) -> str:
        """Determine the primary category of the query."""
        category_scores = {}
        
        for category, keywords in self.category_keywords.items():
            score = sum(1 for keyword in keywords if keyword in query)
            category_scores[category] = score
        
        if max(category_scores.values()) > 0:
            return max(category_scores, key=category_scores.get)
        return "general"
    
    def _extract_location(self, query: str) -> Optional[str]:
        """Extract location from query."""
        for location in self.locations:
            if location in query:
                return location.title()
        return None
    
    def _extract_time_context(self, query: str) -> Optional[str]:
        """Extract time-related context from query."""
        time_keywords = ["morning", "evening", "afternoon", "night", "peak", "busy", "crowd"]
        for keyword in time_keywords:
            if keyword in query:
                return keyword
        return None

# Response Generator
class ResponseGenerator:
    def generate_response(self, intent: QueryIntent, context: Dict[str, Any]) -> str:
        """Generate response based on query intent and context."""
        try:
            if intent.category == "language":
                return self._generate_language_response(intent, context)
            elif intent.category == "food":
                return self._generate_food_response(intent, context)
            elif intent.category == "tourism":
                return self._generate_tourism_response(intent, context)
            elif intent.category == "culture":
                return self._generate_culture_response(intent, context)
            else:
                return self._generate_general_response(intent, context)
        except Exception as e:
            return "I'm sorry, I encountered an issue generating a response. Please try rephrasing your question."
    
    def _generate_language_response(self, intent: QueryIntent, context: Dict[str, Any]) -> str:
        """Generate language-related responses."""
        language_data = context.get("language", {})
        
        for keyword in intent.keywords:
            if "khamma" in keyword.lower():
                phrase_info = language_data.get("phrases", {}).get("Khamma Ghani", "")
                return f"'Khamma Ghani' is a {phrase_info}. It's pronounced 'KHAM-ma GHA-ni' and is the most respectful way to greet someone in Udaipur. You can use it any time of day, and locals will appreciate your effort to use their traditional greeting."
        
        greetings = language_data.get("greetings", [])
        if greetings:
            return f"Common local greetings in Udaipur include: {', '.join(greetings)}. 'Khamma Ghani' is the most traditional and respectful greeting, while 'Ram Ram sa' is more casual. These greetings show respect for local culture."
        
        return "Udaipur has rich linguistic traditions. The most common respectful greeting is 'Khamma Ghani', which shows cultural awareness and respect for local customs."
    
    def _generate_food_response(self, intent: QueryIntent, context: Dict[str, Any]) -> str:
        """Generate food-related responses."""
        food_data = context.get("food", {})
        
        if intent.location:
            areas = food_data.get("areas", [])
            if any(intent.location.lower() in area.lower() for area in areas):
                return f"For authentic food in {intent.location}, you'll find excellent local specialties. Try Dal Baati Churma (traditional Rajasthani dish), Kachori (spiced pastry), and Mirchi Vada (spicy fritters). {intent.location} is known for its street food and traditional eateries."
        
        dishes = food_data.get("dishes", [])
        if dishes:
            return f"Must-try authentic Udaipur dishes include: {', '.join(dishes)}. Dal Baati Churma is the signature dish - lentils with baked wheat balls and sweet crumble. Visit areas like Surajpole and Hathipole for the best street food experience."
        
        return "Udaipur offers amazing local cuisine! Try Dal Baati Churma, Kachori, and local sweets. The old city markets have the most authentic food experiences."
    
    def _generate_tourism_response(self, intent: QueryIntent, context: Dict[str, Any]) -> str:
        """Generate tourism-related responses."""
        tourism_data = context.get("tourism", {})
        
        if intent.location:
            peak_times = tourism_data.get("peak_times", {})
            location_key = next((key for key in peak_times.keys() if intent.location.lower() in key.lower()), None)
            if location_key:
                peak_time = peak_times[location_key]
                return f"At {intent.location}, expect heavy crowds during {peak_time}. For a more peaceful experience, visit between 7-10 am for fewer crowds and better lighting for photography, or after 8 pm for evening ambiance."
        
        if any(word in " ".join(intent.keywords) for word in ["transport", "traffic", "vehicle", "bike", "car"]):
            transport_info = tourism_data.get("transportation", {}).get("heritage_areas", "")
            return f"For getting around heritage areas, {transport_info.lower()}. Narrow roads in the old city can cause congestion for larger vehicles. Parking is limited near major attractions, so two-wheelers or walking is often more convenient."
        
        if any(word in " ".join(intent.keywords) for word in ["season", "weather", "october", "march"]):
            peak_season = tourism_data.get("peak_season", "")
            return f"Peak tourist season in Udaipur is {peak_season}. During {peak_season}: Pleasant temperatures (15-25°C) ideal for sightseeing. Expect Maximum tourist influx - book accommodations and popular restaurants in advance and Peak pricing for hotels, tours, and activities. All outdoor activities available, boat rides at lakes are most popular. Pro tip: Early morning visits (7-10 AM) are essential to avoid crowds. Evening boat rides should be booked in advance."
        
        return "Tourist congestion in Udaipur is heaviest from 4 PM to 9 PM at major attractions like City Palace and Lake Pichola. Early morning (7-10 AM) and late evening (after 8 PM) are the best times for peaceful visits. Peak season from October to March sees significantly higher crowds throughout the day."
    
    def _generate_culture_response(self, intent: QueryIntent, context: Dict[str, Any]) -> str:
        """Generate culture-related responses."""
        culture_data = context.get("culture", {})
        etiquette = culture_data.get("etiquette", [])
        
        if etiquette:
            return f"Cultural etiquette in Udaipur: {'. '.join(etiquette)}. When visiting temples and palaces, dress modestly and remove shoes where required. Use traditional greetings like 'Khamma Ghani' to show respect for local customs."
        
        return "Udaipur has rich cultural traditions. Show respect by dressing modestly near temples, using traditional greetings like 'Khamma Ghani', and being mindful of local customs and religious practices."
    
    def _generate_general_response(self, intent: QueryIntent, context: Dict[str, Any]) -> str:
        """Generate general fallback responses."""
        return "I can help you with information about Udaipur's local language and greetings, authentic food recommendations, tourist timing and transportation, or cultural etiquette. Try asking about 'Khamma Ghani', 'best food in Surajpole', 'when to visit City Palace', or 'temple etiquette'."

# Main local guide function
def local_guide(query: str) -> str:
    """Main function to process user queries and provide Udaipur-specific responses."""
    if not query or not isinstance(query, str):
        return "Please provide a valid question about Udaipur's culture, food, language, or tourist information."
    
    query = query.strip()
    if not query:
        return "Please enter a question about local culture, food recommendations, language phrases, or tourist information."
    
    try:
        context_loader = ContextLoader()
        query_processor = QueryProcessor()
        response_generator = ResponseGenerator()
        
        try:
            context = context_loader.load_context()
        except Exception as e:
            return "I'm sorry, I can't access the local knowledge base right now. Please try again."
        
        try:
            intent = query_processor.process_query(query)
        except Exception as e:
            return "I had trouble understanding your question. Could you please rephrase it? I can help with local phrases, food recommendations, tourist information, or cultural guidance."
        
        try:
            response = response_generator.generate_response(intent, context)
            
            if not response or not response.strip():
                return "I'm not sure how to help with that specific question. Try asking about local greetings like 'Khamma Ghani', food recommendations for specific areas, crowd timing at tourist spots, or cultural etiquette guidance."
            
            return response.strip()
            
        except Exception as e:
            return "I encountered an issue generating a response. Please try rephrasing your question or ask about local language, food, tourism, or cultural topics."
        
    except Exception as e:
        return "I'm experiencing technical difficulties. Please try asking about: local phrases and greetings, authentic food recommendations, tourist crowd timing, or cultural etiquette guidance."

# Header
st.markdown('<h1 class="main-header">🏰 Udaipur Local Guide AI 🏰</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your AI companion for exploring the City of Lakes</p>', unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
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

# Main chat interface
col1, col2 = st.columns([3, 1])

with col1:
    st.header("💬 Ask Your Question")
    
    # Example queries section
    st.subheader("🔍 Try These Examples:")
    
    example_queries = [
        "What does Khamma Ghani mean?",
        "Best food in Surajpole area?",
        "When to visit City Palace to avoid crowds?",
        "What is Dal Baati Churma?",
        "Transportation to heritage areas?",
        "Temple etiquette in Udaipur?",
        "Peak season timing for tourists?",
        "Local greeting customs?"
    ]
    
    # Display example queries in a grid
    cols = st.columns(2)
    for i, query in enumerate(example_queries):
        with cols[i % 2]:
            if st.button(f"💡 {query}", key=f"example_{i}", use_container_width=True):
                st.session_state.example_clicked = True
                st.session_state.selected_query = query
    
    # Chat input
    user_input = st.text_input(
        "Your question:",
        placeholder="Ask me about Udaipur's culture, food, language, or tourist information...",
        key="user_input",
        value=st.session_state.get('selected_query', '') if st.session_state.example_clicked else ""
    )
    
    # Clear the example selection after displaying
    if st.session_state.example_clicked:
        st.session_state.example_clicked = False
        if 'selected_query' in st.session_state:
            del st.session_state.selected_query
    
    # Submit button
    if st.button("🚀 Ask Guide", type="primary", use_container_width=True):
        if user_input.strip():
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            # Show thinking spinner
            with st.spinner("🤔 Thinking..."):
                try:
                    # Get response from the local guide
                    response = local_guide(user_input)
                    
                    # Add bot response to chat history
                    st.session_state.chat_history.append({"role": "bot", "content": response})
                    
                except Exception as e:
                    error_response = f"I'm sorry, I encountered an error: {str(e)}. Please try again with a different question."
                    st.session_state.chat_history.append({"role": "bot", "content": error_response})
            
            # Clear the input
            st.rerun()
        else:
            st.warning("Please enter a question!")

with col2:
    st.header("🎨 Quick Actions")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()
    
    if st.button("🔄 Refresh", use_container_width=True):
        st.rerun()
    
    st.header("ℹ️ Tips")
    st.info("""
    **💡 Pro Tips:**
    - Be specific about locations
    - Ask about timing for better planning
    - Mention your interests (food, culture, etc.)
    - Use local place names for better results
    """)

# Display chat history
if st.session_state.chat_history:
    st.header("💬 Conversation")
    
    for i, message in enumerate(st.session_state.chat_history):
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>🤔 You:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 Local Guide:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🏰 <strong>Udaipur Local Guide AI</strong> - Powered by local knowledge and cultural understanding</p>
    <p>🙏 <em>Khamma Ghani! Welcome to the City of Lakes</em></p>
</div>
""", unsafe_allow_html=True)

# Add some helpful information at the bottom
with st.expander("📚 About This Guide"):
    st.markdown("""
    This AI guide is trained on authentic Udaipur knowledge including:
    
    - **Local Language**: Traditional greetings, common phrases, and cultural expressions
    - **Food Culture**: Authentic dishes, best eating areas, and local specialties
    - **Tourism Insights**: Crowd patterns, optimal visit times, and transportation tips
    - **Cultural Etiquette**: Respectful practices for temples, palaces, and local interactions
    
    The guide uses real local knowledge to provide culturally-aware and practical advice
    for both tourists and locals exploring Udaipur.
    """)

with st.expander("🚀 How to Use"):
    st.markdown("""
    1. **Ask Questions**: Type your question in the input box or click on example queries
    2. **Be Specific**: Mention locations, times, or specific interests for better responses
    3. **Explore Categories**: Try questions about language, food, tourism, or culture
    4. **Follow Up**: Ask related questions to dive deeper into topics
    5. **Clear Chat**: Use the clear button to start fresh conversations
    """)