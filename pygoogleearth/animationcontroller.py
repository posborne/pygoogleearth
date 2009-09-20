import getime

class AnimationController(object):
    """
    This contains animation options and controls.
    
    Use this interface to control animation. To get an instance 
    of IAnimationControllerGE, call IApplicationGE::AnimationController.
    
    Note:
    This interface always reflects the current state of the application's 
    animation, even if changes occur after creation.
    """
    def __init__(self, comobject):
        self.ge_fc = comobject
    
    def __getattr__(self, name):
        if name == 'slider_time_interval':
            return self.ge_fc.SliderTimeInterval
        elif name == 'current_time_interval':
            return self.gc_fc.CurrentTimeInterval
        else:
            raise AttributeError
        
    def __setattr__(self, name, value):
        if name == 'slider_time_interval':
            self.ge_fc.SliderTimeInterval = value
        elif name == 'current_time_interval':
            self.ge_fc.CurrentTimeInterval = value
        else:
            raise AttributeError
            
    def play(self):
        """
        Starts playing animation.

        Plays animation with current settings if available.
        """
        self.ge_fc.Play()
        
    def pause(self):
        """
        Pauses current animation.
        
        Pauses animation if one is playing.
        """
        self.ge_fc.Pause()
    
    