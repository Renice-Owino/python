import random

teamMembers = ['Renice','Moha','Yvette','Nasibo','Shaffie','Neville','Letty','Maureen','Kennedy','Zack','Anwar','Wambua','Shem','Brian','Jason','Jamila','Atsula','Wendy']

teams = ['Team1','Team1','Team2','Team2','Team3','Team3','Team4','Team4','Team5','Team5','Team6','Team6','Team7','Team7','Team8','Team8','Team9','Team9']

for i in teams:
    name = random.choice(teamMembers)
    print i + " - " + name
    teamMembers.remove(name)
