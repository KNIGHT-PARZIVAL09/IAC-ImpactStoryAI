"""
AI Storytelling Application
Auto-Generate Personalized Impact Narratives at Scale

This application generates personalized impact stories for IAC participants
using Google Gemini API based on LinkedIn posts, internship reviews, and
industry training reviews.
"""

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from datetime import datetime

# Import utility functions
from utils.prompts import get_story_prompt, clean_text_content
from utils.pdf_generator import generate_pdf
from utils.docx_generator import generate_docx

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Storytelling - IAC",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for stunning styling
st.markdown("""
    <style>
    /* Main Background with Dark Purple-Black Gradient */
    .main {
        background: linear-gradient(135deg, #0f0f23 0%, #1a0b2e 50%, #16003b 100%);
        background-attachment: fixed;
    }
    
    /* Content Container - Dark Theme */
    .block-container {
        background: linear-gradient(135deg, #1a0b2e 0%, #16003b 100%);
        border-radius: 20px;
        padding: 2rem 3rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(102, 126, 234, 0.3);
    }
    
    /* Animated Title - Purple Neon */
    h1 {
        background: linear-gradient(135deg, #a78bfa 0%, #c084fc 50%, #e879f9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding-bottom: 10px;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        animation: fadeInDown 1s ease-in-out;
        filter: drop-shadow(0 0 20px rgba(167, 139, 250, 0.6));
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Subtitle - Light Purple */
    .subtitle {
        text-align: center;
        color: #c4b5fd;
        font-size: 1.3rem;
        margin-bottom: 30px;
        font-weight: 500;
        animation: fadeIn 1.5s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    /* Section Headers - Purple Gradient */
    h3 {
        background: linear-gradient(90deg, #a78bfa 0%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
        margin-top: 2rem !important;
        filter: drop-shadow(0 0 10px rgba(167, 139, 250, 0.4));
    }
    
    /* All Text Labels - Light Color */
    label, .stMarkdown, p {
        color: #d8b4fe !important;
    }
    
    /* Bold Text - Brighter Purple */
    strong, b {
        color: #e9d5ff !important;
    }
    
    /* Text Areas with STRONG Hover Effect - Dark Theme */
    .stTextArea textarea {
        font-size: 15px !important;
        border: 3px solid #3b2764 !important;
        border-radius: 15px !important;
        padding: 18px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        background: linear-gradient(135deg, #1e1133 0%, #2d1b4e 100%) !important;
        color: #e9d5ff !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2) !important;
    }
    
    .stTextArea textarea:hover {
        border-color: #a78bfa !important;
        box-shadow: 0 10px 40px rgba(167, 139, 250, 0.6) !important;
        transform: translateY(-5px) scale(1.02) !important;
        background: linear-gradient(135deg, #2d1b4e 0%, #3b2764 100%) !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #c084fc !important;
        box-shadow: 0 12px 45px rgba(192, 132, 252, 0.7) !important;
        transform: translateY(-5px) scale(1.02) !important;
    }
    
    .stTextArea textarea::placeholder {
        color: #7c3aed !important;
        opacity: 0.6;
    }
    
    /* Select Boxes - Dark Theme */
    .stSelectbox > div > div {
        border: 3px solid #3b2764 !important;
        border-radius: 12px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        background: linear-gradient(135deg, #1e1133 0%, #2d1b4e 100%) !important;
        color: #e9d5ff !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2) !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #a78bfa !important;
        box-shadow: 0 10px 40px rgba(167, 139, 250, 0.6) !important;
        transform: translateY(-5px) scale(1.05) !important;
        background: linear-gradient(135deg, #2d1b4e 0%, #3b2764 100%) !important;
    }
    
    /* Dropdown options */
    .stSelectbox option {
        background: #1e1133 !important;
        color: #e9d5ff !important;
    }
    
    /* Primary Button - Purple Neon Glow */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #7c3aed 0%, #a78bfa 50%, #c084fc 100%) !important;
        color: #000000 !important;
        border-radius: 15px !important;
        padding: 15px 40px !important;
        font-weight: 800 !important;
        font-size: 18px !important;
        border: none !important;
        box-shadow: 0 10px 40px rgba(124, 58, 237, 0.6), 0 0 20px rgba(167, 139, 250, 0.4) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button[kind="primary"]::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.4);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-8px) scale(1.05) !important;
        box-shadow: 0 20px 60px rgba(124, 58, 237, 0.9), 0 0 40px rgba(167, 139, 250, 0.8) !important;
        background: linear-gradient(135deg, #a78bfa 0%, #c084fc 50%, #e879f9 100%) !important;
    }
    
    .stButton > button[kind="primary"]:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button[kind="primary"]:active {
        transform: translateY(-3px) scale(1.02) !important;
    }
    
    /* Secondary Buttons - Dark with Purple Border */
    .stButton > button {
        background: linear-gradient(135deg, #1e1133 0%, #2d1b4e 100%) !important;
        color: #c084fc !important;
        border: 3px solid #7c3aed !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 5px 20px rgba(124, 58, 237, 0.3) !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #7c3aed 0%, #a78bfa 100%) !important;
        color: #000000 !important;
        border-color: #c084fc !important;
        transform: translateY(-6px) scale(1.05) !important;
        box-shadow: 0 15px 45px rgba(124, 58, 237, 0.7) !important;
    }
    
    /* Download Buttons - Purple/Pink Gradient */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #7c3aed 0%, #c026d3 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.5) !important;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-6px) scale(1.05) !important;
        box-shadow: 0 15px 50px rgba(192, 38, 211, 0.8) !important;
        background: linear-gradient(135deg, #a78bfa 0%, #e879f9 100%) !important;
    }
    
    /* Success Message Box - Dark Purple */
    .success-box {
        padding: 20px;
        border-radius: 15px;
        background: linear-gradient(135deg, #3b2764 0%, #4c1d95 100%);
        border-left: 5px solid #a78bfa;
        margin: 20px 0;
        animation: slideInRight 0.5s ease-out;
        box-shadow: 0 8px 30px rgba(167, 139, 250, 0.4);
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Story Output Box - Purple/Black Theme */
    .story-output {
        background: linear-gradient(135deg, #1e1133 0%, #2d1b4e 100%);
        padding: 30px;
        border-radius: 20px;
        border: 3px solid #7c3aed;
        margin-top: 20px;
        font-size: 16px;
        line-height: 1.9;
        text-align: justify;
        box-shadow: 0 10px 40px rgba(124, 58, 237, 0.6), inset 0 0 20px rgba(167, 139, 250, 0.1);
        animation: zoomIn 0.6s ease-out;
        color: #e9d5ff;
        font-weight: 500;
    }
    
    @keyframes zoomIn {
        from {
            opacity: 0;
            transform: scale(0.9);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    /* Alert Messages - Dark Theme */
    .stAlert {
        border-radius: 12px !important;
        border: 1px solid rgba(167, 139, 250, 0.3) !important;
        box-shadow: 0 5px 20px rgba(124, 58, 237, 0.3) !important;
        background: linear-gradient(135deg, #1e1133 0%, #2d1b4e 100%) !important;
        color: #e9d5ff !important;
    }
    
    /* Info Cards - Dark Purple */
    .info-card {
        background: linear-gradient(135deg, #2d1b4e 0%, #3b2764 100%);
        padding: 20px;
        border-radius: 15px;
        border-left: 4px solid #a78bfa;
        margin: 15px 0;
        box-shadow: 0 8px 30px rgba(124, 58, 237, 0.4);
        transition: all 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(167, 139, 250, 0.6);
        border-left-color: #c084fc;
    }
    
    .info-card h4 {
        color: #c084fc !important;
    }
    
    .info-card p {
        color: #d8b4fe !important;
    }
    
    /* Horizontal Divider - Purple Gradient */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #7c3aed, #a78bfa, #c084fc, transparent);
        margin: 2rem 0;
        box-shadow: 0 0 10px rgba(124, 58, 237, 0.5);
    }
    
    /* Loading Spinner */
    .stSpinner > div {
        border-top-color: #a78bfa !important;
    }
    
    /* Footer Styling - Purple */
    footer {
        text-align: center;
        padding: 20px;
        color: #c4b5fd !important;
        font-weight: 600;
    }
    
    /* Card Containers - Dark Purple */
    div[data-testid="column"] {
        background: rgba(30, 17, 51, 0.6);
        border-radius: 15px;
        padding: 15px;
        transition: all 0.3s ease;
        border: 1px solid rgba(124, 58, 237, 0.2);
    }
    
    div[data-testid="column"]:hover {
        background: rgba(45, 27, 78, 0.8);
        box-shadow: 0 8px 30px rgba(124, 58, 237, 0.4);
        transform: translateY(-3px);
        border-color: rgba(167, 139, 250, 0.5);
    }
    </style>
""", unsafe_allow_html=True)


def initialize_gemini():
    """Initialize Gemini API with API key from environment"""
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        st.error("⚠️ Please set your GEMINI_API_KEY in the .env file")
        st.info("Get your API key from: https://makersuite.google.com/app/apikey")
        st.stop()
    
    try:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('models/gemini-2.5-flash')
    except Exception as e:
        st.error(f"Failed to initialize Gemini API: {str(e)}")
        st.stop()


def generate_story(model, linkedin_posts, internship_reviews, training_reviews, tone, length):
    """
    Generate impact story using Gemini API
    
    Args:
        model: Gemini model instance
        linkedin_posts (str): LinkedIn posts content
        internship_reviews (str): Internship reviews content
        training_reviews (str): Training reviews content
        tone (str): Story tone
        length (str): Story length
    
    Returns:
        str: Generated story or None if failed
    """
    try:
        # Clean input texts
        linkedin_cleaned = clean_text_content(linkedin_posts)
        internship_cleaned = clean_text_content(internship_reviews)
        training_cleaned = clean_text_content(training_reviews)
        
        # Generate prompt
        prompt = get_story_prompt(
            linkedin_cleaned,
            internship_cleaned,
            training_cleaned,
            tone,
            length
        )
        
        # Generate content with GAME-STYLE LOADING
        # Create loading animation
        with st.spinner(''):
            # Display custom loading message
            st.markdown("""
            <div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #2d1b4e 0%, #3b2764 100%); border-radius: 20px; border: 3px solid #7c3aed; box-shadow: 0 10px 40px rgba(124, 58, 237, 0.6);">
                <div style="font-size: 80px; animation: bounce 1s infinite;">🤖</div>
                <h2 style="color: #c084fc; margin: 20px 0; font-size: 2rem; animation: pulse 2s infinite;">
                    ✨ AI Magic in Progress ✨
                </h2>
                <p style="color: #a78bfa; font-size: 1.1rem; margin: 15px 0;">
                    🧠 Analyzing your content...<br>
                    📝 Crafting compelling narratives...<br>
                    ✍️ Polishing your story...
                </p>
                <div style="width: 100%; max-width: 400px; height: 30px; background: rgba(124, 58, 237, 0.3); border-radius: 15px; margin: 25px auto; overflow: hidden; border: 2px solid #7c3aed;">
                    <div style="width: 100%; height: 100%; background: linear-gradient(90deg, #7c3aed, #a78bfa, #c084fc, #7c3aed); background-size: 200% 100%; animation: gradientMove 2s linear infinite;"></div>
                </div>
                <p style="color: #d8b4fe; font-size: 0.95rem; font-style: italic; margin-top: 20px;">
                    💡 <strong>Pro Tip:</strong> The AI is combining insights from all your sources!
                </p>
            </div>
            
            <style>
            @keyframes gradientMove {
                0% { background-position: 0% 50%; }
                100% { background-position: 200% 50%; }
            }
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-15px); }
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Generate the actual content
            response = model.generate_content(prompt)
            story = response.text
        
        return story
    
    except Exception as e:
        st.error(f"Unable to generate story. Please try again. Error: {str(e)}")
        return None


def main():
    """Main application function"""
    
    # Initialize Gemini
    model = initialize_gemini()
    
    # Animated Header with Icon
    st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <div style='font-size: 80px; animation: bounce 2s infinite;'>📖</div>
        </div>
        <style>
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.title("AI Storytelling")
    st.markdown('<p class="subtitle">✨ Auto-Generate Personalized Impact Narratives at Scale ✨</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Introduction with styled card
    st.markdown("""
    <div class="info-card">
        <h4 style='margin:0; color: #c084fc; font-weight: 700;'>🎯 Transform Experiences into Compelling Stories</h4>
        <p style='margin: 10px 0 0 0; color: #d8b4fe;'>
        Generate personalized impact narratives for IAC (India Academia Connect) participants using AI. 
        Choose your preferred length (Short: 7-8 lines, Medium: 10-12 lines, Long: 15-20 lines) and tone 
        to create professional stories ready for reports, LinkedIn, portfolios, and more!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📝 Input Sources")
    
    # Create three columns for input
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**💼 LinkedIn Posts**")
        linkedin_posts = st.text_area(
            "LinkedIn Posts",
            height=250,
            placeholder="Paste LinkedIn posts of IAC members here...",
            label_visibility="collapsed",
            help="Copy and paste LinkedIn posts from IAC members"
        )
    
    with col2:
        st.markdown("**🎓 Internship Reviews**")
        internship_reviews = st.text_area(
            "Internship Reviews",
            height=250,
            placeholder="Paste Internship Reviews here...",
            label_visibility="collapsed",
            help="Copy and paste reviews from the IAC Internship page"
        )
    
    with col3:
        st.markdown("**🏆 Training Reviews**")
        training_reviews = st.text_area(
            "Industry Training Reviews",
            height=250,
            placeholder="Paste Industry Training & Certification Reviews here...",
            label_visibility="collapsed",
            help="Copy and paste reviews from the IAC Industry Training & Certifications page"
        )
    
    st.markdown("---")
    st.markdown("### ⚙️ Story Settings")
    
    # Settings in two columns with emojis
    settings_col1, settings_col2, _ = st.columns([1, 1, 2])
    
    with settings_col1:
        st.markdown("**🎨 Tone**")
        tone = st.selectbox(
            "Tone",
            ["Professional", "Inspirational", "LinkedIn Ready"],
            label_visibility="collapsed",
            help="Choose the tone for your impact story"
        )
    
    with settings_col2:
        st.markdown("**📏 Length**")
        length = st.selectbox(
            "Story Length",
            ["Short", "Medium", "Long"],
            index=1,
            label_visibility="collapsed",
            help="Short: 7-8 sentences | Medium: 10-12 sentences | Long: 15-20 sentences"
        )
    
    st.markdown("---")
    
    # Action buttons
    button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)
    
    with button_col1:
        generate_button = st.button("🚀 Generate Story", type="primary", use_container_width=True)
    
    with button_col2:
        clear_button = st.button("🗑️ Clear Inputs", use_container_width=True)
    
    # Handle clear button
    if clear_button:
        st.session_state.clear()
        st.rerun()
    
    # Handle generate button
    if generate_button:
        # Validation
        if not linkedin_posts.strip() and not internship_reviews.strip() and not training_reviews.strip():
            st.error("⚠️ Please provide at least one source of information.")
        else:
            # Generate story
            story = generate_story(
                model,
                linkedin_posts,
                internship_reviews,
                training_reviews,
                tone,
                length
            )
            
            if story:
                st.session_state['generated_story'] = story
                st.session_state['story_tone'] = tone
                st.session_state['story_length'] = length
                st.success("✅ Story generated successfully!")
    
    # Display generated story and download options
    if 'generated_story' in st.session_state:
        st.markdown("---")
        st.markdown("### 📄 Generated Impact Story")
        
        story = st.session_state['generated_story']
        tone = st.session_state.get('story_tone', 'Professional')
        length = st.session_state.get('story_length', 'Medium')
        
        # Display story in a styled container
        st.markdown(f'<div class="story-output">{story}</div>', unsafe_allow_html=True)
        
        # Download and copy buttons
        st.markdown("---")
        download_col1, download_col2, download_col3, _ = st.columns([1, 1, 1, 2])
        
        with download_col1:
            # Copy button (displays story in text area for easy copying)
            if st.button("📋 Copy Story", use_container_width=True):
                st.text_area("Copy from here:", story, height=200, key="copy_area")
        
        with download_col2:
            # Generate and download DOCX
            docx_bytes = generate_docx(story, tone, length)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            st.download_button(
                label="📥 Download DOCX",
                data=docx_bytes,
                file_name=f"impact_story_{timestamp}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
        
        with download_col3:
            # Generate and download PDF
            pdf_bytes = generate_pdf(story, tone, length)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            st.download_button(
                label="📥 Download PDF",
                data=pdf_bytes,
                file_name=f"impact_story_{timestamp}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #c4b5fd; padding: 20px;'>
            <p style='color: #c4b5fd;'>Powered by Google Gemini AI | Built for IAC (India Academia Connect)</p>
            <p style='font-size: 12px; color: #a78bfa;'>© 2026 IAC Impact Story AI</p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
