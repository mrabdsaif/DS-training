## ***Javascript Object Notation***
## ***JSON***
***JSON** is a standard data format that can be intimidating at first glance* 
* *What we get when we call an API is JSON format in some cases like analyzing an image.*
* *We need to know is how to read this data format using code.*
* *There is a whole bunch of websites and things called JSON linters, and what do these linters do for us is formating it nicely and readable.*
* *But now how to use the JSON format in code:*

  - *JSON contains key pairs*
  
        {'key':'value'.}

  - *Sometimes you have a key and a series of subkeys and subvalues.*

        'key':{'subkey1':'subvalue1','subkey2':'subvalue2',...}

  - *Or for a particular key you might have a list of values.*

        {'key':['listvalue1', 'listvalue2',...]}

* *So when we need to read these formats using our code we need to determine which structure we are dealing with.*
*** 
## ***To retrieve a value from***
       {'key':'value'}
* *We import JSON library*

       results => 'rquestedID':'jfehfjkehud4564sdf45454'*
* *what we can do with our result (I am assuming when I call the code and I call the web service, the result will passed back into a variable called results)* 
* *So results is the variable that contain the big JSON string.*
* *Now what we need to do is just:*

      print(results['requestedID'])
    Then it will return the value of this key.

***
## ***To retrieve a value from***
      {'key':{'subkey1':'subvalue1','subkey2':'subvalue2',...}}

***The way to request a value from this format is:***

* Only specify the key name and the subkey name.

        print(results['key']['subkey1'])

***
## ***To retrieve a value from***
      {'key':{'subkey1':[listvalue0, listvalue1, ...],
              'subkey2':
              [{'key':'value', 'key':'value'}]
              }},

***The way to request a value from this format is:***

* Only specify the key name and the subkey name then the index position of the value to retrieve.

        print(results['key']['listvalue0'][0])
***The way to retrieve all the values from this format is to use loop***

      for item in results['key']['listvalue0']:
          print(item)

***
***
## ***How to create JSON***
***You can create {'key':'value'} JSON objects from a dictionary***
* create a dictionary object :

      person_dic = {'f_name':'Ali', 'l_name':'Alii'}

* Add additional key pairs as needed to dictionary :

       person_dic['City']='Seattle'

* Convert dicationary into JSON object :

      person_json = json.dumps(person_dic)
         print(person_json)


***
***
## ***Nest dictionaries to create JSON in format***

    {'key':{'subkey1':'subvalue1','subkey2':'subvalue2',...}}
* *The whole process is like creating a dictionary in a dictionary.*
* *We create our dictionary :*

      person_dic = {'f_name':'Ali', 'l_name':'Alii'}
* *We create staff dictionary which assigns a person to a role :*

        staff_dic= {}
        staff_dic['program Manager']=person_dic

* *Convert dictionary into JSON object :*

        staff_json = json.dumps(staff_dic)
        print(staff_json)

***Note**: The example above imagine you have a staff directory, and each staff posistion associated with a person, and for that person we know their first name and last name. so I might have staff dictionary which has a key of the program manager, and each program manager is a particular person.*
***
***
## ***Creating JSON in list values format :***

    {'key':{'subkey1':[listvalue0, listvalue1, ...],
              'subkey2':
              [{'key':'value', 'key':'value'}]
              }},
     
* *The process is we have our simple dictionary, then we create our lists and then we start adding them into the dectionary, so it is adding lists into a dectionary.*
 
      person_dic = {'f_name':'Ali', 'l_name':'Alii'}
* Create a list object of programming languages :
    
      languages_list = ['C#','python','Jscript']
* Add the list into the dectionary : 
    
      person_dic['languages'] = languages_list
* Convert dectionary into JSON object :

       person_json= json.dumps(person_dic)
       print(person_json)

