#!/usr/bin/env python3

import time
import pyMatic

class pyIrrigation:

    def __init__(self):
        self.importConfiguration()
        self.initController()
        self.run()
        print(self.schedule)

    def importConfiguration(self):
        import pyIrrigation_conf as iConf
        self.host = iCont.host
        self.port = iConf.port

        self.schedule = {}

        for v in dir(iConf):
            if v.startswith('zone'):
                self.schedule[v[-1]] = eval('iConf.%s'%v)

    def initController(self):
        self.controller = pyMatic.iMatic(self.host, self.port)

    def parseWeekday(self, day):
        if type(day) == int:
            return day
        elif type(eval(day)) == int:
            return eval(day)
        
        try:
            return ['mon', 'tues', 'wed', 'thur', 'fri', 'sat', 'sun'].index(day)+1
        except ValueError:
            pass

        try:
            return ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(day)+1
        except ValueError:
            pass

        raise ValueError('Incorrect day specification in config file')

    def checkSchedule(self):
        now = dt.now()
        wd = now.isoweekday()
        for zone in self.schedule.items():
            

    def run(self):
        while True:
            self.checkSchedule()
            time.sleep(60)


if __name__ == '__main__':
    pI = pyIrrigation()

