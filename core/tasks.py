import os
import django
import sys

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'CPTBackend.settings'
django.setup()

import pprint
import json
from core.models import WebUser, Log
from datetime import datetime
from core.services import SMS
from core.utility import decryptPhoneNumber


with open("core/scheduled_tasks.json") as f:
    tasks = json.load(f)

#TODO: blue站内信
def send_notifitaion(user: WebUser, message: str):
    pass

def launch_tasks(time: int):
    # print(f"Event triggered at {datetime.now()}, with time {time}.")
    # log = Log.objects.create(
    #     user=None,
    #     log=f"Event triggered at {datetime.now()}, with time {time}."
    # )
    # log.save()
    # for task in tasks:
    #     pprint.pprint(task)
    #     break
    
    sub_tasks = filter(lambda x: x["time"] == str(time), tasks)
    for sub_task in sub_tasks:
        for user in WebUser.objects.all():
            # update user validity
            user.validity_check()
            # check group
            if user.group not in sub_task['groups']:
                continue
            startDate = datetime.combine(user.startDate, datetime.min.time())
            today = datetime.combine(datetime.now().date(), datetime.min.time())
            currentDay = (today - startDate).days+1
            if currentDay not in sub_task['days']:
                continue
            # check criteria
            if 'not_banned' in sub_task['criteria']:
                if user.banFlag:
                    continue
            if 'task_not_done' in sub_task['criteria']:
                if user.currentDay >= currentDay:
                    continue
            if 'has_unsent_quality_check_fail_msg' in sub_task['criteria']:
                skip = False
                if skip:
                    continue
            # send message
            print(f"Message {sub_task['_note']} sent to {user.phoneNumber} on task {sub_task['task_no']}, day {currentDay}")
            # res = SMS.SmsService.sendMsg(decryptPhoneNumber(user.phoneNumber), sub_task['template_code'])
            #TODO: blue站内信
            # if res['statusCode'] == 200:
            #     log = Log.objects.create(
            #         user=user,
            #         log=f"Message sent to {user.phoneNumber} on task {sub_task['task_no']} successfully."
            #     )
            #     log.save()
            # else: 
            #     log = Log.objects.create(
            #         user=user,
            #         log=f"Message sent failed. Error message: " + str(res)
            #     )
            #     log.save()

    
    
if __name__ == "__main__":
    launch_tasks(8)
    launch_tasks(20)
    
    # pprint.pprint(tasks)
    
    
