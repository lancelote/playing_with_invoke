from invoke import Collection, task

import docs


# Getting Started #
###################


@task
def pre_task(_):
    print('Pre-task')


@task(pre_task)
def task_itself(_):
    print('Task itself')


@task
def build(_, clean=False):
    if clean:
        print('Cleaning!')
    print('Building!')


@task(help={'name': 'Name of the person to say hi to.'})
def hi(_, name):
    """Say hi to someone."""
    print('Hi %s!' % name)


@task
def show_platform(ctx):
    uname = ctx.run("uname -s").stdout.strip()
    print(platform_response(uname))


def platform_response(uname):
    if uname == 'Darwin':
        return "You paid the Apple tax!"
    elif uname == 'Linux':
        return "Year of Linux on the desktop!"


# Optional value #
##################


@task(optional=['log'])
def compile_src(_, log=None):
    if log:
        log_file = 'output.log'
        # Value was given
        if isinstance(log, str):
            log_file = log
        print(f'Log destination is {log_file}')
    print(f'Log value is {log}')
    # Do something


# Inverse boolean flag #
########################


@task
def make_painting(_, colors=True):
    if colors:
        print('Painting in colors')
    else:
        print('Black & white painting')


namespace = Collection(docs, build, hi, compile_src, show_platform,
                       make_painting)
