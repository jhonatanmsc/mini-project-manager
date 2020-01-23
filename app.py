import json


def set_projects_to(users, project, user_type):
    for user in project[user_type]:
        if not user in users:
            users[user] = []
        users[user].append(project['name'])
        

def main():
    data = {}

    with open('source_file_2.json') as json_file:
      data = json.load(json_file)

    sorted_data = sorted(data, key=lambda x: abs(0 - x['priority']))

    managers = {}
    watchers = {}

    for project in sorted_data:
        set_projects_to(managers, project, 'managers')
        set_projects_to(watchers, project, 'watchers')

    #Exporting files
    with open('managers.json', 'w') as managers_json:
        json.dump(managers, managers_json)

    with open('watchers.json', 'w') as watchers_json:
        json.dump(watchers, watchers_json)

if __name__ == '__main__':
    main()