from DB.database import provider, work_with_db, db_update_table
from xmlParser import getDataFromAdvantaXml
from xmlTags import *


def sql_query_update_insert(file_name, getProjectResult):
    sql = provider.get(file_name,
                       UID=getProjectResult['UID'],
                       ParentProjectId=getProjectResult['ParentProjectId'],
                       Name=getProjectResult['Name'],
                       Status=getProjectResult['Status'],
                       PercentComplete=getProjectResult['PercentComplete'],
                       SystemStartDate=getProjectResult['SystemStartDate'],
                       SystemEndDate=getProjectResult['SystemEndDate'],
                       PlannedStartDate=getProjectResult['PlannedStartDate'],
                       PlannedEndDate=getProjectResult['PlannedEndDate'],
                       ActualStartDate=getProjectResult['ActualStartDate'],
                       ActualEndDate=getProjectResult['ActualEndDate'],
                       OwnerId=getProjectResult['OwnerId'],
                       ResponsibleId=getProjectResult['ResponsibleId'])
    db_update_table(sql)


def getDataForDb():
    try:
        print("Updating data...")
        getProjectRes = getDataFromAdvantaXml('STORAGE/GetProject.xml',
                                              tags=GetProjectTags)
        print("Data updated ✓")
        return getProjectRes
    except Exception:
        print("Error while updating database")


def projectInfoUpdate():
    print('Updating database...')
    sql = provider.get('getProjectData.sql')
    result = work_with_db(sql)
    flag = 0
    getProjectRes = getDataForDb()

    for dict_ in result:
        if dict_['UID'] == getProjectRes['UID']:
            flag = 1

    if flag == 0:
        sql_query_update_insert('insertProjectData.sql', getProjectRes)
    else:
        sql_query_update_insert('updateProjectData.sql', getProjectRes)

    print('Database updated ✓\n\n')
