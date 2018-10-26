# Codefundo-
Team Name - Two and a half men
Rishabh Jain, Himanshu Goyal, Adithya Iyer
Our aim is to help manage natural disasters and we believe that decreasing losses of human life should be our number one priority in this agenda. With that in mind, we present Save-D, a disaster management app which will have your back when you need it the most, even if no one else does. Our app will allow users to get help, even if they themselves are incapacitated to ask for it. Here’s how:

While initially setting up the app, it will ask for the user‘s name, medical record, phone number, alternate phone number and access to the device’s location. Users will also be asked to fill contact details of 3 people (who will henceforth be addressed as the ‘protectorate’) whom he can rely upon or those about whom he wants to know if any disaster strikes.

We aim to use a pre-existing API to get the latest possible news about any disaster/crisis as soon as possible. We then send safety alerts to any user in and around ground zero, confirming his/her well being through a Yes or No question. This can result in 3 possibilities, which are as follows:

1.  If the user responds yes, update in our data-bases that he has been marked safe. 

2. If the user does not respond at all , this means that there are chances of a very serious situation. In this scenario, the app plays its most crucial role. The app will send the user’s last known location with contact details, the severity of the disaster, user’s medical record and the contact information of some members of the ‘healthy survivors’ list who are closest to user.  This search will go on until either the user himself responds.

3. If in a rare case, the user responds ‘no’, then we will present the user with a list of important contact information which can be helpful in such a situation (closest hospital, police station, fire station, etc.). 
    Furthermore, the user-database makes sure it becomes easier for the authorities to understand how many people are present in the disaster prone area, how many people are present in a particular blood group, and the contact details of the people who are in the safe or in the unsafe regions.
    
    Android Application-
    clone from here- https://github.com/Aditywaitadithya/SaveD.git 
    dependencies needed for android- firebase account, details of firebase from adithyaiyer1999@gmail.com
    
    Backend-(current reposiory)
    DEPENDENCIES-
    1.django
    2.djangorestframework
