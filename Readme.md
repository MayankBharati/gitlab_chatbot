# GitLab Handbook & Direction Chatbot

This project implements a chatbot that answers questions about GitLab's Handbook and Direction pages.

## Setup
1. Clone this repository:
git clone https://github.com/yourusername/gitlab-chatbot.git
cd gitlab-chatbot
2. Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
3. Run the app:
streamlit run main.py
4. Open your browser and go to `http://localhost:8501` to interact with the chatbot.

## Project Structure

- `main.py`: Entry point of the application
- `data/`: Contains scripts for data scraping and processing
- `models/`: Implements the chatbot model
- `frontend/`: Contains the Streamlit app for the user interface
- `utils/`: Utility functions

## Deploying

To deploy this app, you can use Streamlit Community Cloud:
1. Push your code to a GitHub repository
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign in with GitHub
4. Select your repository, branch, and `main.py` file
5. Click "Deploy"

Your app will now be available at a public URL!
