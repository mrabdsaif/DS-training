
# The impact of installing packages will be clear when answer this question
# what is going to wind up happening when installing package using pip ..etc is to install the package globally, and globally means that it  will be available for any application or project you are going to be creating but the downside is you might be running into some particular version issues.
# whem it comes to python, it installs packages globally and what we need to do is to install packages locally inside python and we do that  by utilizing a virtual enviornment. 
# a virtual enviornment is nothing but a folder that has all the code you are gonna need to run your application that you are creating. So everything that I need it is going to be installed into this folder.
# but first we need to create that folder, and have a little utility called [virtual env] that we can use to do that.
* create a virtual enviornment globally
pip install virtualenv 
* (for windows systems)create the folder
python -m venv FolderName (you can name it venv) (-m stand for go and grap a particular module)

* for osx/linux (bash)
virtualenv Foldername

# Now, after creating the virtual env we need to activate it, and that depend on you operating system and your enviorment
# ( this if you use the command line enviorment) ( sometimes you need to use .\ to specify the current dir)
# cmd.exe
* FolderName\scripts\activate.bat 
# if you use the powershell
* FOlderName\scripts\activate.ps1
# (if you use the bash shell or window)
* . ./FOlderName/scripts/activate 
(her we use dot and space and another dot and then the folder path (the first dot is the location of your source code ))
 
# for OSx/linux
FolderName/bin/activate

# Now, How to install packages into a virtual env
* install individual package
pip install colorama

* install from a list of packages 
pip install -r requirements.txt

* #requirements.txt
colorama

