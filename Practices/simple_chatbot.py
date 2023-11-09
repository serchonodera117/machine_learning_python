#non generative chatbot 
import json
from difflib import get_close_matches as gcm

path  = "Practices/knowladge_base.json"
#load from json file
def load_knowladgebase(filepath:str) -> dict:
    with open(filepath, 'r') as file:
        data: dict = json.load(file)
    return data

#save updated knowladge base to json file and
def save_knowladgebase(filepath:str, data:dict):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question:str, questions: list[str]) -> str | None:
    matches: list = gcm(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_from_question(user_question:str, base_knowledge:dict) -> str | None:
    for q in base_knowledge["questions"]:
        if(q["question"]== user_question):
            return q["answer"]
    
def chat_bot():
    knowladgeBase: dict = load_knowladgebase(path)
    while True:
        user_input: str = input("You: ")
        if user_input.lower() == "quit":
            break

        bes_match:  str | None = find_best_match(user_input, [q["question"] for q in knowladgeBase["questions"]])
        if(bes_match):
            answer: str = get_answer_from_question(bes_match, knowladgeBase)
            print(f"Lora-chan (0.1): {answer}")
        else:
            print(f"Lora-chan (0.1): no conozco la respuesta, puedes enseñarme?")
            new_answer: str = input("Escribe la respuesta o escribie 'skip' para omitir: ") 
            if new_answer.lower() != "skip":
                knowladgeBase["questions"].append({"question": user_input, "answer": new_answer})
                save_knowladgebase(path, knowladgeBase)
                print(f"Lora-chan (0.1): Gracias!, he aprendido una nueva respuesta")

if __name__ == "__main__":
    chat_bot()