# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Antoine Toullalan
#  Prénom Nom: Rosa Mendas
import strategie
score=0
iteration=0
def get_team_name():
    return "les gentils"

def step(robotId, sensors):
    global score,iteration
    #strategie n°1:
    #return strategie.strategie_braitenberg(robotId, sensors)
    
    #strategie n°2:
    #return strategie.strategie_substomp1(robotId, sensors)
    
    #strategie n°3:
    #return strategie.strategie_substomp2(robotId, sensors)
    
    #strategie n°4:
    return strategie.strategie_genetique2(robotId, sensors)
        
    
    
                
        
