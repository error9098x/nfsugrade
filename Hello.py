import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg
image_path = "nfsu.png"
st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home", "About"]


styles = {
    "nav": {
        "background-color": "rgb(50, 205, 50)",  # Lime green background for nav
    },
    "div": {
        "max-width": "31.25rem",
    },
    "span": {
        "color": "var(--text-color)",  # Keep the text color the same
        "border-radius": "0.5rem",
        "padding": "0.4375rem 0.625rem",
        "margin": "0 0.125rem",
    },
    "active": {
        "background-color": "rgba(144, 238, 144, 0.15)",  # Translucent light lime green for active items
    },
    "hover": {
        "background-color": "rgba(0, 128, 0, 0.25)",  # Translucent dark green for hover items
    },
}

page = st_navbar(pages, styles=styles)
functions = {
      "About": pg.show_about,
    }
go_to = functions.get(page)
if go_to:
  go_to()
else:
  st.write("")
  # with st.sidebar:
  # 	st.write("Sidebar")
      

  col1, col2 = st.columns([1, 3])  

  # Column 1: Image
  with col1:
      st.image(image_path, width=500)  

  grade_points = {
      'A+': 10,
      'A': 9,
      'B+': 8,
      'B': 7,
      'C+': 6
  }
  #add
  def calculate_cgpa(grades, credits):
      total_quality_points = sum(grade_points[grade] * credit for grade, credit in zip(grades, credits))
      total_credits = sum(credits)
      return total_quality_points / total_credits

  # Streamlit UI
  st.title('Semester GPA Calculator')

  # Initialize session state for number of courses
  if 'number_of_courses' not in st.session_state:
      st.session_state.number_of_courses = 9

  # Detect changes to the number of courses input
  number_of_courses = st.number_input(
      'Enter the number of courses including labs:',
      min_value=1,
      value=st.session_state.number_of_courses,
      key='num_courses_selector'
  )

  if number_of_courses != st.session_state.number_of_courses:
      st.session_state.number_of_courses = number_of_courses
      st.experimental_rerun()

  grades = []
  credits = []

  # User input for grades and credits
  with st.form("grades_and_credits_form"):
      # Use session state to track the number of inputs to create
      for i in range(st.session_state.number_of_courses):
          grade = st.selectbox(f'Select grade for course {i+1}:', options=list(grade_points.keys()), index=4, key=f'grade_{i}')
          credit = st.number_input(f'Enter credits for course {i+1}:', min_value=1, max_value=4, value=3, key=f'credit_{i}')
          grades.append(grade)
          credits.append(credit)
          st.write("---")  # Separator line
      
      submitted = st.form_submit_button("Calculate CGPA")
      if submitted:
          cgpa = calculate_cgpa(grades, credits)
          st.write(f'Your CGPA is: {cgpa:.2f}')