# GitHub Profile Analyzer

A Python application that retrieves public GitHub profile and repository data through the GitHub REST API and uses Google's Gemini API to generate a concise summary of the developer's profile.

## Features

- Search for a GitHub user by username
- Retrieve public GitHub profile information
- Retrieve the user's public repositories
- Display profile and repository information
- Extract relevant data before sending it to the AI
- Generate an AI-powered profile summary using Gemini
- Handle API errors and invalid usernames
- Continue searching for multiple users

## How It Works

```text
User
 ↓
GitHub Username
 ↓
GitHub REST API
 ↓
Profile + Repository Data
 ↓
Python extracts relevant information
 ↓
Gemini API
 ↓
AI-generated Summary
 ↓
User
```

## Technologies Used

- Python
- Requests
- GitHub REST API
- Google Gemini API
- python-dotenv
- JSON

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/NisalSadaham/GitHub-Profile-Analyzer.git
cd GitHub-Profile-Analyzer
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install requests google-genai python-dotenv
```

### 4. Create a `.env` file

Create a file named `.env` in the project directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your own Gemini API key.

### 5. Run the application

```bash
python AI_Github_Profile_Analyzer.py
```

## Example

```text
Enter github username to get info: octocat

Username: octocat
Bio: ...
ID: ...
Following: ...
Followers: ...
public_repos: ...

=========Repo list========
Repo_Name: Hello-World
Repo_Name: Spoon-Knife
...
===========================

Account Summary:
[Gemini-generated summary]
```

## Error Handling

The application handles common API errors including:

- `401` — Authentication failed
- `403` — Access forbidden
- `404` — Resource not found
- `429` — Rate limit exceeded
- Connection errors
- Request timeouts
- Other request-related errors

## What I Learned

This project was built as part of my progression toward AI engineering.

Through this project I practiced:

- HTTP and REST APIs
- API endpoints
- GET requests
- HTTP status codes
- JSON responses
- Python dictionaries and lists
- API error handling
- Environment variables
- API integration
- Sending processed API data to an AI model
- Combining multiple APIs in one application
- Modular Python programming

## Notes

The GitHub data used by this application comes from publicly available GitHub profile and repository information.

A Gemini API key is required to generate the AI summary.
