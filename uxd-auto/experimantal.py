from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randrange
from itertools import count
from collections import Counter


def scroll_to(element):
    desired_y = (element.size['height']/2) + element.location['y']
    current_y = (driver.execute_script('return window.innerHeight')/2) + driver.execute_script('return window.pageYOffset')
    scroll_y_by = desired_y - current_y
    driver.execute_script('window.scrollBy(0, arguments[0]);', scroll_y_by)
    
def save_score(score):
    global scoreboard
    score = int(score) - 1
    with open('scoreboard.txt', 'r') as f:
        scoreboard = f.readlines()
    recorded = int(scoreboard[score].rstrip())
    round = int(scoreboard[15].rstrip())
    scoreboard[score] = str(recorded + 1)
    scoreboard[15] = str(round + 1)
    with open('scoreboard.txt', 'w') as f:
        f.write('\n'.join([score.rstrip() for score in scoreboard]))


driver = webdriver.Edge(r"C:\Users\lgf2111\Documents\edgedriver_win64\msedgedriver.exe")
driver.get("https://learn.nyp.edu.sg/")
input('enter to start')
quiz_btn = driver.find_element_by_xpath('//*[@id="anonymous_element_14"]/a')
quiz_btn.click()
begin_btn = driver.find_element_by_xpath('//*[@id="bottom_submitButtonRow"]/input[2]')
begin_btn.click()
start_btn = driver.find_element_by_xpath('//*[@id="retakeAssessmentButtonId"]')
start_btn.click()
questions = driver.find_elements_by_class_name('takeQuestionDiv')

""" COLLECTING QUESTIONS AND OPTIONS """
for question in questions:
    question_set = {}
    question_txt = question.find_element_by_xpath('.//div/ol/li/div/fieldset/legend/div/p').text
    options = question.find_elements_by_xpath('.//div/ol/li/div/fieldset/table/tbody/tr')
    question_set['question'] = question_txt
    question_set['options'] = [option.text for option in options]
    with open('db.txt', 'r') as f:
        question_collection = eval(f.read())
    if question_set['question'] not in [x['question'] for x in question_collection]:
        question_collection.append(question_set)
        with open('db.txt', 'w') as f:
            f.write(str(question_collection))
            
""" ANSWERING THE QUESTIONS (RANDOM IF NO ANSWER GIVEN)"""
for question in questions:
    options = question.find_elements_by_xpath('.//div/ol/li/div/fieldset/table/tbody/tr')
    question_txt = question.find_element_by_xpath('.//div/ol/li/div/fieldset/legend/div/p').text
    with open('ans.txt', 'r') as f:
        answer_collection = eval(f.read())
        if question_txt in [x['question'] for x in answer_collection]:
            question_set = answer_collection[[x['question'] for x in answer_collection].index(question_txt)]
            for i in range(len(options)):
                if options[i].text == question_set['answer']:
                    option = options[i]
        else:
            option = options[randrange(1,4)]
    option_btn = option.find_element_by_xpath('.//td[1]/input')
    scroll_to(option_btn)
    option_btn.click()

            
submit_btn = driver.find_element_by_xpath('//*[@id="bottom_submitButtonRow"]/input[2]')
submit_btn.click()
alert = driver.switch_to.alert
alert.accept()
sleep(1)
ok_btn = driver.find_element_by_xpath('//*[@id="containerdiv"]/p[2]/a')
ok_btn.click()
score = driver.find_element_by_xpath('//*[@id="bbNG.receiptTag.content"]/div/table/tbody/tr[8]/td').text.replace(' out of 15 points', '').rstrip()
save_score(score)

if score == ('15 out of 15 points'):
    driver.close()
    print(f'Finished after {scoreboard["round"]} rounds.')
    break
else:
    ok_btn = driver.find_element_by_xpath('//*[@id="containerdiv"]/p[2]/a')
    ok_btn.click()
    sleep(1)
