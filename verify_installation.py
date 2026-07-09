"""
Installation Verification Script
Run this to verify all dependencies are correctly installed
"""

import sys
import importlib

def check_python_version():
    """Check if Python version is 3.11 or higher"""
    version = sys.version_info
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print("⚠️ Warning: Python 3.11+ recommended")
        return False
    return True

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✓ {package_name}: {version}")
        return True
    except ImportError:
        print(f"✗ {package_name}: NOT INSTALLED")
        return False

def check_environment():
    """Check if .env file exists and has API key"""
    import os
    from pathlib import Path
    
    env_path = Path('.env')
    if not env_path.exists():
        print("✗ .env file: NOT FOUND")
        return False
    
    with open('.env', 'r') as f:
        content = f.read()
        if 'GEMINI_API_KEY' not in content:
            print("✗ .env file: Missing GEMINI_API_KEY")
            return False
        if 'YOUR_API_KEY_HERE' in content:
            print("⚠️ .env file: API key not configured (still has placeholder)")
            return False
    
    print("✓ .env file: Configured")
    return True

def main():
    """Run all verification checks"""
    print("=" * 60)
    print("AI Storytelling - Installation Verification")
    print("=" * 60)
    print()
    
    print("Checking Python Version...")
    python_ok = check_python_version()
    print()
    
    print("Checking Required Packages...")
    packages = [
        ('streamlit', 'streamlit'),
        ('google-generativeai', 'google.generativeai'),
        ('python-docx', 'docx'),
        ('reportlab', 'reportlab'),
        ('python-dotenv', 'dotenv'),
        ('pandas', 'pandas')
    ]
    
    packages_ok = all(check_package(pkg, imp) for pkg, imp in packages)
    print()
    
    print("Checking Environment Configuration...")
    env_ok = check_environment()
    print()
    
    print("=" * 60)
    if python_ok and packages_ok and env_ok:
        print("✅ ALL CHECKS PASSED!")
        print("=" * 60)
        print()
        print("You're ready to run the application:")
        print("  streamlit run app.py")
    else:
        print("⚠️ SOME CHECKS FAILED")
        print("=" * 60)
        print()
        if not packages_ok:
            print("To install missing packages:")
            print("  pip install -r requirements.txt")
        if not env_ok:
            print("\nTo configure API key:")
            print("  1. Get key from: https://makersuite.google.com/app/apikey")
            print("  2. Add to .env file: GEMINI_API_KEY=your_key_here")
    print()

if __name__ == "__main__":
    main()
