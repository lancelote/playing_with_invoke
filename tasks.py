from invoke import Collection, task

import docs


# Getting Started #
###################


# Defining and running task functions
@task
def build(_):
    """
        invoke build
    """
    print('building')


# Task parameters
@task
def build2(_, clean=False):
    """
        invoke build2 -c
        invoke build2 --clean
        """
    if clean:
        print('cleaning')
    print('building')


@task
def hi(_, name):
    """
        invoke hi Name
        invoke hi --name Name
        invoke hi --name=Name
        invoke hi -n Name
        invoke hi -nName
    """
    print('hi %s' % name)


# Adding metadata via @task
@task(help={'name': 'name of the person to say hi to'})
def hi2(_, name):
    """
        invoke --help hi
    """
    print('hi %s' % name)


# Running shell commands
@task
def ls(c):
    c.run('ls')


# Declaring pre-tasks
@task
def clean_all(c):
    c.run('echo removing all...')


@task(clean_all)
def build_all(c):
    c.run('echo building all...')


# Creating namespaces
@task
def deploy(c):
    c.run('echo deploying')


namespace = Collection(docs, deploy, build_all, clean_all, ls, hi, hi2,
                       build, build2)
