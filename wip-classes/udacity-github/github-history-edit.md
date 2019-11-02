# Guide for editing Github History after the fact.   

Source:  https://codewithhugo.com/change-the-date-of-a-git-commit/  

One of the greatest and worst things with git is that you can rewrite the history. Here’s a sneaky way of abusing that, I can’t think of a legitimate reason to do this.  As with anything, thanks StackOverflow for all the options I can pick from 👍.  

#### Set the date of the last commit to the current date  
>GIT_COMMITTER_DATE="$(date)" git commit --amend --no-edit --date "$(date)"  

#### Set the date of the last commit to an arbitrary date  
>GIT_COMMITTER_DATE="Mon 20 Aug 2018 20:19:19 BST" git commit --amend --no-edit --date "Mon 20 Aug 2018 20:19:19 BST"  
  
  ***Woohoo! Worked!***
  >GIT_COMMITTER_DATE="Sep 14, 2019 1:00 PM EST" git commit --amend --no-edit --date "Sep 14, 2019 1:00 PM EST"    
  > (output)
  >[master a78163c] Create git-test-hist1.txt                                                     
  >Author: Jennifer E. Yoon <jenneyoon@gmail.com>                                                
  >Date: Sat Sep 14 13:00:00 2019 -0500                                                          
  >1 file changed, 7 insertions(+)                                                              
  >create mode 100644 git-test-hist1.txt 

 * Then git add . , git commit -m "", git pull to merge two histories, git push to change history on Github.  

#### Set the date of an arbitrary commit to an arbitrary or current date  

Rebase to before said commit and stop for amendment:  
  ```bash
  git rebase /<commit-hash>^ -i  (Copy commit long-hash number)  
  Replace **pick** with **e** (edit) on the line with that commit (the first one)  
  quit the editor (ESC followed by :wq in VIM)  
  ```

Either:
>GIT_COMMITTER_DATE="$(date)" git commit --amend --no-edit --date "$(date)"  
>GIT_COMMITTER_DATE="Mon 20 Aug 2018 20:19:19 BST" git commit --amend --no-edit --date "Mon 20 Aug 2018 20:19:19 BST"  

See here for more information around rebasing and editing in git:  
Split an existing git commit. https://codewithhugo.com/split-an-existing-git-commit/  

Following any of these 3 options, you will want to run:  
>git rebase --continue  

***Woohoo! Also worked!!***  

 * First changed to datasciY repo, git pull to update local repo.  
 * Next, give rebase command with commit number long-hash.  
   git rebase 76ec9db8ec3c7affda7495a619bcbbb6ca1bbe98^ -i  
   ```bash
   (output)               
   Stopped at 76ec9db...  Update tasks-website.md                                                
   You can amend the commit now, with
      git commit --amend                                                                  
   Once you are satisfied with your changes, run  
      git rebase --continue  
   ```  
 * Git opens default editor (Nano) with 4 commits around hash-number-commit.    
 * Replace "pick" with "edit" in front of the commit I want to edit (2nd from top).  
 * Save and Close editor.  
 * Git prompts with: "git commit --amend"  
   Edit with "GIT_COMMITTER_DATE="Sep 14, 2019 1:00 PM EST" git commit --amend ..."  
   Run "git rebase --continue"  
 * Do git add ., git commit, git pull, git push.  
 
#### Result Evalutaion  
Merges both histories of unedited and edited.  Seems to add commit numbers to original date AND changed date.    
Creates /datasciY/.git/rebase-merge.  Need to "rm -fr ..." to do another merge task.
Creates conflicts after the first rebase, so is easiest to move self-contained new file.
Easiest to create a brand new file, commit it once, and edit commit date.
That does not seem to create conflict.
When editing date of existing file that was committed before, that seems to create a conflict.

Works pretty well.  Worth practicing interactive editing with "git rebase".  
Read more about how the **cherry picker** works in **git rebase**.


