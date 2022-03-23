Need to write a User database that will use Classes and tuples to manage the flow. The program should work like this:
1. When we run the script it will require to register 10 users, for each user it will ask for the following information: name, surname, username, email, password, salary and roles
There need to be 3 roles: Manager, Employee and Guest.
Note: Guest should not have salary information.
Note: Registration should first ask the role and only after that additional information (email, salary, etc).
Note: Managers should keep an information about their subordinates (employees). As there may exist 2 or more managers, not all the employees may be subordinates of one manager. Also employee should know information about his/her manager.
2. After registering 10 users the script will ask to sign in. For the sign in it will require username and then password.
3. After successful sign-in the app will show success message or report that password or username is not correct.
4. After signing in user will be able to:
  change his/her username or password and get an information about his/her salary.
Managers can change passwords of themselves, their subordinates (Employees) and all Guests. Also managers can change salaries of their subordinates.
 Employees can change passwords of themselves and all Guests.Cntr-C command need to be handled. Each time user presses Cntr-C the app will:
 if it is in the signed mode - will sign out
 if it is in signed out mode - will switch back to 10 user creation mode
 if it is in user creation mode - will close the appAll the details about the implementation are not mentioned because we want you to take a unique approach. How you are going to display the information, how user can understand in which mode they are, what invalid scenarios need to be handled: they are no any definitions. Make the app as much user friendly as possible.Note: Need to use at least 4 Inheritance Classes, one for Admins, one for Employees, one for Guests and one to keep all the informations that are identical.Note: Usernames and emails should be unique.
