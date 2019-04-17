# dott.dott

from datetime import datetime, timedelta
from time import sleep


class Runner(object):
    """The Runner class.
    
    Attributes:
        func: A function to execute.
        timer: Timer values, describing time between func execution.
        next_run: A function calculating the next run time.
    """
    def __init__(self, func, timer, calc_next_run):
        """Inits a new instance of Runner."""
        self.func = func
        self._timer = timer
        self.next_run = None
        self.has_run = False
        self.calc_next_run = calc_next_run
        self.run()

    @property
    def timer(self):
        return self._timer

    @timer.setter
    def timer(self, arg):
        if arg.__class__ != list:
            self._timer = [arg]
        else:
            self._timer = arg

    @staticmethod
    def get_now():
        """Returns datetime.now().

        Returns:
            A datetime instance.
        """
        return datetime.now()


    def run(self):
        self.func()
        self.has_run = True
        while True:
            if self.has_run:
                self.next_run = self.calc_next_run(self.timer)
                self.has_run = False    
            if self.next_run < datetime.now():
                self.func()
                self.has_run = True
            else:
                sleep(60)


class HourRunner(Runner):
    """The HourRunner class inherits from Runner."""
    def __init__(self, func, timer):
        """Inits a new instance of HourRunner."""
        Runner.__init__(self, func, timer, self._calc_next_run)

    @staticmethod
    def _calc_next_run(timer):
        return HourRunner.get_now() + timedelta(hours=int(timer[0]))


class DayRunner(Runner):
    """The DayRunner class inherits from Runner."""
    def __init__(self, func, timer):
        """Inits a new instance of DayRunner."""
        Runner.__init__(self, func, timer, self.calc_next_run)

    @staticmethod
    def _calc_next_run(timer):
        current = DayRunner.get_now()
        while True:
            # For each timer value in the timers collection; create a
            # datetime object using the current date and the time
            # described by the timer value.
            for val in timer:
                hrs, mins = val.split(":")
                next_run = datetime(
                    current.year,
                    current.month,
                    current.day,
                    int(hrs), 
                    int(mins)
                )
                if next_run > DayRunner.get_now():
                    return next_run
            current = current + timedelta(days=1)