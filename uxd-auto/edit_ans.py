with open('db.txt', 'r') as f:
    question_collection = eval(f.read())

with open('ans.txt', 'r') as f:
    answer_collection = eval(f.read())


for question in question_collection:
    if question['question'] not in [x['question'] for x in answer_collection]:
        question_collection.remove(question)
    else:
        print(f"{question_collection.index(question)+1}) {question['question']}")
        print(*[f"{i+1}. {question['options'][i]}" for i in range(len(question['options']))], sep='\n')
        print(f"Old: {[x['answer'] for x in answer_collection].index([x['answer'] for x in answer_collection][[x['question'] for x in answer_collection].index(question['question'])])+1}")
        while True:
            option = input('New: ') 
            if option.isdigit():
                if int(option) in range(1,5):
                    option = int(option)-1
                    answer = question['options'][option]
                    question = question['question']
                    answer_collection.append({'question': question, 'answer': answer})
                    break
                else:
                    print('invalid')
            else:
                print('invalid')
        
print(answer_collection)
with open('ans.txt', 'w') as f:
    f.write(str(answer_collection))