from datetime import datetime, timedelta

class TimerModel:
    def __init__(self):
        self.minutes = None
        self.time_left = None
        self.end_datetime = None

    def set_30_min(self):
        self.minutes = timedelta(minutes = 30)
        self.time_left = self.minutes

    def start_timer(self):
        if self.minutes is None:
            return
        self.end_datetime = datetime.now() + self.time_left

    def check_time(self):
        if datetime.now() >= self.end_datetime:
            return True
        else:
            return False
        
    def convert_delta_to_str_time(self, delta):
        hours = self.time_left.days * 24 + self.time_left.seconds // 3600
        minutes = (self.time_left.seconds % 3600) // 60 
        seconds = self.time_left.seconds % 60
        return f"{hours}:{minutes:02}:{seconds:02}"
 
         
    def get_time(self):
        if self.minutes is None:
            return "0:00:00"
        if self.end_datetime is None:
            return self.convert_delta_to_str_time(self.time_left)
        self.time_left = self.end_datetime - datetime.now()
        return self.convert_delta_to_str_time(self.time_left)

    def stop_timer(self):
        self.end_datetime = None

    def reset_timer(self):
        self.end_datetime = None
        self.time_left = self.minutes