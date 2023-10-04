#!/usr/bin/env python
# coding: utf-8

# # Install a Python interpreter
# 
# For this class it is recommended that you use a pre-packaged python distribution called anaconda.
# 

# ## Local Installation
# 

# A significant advantage of Python is it is open-source and free. Unlike Matlab, anyone in the world can download and use Python!
# 
# Python is available for Windows, Linux, and Mac.
# 
# Since Python is open source, there are many ways to install it and various distributions.
# 

# ### Recommended Installation (Anaconda)
# 

# I recommend installing the anaconda distribution of python, as this comes with:
# 
# - Many of the valuable packages pre-installed
# - Conda package manager
# - Useful tools for managing python environments
# 

# #### Installation on Windows
# 

# In[1]:


from IPython.display import IFrame

IFrame(
    src="https://docs.anaconda.com/anaconda/install/windows/", width=800, height=600
)


# #### MacOS
# 

# In[2]:


IFrame(src="https://docs.anaconda.com/anaconda/install/mac-os/", width=800, height=600)


# #### Linux
# 

# In[3]:


IFrame(src="https://docs.anaconda.com/anaconda/install/linux/", width=800, height=600)


# 
# 
# > **Tip** **Windows Subsystem for Linux**: If you are working on Windows and want a Linux environment for working with Python, the [Windows Subsystem for Linux](https://learn.microsoft.com/windows/wsl/about) (WSL) is an option for you. If you choose this option, you'll also want to install the [WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl). For more information about using WSL with VS Code, see [VS Code Remote Development](/docs/remote/remote-overview.md) or try the [Working in WSL tutorial](/docs/remote/wsl-tutorial.md), which will walk you through setting up WSL, installing Python, and creating a Hello World application running in WSL.
# 
