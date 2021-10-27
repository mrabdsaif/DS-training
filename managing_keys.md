## ***Managing Keys***
*Whenever you call an external API, you are going to need some keys and passwords, and that`s allowing you to prove to that external service that you are calling that you are who you say you are, and if there is some billing or otherwise, that the service knows who to charge.*

* *We put the key that we are going to need inside the code(source of code)*
* *But for files that we are going to share them with others, this will never be a good practice putting our keys inside the source code*.
* *So it is a bad idea putting our passwords and keys in a text file that is publicly accessible when share it with others for security purposes.*
*  *So whenever we are working on sensitive data, we need to be carfule about that data, we need to ensure that the data is secure and not going to be stored somewhere that is publicly accessible in clear txt. And How do we do this, through the use of enviornmental variables.* *

***We focus here on how to work with secure values, but enviornmental variables are not just about keys and Passwords, there are actually beneifts for anythings that might need to change or otherwise from outside of your application:***
1. *Connecting to databases*

* When it comes to connect to a database, We need a connection string for that database.
* What happens if the database is renamed? or what happens if the database moves or is changed?
* Here we will be able to change that value without going back into the application to update the change.


2. *Determining operating system*
* What happens if I need to be able to read something from th operating system?, Maybe I need to figure out the current directory, or maybe I need to figure out what operating system we are running on.
* Now what we need is to read that or do what we need to do from somewhere external to my application. And that is where enviornment variables come in to play.

3. *settings which need to change*
4. *Sensetivie data*

* *Now the way that we are going to read anything external out of my app or my file is going to be the same.*

* *What we will do to do that, is to import the OS library, and from this library, we call a little helper function called getenv(), and then pass in to this function, the name of the system variable or the eniornmental variable that we want, and this process called read env var.* *

      import os 
      os_version = os.getenv('OS')
      print(os_version)
* *The previous chunk of code is able to read any system or user enviornmental variable that has been set.*

## ***Now We need to be able to set other things that might be external to our app such as :***
* *Passwords*
* *keys*
* *database connection strings*
* *Or those sensitive other things we should not share it with others*.

***Now how do we manage those things and try to make them secure and protect them***.

***Using dotenv***
1. Store enviornmental variables in txt file (.env file) (.env is a package)

     *This file (.env) is nothing but key value pairs(You set your key then you set your value*.

     *The good thing about the .env, it gives you the opportunity to set and store the those enviornmental variables inside a txt file as the folloing example:*

       DATABASE = Sample_Connection_Strings
2. in our code file (app) we import these libraries and these functions :

       from dotenv import load_dotenv
       import os 
       load_dotenv() ==> calling the function to manage our env vars.
       database = os.getenv('DATABASE') ==> grab the enviornmental variables from the txt file.
       print(database)


*So this way you will never hard code anything, you will never checking in those sensitive values into your source code*

*Also there are many egdes of using .env package so when deploying my app or my code it will not change and will keep keys, passwords secure.*

***Important Notes***
1. Do not hard code sensitive information ever.
2. Use dotenv for a simple solution.
3. Add .env to .gitignore (This is the most important point so this will not allow to publish what inside .env file).
