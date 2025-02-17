class Vehicle:
    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction
    
    def command(self, command):
        if command["command"] == "accelerate":
            self.speed += command["value"]
        elif command["command"] == "brake":
            self.speed = max(0, self.speed - command["value"])
        elif command["command"] == "steer":
            self.direction = command["direction"]
            
        return {
            "speed": self.speed,
            "direction": self.direction
        }