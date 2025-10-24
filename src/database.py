"""
Database Manager for AI Skill Gap Analyzer
Handles Supabase connection and data operations.
"""

import os
import json
from typing import List, Dict, Any, Optional
from supabase import create_client, Client

class DatabaseManager:
    """Manages database operations for the skill gap analyzer."""
    
    def __init__(self):
        """Initialize database connection."""
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_ANON_KEY")
        
        if not self.supabase_url or not self.supabase_key:
            raise ValueError("Supabase credentials not found. Please check your .env file.")
        
        self.supabase: Client = create_client(self.supabase_url, self.supabase_key)
    
    def save_job_description(self, description: str, skills: List[str]) -> str:
        """
        Save job description and extracted skills to database.
        
        Args:
            description (str): Job description text
            skills (List[str]): Extracted skills
            
        Returns:
            str: Job ID
        """
        try:
            data = {
                "description": description,
                "skills": skills,
                "skill_count": len(skills)
            }
            
            result = self.supabase.table("job_descriptions").insert(data).execute()
            return result.data[0]["id"]
            
        except Exception as e:
            print(f"Error saving job description: {e}")
            return None
    
    def save_candidate_resume(self, resume: str, skills: List[str]) -> str:
        """
        Save candidate resume and extracted skills to database.
        
        Args:
            resume (str): Resume text
            skills (List[str]): Extracted skills
            
        Returns:
            str: Candidate ID
        """
        try:
            data = {
                "resume": resume,
                "skills": skills,
                "skill_count": len(skills)
            }
            
            result = self.supabase.table("candidate_resumes").insert(data).execute()
            return result.data[0]["id"]
            
        except Exception as e:
            print(f"Error saving candidate resume: {e}")
            return None
    
    def get_job_description(self, job_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve job description by ID.
        
        Args:
            job_id (str): Job ID
            
        Returns:
            Optional[Dict[str, Any]]: Job data or None
        """
        try:
            result = self.supabase.table("job_descriptions").select("*").eq("id", job_id).execute()
            return result.data[0] if result.data else None
            
        except Exception as e:
            print(f"Error retrieving job description: {e}")
            return None
    
    def get_candidate_resume(self, candidate_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve candidate resume by ID.
        
        Args:
            candidate_id (str): Candidate ID
            
        Returns:
            Optional[Dict[str, Any]]: Candidate data or None
        """
        try:
            result = self.supabase.table("candidate_resumes").select("*").eq("id", candidate_id).execute()
            return result.data[0] if result.data else None
            
        except Exception as e:
            print(f"Error retrieving candidate resume: {e}")
            return None
    
    def save_skill_analysis(self, job_id: str, candidate_id: str, analysis: Dict[str, Any]) -> str:
        """
        Save skill gap analysis results.
        
        Args:
            job_id (str): Job ID
            candidate_id (str): Candidate ID
            analysis (Dict[str, Any]): Analysis results
            
        Returns:
            str: Analysis ID
        """
        try:
            data = {
                "job_id": job_id,
                "candidate_id": candidate_id,
                "missing_skills": analysis.get("missing_skills", []),
                "matching_skills": analysis.get("matching_skills", []),
                "gap_percentage": analysis.get("gap_percentage", 0),
                "match_percentage": analysis.get("match_percentage", 0)
            }
            
            result = self.supabase.table("skill_analyses").insert(data).execute()
            return result.data[0]["id"]
            
        except Exception as e:
            print(f"Error saving skill analysis: {e}")
            return None
    
    def get_skill_analysis(self, analysis_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve skill analysis by ID.
        
        Args:
            analysis_id (str): Analysis ID
            
        Returns:
            Optional[Dict[str, Any]]: Analysis data or None
        """
        try:
            result = self.supabase.table("skill_analyses").select("*").eq("id", analysis_id).execute()
            return result.data[0] if result.data else None
            
        except Exception as e:
            print(f"Error retrieving skill analysis: {e}")
            return None
