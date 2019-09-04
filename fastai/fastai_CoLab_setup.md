#  CoLab setup, fastai new and old (also Udacity TensorFlow class)  

### CoLab from Google, free, includes GPU machines.  

  * TensorFlow comes pre-installed on all machines.  
    * But may not include tensorflow-datasets api.  
  * Automatically shuts off after 2 days, but is there a way to manually shut off engine?  
    
  * Use my "datasciY.info@gmail.com" account, also Google Drive is on this account.  
  * Can select pre-built machines from Github.  
  * Search for machine providers.  
  * From a Google Drive saved CoLab notebook, "connect to runtime" to re-start engine.  
  * Specify runtime type (GPU) and runtime engine (Python 3).  


### Fastai New (v 1.0+)  

  1. Log into Google on Chrome.  
     Go to [CoLab Welcome Page](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true)

  1. Colab link -- Github Tab  
     Select machine from "fastai/course-v3" for notebooks in 2019 class.  
     
  1. Select GPU, and Python 3 and runtime type.   
     
  1. Add Google Drive saved location path, also saves downloaded data in notebook.  
  
  1. Before running a notebook, install packages, create a new code cell and run.  
     ```!curl -s https://course.fast.ai/setup.colab | bash ```  
     Yes to "Warning... Reset all runtimes before running" check mark.  
     
  1. Mount Google Drive, add the following to the top of every notebook.  
     ```bash
     from google.colab import drive
     drive.mount('/content/gdrive', force_remount=True)  
     root_dir = '/content/gdrive/My Drive/"
     base_dir = root_dir + "fastai-v3/"
     ```
     
     Next when working with notebook, add base_dir to Path.  
     For example, in "lesson2-download.ipynb":  
     ```bash
     path = Path(base_dir + 'data/bears')
     dest = path/folder
     dest.mkdir(parents=True, exist_ok=True)
     ```
     
  1. Update tensorflow.  Install extra libraries  
     ```bash
     !pip show tensorflow  # check installed package 
     !pip install --upgrade tensorflow  # upgrade version 
     !pip install tensorflow==1.2  # specific version
     
     !pip install -q matplotlib-venn  # python command  
     
     !apt-get -qq install -y libfluidsynth1  # bash command 
     ```
     
     
### Fastai Old (v 0.7)  Use with Courses folder.  

  1. CoLab has option for "fastai/old" and "fastai/courses" notebooks 2018 version.  
  
  1. Is there a saved machine for fastai version 0.7?  
  
  1. Notebook may be able to run on my computer, Ubuntu conda3 setup.
  
  1. Symlink works on Ubuntu  
     ```bash 
     fastai -> '/fastai/old/fastai/'  
     data -> '/fastai/old/data'
     ```

---
