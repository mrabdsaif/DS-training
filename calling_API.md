
## ***What is an API means ?***

- API is the acronym for **application programming interface**.
-  It is a software intermediary that allows two applications to talk or to interact to each other.
- Or in a simple words API is the way for an application to interact with a certin app, system, libraries..etc.
- Each time you use Facebook, send an instant msg, or check the weather on your phone you are using an API.
* You cannot call a function unless you know the function name and the required parameters.
* When you create a web service you create an API.
* The [API]() defines the functions names and its parameters so others know how to call a function.

***
***

## ***What is a web service ?***
##
#
When you create a a function or a library and you want to share this functionality with others not just with yourself. Generally, the way we do that is we create a web service.
#
* We can summarize what web service means in a simple word, as we have a function we send it onto a web server just like you`d like to put a website onto a web server.
* If you have the address of that function on the web server then you can visit or call it (just like if you have the address of a web site you can visit it)
* web server such as contoso.
* When a developer want to share the functionality of a program, but not the actual code. They can place the function or the program on a web server.
* A programmer with the adress of this function on a web server and the required permissions of using the functionality of this program, can call this function (program).
* This process is called a web service.

***
***
## ***Standered for the way we send msgs across the web***

* Hypertext Transfer Protocol [HTTP]() is a standered protocol for sending msgs across the web.
* In other words, a protocol for talking across the Internet.
* There is two standerd protocol for sending msgs across the web:
    - Get
      - Pass values in query string only.
      - Special characters must be escaped, (like slashes or dashes).
      - Limited amount of data.
    - Post
      - Pass values in query string and body.
      - No need to escape special characters if passed in body.
      - Can pass large amount of data, including images, in body.

***
***Note:*** *Get and Post will be written bside the services, so you will know which standard will be using, and the documentaion of the API will explain what you will use. In addition to this, the functions names and their parameters*.
***
***
## ***One of the things that is useful in python something called (requiests library)***
* We have learnd about libraries and how to install it using pip, so you need to install this library.
* One of the libraries you want to use when you are playing with HTTP is requiests library.
* This library simplifies making a Post or a Get call. 

* Ex: when you install the library, you start to use it :   
requiests.post(address, http_headers, function_parameters, message_body)
    - address : what server is this on ?, what is the name of the function you are calling?
    - HTTP_header (will be on the documentation)
    - msg body for example image file.
***
***
## *How to call a web service in a server***
* *Generally speaking, we need to know what server this service on? For instance, if we need to call the analyze image, we need to discover where does this function exist from the documentation, and it is a part of the cognitive service in Azure*.
* The documentation tells you how to create an account (create a service) as a first step to call this function. Cause there is a key and we need that key to call the function. For this step there is a tutorial how to create an account for free.
* Then you create the cognitive services resource [Azure](portal.azure.com).
* Then you need to go to create a resource (or there easy way if you know the function that you want to call you can search for computer vision API because I know that analyze image is a part of computer vision API, and you can discover that from the documentation).






