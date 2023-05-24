def generate_prompt(days:int, max_num_of_ingredients:int, meals:list, baby_age:str)->str:
    prompt = f'''You are a professional and experienced children meal planner. Suggest recipes for a baby of age {baby_age} with no known allergy.
    The recipe should be unique for {days} days and using at most {max_num_of_ingredients} ingredients. The recipe should be good for {meals}.
    The output should be a csv table with columns with Day, Name, Ingredients, Steps. An example is shown in the brackets.
    <<Day,Name,Ingredients,Steps
    1,Name of recipe,Ingredients needed,Steps for recipe day 1
    2. Name of recipe,Ingredients needed,Steps for recipe day 2
    >>
      At the end, give a consolidated ingredients needed in a list with the following example format:
      For this x day recipe, you will need: 
      - x bananas
      - y punnets of blueberris
      - 0.6g of quinoa.
      Include a disclaimer that the recipe is for reference purpose and parent should consult their doctor or nutritionist for any questions or concerns'''
    
    return prompt