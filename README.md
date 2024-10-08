
# **EPICTALK**


##Documentation for EPICTALK

EPICTALK is a backend REST API service for web application to shere photos, posts, commetns.
Each post may have text, photos, geodata for it. Users may add commetns and likes to posts.\
Before run the service be sure to apply requirements.txt. 


###API

[API endpoints documentation](https://documenter.getpostman.com/view/35073725/2sAXxP9CtQ)


###Authorisation and Permissions

Authentication to service based on Token Authentication \
Permissions for service resources:

* LIST - anonuser, user, admin 
  
* RETRIEVE - anonuser, user, admin 
  
* POST - user, admin
    
* PUT - user (object owner)
    
* PATCH - user (object owner)
    
* DELETE - user (object owner), admin

    
###Code documentation

Check files:

* epictalk.app.models
    
* epictalk.app.serializers
    
* epictalk.app.urls
    
* epictalk.app.permissions
    
* epictalk.app.views
  
* epictalk.epictalk.urls
    
* epictalk.epictalk.settings


