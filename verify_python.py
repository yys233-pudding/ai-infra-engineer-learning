#!/usr/bin/env python3
"""
Verification script for Python ML environment
"""

import sys

def check_package(package_name, import_name=None):
    """Check if a package is installed and importable"""
    if import_name is None:
        import_name = package_name

    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✅ {package_name}: {version}")
        return True
    except ImportError:
        print(f"❌ {package_name}: NOT INSTALLED")
        return False

def main():
    print("=" * 50)
    print("Python ML Environment Verification")
    print("=" * 50)
    print(f"\nPython Version: {sys.version}")
    print(f"Python Path: {sys.executable}\n")

    # Core ML packages
    packages = [
        ('PyTorch', 'torch'),
        ('TensorFlow', 'tensorflow'),
        ('Transformers', 'transformers'),
        ('NumPy', 'numpy'),
        ('Pandas', 'pandas'),
        ('scikit-learn', 'sklearn'),
        ('FastAPI', 'fastapi'),
        ('Uvicorn', 'uvicorn'),
        ('Requests', 'requests'),
        ('HTTPX', 'httpx'),
        ('PyYAML', 'yaml'),
        ('python-dotenv', 'dotenv'),
        ('pytest', 'pytest'),
        ('Black', 'black'),
        ('Flake8', 'flake8'),
    ]

    results = []
    print("Checking packages...\n")
    for package, import_name in packages:
        results.append(check_package(package, import_name))

    # Summary
    print("\n" + "=" * 50)
    print(f"Summary: {sum(results)}/{len(results)} packages installed")
    print("=" * 50)

    if all(results):
        print("\n🎉 All packages installed successfully!")
        return 0
    else:
        print("\n⚠️  Some packages are missing. Please install them.")
        return 1

if __name__ == "__main__":
    sys.exit(main())