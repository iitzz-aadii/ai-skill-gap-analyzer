# AI Skill Gap Analyzer

An intelligent tool that analyzes the gap between job requirements and candidate skills using AI-powered skill extraction and matching.

## Features

- 🤖 **AI-Powered Skill Extraction**: Automatically extract skills from job descriptions and resumes
- 📊 **Gap Analysis**: Compare job requirements with candidate skills
- 💾 **Database Integration**: Store and manage data using Supabase
- 📈 **Analytics**: Generate detailed reports on skill gaps and matches
- 🔍 **Smart Matching**: Identify missing and matching skills

## Project Structure

```
/ai-skill-gap-analyzer
├── src/
│   ├── main.py        # Python code for skill extraction and analysis
│   └── database.py    # Supabase connection and data handling
├── .env.example       # Example file for API keys
├── .gitignore         # Git ignore file
└── README.md          # Project details
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ai-skill-gap-analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
1. Copy `.env.example` to `.env`
2. Fill in your API keys and credentials:
   - Supabase URL and API key
   - OpenAI API key (for AI skill extraction)

### 4. Database Setup
1. Create a Supabase project
2. Set up the required tables:
   - `job_descriptions`
   - `candidate_resumes`
   - `skill_analyses`

### 5. Run the Application
```bash
python src/main.py
```

## API Keys Required

- **Supabase**: For database operations
- **OpenAI**: For AI-powered skill extraction
- **Optional**: Other AI services for enhanced functionality

## Usage

### Basic Usage
```python
from src.main import SkillGapAnalyzer

# Initialize analyzer
analyzer = SkillGapAnalyzer()

# Process job description
job_result = analyzer.process_job_description("Job description text...")

# Process candidate resume
candidate_result = analyzer.process_resume("Resume text...")

# Analyze skill gap
analysis = analyzer.analyze_skill_gap(
    job_result["extracted_skills"],
    candidate_result["extracted_skills"]
)
```

## Database Schema

### Tables
- **job_descriptions**: Store job descriptions and extracted skills
- **candidate_resumes**: Store candidate resumes and extracted skills
- **skill_analyses**: Store analysis results and gap reports

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please open an issue in the repository.
