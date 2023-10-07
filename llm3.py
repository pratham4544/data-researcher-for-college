import streamlit as st
import google.generativeai as palm

palm.configure(api_key='AIzaSyAAUSqm46KolD0515tMAsgJuCR_oPI-FKw')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def promt_gen(url):
    prompt = '''

you had assign task to collect the infomation from the official source of
  website and put it on table fomat HTML fomat

  college website is : {}


  the website is always college official website you have to extract some infomation form
  the official source and put it on the table

  make sure they are correct you can scrape all the website pages internal links for correct info

  create table of 3 columns
  in 1st column particular, 2 columns answer found from website, 3rd column source link

  particular are follows :

  1. Established 
  2. Full form
  3. Also known as
  4. Overall NIRF Rank
  5. Entrance Exams
  6. Mode of Application
  7. Courses Offered
  8. Highest CTC Offered
  9. Average CTC Offered
  10. Top Recruiters
  11. Official Website

  Think about it step by step no need to show steps you taken.
  in final create table format for looking good
  also can you double check with this most of time it shows wrong 

'''.format(url)
    return prompt

def promt_gen_cutoff(url):
    prompt = '''

you had assign task to collect the infomation from the official source of
  website and put it on table fomat HTML fomat

  college website is : {}


  the website is always college official website you have to extract some infomation form
  the official source and put it on the table

  make sure they are correct you can scrape all the website pages internal links for correct info

  create table of 3 columns
  in 1st column list of courses college offered, 2 columns Recent Cutoff Marks or Percentage by Entrance exam 
  found from website, 3rd column source link

  particular are follows :

  list of courses college offered

  Think about it step by step no need to show steps you taken.
  in final create table format for looking good

'''.format(url)
    return prompt

def promt_gen_placement(url):
    prompt = '''

you had assign task to collect the infomation from the official source of
  website and put it on table fomat HTML fomat

  college website is : {}


  the website is always college official website you have to extract some infomation form
  the official source and put it on the table

  make sure they are correct you can scrape all the website pages internal links for correct info

  create table of 3 columns
  in 1st column particulars , 2 columns data found from website, 3rd column source link

  particular are follows :

  overvall placement percentage
  average salary
  highest salary
  top recruiters


  Think about it step by step no need to show steps you taken.
  in final create table format for looking good

'''.format(url)
    return prompt

def promt_gen_courses(url):
    prompt = '''

you had assign task to collect the infomation from the official source of
  website and put it on table fomat HTML fomat

  college website is : {}


  the website is always college official website you have to extract some infomation form
  the official source and put it on the table

  make sure they are correct you can scrape all the website pages internal links for correct info

  create table of 3 columns
  in 1st column offerd courses by college , 2 columns details  from website, 3rd column source link and
  4th Selection Criteria

  particular are follows :

  offered courses by college
  Details Columns
    - Duration Of Course
    - Fees
    - Eligibility
  Selection Criteria


  Think about it step by step no need to show steps you taken.
  in final create table format for looking good

'''.format(url)
    return prompt


def complete_task(prompt):
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.6,
    # The maximum length of the response
    max_output_tokens=800,
)
    result = completion.result
    return result

st.title('Data Researcher Tool')
st.subheader('Get info from official Website')


input_url = st.text_input('Enter the college URL : ')
# degree_of_randomness = st.text_input('Enter Creativity Level 0.0 - 1.0')
# # degree_of_randomness = int(degree_of_randomness)

if st.button('Grab Data'):
    st.write('Highlights Data ')
    raw_text = promt_gen(input_url)
    result = complete_task(raw_text)
    with st.container():
        st.write(result)
        st.write('----XOX-----')

    st.write('Cutoff Data ')
    raw_text = promt_gen_cutoff(input_url)
    result = complete_task(raw_text)
    with st.container():
        st.write(result)
        st.write('----XOX-----')

    st.write('Placement Data ')
    raw_text = promt_gen_placement(input_url)
    result = complete_task(raw_text)
    with st.container():
        st.write(result)
        st.write('----XOX-----')

    st.write('Courses Data ')
    raw_text = promt_gen_courses(input_url)
    result = complete_task(raw_text)
    with st.container():
        st.write(result)
        st.write('----XOX-----')