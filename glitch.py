# Libraries are loaded

import random

import time

try:
    import cPickle as pickle
    
except ModuleNotFoundError:
    
    import pickle

from datetime import date

from datetime import datetime

from playsound import playsound

import sys

import string

from playsound import playsound

from os import path

import numpy as np

import sys #For the exit function

import pandas as pd #To manipulate dataframes and analyzing

from os import path #To check if data files exist the first time it is used

from os import system

clear = lambda: system('cls')

def load_object(filename):

    with open(filename, 'rb') as input:
        
        obj = pickle.load(input)

        return obj

def save_object(obj, filename):
    
    with open(filename, 'wb') as output:
        
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

class project:
    
    def __init__(self, **project_info):
        
        for key, value in project_info.items():
            
            setattr(self, key, value)
            
        self.milestone_list = {}
        
        self.stakeholder_assignments = {}
            
    def add_milestone(self, milestone_id, **milestone_info):
        
        self.milestone_list[milestone_id] = milestone(**milestone_info)
        
    def add_phase(self, milestone_id, phase_id, **phase_info):
        
        self.milestone_list[milestone_id].phase_list[phase_id] = phase(**phase_info)
        
    def add_stakeholder(self, stakeholder_id, **stakeholder_info):
        
        self.stakeholder_assignments[stakeholder_id] = stakeholder(**stakeholder_info)
        
        if stakeholder_id not in stakeholder_list.keys():
        
            stakeholder_list[stakeholder_id] = stakeholder(**stakeholder_info)
            
            print("Stakeholder created and assigned")
            
        else:
            
            print("Stakeholder assigned")
        
    def del_milestone(self, milestone_id):
        
        del self.milestone_list[milestone_id]
        
    def del_phase(self, milestone_id, phase_id):
        
        del self.milestone_list[milestone_id].phase_list[phase_id]
        
    def del_stakeholder(self, stakeholder_id):
        
        del self.stakeholder_assignments[stakeholder_id]

    def mod_project(self, **project_info):
        
        for key, value in project_info.items():
            
            setattr(self, key, value)
        
    def mod_milestone(self, milestone_id, **milestone_info):
        
        if milestone_id in self.milestone_list.keys():
        
            self.milestone_list[milestone_id] = milestone(**milestone_info)
            
        else:
            
            print("That milestone is not on the list")
        
    def mod_phase(self, milestone_id, phase_id, **phase_info):
        
        if milestone_id in self.milestone_list.keys():
            
            if phase_id in self.milestone_list[milestone_id].phase_list.keys():
        
                self.milestone_list[milestone_id].phase_list[phase_id] = phase(**phase_info)
            
            else:
                
                print("This is a valid milestone but the phase was not found")
                
        else:
            
            print("That milestone is not on the list")
        
    def mod_stakeholder(self, stakeholder_id, **stakeholder_info):
        
        if stakeholder_id in self.stakeholder_assignments.keys():
        
            self.stakeholder_assignments[stakeholder_id] = stakeholder(**stakeholder_info)
            
            stakeholder_list[stakeholder_id] = stakeholder(**stakeholder_info)
            
        else:
            
            print("That stakeholder is not on the list")
            
class stakeholder:
    
    def __init__(self, **stakeholder_info):
        
        for key, value in stakeholder_info.items():
            
            setattr(self, key, value)
            
class milestone:
    
    def __init__(self, **milestone_info):
        
        for key, value in milestone_info.items():
            
            setattr(self, key, value)
            
        self.phase_list = {}
        
class phase:
    
    def __init__(self, **phase_info):
        
        for key, value in phase_info.items():
            
            setattr(self, key, value)   

if path.exists("project_list.pkl"):

    project_list = load_object("project_list.pkl")
    
else:
    
    project_list = {}
    
if path.exists("stakeholder_list.pkl"):
    
    stakeholder_list = load_object("stakeholder_list.pkl")
    
else:
    
    stakeholder_list = {}

if path.exists("routine_dict.pkl"):
    
    routine_dict = load_object("routine_dict.pkl")
    
else:
    
    routine_dict = {}

def routineCycle(routine_dict = routine_dict):

    diff_var = random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
    
    if str(date.today()) in routine_dict.keys():
        
        routine_dict[str(date.today()) + diff_var] = {}
        
        use_diff = 1
        
    else:
    
        routine_dict[str(date.today())] = {}
        
        use_diff = 0
    
    loop_check = 0
    
    instructions = {"*"*80 + "\n\nStart by meditating of praying\n\nChoose Z to start, M to skip\n\n" + "*"*80 : "magic",
                   "*"*80 + "\n\nSleepy? If you are take a nap\n\nChoose Z to start, M to skip\n\n" + "*"*80 : "sleep",
                   "*"*80 + "\n\nIs everything organized? Take 20 minutes\n\nChoose Z to start, M to skip\n\n" + "*"*80 : "order",
                   "*"*80 + "\n\nHungry? Eat something if you are\n\nChoose Z to start, M to skip\n\n" + "*"*80 : "food",
                   "*"*80 + "\n\nHave you moved your body yet?\n\nChoose Z to start, M to skip\n\n" + "*"*80 : "exercise",
                   "*"*80 + "\n\nAre you entertained? Do something for an hour\n\nChoose Z to start, M to skip\n\n" + "*"*80 : "fun",
                   "*"*80 + "\n\nHave you checked all your messages?\n\nChoose Z to start, M to skip\n\n" + "*"*80 : "messages"}
    
    for key, value in instructions.items():
        
        clear()
        
        print(key)
        
        while loop_check == 0:

            answer = str(input()).lower()

            if answer == "z":

                act_date = time.time()

                print("-"*80, "\nPress ENTER when you are done\n\n", "-"*80, sep = "")

                input()

                act_elapsed = time.time() - act_date

                if use_diff == 0:

                    routine_dict[str(date.today())][value] = act_elapsed

                elif use_diff == 1:

                    routine_dict[str(date.today()) + diff_var][value] = act_elapsed

                break

            if answer == "m":

                print("-"*80, "\nSkipped\n\n", "-"*80, sep = "")

                break

            else:

                print("-"*80, "\nThat is not a valid answer, choose Z to start, M to skip\n\n", "-"*80, sep = "")
                
    return routine_dict

def addProject(project_list = project_list):
    
    loop_var_1 = 0

    while loop_var_1 == 0:
        
        project_var_dict = {}
        
        vars_list = ["project_name", "project_deliverable", "project_deadline"]
        
        questions_list = ["name", "main deliverable", "deadline MM/DD/YYYY"]
        
        for var in range(0, len(vars_list)):
            
            project_var_dict[vars_list[var]] = str(input( f"What is this project's {questions_list[var]}?\n")).lower()
        
        current_project_id = random.choice(string.ascii_letters).lower() + str(time.time())[-3:]
        
        project_var_dict["elapsed_time"] = 0
        
        project_var_dict["status"] = "ongoing"
        
        project_var_dict["start_date"] = time.time()
        
        project_var_dict["completion_date"] = 0

        current_project_name = project_var_dict["project_name"]
         
        loop_var_2 = 0

        while loop_var_2 == 0:
            
            clear()
            
            print("-" * 80 + "\nIs this correct Y/N?:\n\n")
        
            for var in range(0, len(vars_list)):
            
                print(f"{questions_list[var]} = {project_var_dict[vars_list[var]]}")
                
            print("\n\n" + "-" * 80)
            
            input_confirmation = str(input()).lower()

            if input_confirmation == "y":

                project_list[current_project_id] = project(**project_var_dict)

                loop_var_2 = 1

                loop_var_1 = 1

            elif input_confirmation == "n":

                print("Let's try again")

                loop_var_2 = 1

            else:

                print("That is not a valid answer")
                
    loop_var_1 = 0

    while loop_var_1 == 0:
        
        clear()
        
        print("-" * 80 + "\n\nPlease assign a stakeholder to this project. Choose an ID or write a name to add a new one\n" + "-" * 80)
        
        for key, value in stakeholder_list.items():

            try:

                print(key, " : ", value.stakeholder_name)

            except:

                print("No stakeholders added")

                break

        current_stakeholder_id = str(input()).lower()
        
        if current_stakeholder_id in stakeholder_list.keys():
            
            clear()
            
            print("\nWhat is this stakeholder's main expectation\n")
            
            stake_expectation = str(input()).lower()
            
            loop_var_2 = 0
            
            while loop_var_2 == 0:
                
                print_name = stakeholder_list[current_stakeholder_id].stakeholder_name
                
                print(f"\n\nIs this correct?:\nName : {print_name}\nExpectation : {stake_expectation}\n")
            
                answer = str(input()).lower()
                
                if answer == "y":

                    project_list[current_project_id].add_stakeholder(stakeholder_id = current_stakeholder_id, 
                                                                    stakeholder_name = print_name, 
                                                                    stakeholder_role = stakeholder_list[current_stakeholder_id].stakeholder_role, 
                                                                    stakeholder_expectation = stake_expectation)
            
                    print(f"\n\n{print_name} was assigned!\n")
            
                    loop_var_2 = 1
                
                    loop_var_3 = 0
                    
                    while loop_var_3 == 0:
                        
                        print("\nWill you assign another stakeholder Y/N?\n")
                    
                        answer = str(input()).lower()
                        
                        if answer == "y":
                            
                            loop_var_3 = 1
                            
                            loop_var_2 = 1
                            
                        elif answer == "n":
                            
                            print("\nAlright!\n")
                            
                            loop_var_3 = 1
                            
                            loop_var_2 = 1
                            
                            loop_var_1 = 1
                            
                        else:
                            
                            print("\nPlease choose a valid answer")
                    
                elif answer == "n":
                    
                    print("\n\nLet's try again\n\n")
                    
                    loop_var_2 = 1
                    
                else:
                    
                    print("\nPlease choose a valid answer")
                    
                    
        else:
            
            loop_var_2 = 0
            
            while loop_var_2 == 0:
            
                current_stake_name = current_stakeholder_id
                
                clear()

                print("\nWhat is this person's role?\n")

                current_stake_role = str(input()).lower()
                
                clear()

                print("\nWhat is this stakeholder's main expectation\n")

                stake_expectation = str(input()).lower()
                
                clear()
            
                print(f"\nIs this correct?:\nName : {current_stake_name}\nRole : {current_stake_role}\nExpectation : {stake_expectation}\n")
                
                answer = str(input()).lower()
                
                if answer == "y":
                    
                    current_stakeholder_id = random.choice(string.ascii_letters).lower() + str(time.time())[-3:]

                    project_list[current_project_id].add_stakeholder(stakeholder_id = current_stakeholder_id, 
                                                                    stakeholder_name = current_stake_name, 
                                                                    stakeholder_role = current_stake_role, 
                                                                    stakeholder_expectation = stake_expectation)
                    
                    loop_var_2 = 1
                    
                    loop_var_3 = 0
                    
                    while loop_var_3 == 0:
                        
                        print("\nWill you assign another stakeholder Y/N?\n")
                    
                        answer = str(input()).lower()
                        
                        if answer == "y":
                            
                            loop_var_3 = 1
                            
                            loop_var_2 = 1
                            
                        elif answer == "n":
                            
                            print("\nAlright!\n")
                            
                            loop_var_3 = 1
                            
                            loop_var_2 = 1
                            
                            loop_var_1 = 1
                            
                        else:
                            
                            print("\nPlease choose a valid answer")
    
    loop_var_1 = 0

    while loop_var_1 == 0:
        
        clear()
        
        print("-" * 80 + "\n\nPlease add a milestone to this project\n" + "-" * 80)
        
        milestones_var_dict = {}
        
        vars_list = ["description", "deliverable", "deadline"]
        
        questions_list = ["description", "deliverable", "deadline MM/DD/YYYY"]
        
        for var in range(0, len(vars_list)):
            
            clear()
            
            milestones_var_dict[vars_list[var]] = str(input( f"What is this milestone's {questions_list[var]}?\n")).lower()
        
        current_milestone_id = current_project_id + random.choice(string.ascii_letters).lower()
        
        milestones_var_dict["project_id"] = current_project_id
        
        milestones_var_dict["status"] = "ongoing"
        
        milestones_var_dict["start_date"] = time.time()
        
        milestones_var_dict["completion_date"] = 0
         
        loop_var_2 = 0

        while loop_var_2 == 0:
            
            clear()
            
            print("\nIs this correct Y/N?:\n\n")
        
            for var in range(0, len(vars_list)):
            
                print(f"{questions_list[var]} = {milestones_var_dict[vars_list[var]]}")
                
            print("\n\n" + "-" * 80)
            
            input_confirmation = str(input()).lower()

            if input_confirmation == "y":

                project_list[current_project_id].add_milestone(milestone_id = current_milestone_id, **milestones_var_dict)

                loop_var_2 = 1
                
                loop_var_3 = 0
                
                while loop_var_3 == 0:
                    
                    clear()
                
                    print("-" * 80 + "\n\nPlease add a phase to this milestone\n" + "-" * 80)
                    
                    phases_var_dict = {}
        
                    vars_list = ["deliverable", "deadline"]

                    questions_list = ["deliverable", "deadline MM/DD/YYYY"]

                    for var in range(0, len(vars_list)):
                        
                        clear()

                        phases_var_dict[vars_list[var]] = str(input( f"What is this phase's {questions_list[var]}?\n")).lower()

                    current_phase_id = current_project_id + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower()

                    phases_var_dict["project_id"] = current_project_id

                    phases_var_dict["project_name"] = current_project_name
                    
                    phases_var_dict["elapsed_time"] = 0

                    phases_var_dict["status"] = "ongoing"

                    phases_var_dict["start_date"] = time.time()

                    phases_var_dict["completion_date"] = 0
                    
                    loop_var_4 = 0
                    
                    while loop_var_4 == 0:
                        
                        print("\nIs this correct Y/N?:\n\n")
        
                        for var in range(0, len(vars_list)):

                            print(f"{questions_list[var]} = {phases_var_dict[vars_list[var]]}")

                        print("\n\n" + "-" * 80)

                        answer = str(input()).lower()
                        
                        if answer == "y":

                            project_list[current_project_id].add_phase(milestone_id = current_milestone_id, phase_id = current_phase_id, **phases_var_dict)
                            
                            loop_var_4 = 1
                            
                            loop_var_5 = 0
                            
                            while loop_var_5 == 0:
                            
                                print("\nWill you add another phase Y/N?:\n\n")
                                
                                answer = str(input()).lower()
                                
                                if answer == "y":
                                    
                                    loop_var_5 = 1
                                    
                                    loop_var_4 = 1
                                    
                                if answer == "n":
                                    
                                    loop_var_5 = 1
                                    
                                    loop_var_4 = 1
                                    
                                    loop_var_3 = 1
                                    
                                else:
                                    
                                    print("That is not a valid answer")
                                    
                        elif answer == "n":
                            
                            print("Let's try again")
                            
                            loop_var_4 = 1
                            
                        else:
                            
                            print("That is not a valid answer")
                            
                loop_var_3 = 0
                
                while loop_var_3 == 0:
                    
                    clear()
                
                    print("\nWill you add another milestone?\n")

                    answer = str(input()).lower()
                    
                    if answer == "y":
                        
                        loop_var_3 = 1
                        
                        loop_var_2 = 1
                        
                    elif answer == "n":
                        
                        loop_var_3 = 1
                        
                        loop_var_2 = 1
                        
                        loop_var_1 = 1
                        
                    else:
                        
                        print("That is not a valid answer") 
                                        
            elif input_confirmation == "n":

                print("Let's try again")

                loop_var_2 = 1

            else:

                print("That is not a valid answer")
 
    
    return project_list

def projectWork(project_list = project_list):
    
    clear()
    
    print("*"*80 + "\nThese are the closest deadlines\n\n" + 
          "Please indicate the ID of the chosen phase, or choose Q to quit\n" + "*"*80)

    try:

        display_df = pd.DataFrame(columns = ("phase_id", "project", "phase_deliverable", "deadline", "status"))

        for i in project_list:

            for j in project_list[i].milestone_list:

                for f in project_list[i].milestone_list[j].phase_list:

                    display_df = display_df.append([{"phase_id" : f,
                                                     "milestone_id" : j,
                                                     "project_id" : i,
                                                     "project" : project_list[i].project_name,
                                                     "phase_deliverable" : project_list[i].milestone_list[j].phase_list[f].deliverable,
                                                     "deadline" : project_list[i].milestone_list[j].phase_list[f].deadline,
                                                     "status" : project_list[i].milestone_list[j].phase_list[f].status}])

        display_df.loc[:, "deadline"] = pd.to_datetime(display_df.loc[:, "deadline"])

        display_df = display_df.loc[display_df.status == "ongoing", :]

        display_df.sort_values(by = "deadline", inplace = True)

    except:

        print("Warning: No phases available")    
    
    print(display_df.loc[:, ["phase_id", "project", "phase_deliverable", "deadline"]])
    
    loop_check = 0
    
    while loop_check == 0:
        
        phase_choice = str(input()).lower()
    
        if phase_choice == "q":

            mainMenu(message = "What will you do now?")

        elif phase_choice in list(display_df.loc[:, "phase_id"]):
            
            clear()

            print("-"*80, "\nThis is the phase you have chosen\n\n", "-"*80, sep = "")

            print(display_df.loc[display_df.phase_id == phase_choice, :])

            print("-"*80, "\nPress ENTER when you are ready to begin\n\n", "-"*80, sep = "")

            input()

            i = display_df.loc[display_df.phase_id == phase_choice, "project_id"].values[0]

            j = display_df.loc[display_df.phase_id == phase_choice, "milestone_id"].values[0]

            f = phase_choice

            current_time_start = time.time()
            
            clear()

            for iterations in range(1, 8):
    
                print("-" * 80 + "\n")
    
                print("Time to work!")
    
                print("\n"+ "-" * 80)

                playsound("start.mp3")
    
                clear()

                for minutes in range(24, -1, -1):

                    for seconds in range(60, 0, -1):
            
                        print("-" * 80 + "\n")

                        print(f"Remaining work time ({iterations}/7): " + "{:02d}".format(minutes) + ":" + "{:02d}".format(seconds))
            
                        print("\n"+ "-" * 80)

                        time.sleep(1)

                        clear()
            
                print("-" * 80 + "\n")
            
                print("Time to rest")
    
                print("\n"+ "-" * 80)

                playsound("end.mp3")
    
                clear()
    
                print("-"*80, "\nHave you completed the phase? Y/N\n\n", "-"*80, sep = "")

                current_time = (time.time() - current_time_start) + project_list[i].milestone_list[j].phase_list[f].elapsed_time

                phase_update = str(input()).lower()

                loop_check = 0

                while loop_check == 0:

                    if phase_update == "y":
                    
                        print("-"*80, "\nWell done!\n\n", "-"*80, sep = "")

                        project_list[i].milestone_list[j].phase_list[f].elapsed_time = current_time

                        project_list[i].milestone_list[j].phase_list[f].status = "complete"

                        milestone_status_check = []

                        for key in project_list[i].milestone_list[j].phase_list:

                            if project_list[i].milestone_list[j].phase_list[key].status == "complete":

                                milestone_status_check.append("complete")

                            else:

                                milestone_status_check.append("not_complete")

                        if milestone_status_check.count("complete") == len(milestone_status_check):

                            project_list[i].milestone_list[j].status = "complete"

                        project_status_check = []

                        for key in project_list[i].milestone_list:

                            if project_list[i].milestone_list[key].status == "complete":

                                project_status_check.append("complete")

                            else:

                                project_status_check.append("not_complete")

                        if project_status_check.count("complete") == len(project_status_check):

                            project_list[i].status = "complete"

                        break

                    elif phase_update == "n":
                    
                        print("-"*80, "\nUnderstood!\n\n", "-"*80, sep = "")
                    
                        project_list[i].milestone_list[j].phase_list[f].elapsed_time = current_time
                    
                        break

                    else:
                    
                        print("-"*80, "\nPlease choose a valid answer\n\n", "-"*80, sep = "")

                while loop_check == 0:

                    print("-"*80, "\nWill you continue working on this phase? Y/N\n\n", "-"*80, sep = "")
        
                    keep_working = str(input()).lower()
        
                    if keep_working == "y":

                        clear()
            
                        loop_check = 1
            
                    elif keep_working == "n":
            
                        clear()

                        for minutes in range(4, -1, -1):

                            for seconds in range(60, 0, -1):
            
                                print("-" * 80 + "\n")

                                print(f"Remaining rest time ({iterations}/7): " + "{:02d}".format(minutes) + ":" + "{:02d}".format(seconds))

                                print("\n"+ "-" * 80)
                    
                                time.sleep(1)

                                clear()

                        save_object(obj = project_list, filename = "project_list.pkl")
            
                        projectWork()
            
                    else:
            
                        print("-"*80, "\nPlease choose a valid answer\n\n", "-"*80, sep = "")
    
                for minutes in range(4, -1, -1):

                    for seconds in range(60, 0, -1):
            
                        print("-" * 80 + "\n")

                        print(f"Remaining rest time ({iterations}/7): " + "{:02d}".format(minutes) + ":" + "{:02d}".format(seconds))

                        print("\n"+ "-" * 80)
            
                        time.sleep(1)

                        clear()

            print("-"*80, "\nTime to take care of yourself! Press ENTER to go back to the main menu\n\n", "-"*80, sep = "")

            input()

            mainMenu(message = "What will you do now?")

        else:
            
            print("-"*80, "\nPlease choose a valid answer. Press ENTER to try again\n\n", "-"*80, sep = "")

            input()

def projectEnlargement(project_list = project_list):
    
    project_choice_loop_var = 0
    
    while project_choice_loop_var == 0:

        message_1 = ""
    
        clear()
    
        print("*" * 80 + f"{message_1}" + "\nWhich project do you wish to enlarge? Choose an ID or choose Q to quit\n" + "*" * 80)

        display_df = pd.DataFrame()

        for key in project_list:

            if project_list[key].status != "ongoing":

                continue

            else:

                display_df = display_df.append([{"project_id" : key,
                                                "project_name" : project_list[key].project_name,
                                                "deliverable" : project_list[key].project_deliverable,
                                                "deadline" : project_list[key].project_deadline}])
    
        print(display_df)
    
        answer = str(input()).lower()
        
        if answer == "q":
            
            mainMenu(message = "What will you do now?")
            
        elif answer not in list(display_df.loc[:, "project_id"]):
            
            message_1 = "\nPlease choose an existing ID\n"
            
        else:
        
            current_project_id = answer
    
            current_project_name = display_df.loc[display_df.project_id == current_project_id, "project_name"].values
    
            milestone_choice_loop_var = 0

            while milestone_choice_loop_var == 0:
        
                clear()
        
                print("-" * 80 + "\n\nPlease choose a milestone ID to enlarge, or type in a description to add a new one. Press Q to quit\n" + "-" * 80)

                milestone_display = pd.DataFrame()

                for key in project_list[current_project_id].milestone_list:

                    milestone_display = milestone_display.append([{"milestone_id" : key,
                                                                   "deliverable" : project_list[current_project_id].milestone_list[key].deliverable,
                                                                   "deadline" : project_list[current_project_id].milestone_list[key].deadline}])
 
                print(milestone_display)
    
                answer = str(input()).lower()
        
                if answer == "q":
                    
                    mainMenu(message = "What will you do now?")
        
                elif answer not in list(milestone_display.loc[: , "milestone_id"]):
        
                    milestones_var_dict = {}
        
                    vars_list = ["deliverable", "deadline"]
        
                    questions_list = ["deliverable", "deadline MM/DD/YYYY"]
        
                    for var in range(0, len(vars_list)):
            
                        clear()
            
                        milestones_var_dict[vars_list[var]] = str(input( f"What is this milestone's {questions_list[var]}?\n")).lower()
        
                    current_milestone_id = current_project_id + random.choice(string.ascii_letters).lower()
            
                    milestones_var_dict["description"] = answer
        
                    milestones_var_dict["project_id"] = current_project_id
        
                    milestones_var_dict["status"] = "ongoing"
        
                    milestones_var_dict["start_date"] = time.time()
        
                    milestones_var_dict["completion_date"] = 0
         
                    milestone_confirmation_loop_var = 0

                    while milestone_confirmation_loop_var == 0:
            
                        clear()
            
                        print("\nIs this correct Y/N?:\n\n")
                
                        print("-" * 80 + "\n\n")
        
                        for var in range(0, len(vars_list)):
            
                            print(f"{questions_list[var]} = {milestones_var_dict[vars_list[var]]}")
                
                        print("\n\n" + "-" * 80)
            
                        input_confirmation = str(input()).lower()

                        if input_confirmation == "y":

                            project_list[current_project_id].add_milestone(milestone_id = current_milestone_id, **milestones_var_dict)

                            milestone_confirmation_loop_var = 1
                
                            phase_add_loop_var = 0
                
                            while phase_add_loop_var == 0:
                    
                                clear()
                
                                print("-" * 80 + "\n\nPlease add a phase to this milestone\n" + "-" * 80)
                    
                                phases_var_dict = {}
        
                                vars_list = ["deliverable", "deadline"]

                                questions_list = ["deliverable", "deadline MM/DD/YYYY"]

                                for var in range(0, len(vars_list)):
                        
                                    clear()

                                    phases_var_dict[vars_list[var]] = str(input( f"What is this phase's {questions_list[var]}?\n")).lower()

                                current_phase_id = current_project_id + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower()
                        
                                phases_var_dict["project_name"] = current_project_name

                                phases_var_dict["project_id"] = current_project_id

                                phases_var_dict["project_name"] = current_project_name

                                phases_var_dict["elapsed_time"] = 0

                                phases_var_dict["status"] = "ongoing"

                                phases_var_dict["start_date"] = time.time()

                                phases_var_dict["completion_date"] = 0
                                        
                                y_n_phase_conf_loop_var = 0
                                        
                                while y_n_phase_conf_loop_var == 0:
                        
                                    print("\nIs this correct Y/N?:\n\n")
                            
                                    print("-" * 80 + "\n\n")

                                    for var in range(0, len(vars_list)):

                                        print(f"{questions_list[var]} = {phases_var_dict[vars_list[var]]}")

                                    print("\n\n" + "-" * 80)

                                    answer = str(input()).lower()
                        
                                    if answer == "y":

                                        project_list[current_project_id].add_phase(milestone_id = current_milestone_id, phase_id = current_phase_id, **phases_var_dict)
                            
                                        y_n_phase_conf_loop_var = 1
                            
                                        y_n_add_phase_loop_var = 0
                            
                                        while y_n_add_phase_loop_var == 0:
                            
                                            print("\nWill you add another phase Y/N?:\n\n")
                                
                                            answer = str(input()).lower()
                                
                                            if answer == "y":
                                    
                                                y_n_add_phase_loop_var = 1
                                    
                                                y_n_phase_conf_loop_var = 1
                                    
                                            if answer == "n":
                                    
                                                y_n_phase_conf_loop_var = 1
                                    
                                                y_n_add_phase_loop_var = 1
                                    
                                                phase_add_loop_var = 1
                                        
                                                milestone_confirmation_loop_var = 1
                                            
                                                milestone_choice_loop_var = 1
                                                
                                                project_choice_loop_var = 1 
                                    
                                            else:
                                    
                                                print("That is not a valid answer")
                                    
                                    elif answer == "n":
                            
                                        print("Let's try again")
                            
                                        y_n_phase_conf_loop_var = 1
                            
                                    else:
                            
                                        print("That is not a valid answer")
                                
                        elif input_confirmation == "n":
                                
                            print("Let's try again")
                                
                            milestone_confirmation_loop_var = 1
                                
                        else:
                                
                            print("That is not a valid answer")
                            
                else:
                    
                    current_milestone_id = answer
                    
                    phase_add_loop_var = 0
                
                    while phase_add_loop_var == 0:
                    
                        clear()
                
                        print("-" * 80 + "\n\nPlease add a phase to this milestone\n" + "-" * 80)
                    
                        phases_var_dict = {}
        
                        vars_list = ["deliverable", "deadline"]

                        questions_list = ["deliverable", "deadline MM/DD/YYYY"]

                        for var in range(0, len(vars_list)):
                        
                            clear()

                            phases_var_dict[vars_list[var]] = str(input( f"What is this phase's {questions_list[var]}?\n")).lower()

                        current_phase_id = current_project_id + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower()
                        
                        phases_var_dict["project_name"] = current_project_name

                        phases_var_dict["project_id"] = current_project_id

                        phases_var_dict["elapsed_time"] = 0

                        phases_var_dict["status"] = "ongoing"

                        phases_var_dict["start_date"] = time.time()

                        phases_var_dict["completion_date"] = 0
                                        
                        y_n_phase_conf_loop_var = 0
                                        
                        while y_n_phase_conf_loop_var == 0:
                        
                            print("\nIs this correct Y/N?:\n\n")
                            
                            print("-" * 80 + "\n\n")
        
                            for var in range(0, len(vars_list)):

                                print(f"{questions_list[var]} = {phases_var_dict[vars_list[var]]}")

                            print("\n\n" + "-" * 80)

                            answer = str(input()).lower()
                        
                            if answer == "y":

                                project_list[current_project_id].add_phase(milestone_id = current_milestone_id, phase_id = current_phase_id, **phases_var_dict)
                            
                                y_n_phase_conf_loop_var = 1
                            
                                y_n_add_phase_loop_var = 0
                            
                                while y_n_add_phase_loop_var == 0:
                            
                                    print("\nWill you add another phase Y/N?:\n\n")
                                
                                    answer = str(input()).lower()
                                
                                    if answer == "y":
                                        
                                        y_n_add_phase_loop_var = 1
                                            
                                        y_n_phase_conf_loop_var = 1
                                    
                                    if answer == "n":
                                    
                                        y_n_phase_conf_loop_var = 1
                                    
                                        y_n_add_phase_loop_var = 1
                                    
                                        phase_add_loop_var = 1
                                        
                                        milestone_choice_loop_var = 1
                                        
                                        project_choice_loop_var = 1
                                    
                                    else:
                                    
                                        print("That is not a valid answer")
                                    
                            elif answer == "n":
                            
                                print("Let's try again")
                            
                                y_n_phase_conf_loop_var = 1
                            
                            else:
                            
                                print("That is not a valid answer")
                                
    return project_list

def modifyProject(project_list = project_list):
    
    message_1 = ""
    
    loop_var_1 = 0
    
    while loop_var_1 ==  0:
        
        clear()
    
        print("*" * 80 + f"{message_1}" + "\nWhich project do you wish to modify? Choose an ID or choose Q to quit\n" + "*" * 80)

        display_df = pd.DataFrame()

        for key in project_list:

            if project_list[key].status != "ongoing":

                continue

            else:

                display_df = display_df.append([{"project_id" : key,
                                                "project_name" : project_list[key].project_name,
                                                "deliverable" : project_list[key].project_deliverable,
                                                "deadline" : project_list[key].project_deadline}])
    
        print(display_df)
    
        answer = str(input()).lower()
        
        if answer == "q":
            
            mainMenu(message = "What will you do now?")
            
        elif answer not in list(display_df.loc[:, "project_id"]):
            
            message_1 = "\nPlease choose an existing ID\n"
            
        else:
            
            current_id = answer
            
            clear()
            
            print("\nThis is the project you have chosen:\n")
            
            print(display_df.loc[display_df.project_id == current_id, :])
            
            print("\nDo you want to proceed? Y/N\n")
            
            loop_var_2 = 0
            
            while loop_var_2 == 0:
            
                answer = str(input()).lower()

                if answer == "n":
                    
                    message_1 = ""

                    loop_var_2 = 1

                elif answer == "y":
                    
                    loop_var_3 = 0
                    
                    while loop_var_3 == 0:
                        
                        clear()

                        print("*" * 80 + "\nWhat change do you want to make? Choose a number\n")
                    
                        print("1. Rewrite project\n2. Rewrite milestone\n3. Rewrite phase\n4. Choose Q to quit\n\n" + "*" * 80)
                    
                        answer = str(input()).lower()
                        
                        if answer == "q":
                            
                            mainMenu(message = "What will you do now?")
                            
                        elif answer == "1":
                            
                            loop_var_4 = 0
                            
                            while loop_var_4 == 0:
                            
                                current_project_dict = {}

                                current_project_dict["Name"] = project_list[current_id].project_name

                                current_project_dict["Deliverable"] = project_list[current_id].project_deliverable

                                current_project_dict["Deadline"] = project_list[current_id].project_deadline

                                changes_dict = {}

                                change_var_list = ["project_name", "project_deliverable", "project_deadline"]

                                change_var = 0

                                for key in current_project_dict:

                                    clear()

                                    print(f"This is the current {key}: {current_project_dict[key]}\nEnter a new value or press ENTER to accept it")

                                    mod_string = str(input() or current_project_dict[key])

                                    changes_dict[change_var_list[change_var]] = mod_string
                                    
                                    change_var += 1

                                clear()

                                print("\nWill you confirm these changes? Y/N")
                                
                                loop_var_5 = 0
                                
                                while loop_var_5 == 0:
                                
                                    answer = str(input()).lower()
                                
                                    if answer == "n":
                                        
                                        loop_var_5 = 1
                                        
                                    elif answer == "y":

                                        project_list[current_id].mod_project(**changes_dict)
                                        
                                        clear()
                                        
                                        print("Modification performed successfully. Will you change something else about this project?")
                                        
                                        loop_var_6 = 0
                                        
                                        while loop_var_6 == 0:
                                            
                                            answer = str(input()).lower()
                                            
                                            if answer == "y":
                                                
                                                loop_var_6 = 1
                                        
                                                loop_var_5 = 1
                                        
                                                loop_var_4 = 1
                                            
                                            elif answer == "n":
                                                
                                                loop_var_6 = 1
                                        
                                                loop_var_5 = 1
                                        
                                                loop_var_4 = 1
                                            
                                                loop_var_3 = 1
                                                
                                                loop_var_2 = 1
                                                
                                                loop_var_1 = 1
                                                
                                            else:
                                                
                                                print("Please choose a valid answer")
                                          
                                    else:
                                        
                                        print("\nPlease choose a valid answer\n")
                                
                        elif answer == "2":
                            
                            loop_var_4 = 0
                            
                            while loop_var_4 == 0:
                                
                                clear()
                                
                                print("Please choose a milestone, indicate the ID")

                                milestone_display = pd.DataFrame()

                                for key in project_list[current_id].milestone_list:

                                    milestone_display = milestone_display.append([{"milestone_id" : key,
                                                                                   "deliverable" : project_list[current_id].milestone_list[key].deliverable,
                                                                                   "deadline" : project_list[current_id].milestone_list[key].deadline}])
 
                                print(milestone_display)
                                
                                special_loop_var = 0
                                
                                while special_loop_var == 0:
                                    
                                    curr_milestone_id = str(input()).lower()
                                    
                                    if curr_milestone_id in list(milestone_display.loc[:, "milestone_id"]):
                                        
                                        special_loop_var = 1
                                        
                                    else:
                                        
                                        print("Please choose the right ID")
                            
                                current_milestone_dict = {}

                                current_milestone_dict["Description"] = project_list[current_id].milestone_list[curr_milestone_id].description

                                current_milestone_dict["Deliverable"] = project_list[current_id].milestone_list[curr_milestone_id].deliverable

                                current_milestone_dict["Deadline"] = project_list[current_id].milestone_list[curr_milestone_id].deadline

                                changes_dict = {}

                                change_var_list = ["description", "deliverable", "deadline"]

                                change_var = 0

                                for key in current_milestone_dict:

                                    clear()

                                    print(f"This is the current {key}: {current_milestone_dict[key]}\nEnter a new value or press ENTER to accept it")

                                    mod_string = str(input() or current_milestone_dict[key])

                                    changes_dict[change_var_list[change_var]] = mod_string
                                    
                                    change_var += 1

                                clear()

                                print("\nWill you confirm these changes? Y/N")
                                
                                loop_var_5 = 0
                                
                                while loop_var_5 == 0:
                                
                                    answer = str(input()).lower()
                                
                                    if answer == "n":
                                        
                                        loop_var_5 = 1
                                        
                                    elif answer == "y":

                                        changes_dict["project_id"] = current_id
        
                                        changes_dict["status"] = "ongoing"
        
                                        changes_dict["start_date"] = project_list[current_id].milestone_list[curr_milestone_id].start_date
        
                                        changes_dict["completion_date"] = 0

                                        project_list[current_id].mod_milestone(milestone_id = curr_milestone_id, **changes_dict)
                                        
                                        clear()
                                        
                                        print("Modification performed successfully. Will you change something else about this project?")
                                        
                                        loop_var_6 = 0
                                        
                                        while loop_var_6 == 0:
                                            
                                            answer = str(input()).lower()
                                            
                                            if answer == "y":
                                                
                                                loop_var_6 = 1
                                        
                                                loop_var_5 = 1
                                        
                                                loop_var_4 = 1
                                            
                                            elif answer == "n":
                                                
                                                loop_var_6 = 1
                                        
                                                loop_var_5 = 1
                                        
                                                loop_var_4 = 1
                                            
                                                loop_var_3 = 1
                                                
                                                loop_var_2 = 1
                                                
                                                loop_var_1 = 1
                                                
                                            else:
                                                
                                                print("Please choose a valid answer")
                                        
                                        
                                    else:
                                        
                                        print("\nPlease choose a valid answer\n")
                                        
                                        
                        elif answer == "3":
                            
                            loop_var_4 = 0
                            
                            while loop_var_4 == 0:
                                
                                clear()
                                
                                print("Please choose a phase, indicate the ID")

                                phase_display = pd.DataFrame()

                                for key in project_list[current_id].milestone_list:

                                    for key_1 in project_list[current_id].milestone_list[key].phase_list:

                                        if project_list[current_id].milestone_list[key].phase_list[key_1].status != "ongoing":

                                            continue

                                        else:

                                            phase_display = phase_display.append([{"phase_id" : key_1,
                                                                                   "milestone_id" : key,
                                                                                   "deliverable" : project_list[current_id].milestone_list[key].phase_list[key_1].deliverable,
                                                                                   "deadline" : project_list[current_id].milestone_list[key].phase_list[key_1].deadline}])
                                
                                print(phase_display)
                                
                                special_loop_var = 0
                                
                                while special_loop_var == 0:
                                    
                                    curr_phase_id = str(input()).lower()
                                    
                                    if curr_phase_id in list(phase_display.loc[:, "phase_id"]):
                                        
                                        special_loop_var = 1
                                        
                                    else:
                                        
                                        print("Please choose the right ID")

                                current_milestone_id = phase_display.loc[phase_display.phase_id == curr_phase_id, "milestone_id"].values[0]
                            
                                current_phase_dict = {}

                                current_phase_dict["Deliverable"] = project_list[current_id].milestone_list[current_milestone_id].phase_list[curr_phase_id].deliverable

                                current_phase_dict["Deadline"] = project_list[current_id].milestone_list[current_milestone_id].phase_list[curr_phase_id].deadline

                                changes_dict = {}

                                change_var_list = ["deliverable", "deadline"]

                                change_var = 0

                                for key in current_phase_dict:

                                    clear()

                                    print(f"This is the current {key}: {current_phase_dict[key]}\nEnter a new value or press ENTER to accept it")

                                    mod_string = str(input() or current_phase_dict[key])

                                    changes_dict[change_var_list[change_var]] = mod_string
                                    
                                    change_var += 1

                                clear()

                                print("\nWill you confirm these changes? Y/N")
                                
                                loop_var_5 = 0
                                
                                while loop_var_5 == 0:
                                
                                    answer = str(input()).lower()
                                
                                    if answer == "n":
                                        
                                        loop_var_5 = 1
                                        
                                    elif answer == "y":

                                        changes_dict["project_id"] = project_list[current_id].milestone_list[current_milestone_id].phase_list[curr_phase_id].project_id

                                        changes_dict["project_name"] = project_list[current_id].milestone_list[current_milestone_id].phase_list[curr_phase_id].project_name
                                        
                                        changes_dict["elapsed_time"] = project_list[current_id].milestone_list[current_milestone_id].phase_list[curr_phase_id].elapsed_time

                                        changes_dict["status"] = "ongoing"

                                        changes_dict["start_date"] = project_list[current_id].milestone_list[current_milestone_id].phase_list[curr_phase_id].start_date

                                        changes_dict["completion_date"] = 0

                                        project_list[current_id].mod_phase(milestone_id = current_milestone_id, phase_id = curr_phase_id, **changes_dict)
                                        
                                        clear()
                                        
                                        print("Modification performed successfully. Will you change something else about this project?")
                                        
                                        loop_var_6 = 0
                                        
                                        while loop_var_6 == 0:
                                            
                                            answer = str(input()).lower()
                                            
                                            if answer == "y":
                                                
                                                loop_var_6 = 1
                                        
                                                loop_var_5 = 1
                                        
                                                loop_var_4 = 1
                                            
                                            elif answer == "n":
                                                
                                                loop_var_6 = 1
                                        
                                                loop_var_5 = 1
                                        
                                                loop_var_4 = 1
                                            
                                                loop_var_3 = 1
                                                
                                                loop_var_2 = 1
                                                
                                                loop_var_1 = 1
                                                
                                            else:
                                                
                                                print("Please choose a valid answer")
                                        
                                        
                                    else:
                                        
                                        print("\nPlease choose a valid answer\n")
                                        
                        else:
                            
                            print("\nPlease choose a valid answer\n")
                    

                else:

                    print("\nPlease choose a valid answer\n")
                    
    return project_list 

def projectUpdate(project_list = project_list):
    
    message_1 = ""
    
    loop_var_1 = 0
    
    while loop_var_1 == 0:
        
        clear()

        display_df = pd.DataFrame()

        for key in project_list:

            display_df = display_df.append([{"project_id" : key,
                                             "project_name" : project_list[key].project_name,
                                             "project_deliverable" : project_list[key].project_deliverable,
                                             "deadline" : project_list[key].project_deadline}])
       
        print(display_df)
        
        print("*" * 80 + f"\n{message_1}\nPlease select a project, indicate the ID, choose Q to quit\n" + "*" * 80)
            
        answer = str(input()).lower()
            
        if answer == "q":
            
            mainMenu(message = "What will you do now?")
            
        elif answer not in list(display_df.loc[:, "project_id"]):
            
            message_1 = "Choose an existing ID"
            
        else:

            clear()
                
            current_id = answer

            project_completion_list = []

            for key in project_list[current_id].milestone_list:

                if project_list[current_id].milestone_list[key].status == "complete":

                    project_completion_list.append("complete")

                else:

                    project_completion_list.append("not_complete")

            project_completion_percentage = (project_completion_list.count("complete") / len(project_completion_list)) * 100

            milestone_completion_list = {}

            for key in project_list[current_id].milestone_list:

                milestone_completion_check = []

                for key_1 in project_list[current_id].milestone_list[key].phase_list:

                    if project_list[current_id].milestone_list[key].phase_list[key_1].status == "complete":

                        milestone_completion_check.append("complete")

                    else:

                        milestone_completion_check.append("not_complete")

                milestone_completion_list[project_list[current_id].milestone_list[key].description] = (milestone_completion_check.count("complete") / len(milestone_completion_check)) * 100

            clear()

            print("\nThis is the status of the project:\n")
            
            print(f"Total project completion: {project_completion_percentage}%\n\n")

            for key, value in milestone_completion_list.items():

                print(f"{key} / {value}% complete")

            loop_var_1 = 1
    
    return project_list

def viewStats(routine_dict = routine_dict):

    dataset = pd.DataFrame()

    for key in routine_dict:

        for key_1 in routine_dict[key]:

            dataset = dataset.append([{"activity_type" : key_1,
                                       "elapsed_time" : routine_dict[key][key_1]}])
    
    possibilities = set(list(dataset.loc[:, "activity_type"]))
    
    print("*" * 80 + "\nYou have spent on average these many minutes per session for each activity:\n")
    
    for item in possibilities:
        
        print(f"{item}: ", round(np.mean(dataset.loc[dataset.activity_type == item, "elapsed_time"]) / 60, 2))
        
    print("\n" + "*" * 80)
    
    print("*" * 80 + "\nYou have spent in total these many minutes on each activity:\n")
    
    for item in possibilities:
        
        print(f"{item}: ", round(np.sum(dataset.loc[dataset.activity_type == item, "elapsed_time"]) / 60, 2))
        
    print("\n" + "*" * 80)
    
def mainMenu(message, project_list = project_list, routine_dict = routine_dict):
    
    clear()
    
    print("*"*80 + f"\n\n{message}\n\n" + "*"*80,
          "\n\nPlease select an action, indicate its number:\n\n",
          "1. Do routine actions\n 2. Add a project\n 3. Work on a project\n",
          "4. Modify a project\n 5. View project status\n 6. View stats\n 7. Exit")
    
    loop_check = 0
    
    while loop_check == 0:
        
        main_menu_choice = str(input()).lower()

        if main_menu_choice == "1":

            routine_dict = routineCycle()
            
            save_object(obj = routine_dict, filename = "routine_dict.pkl")
            
            mainMenu(message = "What will you do now?")

        elif main_menu_choice == "2":
            
            project_list = addProject()
            
            save_object(obj = project_list, filename = "project_list.pkl")

            save_object(obj = stakeholder_list, filename = "stakeholder_list.pkl")
            
            clear()
            
            print("-" * 80 + "\n\nYour project was added succesfully!" + "-" * 80)
            
            mainMenu(message = "What will you do now?")

        elif main_menu_choice == "3":
            
            projectWork()
            
        elif main_menu_choice == "4":

            message_for_repeating = ""
            
            clear()

            choice_loop_var = 0

            while choice_loop_var == 0:

                print("-" * 80 + f"\n\n{message_for_repeating}\nWhat do you want to do? Choose a number\n\n1. Rewrite a project\n2. Enlarge a project\n" + "-" * 80)

                answer = str(input()).lower()

                if answer == "1":
            
                    project_list = modifyProject()
                    
                    save_object(obj = project_list, filename = "project_list.pkl")
                    
                    print("-" * 80 + "\n\nYour changes were saved succesfully!" + "-" * 80)
                    
                    mainMenu(message = "What will you do now?")

                elif answer == "2":

                    project_list= projectEnlargement()

                    save_object(obj = project_list, filename = "project_list.pkl")
                    
                    print("-" * 80 + "\n\nYour changes were saved succesfully!" + "-" * 80)
                    
                    mainMenu(message = "What will you do now?")

                else:

                    message_for_repeating = "Choose a valid ID"


        elif main_menu_choice == "5":
            
            clear()

            project_list = projectUpdate()
            
            input( "\nPress ENTER to continue\n")
            
            mainMenu(message = "What will you do now?")

        elif main_menu_choice == "6":
            
            clear()
            
            viewStats()
            
            input( "\nPress ENTER to continue\n")
            
            mainMenu(message = "What will you do now?")
            
        elif main_menu_choice == "7":
            
            sys.exit()

        else:

            print("Please choose a valid answer")
            
mainMenu(message = "Welcome back to your life!")