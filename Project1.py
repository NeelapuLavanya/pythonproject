#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip install pyttsx3')


# In[11]:


import pyttsx3
pyobj=pyttsx3.init()
pyobj.say("Welcome to python programming")
pyobj.runAndWait()


# In[19]:


import pyttsx3
pyobj=pyttsx3.init()
fo=open("C:\\Users\\HP\\Desktop\\system1.txt","r")
ip=fo.read()
fo.close()
pyobj.setProperty("rate",200)
pyobj.setProperty("volume",1)
pyobj.save_to_file(ip,"C:\\Users\\HP\\Desktop\\system1.mp3")
pyobj.runAndWait()


# In[ ]:





# In[ ]:





# In[ ]:




