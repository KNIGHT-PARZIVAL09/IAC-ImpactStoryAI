# 🧪 Testing Guide

Comprehensive testing guide for the AI Storytelling application.

## Pre-Testing Checklist

- [ ] Python 3.11+ installed
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Valid Gemini API key configured in `.env`
- [ ] Internet connection available

## Test Cases

### 1. Installation Test

**Objective**: Verify all dependencies install correctly

```bash
cd ImpactStoryAI
pip install -r requirements.txt
```

**Expected Result**: All packages install without errors

---

### 2. Application Launch Test

**Objective**: Verify application starts successfully

```bash
streamlit run app.py
```

**Expected Result**: 
- Application opens in browser
- No error messages
- UI displays correctly

---

### 3. API Key Validation Test

**Test Case 3.1**: Missing API Key

1. Set `.env` to `GEMINI_API_KEY=YOUR_API_KEY_HERE`
2. Launch application
3. **Expected**: Error message about missing API key

**Test Case 3.2**: Valid API Key

1. Set correct API key in `.env`
2. Launch application
3. **Expected**: Application loads without API errors

---

### 4. Input Validation Tests

**Test Case 4.1**: Empty Inputs

1. Leave all text areas empty
2. Click "Generate Story"
3. **Expected**: Error message "Please provide at least one source of information."

**Test Case 4.2**: Single Source Input

1. Paste content in only LinkedIn Posts
2. Click "Generate Story"
3. **Expected**: Story generates successfully

**Test Case 4.3**: Multiple Sources

1. Paste content in all three text areas
2. Click "Generate Story"
3. **Expected**: Story generates combining all sources

---

### 5. Story Generation Tests

**Test Case 5.1**: Short Length

1. Provide input content
2. Select Tone: "Professional", Length: "Short"
3. Click "Generate Story"
4. **Expected**: Story generated (approximately 200-300 words)

**Test Case 5.2**: Medium Length

1. Select Length: "Medium"
2. Click "Generate Story"
3. **Expected**: Story generated (approximately 400-600 words)

**Test Case 5.3**: Long Length

1. Select Length: "Long"
2. Click "Generate Story"
3. **Expected**: Story generated (approximately 700-1000 words)

---

### 6. Tone Variation Tests

**Test each tone**:

1. Professional - Should use formal business language
2. Inspirational - Should use motivating language
3. LinkedIn Ready - Should be engaging and shareable

**Expected**: Noticeable differences in writing style

---

### 7. Text Cleaning Tests

**Test Case 7.1**: URLs Removal

1. Input text with URLs: `Check out https://example.com for more`
2. Generate story
3. **Expected**: URLs removed from processing

**Test Case 7.2**: Hashtags Processing

1. Input: `Great #experience at #IAC internship`
2. **Expected**: Hashtags removed but text preserved

**Test Case 7.3**: Emoji Removal

1. Input: `Amazing experience 🚀 🎉`
2. **Expected**: Emojis removed, text preserved

**Test Case 7.4**: Duplicate Removal

1. Input same review twice
2. **Expected**: Only one instance processed

---

### 8. Export Functionality Tests

**Test Case 8.1**: Copy Story

1. Generate a story
2. Click "📋 Copy Story"
3. **Expected**: Text area appears with story content

**Test Case 8.2**: DOCX Export

1. Generate a story
2. Click "📥 Download DOCX"
3. Open downloaded file
4. **Expected**: 
   - Professional formatting
   - Contains title, story, date
   - No formatting errors

**Test Case 8.3**: PDF Export

1. Generate a story
2. Click "📥 Download PDF"
3. Open downloaded file
4. **Expected**:
   - Professional layout
   - Contains title, story, metadata
   - Proper font rendering

---

### 9. Clear Inputs Test

1. Fill all text areas
2. Click "🗑️ Clear Inputs"
3. **Expected**: All fields cleared, page resets

---

### 10. Responsiveness Tests

**Test Case 10.1**: Wide Screen

1. Open on desktop (1920x1080)
2. **Expected**: All elements properly aligned

**Test Case 10.2**: Narrow Screen

1. Resize browser to narrow width
2. **Expected**: Elements stack appropriately

---

### 11. Error Handling Tests

**Test Case 11.1**: Network Error

1. Disconnect internet
2. Try to generate story
3. **Expected**: Error message displayed

**Test Case 11.2**: API Quota Exceeded

1. If quota exceeded
2. **Expected**: Graceful error message

---

### 12. Performance Tests

**Test Case 12.1**: Generation Speed

1. Provide moderate input (~500 words)
2. Time story generation
3. **Expected**: Completes in 5-20 seconds

**Test Case 12.2**: Large Input Handling

1. Provide maximum input (~5000 words)
2. Generate story
3. **Expected**: Handles without crashes

---

## Regression Testing

After any code changes, run through:

1. ✅ Application launches
2. ✅ Basic generation works
3. ✅ All export formats work
4. ✅ No console errors

---

## User Acceptance Testing

Have real users test:

1. **Ease of Use**: Can they generate a story without instructions?
2. **Output Quality**: Is the story coherent and relevant?
3. **UI Clarity**: Are buttons and fields intuitive?
4. **Export Quality**: Are DOCX and PDF professionally formatted?

---

## Bug Reporting Template

When you find a bug, report:

```
**Bug Description**: [Clear description]
**Steps to Reproduce**: [Numbered steps]
**Expected Behavior**: [What should happen]
**Actual Behavior**: [What actually happened]
**Environment**: [OS, Python version, browser]
**Error Messages**: [Any error messages]
**Screenshots**: [If applicable]
```

---

## Test Results Log

Track your testing:

| Test Case | Date | Result | Notes |
|-----------|------|--------|-------|
| Installation | | ✅/❌ | |
| API Setup | | ✅/❌ | |
| Generation | | ✅/❌ | |
| DOCX Export | | ✅/❌ | |
| PDF Export | | ✅/❌ | |

---

## Automated Testing (Future)

For production deployments, consider adding:

- Unit tests for utility functions
- Integration tests for API calls
- End-to-end tests with Selenium
- Performance benchmarks
- Load testing

---

**Happy Testing! 🎉**
