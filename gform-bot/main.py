from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from random import randrange
from os import environ
from dotenv import load_dotenv

load_dotenv()
url = input('Enter Google Form url:\n')
service = Service(executable_path=environ['EXECUTABLE_PATH'])
driver = webdriver.Edge(service=service)
driver.get(url)
counter = 0

while True:
    # Get Questions
    questions_list = []
    questions = driver.find_elements(By.CLASS_NAME, 'freebirdFormviewerViewNumberedItemContainer')
    for question in questions:
        question_set = {}
        question_txt = question.find_element(By.CLASS_NAME, 'freebirdFormviewerComponentsQuestionBaseTitle').text
        question_set['txt'] = question_txt
        options_list = []
        options = question.find_elements(By.CLASS_NAME, 'freebirdFormviewerComponentsQuestionRadioChoice')
        for option in options:
            option_set = {}
            option_txt = option.find_element(By.CLASS_NAME, 'docssharedWizToggleLabeledLabelText').text
            option_btn = option.find_element(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupElContainer ')
            option_set['txt'] = option_txt
            option_set['btn'] = option_btn
            options_list.append(option_set)
        question_set['opt'] = options_list
        questions_list.append(question_set)

    # Get Answers
    if counter == 0:
        # answers_list = []
        opts_list = []
        for i in range(len(questions_list)):
            answer_set = {'right': None, 'wrong': []}
            question_txt = questions_list[i]['txt']
            question_opt = questions_list[i]['opt']
            print(f'Q{i+1}) {question_txt}')
            for j in range(len(question_opt)):
                print(f"{j+1}. {question_opt[j]['txt']}")
            opt = int(input())-1
            opts_list.append(opt)

    # Make Answers
    answers_list = []
    for i in range(len(questions_list)):
        answer_set = {'right': None, 'wrong': []}
        question_opt = questions_list[i]['opt']
        for j in range(len(question_opt)):
            if j != opt:
                answer_set['wrong'].append(question_opt[j])
            else:
                answer_set['right'] = question_opt[j]
        answers_list.append(answer_set)

        
        
    # Count rounds
    counter += 1
    print(f'Round {counter}')

    # Input Answers
    for answer in answers_list:
        if randrange(len(answer)+1) in range(len(answer)):
            answer['right']['btn'].click()
        else:
            random = randrange(len(answer['wrong']))
            answer['wrong'][random]['btn'].click()

    # Press submit
    submit = driver.find_elements(By.CLASS_NAME, 'appsMaterialWizButtonPaperbuttonContent')[-2]
    submit.click()

    # Submit another reqponse
    another = driver.find_elements(By.TAG_NAME, 'a')[0]
    another.click()