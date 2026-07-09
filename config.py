"""
Configuration settings for AI Storytelling Application
Modify these values to customize application behavior
"""

# Gemini API Configuration
GEMINI_MODEL = "gemini-2.0-flash-exp"  # Model to use for generation
GEMINI_TEMPERATURE = 0.7  # Controls randomness (0.0 to 1.0)
GEMINI_MAX_TOKENS = 2048  # Maximum tokens in response

# Story Length Definitions (in sentences/lines)
STORY_LENGTH = {
    "Short": {
        "min": 7,
        "max": 8,
        "description": "concise (7-8 sentences)"
    },
    "Medium": {
        "min": 10,
        "max": 12,
        "description": "balanced (10-12 sentences)"
    },
    "Long": {
        "min": 15,
        "max": 20,
        "description": "comprehensive (15-20 sentences)"
    }
}

# Tone Descriptions
TONE_GUIDELINES = {
    "Professional": "Use formal business language with a focus on achievements and measurable outcomes.",
    "Inspirational": "Use motivating and uplifting language that emphasizes personal growth and transformation.",
    "LinkedIn Ready": "Use engaging language suitable for LinkedIn posts with a balance of professionalism and relatability."
}

# UI Configuration
APP_TITLE = "AI Storytelling"
APP_SUBTITLE = "Auto-Generate Personalized Impact Narratives at Scale"
APP_ICON = "📖"

# Color Scheme (Hex colors)
COLORS = {
    "primary": "#3B82F6",      # Blue
    "primary_dark": "#1E40AF",  # Dark Blue
    "secondary": "#64748B",     # Gray
    "light_gray": "#94A3B8",    # Light Gray
    "background": "#FFFFFF",    # White
    "card_bg": "#F8FAFC",       # Light background
}

# Text Area Configuration
TEXT_AREA_HEIGHT = 250  # Height in pixels
TEXT_AREA_PLACEHOLDER = {
    "linkedin": "Paste LinkedIn posts of IAC members here...",
    "internship": "Paste Internship Reviews here...",
    "training": "Paste Industry Training & Certification Reviews here..."
}

# Export Configuration
EXPORT_FILENAME_PREFIX = "impact_story"
EXPORT_DATETIME_FORMAT = "%Y%m%d_%H%M%S"

# Document Styling
DOCX_CONFIG = {
    "title_font_size": 28,
    "subtitle_font_size": 14,
    "body_font_size": 12,
    "meta_font_size": 10,
    "font_name": "Calibri",
    "margin_inches": 1.0
}

PDF_CONFIG = {
    "title_font_size": 24,
    "subtitle_font_size": 12,
    "body_font_size": 11,
    "meta_font_size": 9,
    "margin_points": 72
}

# Validation
MIN_INPUT_LENGTH = 10  # Minimum characters required for valid input
MAX_INPUT_LENGTH = 50000  # Maximum characters to prevent abuse

# Footer Text
FOOTER_TEXT = "Powered by Google Gemini AI | Built for IAC (India Academia Connect)"
COPYRIGHT_TEXT = "© 2026 IAC Impact Story AI"
