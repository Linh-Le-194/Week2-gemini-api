# Week 2 Deliverable: APIs & LLM Calls

This repository contains my project submission for Week 2, focusing on setting up a Python environment and integrating with LLM APIs.

## Deliverable Overview
A working Python script that interacts with the official Google GenAI SDK. It takes any user-defined topic from the terminal and prompts the gemini-2.5-flash model to return a concise summary restricted to exactly 3 sentences.

## Features Completed
- [x] Python environment configured (Python 3.12).
- [x] Successfully integrated with Google GenAI client library.
- [x] Handled prompt engineering constraints to ensure strict 3-sentence outputs.

## Setup & Execution Guide

### Step 1: Install Dependencies
Run this command in your terminal to install the official Google GenAI SDK:
pip install google-genai

### Step 2: Get an API Key
Obtain a valid API key from Google AI Studio.

### Step 3: Configure the Script
Open agent_summary.py and insert your credentials into the client initialization line:
client = genai.Client(api_key="YOUR_ACTUAL_API_KEY_HERE")

### Step 4: Run the Script
Execute the program using your Python terminal and enter any topic to test:
python agent_summary.py
