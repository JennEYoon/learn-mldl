# My practice doing fast.ai classes  
- for uploading to datasciY.com  
 
## Author:  Jennifer E Yoon  

#### 2018 Fastai v0.7  

  * Practical Deep Learning for Coders (2018 fastai v0.7)  
    https://github.com/fastai/fastai/tree/master/courses/dl1
    
    * Has cifar 10 image classification example -- to do & upload to website.  
      https://github.com/fastai/fastai/blob/master/courses/dl1/cifar10-simplenet.ipynb  
      Notebook Does NOT load on Github.  Run on other servers.
 
    * There are multiple versions of 2018 fastai class for deep learning part 1.  
       - Full notebooks are only available as part of courses repo:  
         https://github.com/fastai/fastai/tree/master/courses     
 
  * Cutting Edge Deep Learning 2018 - Part 2  
    https://github.com/fastai/fastai/tree/master/courses/dl2
    
  * Machine Learning for Coders (2018 fastai v0.7)  
    * https://github.com/fastai/fastai/tree/master/courses/ml1 
    
  * Math - Linear Algebra for ML 

#### 2019 Fastai v1.0 modules

  * Practical Deep Learning for Coders (Part 1, 2019 fastai v1.0) 
  * Fundamentals of Deep Learning (Part 2, 2019 fastai v1.0))

>DL1 makes extensive use of custon library and functions in fastai v 1.0.  Not easy to translate this to standard libraries.  Just watch the videos and follow along for the concept.  Need to takde DL2 in order to see what is going on from scratch. 

#### My My Fork on Github does NOT merge with Source/Upstream Github account's repo.  

 * First clone on laptop with upstream source repo, i.e., fastai's github URL.
 * Pull from source to my laptop master branch. (download all changed files)
 * Merge with my working files in my own master branch.
 * Push to my own Forked (fastai) repo on MY OWN Github Accout.

>Commits made to my fork does not count towards Github contributions graph, bad!

#### Tasks - Date 8/7/2019  6:40 PM EST  

 * Keep full fastai repo on my account, to push updates to.
 * Manually upload fastai exercise for uploading to my website, datasciY.com
 
#### Tasks - 8/11/2019 12:17 PM  

 * Uploaded CoLab folder from Google Drive 
 * Has Fastai exercise notebook.
 * Do timeing test, get faster GPU to test on.

  
#### Tasks -- 8/18/2019  5:44 PM  

  * Markdown -- learn a few more format items each week.  
  * Github -- look into "rebase" and "merging" 2 upstream soruces.  Test it out.
  * Git -- also practice using branches.  Different ones for different small projects.
  * Jupyter Notebook (Lab) -- Learn a few keyboard shortcuts each week.
  * Become faster and accurate typist -- each small bug from typing error takes 30 minutes to hours to find and fix!
  
###  WIP Tasks 8/22/2019  

  * GOAL:  to setup fastai software to work with version 1.0 and version 0.7
  * Last 3 days - CoLab works with version 1.0
     - Test saving of downloaded data -- Google Drive mounted, but no data saved yet. 
     - CoLab each notebook at the beginning need "symlink" symbolic link, can work with version 0.7
     - CoLab is Unix
     
  * Windows - WSL Ubuntu  
    Copied repo to $home Linux location (& to c:\python\conda3linux\envs\
     - Version 1.0 works with CPU and GPU -- Ubuntu WSL
     - Linux home - copied full repo and version 1.0 works.
     - Need to add "symlink" to have it work with version 0.7.
     - Was able to import one module from 0.7 by moving working .py file, but that module calls a bunch of other modules in fastai directory that it cannot import, recursive.
     - Need a global way to add a path to the old fastai versions folder, and replace the new fastai folder.  There should be a way to do this.  Maybe create a whole new place for conda env along with only old fastai folders as a short-term fix?
  
  * Windows 10 with CMD.exe  
    Full repo copied to  C:\python\work\w_fastai\fastai  (version 1.0 top level)
     * version 0.7 in sub-level  ..\old\fastai\  
      - CMD.exe -- fastai version 1.0 may also work here.
      - Some sort of path twicking at the top of each notebook to work with version 0.7.
      - **Added User Env Path: C:\python\work\w_fastai\fastai\old\fastai**
      - May need "conda install" into new windows env.  Use Yaml file and setup new env for v 0.7.
      
        > If I can figure out how PATH is called in Linux for sub-modules, I can do the same for CMD.exe shell.  Read about "symlink" in Ubuntu.  Read about setting PATH for jupyter notebook in Windows 10.
  
  * Google Cloud  GCI, datasciY.info@ acct.    
     - free $300 credit expires soon
     - CS231N may have already set up AWS AMI machine. Try it out.
     - Try with fastai too.  Have AMI setup?  
  * AWS GPU AMI -- fastai has AMI "Public Community Machines" setup.  Try it out.
  * AWS AMI for cs231n -- may also exist, look into it.
  * Try Papersource for fastai -- since it is cheaper and there is an AMI for it.      
     
#### fastai setup WIP  

  * Stackoverflow -- lookup questions on fastai setup.
  * A few promising answers & questions.
  * Later -- Maybe ask a Stackoverflow question:  
    In 2019, setting up fastai v0.7 conda env on Windows WSL Ubuntu, with Python 3.7.  
    Use symlink for PATH.
  

