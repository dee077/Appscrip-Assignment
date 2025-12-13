# Appscrip Assignment Submission ✅

### Live Link: [http://appscrip-assignment-u54z.onrender.com/](http://appscrip-assignment-u54z.onrender.com/)

### Postamn Workspace [https://www.postman.com/flight-physicist-9054540/workspace/appscrip-assignment](https://www.postman.com/flight-physicist-9054540/workspace/appscrip-assignment)

## Overview

This is a backend service that analyzes **Indian market sectors** and produces **structured trade opportunity reports** based on recent market signals.

The system accepts a sector name as input, collects relevant market news from the web, and uses a Large Language Model (Google Gemini) to synthesize the information into a **markdown-formatted analytical report**. Each report highlights market conditions, key developments, potential trade opportunities, and associated risks.

The application tackles the assignment challenges
- A **single, well-defined API endpoint** ✅
- **Session-based authentication** ✅
- **Rate limiting to prevent abuse** ✅
- **Clean separation of concerns** between data collection, analysis, and API layers ✅
- **In-memory storage**, as required by the assignment ✅

The API returns output in Markdown format, making the analysis portable, human-readable, and suitable for direct storage or sharing as a `.md` file.

## Installation and Setup

Follow these steps to get the project running locally:

### Steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/dee077/Appscrip-Assignment.git
   ```

2. **Start virtual env**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate # venv\Scripts\activate (for windows)
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run server**:

   ```bash
   uvicorn app.main:app --reload
   ```
Access the app at `http://localhost:8000`

Note: Make sure have .env with

```bash
APP_NAME=Trade Opportunities API
API_TOKEN=<your-gemini-api-key>
```


# Sample Response:

Endpoint `/analyze/{sector}/`
Available sectors
- pharmaceuticals
- technology
- agriculture
- finance
- energy
- manufacturing

# Market Analysis — Pharmaceuticals

**Generated at:** 2025-12-13T20:37:50.183395+05:30

## Market Summary
The Indian pharmaceutical market experienced a significant year-on-year growth of 7.3% in September, reaching a value of ₹20,886 crore. This growth was primarily driven by robust performance in chronic drug categories.

## Key Developments
The market's expansion in September was notably propelled by strong growth in antidiabetic, cardiac, and respiratory therapies. The sector is actively covered by various news and insights platforms, reporting on the latest new updates, drug discoveries, research reports, pharma tenders, pharma projects, pharma export & import activities, pharma laws & documents, pharma policies, pharma events, and allied sectors like hospitals & diagnostic services.

## Trade Opportunities
Significant trade opportunities are evident within the chronic drug segment, particularly in antidiabetic, cardiac, and respiratory therapies, given their robust growth contribution to the overall market. The existence of platforms covering "pharma export & import" indicates ongoing international trade activities, suggesting potential for further opportunities in these and other areas.

## Risks
Information regarding specific risks to the Indian pharmaceuticals sector is insufficient based on the provided text.

## Data Sources
- [Indian Pharma Post - Latest news and insights on the pharmaceutical ...](https://www.indianpharmapost.com/)
- [India pharmaceutical market - Latest india pharmaceutical market ...](https://pharma.economictimes.indiatimes.com/tag/india+pharmaceutical+market)
- [India pharma market Latest News- Top News on India pharma market ...](https://www.zeebiz.com/topics/india-pharma-market)
- [India's most comprehensive portal on pharmaceutical News, Tenders ...](https://pharmabiz.com/)
- [Indian pharma market grows 7.3% in September, chronic drugs gain ...](https://www.business-standard.com/economy/news/indian-pharma-market-grows-7-3-percent-in-september-2025-125100601162_1.html)
