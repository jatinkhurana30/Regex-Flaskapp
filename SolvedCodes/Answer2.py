import re
import sys

def find_answer2():
    log_file = open("assignment.log")
    log_data = log_file.readlines()
    log_list = {
        "machine1":[],
        "machine2":[]
    }

    regexp_machine1 = re.compile('Ping Identity')
    regexp_machine2 = re.compile('PulseSecure')

    for line in log_data:
        if regexp_machine1.search(line):
            logs1 = []
            dvc_host = re.findall('(?<=dvchost=).+?(?= )', line)[0]
            src = re.search("(?<=src=)([0-9]{1,3}[.][0-9]{1,3})[.][0-9]{1,3}[.][0-9]{1,3}(?= )", line).group(0)
            print('dvchost =' + dvc_host)
            logs1.append('dvchost =' + dvc_host)
            print('src = ' + src)
            logs1.append('src = ' + src)

            log_list["machine1"].append(logs1)
            print()
        elif regexp_machine2.search(line):
            logs2 = []
            time = re.findall('(?<=time="").+?(?=")', line)[0]
            vpn = re.findall('(?<=vpn=).+?(?= )', line)[0]
            user = re.findall('(?<=user=).+?(?= )', line)[0]
            user_activity = re.findall('(?<=msg="").+(?="")', line)[0]
            logs2.append('Time = '+ time)
            logs2.append('VPN = '+ vpn)
            logs2.append('User = '+ user)
            logs2.append('Activity Done '+ user_activity)
            print('Time = ', time)
            print('VPN = ', vpn)
            print('User = ', user)
            print('Activity Done ', user_activity)
            print()
            log_list["machine2"].append(logs2)
        else:
            continue

    log_file.close()
    return log_list