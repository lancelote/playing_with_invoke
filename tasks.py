from invoke import task


@task
def build(_, clean=False):
    if clean:
        print('Cleaning!')
    print('Building!')


@task
def show_platform(ctx):
    uname = ctx.run("uname -s").stdout.strip()
    print(platform_response(uname))


def platform_response(uname):
    if uname == 'Darwin':
        return "You paid the Apple tax!"
    elif uname == 'Linux':
        return "Year of Linux on the desktop!"
