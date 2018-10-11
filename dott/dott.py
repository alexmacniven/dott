# dott.dott

from datetime import datetime, timedelta
from time import sleep


class Dott(object):
    """The Schedule class."""

    def __init__(self, func, rule, time, *targs, msg=False, cprint=print):
        """Constructs an instance of Dott.

        Args:
            func: A function to invoke
            rule: The type of scheduling (day or hour)
            time: First rule element.
            *targs: Additional rule elements.
            msg: Prints the next run time when True.
            cprint: Function to use for printing, default is `print()`.

            Note:
                When `--day` is supplied as the rule, then the `time`
                should be in 24-hour format. i.e. 0800.

                If `--hour` is supplied as the rule, then the `time`
                should be the number of hours between invocation.
        """
        self.func = func
        self.rule = rule
        self.times = time
        # if len(targs) > 0:
        #     self.times.extend(list(targs))
        self.msg = msg
        self.print = cprint
        self.next_run = None
        self.run()

    
    def run(self):
        """Runtime for an instance of Schedule."""
        # Evaluate whether the application should be run rightaway.
        # The criteria is;
        #   - '--hour' has been supplied as `rule`.
        if self.rule == 'hour':
            self.func()
        has_run = True

        while True:
            if has_run:
                self.calculate_next_run()
                has_run = False
                if self.msg:
                    self.print(
                        '\nNext execution at {}...'.format(str(self.next_run))
                    )    
            if self.next_run < datetime.now():
                self.func()
                has_run = True
            else:
                sleep(60)

    def calculate_next_run(self):
        """Calculates the next time the function is run."""
        # if rule is --hour, set the next run time as now + hour
        if self.rule == 'hour':
            self.next_run = datetime.now() + timedelta(
                hours=int(self.times[0])
            )
        elif self.rule == 'day':
            # Get the current day, month, and year values.
            current = datetime.now()
            day = current.day
            month = current.month
            year = current.year

            # Set next_run to a date that has past.
            self.next_run = datetime(year, month, day)
            time_set = False
            while not time_set:
                for time in self.times:
                    # Split the time into HH and MM
                    hour, minute = time.split(':')
                    # Cast hour and minute into integer type.
                    hour = int(hour)
                    minute = int(minute)

                    # Make a datetime with the given hours and minutes.
                    self.next_run = datetime(year, month, day, hour, minute)
                    if self.next_run > datetime.now():
                        time_set = True
                        break
                # Move to the next days day, month, and year values.
                current = current + timedelta(days=1)
                day = current.day
                month = current.month
                year = current.year
