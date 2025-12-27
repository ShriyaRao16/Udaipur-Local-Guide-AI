#!/usr/bin/env python3
"""
Test script to verify tourism and traffic response functionality.
"""

from src.response_generator import ResponseGenerator
from src.query_processor import QueryIntent

def test_tourism_responses():
    """Test various tourism and traffic related queries."""
    generator = ResponseGenerator()
    
    # Sample context data matching product.md
    context = {
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
    
    # Test cases for tourism and traffic responses
    test_cases = [
        # Crowd estimation queries (Requirement 3.1)
        {
            "description": "Crowd estimation - general",
            "intent": QueryIntent(
                category="tourism",
                keywords=["crowd", "busy"],
                location=None,
                time_context=None
            )
        },
        {
            "description": "Crowd estimation - City Palace",
            "intent": QueryIntent(
                category="tourism", 
                keywords=["crowd", "congestion"],
                location="City Palace",
                time_context=None
            )
        },
        {
            "description": "Crowd estimation - Lake Pichola",
            "intent": QueryIntent(
                category="tourism",
                keywords=["tourist", "crowded"],
                location="Lake Pichola", 
                time_context=None
            )
        },
        
        # Transportation recommendations (Requirement 3.3)
        {
            "description": "Transportation - heritage areas",
            "intent": QueryIntent(
                category="tourism",
                keywords=["transportation", "heritage"],
                location=None,
                time_context=None
            )
        },
        {
            "description": "Transportation - City Palace",
            "intent": QueryIntent(
                category="tourism",
                keywords=["transport", "vehicle"],
                location="City Palace",
                time_context=None
            )
        },
        {
            "description": "Transportation - traffic",
            "intent": QueryIntent(
                category="tourism",
                keywords=["traffic", "bike", "car"],
                location=None,
                time_context=None
            )
        },
        
        # Timing suggestions (Requirement 3.4)
        {
            "description": "Timing - best visit time",
            "intent": QueryIntent(
                category="tourism",
                keywords=["timing", "best", "visit"],
                location=None,
                time_context=None
            )
        },
        {
            "description": "Timing - City Palace optimal",
            "intent": QueryIntent(
                category="tourism",
                keywords=["when", "optimal", "avoid"],
                location="City Palace",
                time_context=None
            )
        },
        
        # Seasonal information (Requirement 3.5)
        {
            "description": "Seasonal - peak season",
            "intent": QueryIntent(
                category="tourism",
                keywords=["season", "peak", "october"],
                location=None,
                time_context=None
            )
        },
        {
            "description": "Seasonal - weather timing",
            "intent": QueryIntent(
                category="tourism",
                keywords=["seasonal", "march", "weather"],
                location=None,
                time_context=None
            )
        }
    ]
    
    print("Testing Tourism and Traffic Response Implementation")
    print("=" * 60)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{i}. {test_case['description']}")
        print(f"   Intent: {test_case['intent']}")
        
        response = generator.generate_response(test_case['intent'], context)
        print(f"   Response: {response}")
        print("-" * 50)

if __name__ == "__main__":
    test_tourism_responses()