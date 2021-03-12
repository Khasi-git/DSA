#!/usr/bin/env python
# coding: utf-8

# ### Days between Dates
# 

# In[72]:


def isLeapyear(year):
    if year%4 == 0:
        return True
    return False
def daysinmonth(year,month):
    if month%2 == 1:
        return 31
    elif month == 2 and isLeapyear(year):
        return 29
    elif month == 2 and not isLeapyear(year):
        return 28
    elif month%2==0:
        return 30
def nextday(year,month,day):
    if day < daysinmonth(year,month):
        return year,month, day+1
    else:
        if month == 12:
            return year+1 , 1, 1
        else:
            return year, month+1 ,1
def dateisbefore(year1,month1,day1,year2,month2,day2):
    if year1<year2:
        return True
    elif year1 == year2:
        if month1<month2:
            return True
        elif month1 == month2:
            if day1<=day2:
                return True
    return False

def daysbetweendates(year1,month1,day1,year2,month2,day2):
        assert not dateisbefore(year2,month2,day2,year1,month1,day1)
        days==0
        while dateisbefore(year1,month1,day1,year2,month2,day2):
            year1,month1,day1 = nextday(year1,month1,day1)
            days = days +1
        return days


# In[76]:


## test cases
#daysBetweenDates(2017, 12, 30, 2017, 12, 30)
#daysBetweenDates(2017, 12, 30, 2017, 12, 31)
daysBetweenDates(2017, 12, 30, 2018, 12, 30)
#daysBetweenDates(2013, 12, 30, 2017, 12, 30)


# In[ ]:




