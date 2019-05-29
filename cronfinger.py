import time
import osquery
import os, sys, re, threading

class ReadLog:

    def __init__(self):
        self._logfile = "logfile"

    def insert(self):
        self.token = ""
        instance = osquery.SpawnInstance()
        instance.open()
        while True:
            try:
                time.sleep(60)
      
                ret = instance.client.query("select command as cmd from crontab")
                res_s = ret.response
      

                joinstr = ""
                for item in res_s:
                        joinstr= joinstr +  item['cmd']
      
                joinstr = joinstr + '192.168.1.5'
                import hashlib
                m1 = hashlib.md5()
                m1.update(joinstr)
                token = m1.hexdigest()
               
                import DataCenter
                log = DataCenter.Syslog("192.168.1.5")
                message_info = '{"source":"192.168.1.5","cnt":5,'+'"token":"'+token + '"}'
                log.send(message_info, syslog_client.Level.INFO)
                print(token)

            except KeyboardInterrupt:
                break

    def start(self):
        self.status = ""
        threadings = []
        threadings.append(threading.Thread(target=self.insert))

        for t in threadings:
            t.start()

if __name__ == '__main__':
    Commandlog = ReadLog()
    Commandlog.start()
