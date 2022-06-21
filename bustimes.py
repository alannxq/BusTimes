from datetime import datetime, timedelta


class Time:
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)
        
    def __repr__(self):
        minute = self.minute if len(str(self.minute)) > 1 else "0" + str(self.minute)
        hour = self.hour if len(str(self.hour)) > 1 else "0" + str(self.hour)
        return f"{hour}:{minute}"

    @staticmethod
    def string_to_time(string_time):
        '''
        Works only if given in the format of "HH MM"
        '''
        hour, minute = string_time.split()
        return Time(hour, minute)

    def minutes_left(self):
        # due_time = timedelta(hours=self.hour, minutes=self.minute)
        # cur_time = timedelta(hours=cur_time.hour, minutes=cur_time.minute)
        # print(due_time.total.minutes)

        cur_time = datetime.now()
        due_time = datetime(year=cur_time.year, month=cur_time.month, day=cur_time.day, hour=self.hour, minute=self.minute)
        remaining = due_time - cur_time
        return remaining.total_seconds() // 60 + 1


## UXBRIDGE TO SLOUGH
UTS_bus_times = [
    Time(6,25),
    Time(6,45),
    Time(7,20),
    Time(7,55),
    Time(8,30),
    Time(9,12),
    Time(9,42),
    Time(10,12),
    Time(10,42),
    Time(11,12),
    Time(11,42),
    Time(12,12),
    Time(12,42),
    Time(13,12),
    Time(13,42),
    Time(14,12),
    Time(14,42),
    Time(15,12),
    Time(15,53),
    Time(16,23),
    Time(16,53),
    Time(17,33),
    Time(18,5),
    Time(18,35),
    Time(19,14),
    Time(19,37)
]

CTS_bus_times = [
    Time(6,13),
    Time(6,46),
    Time(7,11),
    Time(7,49),
    Time(8,23),
    Time(8,48),
    Time(9,23),
    Time(9,48),
    Time(10,23),
    Time(10,48),
    Time(11,23),
    Time(11,48),
    Time(12,23),
    Time(12,48),
    Time(13,23),
    Time(13,48),
    Time(14,23),
    Time(14,53),
    Time(15,27),
    Time(15,53),
    Time(16,27),
    Time(16,53),
    Time(17,27),
    Time(17,53),
    Time(18,27),
    Time(18,57),
    Time(19,27)
]

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H %M")
    time = Time.string_to_time(current_time)

    return time


def available_times(location):
    if location == "cippenham":
        bus_times = CTS_bus_times
    else:
        bus_times = UTS_bus_times

    for index, btime in enumerate(bus_times):
        if btime.hour >= get_current_time().hour:
            if btime.hour > get_current_time().hour or btime.minute > get_current_time().minute:
                next_time = bus_times[index]
                try:
                    times = bus_times[index:index+4]
                except:
                    times = bus_times[index:]
                return times
    
    return []
