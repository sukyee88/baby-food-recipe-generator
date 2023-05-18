def generate_prompt(days:int, max_num_of_ingredients:int, meals:list, baby_age:str)->str:
    prompt = f'''You are a professional and experienced children meal planner. Suggest recipes for a baby of age {baby_age} with no known allergy.
    The recipe should be unique for {days} days and using at most {max_num_of_ingredients} ingredients. The recipe should be good for {meals}.
    The output should include the following information, represented in the brakcets.
    <<Day 1: Name of recipe
      Ingredients:
      Steps: Steps to prepare and store food for day 1
      Day2: Name of recipe
      Ingredients
      Steps: Steps to prepare and store food for day 2
      >>
      These information should be arrange in a csv table with Day, Name, Ingredients, Steps.
      At the end, give a consolidated ingredients needed in a list with the following example format:
      For this x day recipe, you will need: 
      - x bananas
      - y punnets of blueberris
      - 0.6g of quinoa.'''
    
    return prompt