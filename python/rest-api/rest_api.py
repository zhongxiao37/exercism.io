import json

class RestAPI(object):
    def __init__(self, database=None):
        self._database = database

    def get(self, url, payload=None):
        if url == '/users':
            if payload is None:
                return json.dumps(self._database)
            else:
                payload_json = json.loads(payload)
                users = [record for record in self._database['users'] for user in payload_json['users'] if user == record['name']]
                return json.dumps({'users': users})


    def post(self, url, payload=None):
        payload_json = json.loads(payload)
        if url == '/add':
            user = {'name': payload_json['user'],
                    'owes': {},
                    'owed_by': {},
                    'balance': 0
                    }
            self._database['users'].append(user)
            return json.dumps(user)
        elif url == '/iou':
            lender = payload_json['lender']
            borrower = payload_json['borrower']
            users = []
            for user in self._database['users']:
                amount = payload_json['amount']
                if user['name'] == lender:
                    # check if lender owes borrower
                    if borrower in user['owes'].keys():
                        _min_amt = min(user['owes'][borrower], amount)
                        user['owes'][borrower] -= _min_amt
                        if user['owes'][borrower] == 0:
                            user['owes'].pop(borrower)
                        user['balance'] += _min_amt
                        amount -= _min_amt

                    # track owed_by
                    if amount > 0:
                        if borrower in user['owed_by'].keys():
                            user['owed_by'][borrower] += amount
                        else:
                            user['owed_by'][borrower] = amount

                    user['balance'] += amount
                    users.append(user)
                elif user['name'] == borrower:
                    # check if lender owes borrower
                    if lender in user['owed_by'].keys():
                        _min_amt = min(user['owed_by'][lender], amount)
                        user['owed_by'][lender] -= _min_amt
                        if user['owed_by'][lender] == 0:
                            user['owed_by'].pop(lender)
                        amount -= _min_amt
                        user['balance'] -= _min_amt

                    # check owes
                    if amount > 0:
                        if lender in user['owes'].keys():
                            user['owes'][lender] += amount
                        else:
                            user['owes'][lender] = amount
                    user['balance'] -= amount
                    users.append(user)
            
            return json.dumps({'users': users})

            
