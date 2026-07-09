# AI Storytelling: Auto-Generate Personalized Impact Narratives at Scale

A production-ready web application that generates personalized impact stories for IAC (India Academia Connect) participants using AI. The application combines LinkedIn posts, internship reviews, and industry training reviews to create compelling professional narratives.

## 🚀 Features

- **AI-Powered Story Generation**: Uses Google Gemini 2.5 Flash for intelligent narrative creation
- **Multi-Source Input**: Combines three data sources for comprehensive stories
- **Customizable Output**: Choose tone (Professional, Inspirational, LinkedIn Ready) and length (Short, Medium, Long)
- **Smart Text Cleaning**: Automatically removes duplicates, URLs, hashtags, and emojis
- **Multiple Export Formats**: Download as DOCX or PDF with professional formatting
- **Clean UI**: Modern, responsive interface built with Streamlit
- **Production Ready**: Proper error handling, validation, and API key management

## 📋 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.11+
- **AI Model**: Google Gemini API (Gemini 2.5 Flash)
- **Libraries**:
  - `google-generativeai` - AI integration
  - `python-docx` - Word document generation
  - `reportlab` - PDF generation
  - `python-dotenv` - Environment management
  - `pandas` - Data processing

## 📁 Project Structure

```
ImpactStoryAI/
├── app.py                      # Main Streamlit application
├── utils/
│   ├── prompts.py             # Prompt templates and text cleaning
│   ├── pdf_generator.py       # PDF generation utilities
│   └── docx_generator.py      # DOCX generation utilities
├── assets/
│   └── logo.png               # Application logo (optional)
├── .env                        # Environment variables (API keys)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🔧 Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Google Gemini API key

### Step 1: Clone or Download


Download or navigate to the ImpactStoryAI directory:

```bash
cd ImpactStoryAI
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

### Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### Configure Environment Variables

1. Open the `.env` file in the project root
2. Replace `YOUR_API_KEY_HERE` with your actual API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

**⚠️ Important**: Never commit your `.env` file to version control!

## 🎯 Running the Application

### Start the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Application

1. **Input Data**:
   - Paste LinkedIn posts in the first text area
   - Paste internship reviews in the second text area
   - Paste training reviews in the third text area
   - You must provide at least one source

2. **Configure Settings**:
   - Select **Tone**: Professional, Inspirational, or LinkedIn Ready
   - Select **Length**: Short (200-300 words), Medium (400-600 words), or Long (700-1000 words)

3. **Generate Story**:
   - Click "🚀 Generate Story"
   - Wait for AI processing (typically 5-15 seconds)
   - Review the generated narrative

4. **Export Options**:
   - **Copy Story**: Click to display story in copyable text area
   - **Download DOCX**: Get professionally formatted Word document
   - **Download PDF**: Get professionally formatted PDF document

5. **Clear & Restart**:
   - Click "🗑️ Clear Inputs" to reset and start over


## 🧹 Text Cleaning Features

The application automatically cleans input text by:

- ✅ Removing duplicate reviews
- ✅ Removing URLs
- ✅ Removing hashtags (keeping text)
- ✅ Removing emojis
- ✅ Normalizing whitespace
- ✅ Removing excessive blank lines

## 📝 How It Works

1. **Input Processing**:
   - User provides LinkedIn posts, internship reviews, and/or training reviews
   - Application cleans and normalizes the text
   - Removes duplicates and formatting issues

2. **AI Generation**:
   - Combines cleaned inputs into a structured prompt
   - Sends to Google Gemini API with tone and length specifications
   - AI generates a coherent, personalized narrative

3. **Output Formatting**:
   - Displays generated story in clean, readable format
   - Generates professional DOCX with proper styling
   - Creates PDF with formatted layout and metadata

## 🎨 Customization

### Modifying Prompts

Edit `utils/prompts.py` to customize:
- Length definitions
- Tone descriptions
- Story structure requirements
- Writing style guidelines

### Styling the UI

Edit the CSS in `app.py` (inside `st.markdown()` blocks) to change:
- Colors and themes
- Button styles
- Text formatting
- Layout spacing

### Export Format

Modify generators in:
- `utils/docx_generator.py` for Word document styling
- `utils/pdf_generator.py` for PDF layout and fonts

## 🐛 Troubleshooting

### API Key Issues

**Problem**: "Please set your GEMINI_API_KEY in the .env file"

**Solution**: 
- Verify `.env` file exists in project root
- Check API key is correctly entered without quotes
- Ensure no extra spaces around the key

### Import Errors

**Problem**: "ModuleNotFoundError: No module named 'streamlit'"

**Solution**:
```bash
pip install -r requirements.txt
```

### Generation Failures

**Problem**: "Unable to generate story. Please try again."

**Solution**:
- Check internet connection
- Verify API key is valid and active
- Ensure you have API quota remaining
- Try with shorter input text


### Port Already in Use

**Problem**: Port 8501 is already in use

**Solution**:
```bash
streamlit run app.py --server.port 8502
```

## 🔒 Security Best Practices

- ✅ Never commit `.env` file to version control
- ✅ Add `.env` to `.gitignore`
- ✅ Rotate API keys regularly
- ✅ Use environment-specific API keys (dev/prod)
- ✅ Monitor API usage and set quotas

## 📊 Example Use Cases

### For Students
Generate professional narratives for:
- Resume summaries
- LinkedIn About sections
- College applications
- Scholarship essays

### For Organizations
Create impact reports for:
- Annual reports
- Donor communications
- Program evaluations
- Marketing materials

### For Professionals
Develop content for:
- Personal branding
- Portfolio descriptions
- Professional bios
- Case studies

## 🛠️ Development

### Running in Development Mode

```bash
streamlit run app.py --server.runOnSave true
```

### Code Structure

- **app.py**: Main application logic and UI
- **utils/prompts.py**: Prompt engineering and text processing
- **utils/docx_generator.py**: Word document creation
- **utils/pdf_generator.py**: PDF document creation

### Adding New Features

1. Create new utility modules in `utils/`
2. Import in `app.py`
3. Integrate into the UI workflow
4. Test thoroughly before deployment

## 📄 License

This project is created for IAC (India Academia Connect).

## 🤝 Support

For issues or questions:
- Check the Troubleshooting section
- Review [Streamlit documentation](https://docs.streamlit.io/)
- Consult [Gemini API documentation](https://ai.google.dev/docs)

## 🎯 Future Enhancements

Potential features for future versions:
- Batch processing multiple participants
- Template customization
- Multi-language support
- Story comparison and A/B testing
- Analytics dashboard
- Database integration for story history

---

**Built with ❤️ for IAC (India Academia Connect)**
