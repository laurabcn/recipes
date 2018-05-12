#! /usr/bin/env python
import os;

print "Welcome to API recipes docker environment operation, choose an option:"
print "1 - Build full recipes environment"
print "2 - Composer install"
print "3 - Remove full recipes environment"
print "0 - Exit \n"

def switcher(choice='0'):
    switch = {
        '1': init,
        '2': composerInstall,
        '3': removeEnvirontment,
        '0': exit
    }
    if choice in switch.keys() :
        func = switch.get(choice)
        print func
        return func()
    else:
        return nothing()

def init() :
    container = "recipes"
    print "########## REMOVE CONTAINERS ##########"
    removeEnvirontment()
    print "########## BUILDING CONTAINERS ##########"
    print "Starting", container, "build with docker: \n"
    os.system("docker-compose up --build -d recipes")
    runningContainers = os.popen("docker ps -f status=running")
    output = runningContainers.read()

def composerInstall() :
    print "Composer Install..."
    containerId = os.popen("docker ps -q --filter name=recipes-php-fpm")
    if containerId.read():
        os.system("docker exec -it recipes-php-fpm /bin/bash -c 'composer install'")
    else:
        os.system("docker run --rm -v $PWD:/var/www/recipes -v ~/.ssh:/home/wwwagent/.ssh -it recipes-php-fpm:latest / bin/bash -c 'composer install'")
                  
def removeEnvirontment():
    print "Removing... \n"
    os.system("rm -Rf docker/data/*")
    os.system("docker-compose stop && docker-compose rm -v")

def exit() :
    print "See you soon! \n"

choice = raw_input("Your choice: ")
switcher(choice)
