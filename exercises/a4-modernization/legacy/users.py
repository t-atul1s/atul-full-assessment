# Legacy user loader — pre-modernization (Python 2 style patterns)

def load_users(records):
    out = []
    for i in range(len(records)):
        r = records[i]
        if r.has_key('email') and r.has_key('name'):
            out.append({'email': r['email'], 'name': r['name'], 'active': r.get('active', True)})
    return out


def find_by_email(users, email):
    for u in users:
        if u['email'] == email:
            return u
    return None
