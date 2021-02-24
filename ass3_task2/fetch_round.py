from selenium import webdriver
import os

contest_number = input()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

contest = "https://codeforces.com/contest/" + str(contest_number) + "/problems"

driver.get(contest)

problems = driver.find_elements_by_class_name("problemindexholder")
 
problem_indexes = [i.get_attribute("problemindex") for i in problems]

problem_statements = driver.find_elements_by_class_name("problem-statement")

inputs = [i.find_elements_by_class_name("input") for i in problem_statements]
outputs = [ i.find_elements_by_class_name("output") for i in problem_statements]

path = "C:/" + str(contest_number)
os.mkdir(path)

for i in range(len(problem_statements)):

    path = path + "/" + problem_indexes[i]
    os.mkdir(path)

    i_path = path  + "/inputs"
    o_path = path + "/outputs"

    os.mkdir(i_path)
    os.mkdir(o_path)
    problem_statements[i].screenshot(path + "/image.png")

    for j in range(len(inputs[i])):

        i_text = inputs[i][j].find_element_by_tag_name("pre").text
        o_text = outputs[i][j].find_element_by_tag_name("pre").text

        file_i = i_path + "/input" + str(j+1) + ".txt"
        file_o = o_path + "/output" + str(j+1) + ".txt"

        f = open(file_i, "w")
        f.write(i_text)
        f.close()

        f = open(file_o, "w")
        f.write(o_text)
        f.close()
    
    path = "C:/" + str(contest_number)

driver.quit()













