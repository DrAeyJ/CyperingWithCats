class SiteManager:
    def __init__(self): pass

    def raise_operating_error(self, operation, message): #console writing instead of raising exception
        import datetime
        time = datetime.datetime.now() #capture current time
        print(f'\n\nWHILE PERFORMING OPERATION AN ERROR OCCURRED\nFAILED OPERATION: {operation}\nERROR MESSAGE: {message}\n\n') #console error output
        with open('error_log.txt', 'a') as er_log:
            er_log.write(f'{time}\nWHILE PERFORMING OPERATION AN ERROR OCCURRED\nFAILED OPERATION: {operation}\nERROR MESSAGE: {message}\n\n\n\n') #logging the error

    def request_auth(self, user_id):        #console authorization request
        answer = input(f'AN user_id PROFILE REQUESTED AUTHORIZATION\nPROFILE: {user_id}\nAPPROVE REQUEST? [Y/N]: ') #request in console
        if answer.lower() not in ['y', 'n']: return self.request_auth(user_id) #recursive asking until normal answer
        return True if answer.lower() == 'y' else False #return answer

    def authorize_user_by_request(self, user_id): #authorise user: allow him to use cuser_idhering
        if self.request_auth(user_id):
            with open('user_authorization.txt') as auth_file:
                auth_list = {i[:-1].split(':')[0]: {'authorized': i[:-1].split(':')[1], 'name': i[:-1].split(':')[2], 'password': i[:-1].split(':')[3]} for i in auth_file.readlines()}
                print(auth_list)
                auth_list[user_id]['authorized'] = 'Y'
            with open('user_authorization.txt', 'w') as auth_file:
                for auth_user_id in auth_list:
                    auth_file.write(f'{auth_user_id}:{auth_list[auth_user_id]['authorized']}:{auth_list[auth_user_id]['name']}:{auth_list[auth_user_id]['password']}\n')
                return 1
        else:
            return 0

    def login_user_id(self, data): #add new user_id profile in list
        with open('user_authorization.txt') as auth_file:
            f = [i[:-1] for i in auth_file.readlines()]
        said_user = False
        for i in range(len(f)):
            if data[0] == f[i].split(':')[2]:
                if data[1] != f[i].split(':')[3]: return 'Invalid password.'
                said_user = f[i].split(':')[0]
                break
        if not said_user:
            user_id = str(max([int(i.split(':')[1]) for i in f]) + 1).zfill(8) if [int(i.split(':')[1]) for i in f] else '00000000'
            f.append(f'{user_id}:N:{data[0]}:{data[1]}')
            with open('user_authorization.txt', 'w') as file:
                for user in f:
                    user = user.split(':')
                    file.write(f'{user_id}:{user[1]}:{user[2]}:{user[3]}\n') #text file auth standard representation
        else: user_id = said_user
        return f'Registered: {user_id}' #return user info.txt into get_auth

    def get_authorization(self, user_id): #fetching info on user_id profile
        with open('user_authorization.txt') as auth_file:
            auth_list = {i[:-1].split(':')[0]: {'authorized': i[:-1].split(':')[1], 'name': i[:-1].split(':')[2], 'password':i[:-1].split(':')[3]} for i in auth_file.readlines()}
            if user_id in auth_list: return {'user_id': user_id, 'authorized': auth_list[user_id]['authorized'], 'name': auth_list[user_id]['name'], 'password': auth_list[user_id]['password']}
        return None
