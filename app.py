"""
Udaipur Local Guide AI - Main Application

A lightweight AI tool that provides culturally-aware assistance to tourists
and locals in Udaipur by leveraging local knowledge from a product.md context file.
"""

from src.context_loader import ContextLoader
from src.query_processor import QueryProcessor
from src.response_generator import ResponseGenerator


def local_guide(query: str) -> str:
    """
    Main function to process user queries and provide Udaipur-specific responses.
    
    Orchestrates the interaction between context loader, query processor, and response generator
    to deliver culturally-aware assistance based on local knowledge from product.md.
    
    Args:
        query: User's input query string
        
    Returns:
        Contextually relevant response based on local knowledge
        
    Implements Requirements 5.1, 5.4:
    - Processes user input and provides relevant responses within reasonable time
    - Formats responses in a clear and readable manner
    """
    # Input validation
    if not query or not isinstance(query, str):
        return "Please provide a valid question about Udaipur's culture, food, language, or tourist information."
    
    # Normalize input
    query = query.strip()
    if not query:
        return "Please enter a question about local culture, food recommendations, language phrases, or tourist information."
    
    try:
        # Initialize components with error handling
        context_loader = ContextLoader()
        query_processor = QueryProcessor()
        response_generator = ResponseGenerator()
        
        # Load context data with specific error handling
        try:
            context = context_loader.load_context()
        except FileNotFoundError:
            return "I'm sorry, I can't access the local knowledge base right now. Please ensure the product.md file is available and try again."
        except ValueError as e:
            return f"There's an issue with the local knowledge base: {str(e)}. Please check the product.md file format."
        
        # Process the query with error handling
        try:
            intent = query_processor.process_query(query)
        except Exception as e:
            return "I had trouble understanding your question. Could you please rephrase it? I can help with local phrases, food recommendations, tourist information, or cultural guidance."
        
        # Generate response with error handling
        try:
            response = response_generator.generate_response(intent, context)
            
            # Ensure response is properly formatted and not empty
            if not response or not response.strip():
                return "I'm not sure how to help with that specific question. Try asking about local greetings like 'Khamma Ghani', food recommendations for specific areas, crowd timing at tourist spots, or cultural etiquette guidance."
            
            return response.strip()
            
        except Exception as e:
            return "I encountered an issue generating a response. Please try rephrasing your question or ask about local language, food, tourism, or cultural topics."
        
    except Exception as e:
        # Fallback error handling with helpful guidance
        return "I'm experiencing technical difficulties. Please try asking about: local phrases and greetings, authentic food recommendations, tourist crowd timing, or cultural etiquette guidance."


def main():
    """
    Main entry point for interactive usage.
    
    Provides a user-friendly interface for interacting with the Udaipur Local Guide AI,
    with proper error handling and graceful exit options.
    
    Implements Requirements 5.1, 5.4:
    - Handles user input/output in a clear and readable manner
    - Provides component coordination through the local_guide function
    """
    print("🏰 Welcome to the Udaipur Local Guide AI! 🏰")
    print("I can help you with:")
    print("  • Local phrases and greetings (like 'Khamma Ghani')")
    print("  • Authentic food recommendations and locations")
    print("  • Tourist crowd timing and transportation advice")
    print("  • Cultural etiquette for temples and palaces")
    print("\nType 'quit', 'exit', or 'bye' to exit.")
    print("=" * 50)
    
    while True:
        try:
            # Get user input with clear prompt
            user_input = input("\n🤔 Ask me about Udaipur: ").strip()
            
            # Handle exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print("\n🙏 Thank you for using the Udaipur Local Guide AI!")
                print("Khamma Ghani! (Traditional farewell)")
                break
            
            # Handle empty input
            if not user_input:
                print("💭 Please enter a question, or type 'quit' to exit.")
                print("   Try asking: 'What does Khamma Ghani mean?' or 'Best food in Surajpole?'")
                continue
            
            # Handle help requests
            if user_input.lower() in ['help', 'h', '?']:
                print("\n📚 I can help you with:")
                print("  • Language: 'What does Khamma Ghani mean?'")
                print("  • Food: 'Best food in Hathipole?' or 'What is Dal Baati Churma?'")
                print("  • Tourism: 'When to visit City Palace?' or 'Transportation to heritage areas?'")
                print("  • Culture: 'Temple etiquette?' or 'How to greet locals respectfully?'")
                continue
            
            # Process the query and display response
            print("\n🤖 Guide:", end=" ")
            response = local_guide(user_input)
            print(response)
            
            # Add separator for readability
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\n\n🙏 Thank you for using the Udaipur Local Guide AI!")
            print("Khamma Ghani! (Traditional farewell)")
            break
        except EOFError:
            print("\n\n🙏 Thank you for using the Udaipur Local Guide AI!")
            print("Khamma Ghani! (Traditional farewell)")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {str(e)}")
            print("💡 Please try again or type 'quit' to exit.")
            continue


if __name__ == "__main__":
    main()