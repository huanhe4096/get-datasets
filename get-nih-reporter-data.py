'''
Download Grant Information from NIH RePORTER API
'''
#%% load libs
import requests
from pprint import pprint

print('* load libs')


#%% get grant info
# grant_number = 'UG3EB034710'
def get_grant_info(grant_number):
    '''
    Get grant information from NIH RePORTER API

    For more information, see: https://api.reporter.nih.gov/
    '''
    url = 'https://api.reporter.nih.gov/v2/projects/search'
    request_body = {
        "criteria": {
            "project_nums": [
                grant_number
            ],
        },
        "include_fields": [
            "ApplId", "SubprojectId","FiscalYear",
            "Organization", 
            "ProjectNum",
            "ProjectNumSplit","ContactPiName",
            "FullStudySection",
            "ProjectStartDate","ProjectEndDate",
            "ProjectTitle", "PhrText",
        ],
        "offset":0,
        "limit":25,
        "sort_field":"project_start_date",
        "sort_order":"desc"
    }

    # request headers
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=request_body, headers=headers)
    return response.json()

print('* defined get_grant_info')
grant_info = get_grant_info('K99AG068425')
pprint(grant_info)
