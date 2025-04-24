import streamlit as st
from chatbot import get_general_response, get_study_response
from mcq_generator import create_mcqs_from_pdf
from pdf_summarizer import summarize_pdf

# Streamlit Title
st.title("Personal Study Assistant 📚")

# Chat Type Selection
chat_type = st.selectbox("Select chat type:", ("General Chat", "Study Chat", "PDF MCQ Generator", "PDF Summarizer"))

# General/Study Chat:
if chat_type == "General Chat" or chat_type == "Study Chat":
    # User Input
    user_input = st.text_input("You:")

    if user_input:
        if chat_type == "General Chat":
            reply = get_general_response(user_input)
        elif chat_type == "Study Chat":
            reply = get_study_response(user_input)
        st.markdown(f"**StudyBot:** {reply}")

# PDF MCQ Generator:
elif chat_type == "PDF MCQ Generator":
    uploaded_pdf = st.file_uploader("Upload your PDF for MCQ generation", type="pdf")
    if uploaded_pdf is not None:
        # Save the uploaded PDF file temporarily
        with open("uploaded_file.pdf", "wb") as f:
            f.write(uploaded_pdf.read())

        # Generate MCQs from the uploaded PDF
        mcqs = create_mcqs_from_pdf("uploaded_file.pdf")
        st.subheader("Generated MCQs:")
        st.markdown(mcqs)

# PDF Summarizer:
elif chat_type == "PDF Summarizer":
    uploaded_pdf = st.file_uploader("Upload your PDF for Summarization", type="pdf")
    if uploaded_pdf is not None:
        # Save the uploaded PDF file temporarily
        with open("uploaded_file.pdf", "wb") as f:
            f.write(uploaded_pdf.read())

        # Summarize the uploaded PDF
        summary = summarize_pdf("uploaded_file.pdf")
        st.subheader("Summary of the PDF:")
        st.markdown(summary)
st.markdown("MADE WITH 🧡 BY KEVIN JAMES")