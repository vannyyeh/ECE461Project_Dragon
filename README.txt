Prerequisites (can typically be downloaded through your IDE's extensions or plugins menu):
 - Python 3.9 or newer
 - Javascript 
 - React
 - C++ (not really sure, but can resolve annoying dependency errors IGNORE FOR NOW)

Pulling this code from the repository:
1. click the green, Code dropdown menu button
2. On the Local tab, click HTTPS under clone
3. Copy the link underneath HTTPS 
4. In a command prompt: navigate to a directory you'd like to have the code located in
	a. you can do this using the 'cd' command on windows and pasting the file path after it
	b. for example: "cd C:\Users\Cord\eclipse-workspace"
5. then entire the following command:
	a. "git clone https://github.com/vannyyeh/ECE461Project_Dragon.git"

Now that you have an initialized local repo, we need to download the 
dependencies (code and other libraries) that this project will depend on.

Initializing your local development environment:
1. Navigate into the repo that you just cloned onto your computer in a command prompt
2. venv: In order to keep our work environments ~fairly~ clean and separate from each other we need to create what is called a virtual environment
	a. A virtual environment allows us to download multiple libraries that our project depends on without adding it to a global environment on our computer
		i. for example: On my system, outside our projects repo and virtual environment (venv), I have installed a JSON parsing library
			My project will not have dependencies on this JSON parser, so I create a venv where I install the following libraries: webpack, and Django. Once activated,
			my venv restricts the libraries that my code can access strictly to the ones installed in my venv, those being webpack and Django. 
	b. In order to activate your venv, we are going to call its activate script, which resides among other useful scripts (which we probably won't use) inside the Scripts folder in venv.
		i. Depending on where you are in the file directory this command will change as all its doing is telling the computer to run whatever is at that location
			1. side note: this may only work on Windows, if you don't use windows, just double click the activate script in the Scripts folder under venv
		ii. If you are in the root directory of your local repo, the command will look like this:
			1. ".\venv\Scripts\activate"
3. pip install: Now that you have a venv and it is active, you need to install all the dependencies that this project requires to run successfully.
	a. I have included a requirements.txt file in the root directory of the project which contains all the dependencies and their versions used by the project.
	b. If you have python, pip comes packaged with it. pip is a package manager for python. Long story short: it downloads stuff
	c. in the main directory, enter the following command:
		i. "pip install -r requirements.txt"
	d. That command will open the requirements.txt file and install every dependency with the specified version listed. I recommend looking in that file to see what's installed.
	e. If you add a dependency to the project in the future, you need to add the name of the library (that pip would call to install) and its version like this:
		library1==3.1
		library2==1.3.4.5
		library3==13.2.2
	f. or you can use the following command to update the requirements file automatically (if you are in the root directory)
		i. pip3 freeze > requirements.txt
	g. NOTICE: our dependencies may differ across machines and we should like include the requirements.txt file in the gitignore later
4. You now have the required code to develop without any errors except for your own! yay!
