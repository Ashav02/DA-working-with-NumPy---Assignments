

import numpy as np

messages = np.array([[55, 60, 45, 35, 30, 45, 50],
                     [32, 35, 57, 44, 66, 78, 49],
                     [11, 54, 12, 15, 65, 26, 33],
                     [29, 25, 56, 97, 46, 64, 49]])

new_user = np.array([9, 10, 15, 35, 15, 65, 7])

#new user add using np.insert()
messages = np.insert(messages,4 ,new_user,axis=0)
print(messages)

#delete user using np.delete()
messages = np.delete(messages, new_user, axis=0)
print(messages)
