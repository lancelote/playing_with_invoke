from invoke import task


@task
def clean(c):
    c.run('echo removing...')


@task(clean)
def build(c):
    c.run('echo building...')
