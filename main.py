import streamlit as st
from frontend.app import run_app
from data.scraper import scrape_gitlab_data
from data.data_processor import process_data
from models.chatbot import initialize_chatbot

def main():
    # Scrape and process data (you might want to do this offline and save results)
    raw_data = scrape_gitlab_data()
    processed_data = process_data(raw_data)

    # Initialize chatbot
    chatbot = initialize_chatbot(processed_data)

    # Run the Streamlit app
    run_app(chatbot)

if __name__ == "__main__":
    main()
