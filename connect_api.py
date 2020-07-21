#Prior to running script activate venv with ".\env\Scripts\activate"
# Set .env file with USER=      PASS=
from decouple import config
USER = config('USER')
PASS = config('PASS')

import jenkins
import time

server = jenkins.Jenkins('http://localhost:8080', username= USER, password= PASS)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

#The various api commands

#server.create_job('cool-job', jenkins.EMPTY_CONFIG_XML)
#jobs = server.get_jobs()
#print(jobs)
my_job = server.get_job_config('multi-step-pipeline')
#print(my_job) # prints XML configuration
server.build_job('multi-step-pipeline')
time.sleep(8)
server.build_job('delay-ok-pipeline')
#time.sleep(2)
#server.disable_job('new-build')
#server.build_job('tutorial')
#server.copy_job('tutorial', 'duplicate-tutorial')
#time.sleep(5)
#server.enable_job('duplicate-tutorial')
#server.reconfig_job('duplicate-tutorial', jenkins.RECONFIG_XML)
#other_job = server.get_config('duplicate-tutorial')
#print(other_job)
#server.build_job('duplicate-tutorial')
#server.reconfig_job('duplicate-tutorial', jenkins.RECONFIG_XML)
#time.sleep(10)
#server.delete_job('duplicate-tutorial')
#print(duplicate-tutorial ran)

# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
# server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
# last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
# build_info = server.get_build_info('api-test', last_build_number)
# print build_info

# get all jobs from the specific view
# jobs = server.get_jobs(view_name='View Name')
# print(jobs)
