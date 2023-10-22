
# 25 * 4 deserve a long break 15mins
class PomodoroTimer():
    def __init__(self, mins):
        self.running = False
        self.seconds = 0
        self.max_seconds = mins 


    def start(self):
        self.running = True
        self.seconds = 0


    def stop(self):
        self.running = False


    def get_seconds(self):
        return self.seconds
    

    def get_status(self):
        return self.running
    
    def inc_second(self):
        self.seconds += 1

    def pause(self):
        pass


    def resume(self):
        pass

    def skip(self):
        pass
