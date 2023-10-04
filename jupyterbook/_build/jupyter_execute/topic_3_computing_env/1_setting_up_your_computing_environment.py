#!/usr/bin/env python
# coding: utf-8

# # Setting up your Computing Environment
# 
# Python is highly flexible. Thus there are many good ways to set up your computing environment. However, each has its advantages and disadvantages.
# 

# ## Introduction to the JupyterLab and Jupyter Notebooks
# 
# This is a short introduction to two flagship tools created by [the Jupyter Community](https://jupyter.org).
# 

# ### JupyterLab 🧪
# 
# **JupyterLab** is a next-generation web-based user interface for Project Jupyter. It enables you to work with documents and activities such as Jupyter notebooks, text editors, terminals, and custom components in a flexible, integrated, and extensible manner. It is the interface that you're looking at right now.
# 
# > **See Also**: For a more in-depth tour of JupyterLab with a full environment that runs in the cloud, see [the JupyterLab introduction on Binder](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/HEAD?urlpath=lab/tree/demo).
# 

# ### Jupyter Notebooks 📓
# 
# **Jupyter Notebooks** are a community standard for communicating and performing interactive computing. They are documents that blend computations, outputs, explanatory text, mathematics, images, and rich media representations of objects.
# 
# JupyterLab is one interface used to create and interact with Jupyter Notebooks.
# 

# In this course, we will primarily use Jupyter Notebooks as an interface. Jupyter is extremely powerful. All the content in this course (including the book) was built with Jupyter. We will discuss more using Jupyter later. First, we need a way to access Jupyter.
# 

# ## Google Colab
# 
# ### What is Colab?
# 
# Colab, or "Colaboratory", allows you to write and execute Python in your browser, with
# 
# - Zero configuration required
# - Access to GPUs free of charge
# - Easy sharing
# 
# Whether you're a **student**, a **data scientist**, or an **AI researcher**, Colab can make your work easier. Watch [Introduction to Colab](https://www.youtube.com/watch?v=inN8seMm7UI) to learn more.
# 

# ### Advantages:
# 
# - You can go to [colab](https://colab.research.google.com/), and you are off to the races
# 

# - The interface works like google docs; there are good autosaving and collaboration features
# 

# - The interface is a standard jupyter notebook; files are fully-interoperable with other platforms
# 

# - The interface is a standard jupyter notebook; files are fully-interoperable with other platforms
# 

# - Many of the essential software packages are pre-installed; you can also install your packages
# 

# - Google provides you free access to a decent GPU for machine learning applications
# 

# - Since all the computation happens on google's servers, you can run colab on any device, even a cellphone
# 

# ### Disadvantages:
# 
# - Limited access to the command line interface
# 

# - The file system is either temporary or restricted to google drive
# 

# - Requires a Google account
# 

# - A limited number of active sessions per user
# 

# - Provides limited CPU cores
# 

# - Has built-in timeouts (premium services can improve this)
# 

# - Limited access to the terminal and interactive python functionalities
# 

# ## JupyterHub
# 
# If you have a server, you can set up JupyterHub. This is hosting for a python instance with preconfigured environments.
# 

# At Drexel, we have set up a small JupyterHub. To access JupyterHub.
# 
# 1. Log into the Drexel network or connect using the [VPN](https://drexel.edu/it/help/a-z/VPN/).
# 1. The JupyterHub can be accessed at https://jupyterhub.coe.drexel.edu To get access, you need to have an account made for you. Please send a [ticket](coe.helpdesk@drexel.edu) and an account can be made.
# 1. Once up and running, you will have access to a JupyterLab instance
# 

# ### Advantages:
# 
# - This is a standard Jupyter interface accessible from a web browsers
# 

# - Can be configured with custom packages installed
# 

# - Provides sufficient command line and file system access
# 

# - Can provide burstable computational capabilities
# 

# ### Disadvantages
# 
# - Restricted to the web browser, independent graphical applications cannot be used.
# - The Drexel server is underpowered; there is currently no GPU access.
# 

# ## Local Jupyter
# 

# To run Jupyter Notebook, you can type `jupyter notebook` in the Anaconda Prompt. If you want to run JupyterLab you can type `jupyter lab`
# 

# ### Advantages:
# 
# - You are in complete control of your Python environment
# 

# - All features are available
# 

# - You can install packages (this is rare) that require admin access
# 

# - You have access to your file system
# 

# - You have all the computing capabilities you can afford.
# 

# ### Disadvantages
# 
# - You can do things (if you copy-paste commands blindly from online sites) that can mess up your python instance or mess with apps on your computer
# 

# - You have to manage your Python environment
# 

# - You have to work on the command line
# 

# - You have to use your computing resources - Most people today rely on laptops as their primary computers. These rarely have GPUs for machine learning. If they do, it will burn through your battery fast.
# 

# ## Visual Studio Code (or Interactive Development Environments)

# Visual Studio Code (VSCode) is a lightweight, extensible IDE that has gained significant traction among Python developers. Below are some of the key advantages and disadvantages of using VSCode for Python development.

# ### Advantages:
# 
# 1. **Language Server Protocol Integration**: VSCode leverages Microsoft's Python Language Server, which enhances capabilities such as IntelliSense, code navigation, and refactoring. This feature benefits from static and dynamic analysis to provide accurate autocompletions, real-time function signatures, and variable types, aiding in the development of Pythonic code with higher efficiency and fewer errors.

# 2. **Debugger Flexibility**: VSCode's Python debugger supports various configurations like remote debugging, debugging within Jupyter notebooks, and conditional breakpoints. It's highly configurable through `launch.json` and integrates well with other Python tools like `pytest` for test debugging.

# 3. **Rich Extension Ecosystem**: The marketplace for VSCode extensions is robust and offers a wide variety of Python-specific extensions like Python Docstring Generator, Kite, and Jupyter support. This allows customization tailored to specific project needs or workflows, such as data science or machine learning tasks.

# 4. **Git Integration and DevOps**: VSCode has built-in Git support, which is especially useful for version control in Python projects. It also integrates well with CI/CD pipelines and offers extensions for containerization (e.g., Docker) and cloud deployments, providing a unified environment for the entire DevOps lifecycle.

# ### Disadvantages:
# 
# 1. **Initial Configuration Complexity**: While VSCode is extensible, the initial setup for Python development (e.g., selecting the correct interpreter, installing linters and formatters like `flake8` or `black`) can be complex. The `settings.json` can become convoluted quickly, particularly for large projects or polyglot environments.

# 2. **Resource Usage for Extensions**: As you add more extensions, the resource consumption can increase significantly. This is particularly important for Python projects that already require substantial computational resources for tasks like data analysis or machine learning model training.

# 3. **Overhead in Multi-environment Management**: While VSCode supports Python virtual environments, managing multiple environments for different Python projects can become cumbersome. This can lead to issues like package conflicts and interpreter selection problems, especially when dealing with complex dependencies in scientific computing or data science projects.

# ## Recommendations
# 
# It is up to you and your comfort level what tools you use in this course. However, I recommend the following:
# 

# 1. I would recommend you set up your own instance in VSCode. This will give you the most flexibility, and can grow with you as you learn more about Python.
# 2. If you are tinkering around Google Colab and Jupyter can be convenient. They are great for testing, but not great for research. 
# 3. If you are working on a project that requires a lot of computing power, I would recommend using the Drexel computing resources at URCF. This will give you access to a GPU and more computing power than your laptop. However, you will need to be on the Drexel network or VPN to access it.
# 

# If your project is related to research and you require additional computing capabilities, other options exist:
# 
# 1. You can pay for cloud services through Google, Azure, AWS, etc.
# 1. URCF has GPUs resources that can be used for a fee
# 1. You can talk with me, and I might have some additional GPU resources available
# 
