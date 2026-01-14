# PRACTICAL 1: Installation of IDE with Necessary Libraries

## Course Information
- **Course Code:** 316316
- **Course Title:** Machine Learning
- **Semester:** 6th
- **Practical Duration:** 2 Hours
- **Learning Outcome Code:** LLO 1.1
- **Aligned Course Outcome:** CO1 - Explain the role of machine learning in AI and data science

---

## Learning Outcomes (Practical Level)

After completing this practical, students will be able to:

1. **Install and configure Python** on their system
2. **Set up an IDE or Jupyter environment** for Machine Learning development
3. **Install and verify essential ML libraries** (NumPy, Pandas, Matplotlib, Scikit-learn)
4. **Create and execute a simple Python script** to test the installation
5. **Troubleshoot common installation issues** and understand dependency management

---

## Practical Objective

The primary objective of this practical session is to establish a complete, functional development environment for Machine Learning. This is the foundation upon which all subsequent practicals will be built. Without a properly configured environment, students cannot proceed with data preprocessing, model building, or evaluation tasks.

---

## Pre-Practical Requirements (Students Should Know)

Before starting this practical, ensure that you have:

1. **Administrative access** to your computer (to install software)
2. **Internet connectivity** for downloading Python and libraries
3. **At least 2-3 GB of free disk space** for Python and libraries
4. **Basic understanding of command line/terminal** (opening, typing commands)
5. **Patience** – installations can sometimes take several minutes

---

## Part 1: Python Installation

### Step 1.1: Download Python

We will use **Python 3.9 or higher** (preferably 3.10 or 3.11) for this course.

**For Windows and macOS:**

1. Visit the official Python website: `https://www.python.org/downloads/`
2. Download the latest **stable version** (currently Python 3.11.x or 3.12.x)
3. Choose the appropriate installer:
   - **Windows:** Download the `.exe` file (64-bit recommended)
   - **macOS:** Download the `.pkg` file (universal installer)

**For Linux (Ubuntu/Debian):**

Python usually comes pre-installed. To check and install if needed:

```bash
python3 --version
# If not installed, run:
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Step 1.2: Install Python on Windows

1. Run the downloaded `.exe` file
2. **IMPORTANT:** Check the box that says **"Add Python to PATH"** (at the bottom of the first dialog)
3. Click "Install Now" for standard installation, or "Customize Installation" for advanced options
4. Wait for installation to complete (usually 1-2 minutes)
5. Click "Close" when done

### Step 1.3: Install Python on macOS

1. Run the downloaded `.pkg` file
2. Follow the installation wizard
3. Python will be installed in `/Library/Frameworks/Python.framework/Versions/3.x/`
4. The installer automatically configures PATH

### Step 1.4: Verify Python Installation

Open **Command Prompt** (Windows) or **Terminal** (macOS/Linux) and type:

```bash
python --version
```

**Expected output:** `Python 3.10.x` or higher (version number should appear)

Also verify pip (Python package manager):

```bash
pip --version
```

**Expected output:** `pip x.x.x from ... (python 3.x)`

---

## Part 2: Setting Up the Development Environment

### Option A: Anaconda Installation (Recommended for Beginners)

Anaconda is a complete package that includes Python, Jupyter, and most ML libraries pre-installed.

**Step 2A.1: Download Anaconda**

1. Visit: `https://www.anaconda.com/download`
2. Download the **Anaconda Individual Edition** (free)
3. Choose the installer for your OS (Windows, macOS, or Linux)
4. Download the **Python 3.x version** (latest)

**Step 2A.2: Install Anaconda**

- **Windows:** Run the `.exe` file and follow the installer. Accept defaults for most options.
- **macOS:** Run the `.pkg` file and follow the installer
- **Linux:** Run the bash script: `bash Anaconda3-2024.02-Linux-x86_64.sh`

**Step 2A.3: Verify Anaconda Installation**

Open a new Command Prompt/Terminal and type:

```bash
conda --version
```

**Expected output:** `conda 23.x.x` or higher

### Option B: Miniconda Installation (Lightweight Alternative)

Miniconda is a minimal version of Anaconda. Use this if you have limited disk space.

**Step 2B.1: Download Miniconda**

Visit: `https://docs.conda.io/projects/miniconda/en/latest/`

Download the **Miniconda3 installer** for your OS.

**Step 2B.2: Install and Verify**

Follow similar steps as Anaconda. Verify with:

```bash
conda --version
```

### Option C: Using Python Virtual Environment (Advanced, Manual Setup)

If you prefer not using Anaconda, create a virtual environment using built-in `venv`:

```bash
# Create a virtual environment named 'ml_env'
python -m venv ml_env

# Activate the environment
# On Windows:
ml_env\Scripts\activate

# On macOS/Linux:
source ml_env/bin/activate
```

After activation, your command prompt will show `(ml_env)` prefix.

---

## Part 3: Installing Essential Libraries

### Step 3.1: Create a Project Folder

Create a dedicated folder for your Machine Learning practicals:

```bash
# Windows
mkdir C:\Users\YourName\ML_Course

# macOS/Linux
mkdir ~/ML_Course
cd ~/ML_Course
```

### Step 3.2: Install Libraries Using pip

If using **Anaconda/Miniconda**, open **Anaconda Prompt** (Windows) or Terminal (macOS/Linux).

If using **Python virtual environment**, make sure it is activated (you should see `(ml_env)` in your command prompt).

**Install all required libraries at once:**

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

This single command installs:
- **NumPy:** Numerical computing and array operations
- **Pandas:** Data manipulation and analysis
- **Matplotlib:** Data visualization and plotting
- **Scikit-learn:** Machine learning algorithms and tools
- **Jupyter:** Interactive notebook environment

**Alternative: Install Individual Libraries**

If you want to install one at a time:

```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install jupyter
```

**Wait for the installation to complete.** You will see messages like `Successfully installed ...` for each library.

### Step 3.3: Verify Library Installation

Create a Python file to verify all installations. In your project folder, create a file named `test_installation.py`:

```python
# test_installation.py
# Script to verify Machine Learning environment installation

print("=" * 60)
print("Machine Learning Environment Verification")
print("=" * 60)

# Test NumPy
try:
    import numpy as np
    print(f"✓ NumPy version: {np.__version__}")
except ImportError as e:
    print(f"✗ NumPy installation failed: {e}")

# Test Pandas
try:
    import pandas as pd
    print(f"✓ Pandas version: {pd.__version__}")
except ImportError as e:
    print(f"✗ Pandas installation failed: {e}")

# Test Matplotlib
try:
    import matplotlib.pyplot as plt
    import matplotlib
    print(f"✓ Matplotlib version: {matplotlib.__version__}")
except ImportError as e:
    print(f"✗ Matplotlib installation failed: {e}")

# Test Scikit-learn
try:
    import sklearn
    print(f"✓ Scikit-learn version: {sklearn.__version__}")
except ImportError as e:
    print(f"✗ Scikit-learn installation failed: {e}")

# Test Jupyter
try:
    import jupyter
    print(f"✓ Jupyter is installed")
except ImportError as e:
    print(f"✗ Jupyter installation failed: {e}")

print("=" * 60)
print("Installation verification complete!")
print("=" * 60)
```

**Run the verification script:**

```bash
python test_installation.py
```

**Expected output:**

```
============================================================
Machine Learning Environment Verification
============================================================
✓ NumPy version: 1.24.x
✓ Pandas version: 2.0.x
✓ Matplotlib version: 3.7.x
✓ Scikit-learn version: 1.3.x
✓ Jupyter is installed
============================================================
Installation verification complete!
============================================================
```

If all libraries show checkmarks (✓), your installation is **successful**.

---

## Part 4: Setting Up Jupyter Notebook

Jupyter Notebook provides an interactive environment for writing and testing Python code with immediate feedback. This is where you will do most of your practical work.

### Step 4.1: Launch Jupyter Notebook

In your command prompt/terminal (with environment activated if using virtual environment), type:

```bash
jupyter notebook
```

**What happens:**

1. Your default web browser opens automatically
2. You see a page showing your file system
3. A local server runs on `http://localhost:8888`

### Step 4.2: Create Your First Notebook

1. In the Jupyter interface, click the **"New"** button (top right)
2. Select **"Python 3"**
3. A new notebook opens with the name `Untitled.ipynb`
4. Rename it to `ML_Test.ipynb` by clicking on "Untitled" and typing a new name

### Step 4.3: Test the Notebook

In the first cell, type and execute this code:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import __version__

print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", plt.matplotlib.__version__)

# Create a simple plot to test matplotlib
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Test Plot - Machine Learning Environment')
plt.xlabel('X axis')
plt.ylabel('Sin(x)')
plt.grid(True)
plt.show()
```

Press **Shift + Enter** to execute the cell. You should see:
- Version numbers printed
- A sine wave graph displayed

### Step 4.4: Save Your Notebook

Use **Ctrl+S** (or **Cmd+S** on macOS) to save. The file will be saved as `.ipynb` in your project folder.

---

## Part 5: Alternative: Using Google Colab (Cloud-Based, No Installation)

If you face any installation issues or prefer cloud-based development, use **Google Colab**:

### Step 5.1: Access Google Colab

1. Go to: `https://colab.research.google.com/`
2. Sign in with your Google account
3. Click **"+ New Notebook"**

### Step 5.2: Benefits of Google Colab

- **No installation required** – everything is cloud-based
- **Free GPU/TPU access** for faster computation
- **Pre-installed ML libraries** – NumPy, Pandas, Matplotlib, Scikit-learn already available
- **Automatic saving** to Google Drive
- **Easy sharing** with classmates and instructors

### Step 5.3: Running Code in Colab

Cells work exactly like Jupyter. Type your code and press **Shift + Enter** to execute.

Example code for Colab:

```python
# Check pre-installed versions
import numpy as np
import pandas as pd
import sklearn

print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
```

---

## Part 6: Troubleshooting Common Installation Issues

### Issue 1: "Python is not recognized as an internal or external command"

**Cause:** Python is not added to system PATH

**Solution:**
1. Reinstall Python
2. **During installation, check "Add Python to PATH"**
3. Restart Command Prompt and try again

### Issue 2: "pip: command not found"

**Cause:** pip is not installed or not in PATH

**Solution:**
```bash
python -m pip install --upgrade pip
```

Then use `python -m pip` instead of just `pip`:
```bash
python -m pip install numpy
```

### Issue 3: "ModuleNotFoundError: No module named 'numpy'"

**Cause:** Library not installed or virtual environment not activated

**Solution:**
```bash
pip install numpy
```

Or if using Anaconda:
```bash
conda install numpy
```

### Issue 4: Permission Denied (Linux/macOS)

**Cause:** Insufficient permissions

**Solution:**
```bash
pip install --user numpy
```

### Issue 5: Installation Very Slow or Hanging

**Cause:** Network issues or slow PyPI server

**Solution:**
```bash
pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy
```

(Alternative mirror – choose the one fastest for your location)

### Issue 6: Jupyter Notebook Won't Open Browser

**Cause:** Port 8888 is in use or browser issue

**Solution:**
```bash
jupyter notebook --port 8889
```

(Use a different port number)

---

## Part 7: Best Practices for ML Development

### Practice 1: Organize Your Work

Create a proper folder structure:

```
ML_Course/
├── practicals/
│   ├── practical_1_installation/
│   ├── practical_2_preprocessing/
│   └── ...
├── datasets/
├── notebooks/
└── README.md
```

### Practice 2: Use Version Control (Optional but Recommended)

Initialize Git in your project folder:

```bash
git init
git add .
git commit -m "Initial ML environment setup"
```

This helps track changes and collaborate with others.

### Practice 3: Create an Environment File (For Reproducibility)

If sharing your work, create a `requirements.txt`:

```bash
pip freeze > requirements.txt
```

This file lists all installed packages. Others can recreate your environment:

```bash
pip install -r requirements.txt
```

### Practice 4: Use Comments and Documentation

Always document your code:

```python
# Purpose: Test ML library installation
# Author: Student Name
# Date: December 2024

import numpy as np

# Create a simple array
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
```

---

## Assessment Criteria

Your Practical 1 submission will be evaluated on the following:

### Process (60% weightage)

1. **Proper Installation Steps** – Did you follow the documented process?
2. **Understanding** – Can you explain each component installed?
3. **Verification** – Did you run verification tests?
4. **Documentation** – Did you document what you installed and why?

### Product (40% weightage)

1. **Complete Installation** – All required libraries installed successfully
2. **Functional Environment** – Can you create and run a Jupyter notebook?
3. **Test Script Execution** – Does your verification script run without errors?
4. **Environment Correctness** – All libraries import without errors in a Python script

---

## Deliverables (What to Submit)

1. **Screenshots of successful installation:**
   - Python version output
   - pip version output
   - Output of `test_installation.py` script
   - Jupyter Notebook running with a test plot

2. **Saved files:**
   - `test_installation.py` script
   - `ML_Test.ipynb` notebook file with executed cells showing output

3. **Documentation:**
   - Brief report (1-2 pages) explaining:
     - Which IDE/environment you chose and why
     - Any installation issues you faced and how you resolved them
     - Confirmation that all libraries are working
     - Screenshot or copy of successful test runs

---

## Next Steps After Practical 1

Once your installation is complete and verified:

1. Review **Python basics** (if needed) – variables, loops, functions
2. Familiarize yourself with **Jupyter Notebook interface**
3. Practice **basic NumPy operations** – creating arrays, indexing, slicing
4. Begin **Practical 2: Data Preprocessing** (next practical)
5. Explore the suggested **learning websites** mentioned in the course syllabus

---

## Useful Commands Summary

```bash
# Check versions
python --version
pip --version
python -c "import numpy; print(numpy.__version__)"

# Install packages
pip install package_name
pip install -r requirements.txt

# Virtual environment (if not using Anaconda)
python -m venv ml_env
source ml_env/bin/activate  # macOS/Linux
ml_env\Scripts\activate     # Windows
deactivate

# Jupyter
jupyter notebook
jupyter notebook --port 8889

# Freeze requirements
pip freeze > requirements.txt
```

---

## References and Resources

1. **Official Python Documentation:** https://docs.python.org/3/
2. **NumPy Documentation:** https://numpy.org/doc/
3. **Pandas Documentation:** https://pandas.pydata.org/docs/
4. **Matplotlib Documentation:** https://matplotlib.org/
5. **Scikit-learn Documentation:** https://scikit-learn.org/
6. **Jupyter Documentation:** https://jupyter.org/
7. **Anaconda Documentation:** https://docs.anaconda.com/

---

## FAQ (Frequently Asked Questions)

**Q: Do I need to install all libraries manually if I use Anaconda?**
A: No. Anaconda includes NumPy, Pandas, Matplotlib, and Jupyter pre-installed. You only need to install Scikit-learn separately: `conda install scikit-learn`

**Q: Can I use Python 2 instead of Python 3?**
A: No. Python 2 is obsolete and unsupported. We use Python 3.9 or higher.

**Q: Why do I need all these libraries?**
A: Each serves a specific purpose:
- **NumPy:** Fast numerical computations
- **Pandas:** Data manipulation and handling
- **Matplotlib:** Creating visualizations
- **Scikit-learn:** Pre-built ML algorithms

**Q: Can I use a different IDE like PyCharm or VS Code?**
A: Yes, but we recommend starting with Jupyter for interactive learning. PyCharm and VS Code can be used later.

**Q: My installation is taking very long. Is this normal?**
A: Yes. First-time installations with many packages can take 5-10 minutes depending on internet speed.

**Q: What if I want to use a Mac with M1 chip?**
A: Download the **Apple Silicon** version of Anaconda or use the universal installer for Python.

---

## Submission Checklist

Before submitting your practical:

- [ ] Python installed and verified
- [ ] IDE/Jupyter environment set up
- [ ] All 5 libraries installed and verified
- [ ] `test_installation.py` runs successfully
- [ ] Jupyter Notebook creates and runs correctly
- [ ] Screenshots captured
- [ ] Documentation completed
- [ ] All files saved in your project folder

---

**End of Practical 1 Guide**

*For any doubts or issues, refer to the troubleshooting section or consult your instructor.*
