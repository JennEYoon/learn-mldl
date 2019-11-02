# Useful Git notes, commands

Git Fork vs Clone
Pragya Rathore Pragya Rathore, studies VLSI Design at San Jose State University (2020) Answered Mar 7, 2016

When you are Forking a repository you are creating a copy of repository under the GitHub Id. Any changes made to the original repository will be reflected back to your forked repository. However, if you make any changes to your forked repository you will have to explicitly create a pull request to the original repository. When your pull request is approved by the administrator of the original repository, then your changes will be merged with the existing original code-base. Until then, your changes will be reflected only in the copy you forked.

A Clone is where you have proper duplication, and separation between, two versions of a repository. When one repository is amended, the new content must be actively copied to the other repository using a push command. And changes in the other repository are fetched.
/---------------------------------

Git remove Forked Repo
From my Git accout, goto forked repo to be removed.
Next to name of repo - click on Settings
Scroll all the way down to "Danger Zone" and select Delete Repo
Go through security checks, retype Github password is asked.
Refresh repo list to verify that the forked repo is gone.
Git commit setting time zone - Copy image from StackOverflow.com
add timezone to git commit

Add image using Markdown
![alt text](http://url/to/img.png)  
I think you can link directly to the raw version of an image if it's stored in your repository. i.e.  

![alt text](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)"  
