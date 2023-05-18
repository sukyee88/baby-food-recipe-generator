from src import generate_prompt, get_params
import json
import openai
def main():
    openai.api_key = get_params.get_api_key()
    project_params = get_params.load_yaml()
    gpt_params = project_params["gpt_params"]["gpt_3.5_params"]
    prompt = generate_prompt(7, 2, ['breakfast', 'lunch'], "6 months")

    gpt_params['messages'][0]['content'] = prompt
    run_model = gpt_params['model']
    messages = gpt_params['messages']
    completion = openai.ChatCompletion.create(model=run_model, messages=messages)
    print(completion.choices[0].message.content)



if __name__=="__main__":
    main()
