# Udaipur Local Guide AI 🏰

A lightweight AI tool that provides culturally-aware assistance to tourists and locals in Udaipur. The system leverages a custom `product.md` context file containing local knowledge about Udaipur's culture, food, language, and tourist patterns to deliver contextually relevant responses.

## Features

- **Local Language Support**: Understand and explain local greetings, phrases, and Hindi-Mewari expressions
- **Food Recommendations**: Get authentic street food and café suggestions with location-specific guidance
- **Tourist Intelligence**: Access crowd estimates, traffic conditions, and optimal timing for heritage sites
- **Cultural Guidance**: Learn about local customs, etiquette, and respectful interaction practices
- **Context-Aware Responses**: All information is grounded in local knowledge from the `product.md` context file

## How product.md Context File is Utilized

The system's intelligence comes from the `.kiro/product.md` file, which contains structured information about:

- **Local Language & Slang**: Traditional greetings like "Khamma Ghani", casual phrases, and their cultural significance
- **Food Culture**: Popular dishes (Dal Baati Churma, Kachori), famous food areas (Surajpole, Hathipole)
- **Traffic & Tourist Patterns**: Peak crowd times, transportation recommendations, seasonal guidance
- **Cultural Etiquette**: Temple protocols, dress codes, and respectful interaction guidelines

The context loader reads this file at startup, and the response generator references appropriate sections based on query analysis to ensure all responses are culturally accurate and locally relevant.

## Project Structure

```
udaipur-local-guide/
├── app.py                    # Main application entry point
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── .kiro/
│   └── product.md           # Local knowledge context file
├── src/                     # Source code modules
│   ├── __init__.py
│   ├── context_loader.py    # Loads and parses product.md
│   ├── query_processor.py   # Analyzes user queries and extracts intent
│   └── response_generator.py # Generates culturally-aware responses
└── tests/                   # Test files with unit and property-based tests
    ├── __init__.py
    ├── test_context_loader.py
    ├── test_query_processor.py
    ├── test_response_generator.py
    └── test_integration.py
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone or download the project** to your local machine

2. **Create a virtual environment**:
```bash
python -m venv venv
```

3. **Activate the virtual environment**:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

5. **Verify installation** by running tests:
```bash
python -m pytest tests/
```

## Usage

### Web Interface (Recommended)

Run the Streamlit web application for an interactive web interface:
```bash
streamlit run streamlit_app.py
```

This opens a user-friendly web interface in your browser where you can:
- Ask questions through a chat interface
- Click on example queries to get started quickly
- View helpful tips and location information in the sidebar
- Clear chat history and refresh as needed

### Command Line Interface

Run the application for interactive terminal queries:
```bash
python app.py
```

This starts an interactive session where you can ask questions about Udaipur. Type 'quit', 'exit', or 'bye' to exit.

### Programmatic Usage

You can also use the `local_guide()` function directly in your code:

```python
from app import local_guide

# Ask about local greetings
response = local_guide("What does Khamma Ghani mean?")
print(response)

# Get food recommendations
response = local_guide("Best food in Surajpole?")
print(response)

# Check tourist timing
response = local_guide("When to visit City Palace?")
print(response)
```

## Deployment

### Streamlit Cloud Deployment

1. **Push to GitHub**: Ensure your repository is on GitHub with all files
2. **Visit Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io)
3. **Connect Repository**: Link your GitHub repository
4. **Set Main File**: Use `streamlit_app.py` as the main file path
5. **Deploy**: Click deploy and your app will be live!

### Local Streamlit Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run streamlit_app.py
```

### Other Deployment Options

The application can also be deployed on:
- **Heroku**: Add a `Procfile` with `web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`
- **Railway**: Use the `streamlit_app.py` as the main file
- **Render**: Configure with `streamlit run streamlit_app.py` as the start command

## Example Queries and Expected Responses

### Language and Culture Queries

**Query**: "What does Khamma Ghani mean?"
**Expected Response**: Explanation of the traditional greeting, its cultural significance, and appropriate usage context.

**Query**: "How should I greet locals respectfully?"
**Expected Response**: Information about "Khamma Ghani", "Ram Ram sa", and cultural context for respectful interaction.

**Query**: "Temple etiquette in Udaipur?"
**Expected Response**: Guidance on modest clothing, respectful behavior, and local customs near temples and palaces.

### Food Recommendation Queries

**Query**: "Best food in Hathipole?"
**Expected Response**: Area-specific food recommendations based on the context file's food culture data.

**Query**: "What is Dal Baati Churma?"
**Expected Response**: Description of the traditional dish with cultural context and preparation details.

**Query**: "Authentic street food recommendations?"
**Expected Response**: List of local specialties like Kachori, Mirchi Vada, and Ghewar with location information.

### Tourism and Traffic Queries

**Query**: "When to visit City Palace?"
**Expected Response**: Information about peak crowd times (4 PM - 9 PM) and suggestions for optimal visit timing.

**Query**: "Transportation to heritage areas?"
**Expected Response**: Recommendation for two-wheelers as the fastest mode in heritage areas, with traffic considerations.

**Query**: "Best time to visit Udaipur?"
**Expected Response**: Peak season guidance (October to March) with seasonal context.

### Multi-Category Queries

**Query**: "Food and culture near Lake Pichola?"
**Expected Response**: Combined information about nearby food options and cultural etiquette for the area.

## Error Handling

The system provides graceful error handling for various scenarios:

- **Missing context file**: Clear error message with guidance for ensuring `product.md` availability
- **Corrupted context data**: Specific parsing error information with fallback responses
- **Unclear queries**: Helpful guidance on available topics and query reformulation suggestions
- **No matching patterns**: Alternative query suggestions and available topic areas

## Testing

The project includes comprehensive testing with both unit tests and property-based tests:

### Run All Tests
```bash
python -m pytest tests/
```

### Run Specific Test Categories
```bash
# Unit tests only
python -m pytest tests/ -k "not property"

# Property-based tests only
python -m pytest tests/ -k "property"
```

### Test Coverage
- **Unit Tests**: Verify specific functionality like "Khamma Ghani" explanations, error handling, and component integration
- **Property-Based Tests**: Validate universal properties across all inputs using the Hypothesis library
- **Integration Tests**: Test end-to-end query processing workflows

## Development

### Adding New Context Information

To extend the system's knowledge:

1. Edit `.kiro/product.md` with new information
2. Follow the existing structure (Language, Food Culture, Traffic & Tourist Nuances, Cultural Etiquette)
3. The system will automatically reflect changes in subsequent responses

### Modifying Response Logic

The response generation logic is in `src/response_generator.py`. Key areas:

- **Category Detection**: Modify keyword matching in `src/query_processor.py`
- **Response Templates**: Update response formatting in `ResponseGenerator` class
- **Context Integration**: Adjust how context data is referenced in responses

## Contributing

1. Ensure all tests pass before submitting changes
2. Add appropriate unit tests for new functionality
3. Update the `product.md` context file if adding new local knowledge
4. Follow the existing code structure and documentation patterns

## License

This project is designed for educational and local assistance purposes. Please respect local customs and use the cultural information responsibly.