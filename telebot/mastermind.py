

def get_response(upd):
    user = upd.message.from_user
    fname = user.first_name
    lname = user.last_name

    if user.username == 'vlaskz':
        res = 'Hi Master!, We\'re glad to see you again'
    else:
        res = 'thanks for your msg, {FIRST_NAME} {LAST_NAME}'.format(FIRST_NAME = fname, LAST_NAME = lname)
    return res