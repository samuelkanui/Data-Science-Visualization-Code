Cybersecurity Investigation: Web Traffic Visualization
Project Overview
This project is part of a cybersecurity investigation for a financial institution that has experienced recent security incidents. The goal is to analyze web traffic data to identify potential insider threats while considering privacy and ethical implications. The provided dataset tracks visitors by web traffic sources (Search, Direct, Social Media) from July to November 2019. This repository contains a Python script to visualize the data as a histogram, with visitor counts displayed on top of each bar, as well as a detailed analysis of the findings.
Scenario
You are a data scientist in the cybersecurity division of a large financial institution. The company has experienced a series of security incidents, and the IT security team suspects a potential insider threat. Your task is to analyze diverse data sources (network logs, employee access records, email communications) to identify unusual patterns or behaviors that could indicate malicious activity, while ensuring privacy and ethical considerations are maintained.
Objective
Identify anomalous or suspicious behavior in the web traffic data.

Discuss challenges in distinguishing legitimate and malicious actions.

Balance cybersecurity needs with employee privacy rights.

Propose strategies for transparency and ethical investigation.

Communicate findings to technical and non-technical stakeholders.

Generate a visualization of the web traffic data and share the GitHub repository.

Visualization Description
The visualization is a histogram showing the number of visitors (in thousands) by web traffic sources (Search, Direct, Social Media) from July to November 2019. The bars are color-coded:
Search: Blue

Direct: Pink

Social Media: Yellow

Visitor counts are displayed on top of each bar for clarity, matching the provided dataset:
Search: 50, 53, 59, 56, 62 (in thousands)

Direct: 39, 47, 42, 51, 51 (in thousands)

Social Media: 70, 80, 90, 87, 92 (in thousands)

The histogram highlights significant spikes in Social Media traffic in August, October, and November, which may indicate potential insider threats.
Analysis Summary
Anomalous Behavior: Social Media traffic spikes in August (90,000), October (97,000), and November (92,000) compared to July (70,000) and September (53,000). Search and Direct traffic remain stable (39,000–62,000). These spikes could suggest Ascertain spikes may suggest phishing, social engineering, or data exfiltration via social platforms—common insider threat tactics.

Challenges:
False Positives: Spikes might be legitimate (e.g., marketing campaigns).

Data Overload: Analyzing diverse sources (logs, access records, emails) creates large datasets.

Behavioral Ambiguity: Legitimate Social Media use (e.g., customer outreach) may mimic malicious activity.

Privacy and Ethics:
Privacy Risks: Monitoring emails and access records can infringe:on employee privacy.

Ethical Concerns: Over-monitoring may erode trust and morale.

Transparency Strategies:
Clear policies on monitoring.

Minimize data collection (e.g., focus on work-related data).

Involve HR/ethics oversight.

Secure, summarized reporting.

Stakeholder Communication:
Technical (IT Security): Detailed reports with visualizations, recommend stricter Social Media controls.

Non-Technical (Management, HR): Simple language, emphasize privacy safeguards, propose training.

Prerequisites
To run the code, you’ll need:
Python 3.x (e.g., 3.11 or 3.12)

Required libraries: matplotlib, numpy

Installation and Setup
Option 1: Running in Google Colab
Open Google Colab: colab.research.google.com.

Create a new notebook: "File" > "New notebook".

Copy and paste the code below into a code cell.
4expl4. Run the cell: Click the "Run" button or press Shift + Enter.

The histogram will display inline.

Option 2: Running in Visual Studio Code (VS Code)
Install VS Code:
Download from code.visualstudio.com.

Follow the installer prompts to install.

Install Python:
Download from python.org.

Install, ensuring "Add Python to PATH" is checked (Windows).

Set Up VS Code:
Open VS Code, install the "Python" extension (Extensions Marketplace: Ctrl+Shift+X).

Select Python interpreter: Ctrl+Shift+P, search "Python: Select Interpreter".

Create Project Folder:
Create a folder (e.g., Cybersecurity_Visualization).

Open in VS Code: "File" > "Open Folder".

Create and Save File:
Create web_traffic_histogram.py in the folder.

Copy and paste the code below.

Install Libraries:
Open terminal in VS Code: "Terminal" > "New Terminal".

Run:

pip install matplotlib numpy

Run the Code:
Click the "Run" button (top-right) or run in terminal:

python web_traffic_histogram.py

A window will display the histogram.

# Data-Science-Visualization-Code
