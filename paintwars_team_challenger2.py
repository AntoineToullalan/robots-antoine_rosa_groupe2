import math

def extend_sensors(sensors):
    for key in sensors:
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors

def strategie_substomp2(robotId, sensors):
    sensors=extend_sensors(sensors)
    #eviter les collisions avec les murs
    def priorite1(sensors):
        if(sensors["sensor_front"]["distance_to_wall"]+sensors["sensor_front_left"]["distance_to_wall"]+sensors["sensor_front_right"]["distance_to_wall"]<3.):
            return True
        return False
    #eviter les collisions avec les robots de la même equipe
    def priorite2(sensors):
        for key in ["sensor_front","sensor_front_left","sensor_front_right"]:
            if(sensors[key]["distance_to_robot"]<1 and sensors[key]["isSameTeam"]):
                    return True
        return False
    #suivre les robots de l'équipe adverse
    def priorite3(sensors):
        for key in sensors:
            if(sensors[key]["distance_to_robot"]<1 and not sensors[key]["isSameTeam"]):
                return key
        return False
        
    translation=1
    rotation=0
    
    s=priorite2(sensors)
    t=priorite3(sensors)
    if(priorite1(sensors)): 
        if sensors["sensor_front_right"]["distance_to_wall"] < 1 or sensors["sensor_front"]["distance_to_wall"] < 1:
            rotation = -0.4*sensors["sensor_front"]["distance_to_wall"]-0.3*sensors["sensor_front_right"]["distance_to_wall"]
        elif sensors["sensor_front_left"]["distance_to_wall"] < 1:
            rotation = sensors["sensor_front_left"]["distance_to_wall"]
    elif(s):
        if sensors["sensor_front_right"]["distance_to_robot"] < 1 or sensors["sensor_front"]["distance_to_robot"] < 1:
            rotation = -sensors["sensor_front"]["distance_to_robot"]-sensors["sensor_front_right"]["distance_to_robot"]
        elif sensors["sensor_front_left"]["distance_to_robot"] < 1:
            rotation = sensors["sensor_front_left"]["distance_to_robot"]
    elif(t):
        if(t=="sensor_left"):
            rotation=-0.5
        elif(t=="sensor_front_left"):
            rotation=-0.25
        elif(t=="sensor_front"):
            rotation=0
        elif(t=="sensor_front_right"):
            rotation=0.25
        elif(t=="sensor_right"):
            rotation=0.5
        elif(t=="sensor_back_right"):
            rotation=0.75
        elif(t=="sensor_back"):
            rotation=1
        elif(t=="sensor_back_left"):
            rotation=-0.75
        
    return max(-1,min(translation,1)),max(-1, min(rotation, 1))


score=0
iteration=0
def get_team_name():
    return "les gentils"

def step(robotId, sensors):
    global score,iteration

    return strategie_substomp2(robotId, sensors)
    
    