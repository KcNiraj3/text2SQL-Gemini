from dotenv import load_dotenv
load_dotenv()    #load all env variables


import streamlit as st
import os
import sqlite3

import google.generativeai as genai

 
# Configure API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#fUNCTION TO LOAD gEMINI MODEL FROM GOOGLE and provide sql query i.e it will convert text to sql query
def get_gemini_response(question,prompt): # question is our question, Natural language text, & we wil supply prompt so that model knows how to behave
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0], question])
    return response.text


## Now from aql generated above will fetch records from databse and display in streamlit
def read_sql_query(sql, db):
    
    conn = sqlite3.connect(db) # Connect to the SQLite database
    
    
    c = conn.cursor() # Create a cursor object using the connection
    
   
    c.execute(sql)  # Execute the SQL query passed to the function
    
   
    rows = c.fetchall()  # Fetch all the rows resulting from the executed query
    
    
    conn.commit()  # This line is actually not necessary for SELECT queries but won't harm # Commit the transaction (though not necessary for SELECT queries)
    
    
    conn.close() # Close the connection to the database
    
    # Log the fetched rows to the console
    for row in rows:
       # print(row) # Print in vscode terimnal
    
    # Return the fetched rows
        return rows
  

## Prompt

prompt =["""
    You are expert in converting English questions to SQL query!
     The SQL datababse has the name STUDENTS with the following columns:
      id, name, age, marks \n\n\For example: \nExample1 - How many enteries of records are present?,
         the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS;
         \nExample2 - What is the name of the student with the highest marks?, the sql command will be something like this SELECT name FROM STUDENTS WHERE marks=(SELECT MAX(marks) FROM STUDENTS); 
         also the sql code should not have any ''' in the beginning or end and sql word in output.

"""]

## Streamlit App

st.title("SQL Generator")
st.header("Geminin Application for SQL data Retriever")

question = st.text_input("Give the question: ", key="input")
submit=st.button("Submit")

# if submit is clicked


if submit:
    response=get_gemini_response(question,prompt)
    print(response) #print sql query in vs code terminal
    data=read_sql_query(response, "EXAMPLE.db")
    print(data)
    st.subheader("The response is")
    if data:
            for row in data:
                print(row)
                st.write(row)



