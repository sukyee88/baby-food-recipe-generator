import streamlit as st
from src import prompt
from src import get_params
import openai
import pandas as pd
from io import StringIO
import tabulate


def sidebar():
    num_days = st.sidebar.number_input('Input number of days:', min_value=1, max_value=7, step=1)
    num_ingredients = st.sidebar.number_input('Input max number of ingredients:', min_value=1, max_value=5, step=1)
    with st.sidebar.container():
        st.write('Which meals do you need suggestion for?')
        breakfast = st.sidebar.checkbox('Breakfast', value=False)
        lunch = st.sidebar.checkbox('Lunch', value=False)
        dinner = st.sidebar.checkbox('Dinner', value=False)
        tea = st.sidebar.checkbox('Tea', value=False)
    
    with st.sidebar.container():
        st.write('How old is your baby?')
        age = st.sidebar.slider('Age(months)', min_value=6, max_value=24, step=1)
    
    meals = []
    if breakfast:
        meals.append(breakfast)
    if lunch:
        meals.append(lunch)
    if dinner:
        meals.append(dinner)
    if tea:
        meals.append(tea)


    return num_days, num_ingredients,age, meals

def main_run():
    openai.api_key = get_params.get_api_key()
    project_params = get_params.load_yaml()
    num_days, num_ingredients,age, meals = sidebar()
    generate = st.button("Generate")
    if generate:
        gpt_params = project_params["gpt_params"]["gpt_3.5_params"]
        
        input_prompt = prompt.generate_prompt(num_days, num_ingredients, meals, age)

        gpt_params['messages'][0]['content'] = input_prompt
        run_model = gpt_params['model']
        messages = gpt_params['messages']
        completion = openai.ChatCompletion.create(model=run_model, messages=messages)
    return completion.choices[0].message.content

if __name__ == "__main__":
    # text = main_run()
    generate = st.button("Generate")
    text = '''Day,Name,Ingredients,Steps
1,Sweet Potato Puree,Sweet Potato,"1.Peel and chop sweet potato.<br>2.Steam for 10-15 minutes or until tender.<br>3.Puree in blender until completely smooth."
2,Broccoli & Apple Puree,"Broccoli<br>Apple",1.Cut broccoli into florets and peel and chop apple. 2.Steam broccoli for 8-10 minutes or until tender. 3.Add apples and continue to steam for another 2-3 minutes. 4.Puree in blender until completely smooth."

For this 2-day recipe, you will need:
- 1 sweet potato
- 1/2 head of broccoli
- 1 apple

Disclaimer: These recipes are for reference purposes only. Parents should consult their doctor or nutritionist for any questions or concerns regarding their baby's diet.'''
    if generate:
        text_group = text.split("\n\n")
        table = pd.read_csv(StringIO(text_group[0]), index_col=None)
        print(table)
        html_table = tabulate(table, table.columns, tablefmt='html')
        
        print(html_table) 
        st.write(html_table)
        # st.table(pd.read_csv(StringIO(table), index_col=None))
        st.write(text_group[1])
        st.write("Disclaimer:")
        st.write(text_group[2])
