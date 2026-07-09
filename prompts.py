"""
Prompt templates for AI story generation
"""

def get_story_prompt(linkedin_posts, internship_reviews, training_reviews, tone, length):
    """
    Generate the prompt for Gemini API based on user inputs
    
    Args:
        linkedin_posts (str): LinkedIn posts content
        internship_reviews (str): Internship reviews content
        training_reviews (str): Training reviews content
        tone (str): Desired tone (Professional/Inspirational/LinkedIn Ready)
        length (str): Desired length (Short/Medium/Long)
    
    Returns:
        str: Formatted prompt for Gemini
    """
    
    # Define length guidelines based on lines/sentences
    length_guide = {
        "Short": "Write a very concise story of exactly 7-8 sentences. Keep it brief and impactful.",
        "Medium": "Write a balanced story of exactly 10-12 sentences. Develop the narrative with moderate detail.",
        "Long": "Write a comprehensive story of exactly 15-20 sentences. Provide rich details and full context."
    }
    
    # Define tone guidelines
    tone_guide = {
        "Professional": "Use formal business language with a focus on achievements and measurable outcomes.",
        "Inspirational": "Use motivating and uplifting language that emphasizes personal growth and transformation.",
        "LinkedIn Ready": "Use engaging language suitable for LinkedIn posts with a balance of professionalism and relatability."
    }
    
    prompt = f"""You are an expert storytelling assistant specializing in creating personalized impact narratives for IAC (India Academia Connect) participants.

**TASK**: Generate a compelling, personalized impact narrative based on the provided information.

**SOURCE MATERIALS**:

LinkedIn Posts:
{linkedin_posts if linkedin_posts.strip() else "No LinkedIn posts provided."}

---

Internship Reviews:
{internship_reviews if internship_reviews.strip() else "No internship reviews provided."}

---

Industry Training & Certification Reviews:
{training_reviews if training_reviews.strip() else "No training reviews provided."}

---

**REQUIREMENTS**:

1. **Language**: Write in fluent, natural English
2. **Tone**: {tone_guide.get(tone, tone_guide["Professional"])}
3. **Length**: {length_guide.get(length, length_guide["Medium"])} **STRICTLY FOLLOW THIS SENTENCE COUNT.**
4. **Content Focus**:
   - Highlight personal growth and development
   - Showcase concrete achievements and skills acquired
   - Emphasize learning experiences and insights gained
   - Demonstrate teamwork, collaboration, and leadership
   - Illustrate career impact and professional transformation
   - Connect experiences to IAC's mission and impact

5. **Writing Style**:
   - Create one coherent, flowing paragraph (not multiple paragraphs)
   - Avoid repetition of information across sources
   - Use smooth transitions between different experiences
   - If information is limited, create logical connections without fabricating facts
   - Make the story inspiring and relatable
   - Use specific examples when available
   - Each sentence should be clear and concise

6. **Structure**:
   - Begin with an engaging opening sentence that sets context
   - Develop the narrative chronologically or thematically in the middle sentences
   - End with impact, reflection, or future outlook in the final sentence

**CRITICAL**: The output must be EXACTLY the specified number of sentences. Count carefully and ensure you meet the sentence count requirement.

**OUTPUT**: Generate only the story narrative as one flowing paragraph. Do not include titles, headings, line breaks, or meta-commentary."""

    return prompt


def clean_text_content(text):
    """
    Clean and normalize input text before processing
    
    Args:
        text (str): Raw input text
    
    Returns:
        str: Cleaned text
    """
    import re
    
    if not text:
        return ""
    
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove hashtags but keep the text
    text = re.sub(r'#(\w+)', r'\1', text)
    
    # Remove most emojis (Unicode emoji ranges)
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001F900-\U0001F9FF"  # supplemental symbols
        u"\U0001FA00-\U0001FA6F"
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove excessive blank lines
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    
    # Remove duplicate reviews (basic approach - exact duplicates)
    lines = text.split('\n')
    seen = set()
    unique_lines = []
    for line in lines:
        line_stripped = line.strip()
        if line_stripped and line_stripped not in seen:
            seen.add(line_stripped)
            unique_lines.append(line)
        elif not line_stripped:
            unique_lines.append(line)
    
    text = '\n'.join(unique_lines)
    
    # Final cleanup
    text = text.strip()
    
    return text
