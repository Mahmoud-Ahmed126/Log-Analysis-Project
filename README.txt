Log-Analysis Third project From udacity Fullstack web Developer NanoDegree
Project OverView:

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

How to Run?

PreRequisites:

Python3
Vagrant
VirtualBox

Setup Project:

1-Install Vagrant and VirtualBox
2-Download or Clone fullstack-nanodegree-vm repository.
3-Download the data from here.
4-Unzip this file after downloading it. The file inside is called newsdata.sql.
5-Copy the newsdata.sql file and content of this current repository.
Launching the Virtual Machine:

Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  $ vagrant up
Then Log into this using command:
  $ vagrant ssh
Change directory to cd /vagrant and look around with ls.
and  python logs_analysisdb.py


