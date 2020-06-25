import random
class Agent:
    def __init__(self,is_available,available_since,roles):
        self.is_available = is_available
        self.available_since = available_since
        self.roles = roles


def issue(select_mode, Agent, issue_role):
    valid_agent = []
    for agent in Agent:
        if (agent.is_available):
            if (all(x in agent.roles for x in issue_role)):
                print(agent.roles)
                valid_agent.append(agent)
            
    if select_mode == "all available":
        return valid_agent

    elif select_mode == "least busy":
        
        return sorted(valid_agent, key=lambda agent: agent.available_since, reverse= True)
    
    else :
        return [random.choice(valid_agent)]

#Example output and way to deliver the output
        
'''
Agents = [Agent(True,15,["sales","support"]),Agent(True,12,["sales","support"])]
print(issue("random",Agents,["sales","support"])[0].available_since)
'''
