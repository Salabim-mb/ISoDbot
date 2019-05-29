import getLoginTest as login
import getPasswordTest as password
import deleteMyDataTest as delete
import encryptTest as enc
import decryptTest as dec
import verifyDataTest as data
import RegistrationTest as reg
import fileSizeTest as fst
import getDayTest as day
import getAPITest as api

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
print('\n------------------ test metody wantToGetPlan z klasy Utils ------------------')
planTest = day.run()
for test in planTest:
    print (test + ' -> ' + str(planTest[test]))
print('\n------------------ test metody encrypt z klasy Ciphartor ------------------')
encTest = enc.run()
for test in encTest: 
    print (test + ' -> ' + str(encTest[test]))
print('\n------------------ test metody decrypt z klasy Ciphartor ------------------')
decTest = dec.run()
for test in decTest: 
    print (test + ' -> ' + str(decTest[test]))

print('\n------------------ test metody verifyData z klasy Isod ------------------')
dataTest = data.run()
for test in dataTest:
    print (test + ' -> ' + str(dataTest[test]))
    
print('\n------------------ test metody register z klasy Registration ------------------')
regTest = reg.run()
for test in regTest:
    print (test + ' -> ' + str(regTest[test]))

print('\n------------------ test metody getAPI z klasy Isod ------------------')
APITest = api.run()
for test in APITest:
    print (test + ' -> ' + str(APITest[test]))

print('\n------------------ test metody fileSize z klasy Registration ------------------')
fstTest = fst.run()
for test in fstTest:
    print (test + ' -> ' + str(fstTest[test]))
