import datetime
import robot

print((datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H") + ':00')
r = robot.get_version()
print(r)
