# Google Scholar Citations Tracker

This repository automatically tracks and exposes Google Scholar citation metrics using SerpAPI and GitHub Actions. It provides a JSON API endpoint hosted on GitHub Pages that can be consumed by web applications to display real-time citation data.

## Overview

This system consists of three main components:

1. **Automated Data Collection**: A GitHub Actions workflow that runs twice daily to fetch citation data from Google Scholar via SerpAPI
2. **Data Storage**: Citation metrics stored as JSON in the repository
3. **API Endpoint**: The JSON file hosted on GitHub Pages for easy consumption by frontend applications

## How It Works

### 1. Data Collection Pipeline

The repository uses a scheduled GitHub Actions workflow (`.github/workflows/gscholar-citations.yaml`) that:

- Runs automatically twice daily at 6:00 AM and 6:00 PM CET
- Triggers on pushes to the main branch
- Executes a Python script (`build_json.py`) that:
  - Connects to SerpAPI with your API key
  - Fetches citation data for the specified Google Scholar profile
  - Extracts key metrics: total citations, h-index, i10-index, and yearly citation graph
  - Saves the data to `citations.json`
- Commits and pushes the updated JSON file back to the repository

### 2. Data Structure

The generated `citations.json` contains:

```json
{
  "total": 431,
  "h_index": 12,
  "i10_index": 12,
  "year_graph": [
    {
      "year": 2021,
      "citations": 5
    },
    {
      "year": 2022,
      "citations": 48
    }
  ]
}
```

### 3. GitHub Pages Integration

Once GitHub Pages is enabled for this repository, the JSON file becomes accessible at:
```
https://jpwahle.github.io/jpwahle.com-citations/citations.json
```

This creates a simple REST API endpoint that frontend applications can fetch from.

## Setup Instructions

### Prerequisites

- GitHub repository with Actions enabled
- SerpAPI account and API key
- Google Scholar profile ID

### Configuration

1. **Get your Google Scholar Author ID**:
   - Visit your Google Scholar profile
   - The ID is in the URL: `https://scholar.google.com/citations?user=YOUR_ID_HERE`

2. **Set up SerpAPI**:
   - Sign up at [SerpAPI](https://serpapi.com/)
   - Get your API key from the dashboard

3. **Configure GitHub Secrets**:
   - Go to repository Settings → Secrets and variables → Actions
   - Add `SERPAPI_KEY` with your SerpAPI key value

4. **Update the workflow**:
   - Edit `.github/workflows/gscholar-citations.yaml`
   - Replace `MI0C9mAAAAAJ` with your Google Scholar ID

5. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Set source to "Deploy from a branch"
   - Select the main branch

## Usage

### Manual Trigger
You can manually trigger the workflow by pushing to the main branch or running it from the GitHub Actions tab.

### Consuming the API
Frontend applications can fetch the citation data:

```javascript
fetch('https://jpwahle.github.io/jpwahle.com-citations/citations.json')
  .then(response => response.json())
  .then(data => {
    console.log('Total citations:', data.total);
    console.log('H-index:', data.h_index);
    console.log('Citation graph:', data.year_graph);
  });
```

### Local Development
To test the script locally:

```bash
pip install serpapi
python build_json.py YOUR_SERPAPI_KEY YOUR_SCHOLAR_ID
```

## Files

- **`.github/workflows/gscholar-citations.yaml`**: GitHub Actions workflow for automated data collection
- **`build_json.py`**: Python script that fetches and processes Google Scholar data
- **`citations.json`**: Generated JSON file containing citation metrics
- **`index.html`**: Simple HTML page (can be enhanced to display the data)

## Scheduling

The workflow runs:
- **6:00 AM CET** (4:00 AM UTC): Morning update
- **6:00 PM CET** (4:00 PM UTC): Evening update

You can modify the schedule by editing the cron expressions in the workflow file.

## Dependencies

- **serpapi**: Python package for SerpAPI integration
- **GitHub Actions**: For automation
- **GitHub Pages**: For hosting the JSON endpoint