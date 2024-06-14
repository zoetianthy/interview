# It’s a couple of weeks after joining your new team and you've been tasked with analyzing some background jobs 
# for compute time used. The jobs are taking longer than expected, so your task is to determine the total cost of the most 
# expensive job.

#Your team’s senior engineer explained that the jobs by themselves usually don’t take very long to complete, 
# but each job can spawn between 1–15 other jobs, which can themselves spawn more jobs. They explain that the total cost 
# for a job is the sum of how long the job took plus the time all of the jobs it spawned took.

#They sketch out a quick example illustrating their point:

#         A: 5ms
#          / \
#        /   \
#   B: 1ms   C: 3ms
#The total cost for A is 5 + 1 + 3, or 9ms.

#They also mention that the top-level jobs like A do not have a parent_id set, 
# and that the jobs are stored in execution order - meaning spawned jobs occur after the spawning job in the file.

#Feeling that you’ve got a handle for the problem, 
# they share the jobs.json file with you and ask you to send them the total cost of the longest job within the hour. 
# Oddly enough, they also mention that the third-longest job took 8967ms to run…

#Each id only occurs once in the file, although it may appear many times as a parent_id.

#Please respond with the total cost for the longest job in jobs.json.


# thought process : go thru every date line/tree, total coast  = sum of nodes of a tree, find out the higest sum/total cost



#first solution during interivew
#f = open('jobs.json')
#jobs = json.load(f)
#for i in jobs:
#   print(i)
#f.close()
#class Node:
#    def __init__(self):
#        self.key = 0
#        self.child = []
#def newNode(key):
#    temp = Node()
#    temp.key = key
#    temp.child = []
#    return temp
#def sumNodes(root):
#    Sum = 0
#    if root == None:
#        return 0
#    q = []
#    q.append(root)
#    while len(q) != 0:
#        n = len(q)
#        while n > 0:
#            p = q[0]
#            q.pop(0)
#            Sum += p.key
#            for i in range(len(p.child)):
#                q.append(p.child[i])
#            n -= 1
#    return Sum
#root = jobs
#print(max(Sum))


import json

# Load the JSON data from the file
with open('jobs.json') as f:  
    jobs = json.load(f)  

# Create a dictionary to store the jobs by their id
jobs_dict = {}
for job in jobs:  
    job_id = job['id']  # Get the job's unique identifier
    jobs_dict[job_id] = job  # Add the job to the jobs_dict dictionary with the job_id as the key

# Create a dictionary to store the children for each job
children_dict = {}
for job in jobs:  
    parent_id = job.get('parent_id')  # Get the parent_id of the job (if it exists)
    if parent_id:  
        if parent_id not in children_dict:  
            children_dict[parent_id] = []  # Initialize an empty list for the parent_id in the children_dict
        children_dict[parent_id].append(job['id'])  # Add the job's id to the parent_id's list of children

# Represents a node of an n-ary tree
class Node:
    def __init__(self, key, duration):  
        self.key = key  
        self.duration = duration  
        self.child = []  

# Function to build the tree from the job data
def build_tree(job_id):
    job = jobs_dict[job_id]  
    root = Node(job_id, job['duration'])  
    if job_id in children_dict:  
        for child_id in children_dict[job_id]: 
            root.child.append(build_tree(child_id))  
    return root  

# Function to compute the sum of all elements in the tree
def sumNodes(root):
    if root is None:  # If the root is None, return 0
        return 0
    total_sum = root.duration  # Initialize the total sum with the root's duration
    for child in root.child:  # Iterate over each child node
        total_sum += sumNodes(child)  # Recursively add the sum of the child nodes
    return total_sum  # Return the total sum

# Find the job with the highest total cost
max_cost = 0  
max_job_id = None  

for job in jobs:  
    if job.get('parent_id') is None:  
        root = build_tree(job['id'])  
        total_cost = sumNodes(root) 
        if total_cost > max_cost:  
            max_cost = total_cost  
            max_job_id = job['id']  

print(f"The total cost for the longest job is: {max_cost} ms")  # Print the maximum cost





