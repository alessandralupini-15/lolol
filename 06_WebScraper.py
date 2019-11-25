#!/usr/bin/env python
# coding: utf-8

# In[4]:


from IES_Downloader import IES_Downloader


# In[13]:


#Initialize downloader
dl = IES_Downloader()

# find all links for people
dl.getPeopleLinksForCategory('http://ies.fsv.cuni.cz/en/node/48','Current faculty')
dl.getPeopleLinksForCategory('http://ies.fsv.cuni.cz/en/node/49','External lecturers')
#dl.getPeopleLinksForCategory('http://ies.fsv.cuni.cz/en/node/51','Ph.D. candidates')
#dl.getPeopleLinksForCategory('http://ies.fsv.cuni.cz/en/node/50','Administration')

# find all links for theses 
#dl.getThesesLinksForCategory('http://ies.fsv.cuni.cz/en/node/112/','Masters')
#dl.getThesesLinksForCategory('http://ies.fsv.cuni.cz/en/node/111/','Bachelors')
#dl.getThesesLinksForCategory('http://ies.fsv.cuni.cz/en/node/113/','Rigorosis')
#dl.getThesesLinksForCategory('http://ies.fsv.cuni.cz/en/node/270/','Doctoral')

# donload all people from already downloaded links
dl.downloadPeople()

# find all links on courses from already parsed people
dl.getCoursesLinksFromPersons()

# download all courses from already downloaded links
dl.downloadCourses()

# download all theses from already downloaded links
dl.downloadTheses(pause=2) #Many thanks to Mr. Gottfried who doesnt want us too scrape too much, so we must slow down here!

#save Dfs to dl.dfs dictionary
dl.saveDFs()


# In[17]:


print(dl)


# In[16]:


dl.dfs['people']


# In[ ]:





# In[ ]:




