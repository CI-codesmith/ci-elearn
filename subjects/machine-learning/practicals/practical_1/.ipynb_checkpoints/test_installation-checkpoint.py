#!/usr/bin/env python3
"""
test_installation.py
==================
Script to verify Machine Learning environment installation

Purpose: Verify that all required libraries for ML course are installed
Author: ML Course
Date: December 2024

Usage:
    python test_installation.py
"""

import sys
from datetime import datetime

print("=" * 70)
print("MACHINE LEARNING ENVIRONMENT VERIFICATION")
print("=" * 70)
print(f"\nVerification started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print("\n" + "-" * 70)
print("LIBRARY VERIFICATION RESULTS")
print("-" * 70 + "\n")

# Track success and failures
success_count = 0
failure_count = 0
libraries_info = []

# Test NumPy
print("1. Testing NumPy...")
try:
    import numpy as np
    version = np.__version__
    print(f"   ✓ NumPy version: {version}")
    print(f"   ✓ NumPy location: {np.__file__}")
    libraries_info.append(("NumPy", version, True))
    success_count += 1
except ImportError as e:
    print(f"   ✗ NumPy installation failed: {e}")
    libraries_info.append(("NumPy", "N/A", False))
    failure_count += 1
except Exception as e:
    print(f"   ✗ NumPy error: {e}")
    libraries_info.append(("NumPy", "N/A", False))
    failure_count += 1

# Test Pandas
print("\n2. Testing Pandas...")
try:
    import pandas as pd
    version = pd.__version__
    print(f"   ✓ Pandas version: {version}")
    print(f"   ✓ Pandas location: {pd.__file__}")
    libraries_info.append(("Pandas", version, True))
    success_count += 1
except ImportError as e:
    print(f"   ✗ Pandas installation failed: {e}")
    libraries_info.append(("Pandas", "N/A", False))
    failure_count += 1
except Exception as e:
    print(f"   ✗ Pandas error: {e}")
    libraries_info.append(("Pandas", "N/A", False))
    failure_count += 1

# Test Matplotlib
print("\n3. Testing Matplotlib...")
try:
    import matplotlib
    import matplotlib.pyplot as plt
    version = matplotlib.__version__
    print(f"   ✓ Matplotlib version: {version}")
    print(f"   ✓ Matplotlib location: {matplotlib.__file__}")
    libraries_info.append(("Matplotlib", version, True))
    success_count += 1
except ImportError as e:
    print(f"   ✗ Matplotlib installation failed: {e}")
    libraries_info.append(("Matplotlib", "N/A", False))
    failure_count += 1
except Exception as e:
    print(f"   ✗ Matplotlib error: {e}")
    libraries_info.append(("Matplotlib", "N/A", False))
    failure_count += 1

# Test Scikit-learn
print("\n4. Testing Scikit-learn...")
try:
    import sklearn
    version = sklearn.__version__
    print(f"   ✓ Scikit-learn version: {version}")
    print(f"   ✓ Scikit-learn location: {sklearn.__file__}")
    libraries_info.append(("Scikit-learn", version, True))
    success_count += 1
except ImportError as e:
    print(f"   ✗ Scikit-learn installation failed: {e}")
    libraries_info.append(("Scikit-learn", "N/A", False))
    failure_count += 1
except Exception as e:
    print(f"   ✗ Scikit-learn error: {e}")
    libraries_info.append(("Scikit-learn", "N/A", False))
    failure_count += 1

# Test Jupyter
print("\n5. Testing Jupyter...")
try:
    import jupyter
    print(f"   ✓ Jupyter is installed")
    print(f"   ✓ Jupyter location: {jupyter.__file__}")
    libraries_info.append(("Jupyter", "installed", True))
    success_count += 1
except ImportError as e:
    print(f"   ✗ Jupyter installation failed: {e}")
    libraries_info.append(("Jupyter", "N/A", False))
    failure_count += 1
except Exception as e:
    print(f"   ✗ Jupyter error: {e}")
    libraries_info.append(("Jupyter", "N/A", False))
    failure_count += 1

# Print Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

# Summary Table
print(f"\n{'Library':<20} {'Version':<20} {'Status':<10}")
print("-" * 50)
for lib_name, version, success in libraries_info:
    status = "✓ OK" if success else "✗ FAILED"
    print(f"{lib_name:<20} {version:<20} {status:<10}")

print("\n" + "-" * 70)
print(f"Total libraries: {len(libraries_info)}")
print(f"Successfully installed: {success_count}")
print(f"Failed to install: {failure_count}")
print("-" * 70)

# Final Result
if failure_count == 0:
    print("\n🎉 SUCCESS! All libraries are installed correctly.")
    print("   Your ML development environment is ready to use!")
    print("\n   Next steps:")
    print("   1. Launch Jupyter: jupyter notebook")
    print("   2. Create your first notebook")
    print("   3. Start working on Machine Learning practicals")
    sys.exit(0)
else:
    print(f"\n⚠️  WARNING! {failure_count} library(ies) failed to install.")
    print("   Please install the missing libraries using:")
    print("   pip install numpy pandas matplotlib scikit-learn jupyter")
    print("\n   If issues persist, refer to INSTALLATION_GUIDE.md")
    sys.exit(1)

print("=" * 70)
print(f"\nVerification completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)
