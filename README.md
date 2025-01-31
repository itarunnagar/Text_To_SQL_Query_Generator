# Text_To_SQL_Query_Generator
AI-Powered SQL Query Generator 📊 A Streamlit app that generates and executes SQL queries using Google Gemini AI. It supports natural language input, real-time query execution on SQLite, and built-in error handling. Powered by Python, Streamlit, and SQLite. 🚀

# ChatBot_SQL_Query_Generator
# i) **Explanation of How the Assistant Works**
This project is a simple Streamlit-based web app powered by Google Gemini AI that allows users to generate SQL queries based on natural language input. The user can ask various types of queries related to employee and department data from a sample company database.

## Features:
- Generate SQL queries using natural language inputs.
- Handle specific SQL queries for employees and departments.
- Display query results in a clean tabular format.


# ii) Steps to Run the Project Locally
## Running the Project Locally

### Prerequisites:
- Python 3.8+
- `pip` (Python package manager)

### Steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirement.txt
    ```

4. Set up your environment variables:
    - Create a `.env` file and add your `GOOGLE_API_KEY`:
      ```env
      GOOGLE_API_KEY=your_api_key
      ```

5. Run the app:
    ```bash
    streamlit run app.py
    ```

6. Open the app in your browser at `http://localhost:8501`.


# iii) Known Limitations or Suggestions for Improvement
This section should highlight any potential areas for improvement or limitations of your assistant.

**Example**:
## Known Limitations:
- The current version does not support complex queries involving multiple tables or joins beyond the `Employees` and `Departments` tables.
- The error handling for incorrect queries can be improved.
- The database is static, so it cannot be modified through the app itself.

## Suggestions for Improvement:
- Support for more complex queries with additional tables and filtering options.
- Implement user authentication and authorization for accessing sensitive data.
- Implement a feature to update or modify database records via the assistant.


