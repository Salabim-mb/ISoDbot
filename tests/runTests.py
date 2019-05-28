import getLoginTest as login
import getPasswordTest as password
import deleteMyDataTest as delete
import encryptTest as enc
import decryptTest as dec
import verifyDataTest as data

print('------------------ test metody getLogin z klasy Utils ------------------')
loginTest = login.run()
for test in loginTest: 
    print (test + ' -> ' + str(loginTest[test]))
print('\n------------------ test metody getPassword z klasy Utils ------------------')
passwordTest = password.run()
for test in passwordTest: 
    print (test + ' -> ' + str(passwordTest[test]))
print('\n------------------ test metody delete_my_data z klasy Utils ------------------')
deleteTest = delete.run()
for test in deleteTest: 
    print (test + ' -> ' + str(deleteTest[test]))
print('\n------------------ test metody encrypt z klasy Ciphartor ------------------')
encTest = enc.run()
for test in encTest: 
    print (test + ' -> ' + str(encTest[test]))
print('\n------------------ test metody decrypt z klasy Ciphartor ------------------')
decTest = dec.run()
for test in decTest: 
    print (test + ' -> ' + str(decTest[test]))

print('\n------------------ test metody decrypt z klasy Isod ------------------')
dataTest = data.run()
for test in dataTest:
    print (test + ' -> ' + str(dataTest[test]))
