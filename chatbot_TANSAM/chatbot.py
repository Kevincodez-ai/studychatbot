import cohere
import streamlit as st
from temp import get_temp




API_KEY = "3GO3Yqcr7ON3XWRXC65XU8ssQg6Dl6rKBcF84CoR"
co = cohere.Client(API_KEY)

def get_general_response(prompt):
    """ General chat responses """
    try:
        response = co.chat(
            message=prompt,
            model="command-r-plus",  # You can also try "command-r"
            temperature=get_temp("secure1")
        )
        return response.text
    except Exception as e:
        return f"Sorry, I ran into an error: {e}"

def get_study_response(prompt):
    """ Study-related responses based on keywords """
    study_keywords = [
        ("time management", "Time management is key! Try breaking study sessions into chunks of 25 minutes with 5-minute breaks in between (Pomodoro technique)."),
        ("study tips", "Focus on understanding concepts rather than memorizing. Active recall and spaced repetition can really boost your retention."),
        ("focus", "Eliminate distractions, keep your phone on 'Do Not Disturb,' and focus on one task at a time."),
        ("motivation", "Keep going! Every study session brings you closer to your goal. Progress may seem slow, but consistency wins."),
        ("algorithms", "For studying algorithms, try to visualize the steps and practice with coding problems on platforms like LeetCode or Codeforces."),
        ("programming", "In programming, practice is everything! Write code every day and debug it yourself to improve problem-solving skills."),
    ]
    
    prompt_lower = prompt.lower()
    
    for keyword, response in study_keywords:
        if keyword in prompt_lower:
            return response
    
    # Default response using AI (if no match)
    try:
        response = co.chat(
            message=prompt,
            model="command-r-plus",  
            temperature=get_temp("secure2")
            
        )
        return response.text
    except Exception as e:
        return f"Sorry, I ran into an error: {e}"
