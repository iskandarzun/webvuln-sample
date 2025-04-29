
# Prerequisites and Setup Guide

⚠️ This is for educational purpose only, author is not responsible for misuse of this application. This application shows variation of security vulnerabilities on website, along with the implementation of fixes needed to remediate the issues.

----------

## 1. Install Python

### Windows:

-   Download Python from [python.org](https://www.python.org/)
    
-   Run installer > Check "Add Python to PATH" > Install
    
-   Verify in Command Prompt:
    `python –version`

### MacOS/Linux:

-   Preinstalled, but update via terminal:    
	```
	# macOS (using Homebrew)
	brew install python

	# Linux (Debian/Ubuntu)
	sudo apt update && sudo apt install python3 python3-pip
	```
  

----------

## 2. Install Required Libraries

- Open a terminal/command prompt and run:
	`pip install flask requests markupsafe`

----------

## 3. Verify Installations

- Check installed packages:
	`pip list | grep -E 'Flask | requests | MarkupSafe'`

- Expected output:
	```
	Flask 3.0.x
	MarkupSafe 2.1.x
	requests 2.31.x
	```
----------

## 4. Project Setup

- Clone and download project folder:
	`git clone https://github.com/iskandarzun/webvuln-sample.git`
	
- Create virtual environment (optional):
	`python -m venv venv`

- Activate virtual environment (optional):
	```
	# Windows
	.\venv\Scripts\activate

	# MacOS/Linux
	source venv/bin/activate
	```
Install libraries in a virtual environment (repeat Step 2 if you create a virtual environment).

----------

## 5. Folder Structure

Make sure the directory would be like this:
```
webvuln-sample/
├── webvuln.py 			# Vulnerable application code
├── webfix.py 			# Fixed application code
├── templates/ 			# HTML templates
│ └── profile.html 		# Profile Page template
│ └── search.html 		# Search Page template
│ └── upload.html 		# Upload Page template
└── uploads/ 			# Folder uploads
```
----------

## 6. Test Installation

- Run and test:
	```
	python webvuln.py # For Vulnerable version
	python webfix.py # For Fix Version
	```
- Visit http://localhost:5000 in your browser.

----------

## Troubleshooting

### Permission Errors (Linux/macOS):

```
# Not recommended, use virtualenv instead to prevent break of local python libraries
sudo pip install flask requests markupsafe
```

### PATH Issues (Windows):

-   Reinstall Python with "Add to PATH" checked
    
-   Use full path: C:\Python3xx\python.exe
    

### Package Conflicts:

```
pip uninstall flask markupsafe requests
pip install --no-cache-dir flask requests
```
----------

