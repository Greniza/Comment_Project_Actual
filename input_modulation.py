import csv
import random as rng


revised_list = [line[:3] for line in csv.reader(open('name_csv.csv', 'r'))]
headers = revised_list.pop(0)
hnames = ['Alex', 'Ryan', 'Jack', 'Colin', 'Simon', 'Mason', 'Matt',
          'Hayden', 'Max', 'Thomas', 'Jacen', 'Dustin', 'Hugh', 'Matthew', 'John',
          'Christopher', 'Ethan', 'Henry', 'Nicholas', 'Lincoln', 'Evan',
          'Jonah', 'Tadhg', 'Kennedy', 'Daniel', 'Ashok', 'Ian', 'Tod', 'Justin',
          'Aneesh', 'Cameron', 'Jackson', 'David', 'Andre', 'SkyCat', 'Red',
          'Viraj', 'Luca', 'Asa', 'Cheney', 'Musa', 'Walker', 'Garrett', 'Luke', 'Frank', 'Ant',
          'Anshul', 'Andrew', 'Emilio', 'Vernon', 'Charlie', 'Oliver', 'Kanye', 'Gucci', 'Trevor',
          'Abe', 'Darren', 'Teddy', 'Noah', 'Jason', 'ZW', 'Zach']
snames = ['Jillian', 'Audrey','Lauren', 'Claire', 'Kendall', 'Anna', 'Meaghan',
          'Stephanie', 'Isabelle', 'Noe', 'Lucy', 'Sherry', 'Rachel', 'Maud',
          'Olivia', 'Emily', 'Paige', 'Lydia', 'Maya', 'Alma', 'Joanna', 'Addison',
          'Ella', 'Alexa', 'Lexi', 'Sophie', 'Skye', 'Sara',
          'Christina', 'Sheilan', 'Simran', 'Aashna', 'Rhea', 'Ellie', 'Brooke', 'Ky', 'Harper',
          'Sydney', 'Lola', 'Greta', 'Amanda', 'Zoe', 'Megan', 'Maddy', 'Mary', 'Ava', 'Kelly',
          'Maxine', 'Hannah', 'Madeleine', 'Ingrid', 'Jane', 'Bridget', 'Grace', 'Daisy', 'Emma',
          'Sarah', 'Vasti', 'Rebecca', 'Becca', 'Susan', 'Samantha', 'Gracie', 'Tara', 'Ekki',
          'Alison', 'Aida']

for line in range(len(revised_list)):
    if not revised_list[line]:
        continue
    if revised_list[line][2] in hnames:
        p = 'h'
    else:
        p = 's'
    revised_list[line].insert(3, p)
while [] in revised_list:
    del revised_list[revised_list.index([])]
headers.insert(3, 'Pronoun')
revised_list.insert(0, headers)

raw_in = revised_list
tags = ['work_ethic', 'habits', 'homework', 'participation',
        'asks_questions', 'test_avg', 'final_score', 'overall_grade']
headers = raw_in.pop(0) + tags
for x in range(len(raw_in)):
    for item in tags[:-1]:
        q = rng.randint(-50, 200)/10
        if q < 0:
            raw_in[x].append(100.0)
        else:
            raw_in[x].append(100.0 - q)
    q = raw_in[x][4:]
    raw_in[x].append(float(str(sum(q)/len(q))[:5]))
outloc = csv.writer(open('student_grades.csv', 'w'))
outloc.writerow(headers)
for info in raw_in:
    if len(info) == len(headers):
        outloc.writerow(info)
