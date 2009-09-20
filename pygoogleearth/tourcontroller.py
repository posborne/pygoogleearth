class TourController(object):
    def __init__(self, comobject):
        self.ge_tc = comobject
        
    def __getattr__(self, name):
        if name == 'speed':
            return self.ge_tc.Speed
        elif name == 'pause_delay':
            return self.ge_tc.PauseDelay
        elif name == 'cycles':
            return self.ge_tc.Cycles
        else:
            raise AttributeError
    
    def __setattr__(self, name, value):
        if name == 'speed':
            self.ge_tc.Speed = value
        elif name == 'pause_delay':
            self.ge_tc.PauseDelay = value
        elif name == 'cycles':
            self.ge_tc.Cycles = value
        else:
            raise AttributeError
    
    def play_or_pause(self):
        self.ge_tc.PlayOrPause()
    
    def stop(self):
        self.ge_tc.Stop()
