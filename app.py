import streamlit as st
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables (API key)
load_dotenv()

# Set up Google GenAI API key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Function to get response from Google GenAI (Gemini)
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content([prompt, question])
        return response.text.strip()  # Strip extra spaces/newlines
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Function to clean up the SQL query
def clean_sql_query(query):
    return query.strip().replace('```sql', '').replace('```', '').strip()

# Function to execute SQL Query and return DataFrame
def execute_sql_query(sql, db):
    try:
        sql = clean_sql_query(sql)  # Clean query
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        cur.execute(sql)
        col_names = [desc[0] for desc in cur.description]  # Get column names
        rows = cur.fetchall()

        conn.commit()
        conn.close()

        return pd.DataFrame(rows, columns=col_names) if rows else pd.DataFrame()
    except sqlite3.Error as e:
        return f"SQL Error: {str(e)}"

# SQL Prompt for Gemini AI
prompt = '''
Hi, please act as a senior SQL query writer. The available tables are:

1. **Employees**: (`id`, `name`, `department`, `salary`, `hire_date`)
2. **Departments**: (`id`, `name`, `manager`)

The joining columns used to join the tables are as follows:
- From the **Employees** table, the column **department** contains the name of the department (e.g., 'Engineering').
- From the **Departments** table, the column **name** contains the department name (e.g., 'Engineering').
- The tables are joined on the condition: **Employees.department = Departments.name**.

Follow these rules:
- "Show all employees" → `SELECT * FROM Employees`
- "Show employees with salary > 50000" → `SELECT * FROM Employees WHERE salary > 50000`
- "Show employees with department names" → `SELECT name, department FROM Employees`
- "Show me all employees in the Engineering department" → `SELECT * FROM Employees WHERE department = 'Engineering';`
- "Who is the manager of the Engineering department?" → `SELECT manager FROM Departments WHERE name = 'Engineering';`
- "List all employees hired after [date]" → `SELECT * FROM Employees WHERE hire_date > [date];`
- "What is the total salary expense for the [department] department?" → `SELECT SUM(salary) AS total_salary FROM Employees JOIN Departments ON Employees.department = Departments.name WHERE Departments.name = '[department]';`

Only generate SQL queries using these tables: **Employees, Departments**. If the user makes a spelling mistake in the table name (e.g., "employee" instead of "Employees"), please correct it automatically.
And Also If User Try to write any other table from these two tables show them a meaning message that the database will only contain two tables & named of the tables in  avery concise way so the user will understand and I also give you all columns details as well if user will try to fetch unknown columns from these two tables and the columns was not available so also show them the mmeaning full message.
'''


# Function to clean up the SQL query
def clean_sql_query(query):
    # Remove unwanted backticks, 'sql' keyword and extra spaces
    cleaned_query = query.strip().replace('```sql', '').replace('```', '').strip()
    return cleaned_query

# Streamlit app setup
st.set_page_config(page_title="SQL Query Generator", page_icon="📊", layout="wide")

st.title("🔍 AI-Powered SQL Query Generator")

# Display Allowed Tables
# Streamlit info message with better formatting
st.info("""
**Note**: You can only query from the following two tables:

### 📋 Tables:
1. **Employees**:
    - Columns: `id`, `name`, `department`, `salary`, `hire_date`
2. **Departments**:
    - Columns: `id`, `name`, `manager`
""")

# User input
question = st.text_input('Enter your query request:', key='input')
submit = st.button('Generate SQL Query')

# If Submit is Clicked
if submit:
    # Get response (SQL query)
    sql_query = get_gemini_response(question, prompt)

    # Clean the query before displaying
    sql_query_cleaned = clean_sql_query(sql_query)

    # Check if the query is error or not
    if sql_query_cleaned.startswith("Error"):
        st.error(sql_query_cleaned)
    else:
        # Display SQL Query in a code block
        st.subheader('Generated SQL Query:')
        st.code(sql_query_cleaned, language='sql')

        # Execute SQL Query
        result = execute_sql_query(sql_query_cleaned, 'company.db')

        # Display Query Results in Table Format
        st.subheader('Query Results:')
        if isinstance(result, pd.DataFrame) and not result.empty:
            st.dataframe(result)  # Display results as a table
        else:
            st.warning("No data found for the query.")