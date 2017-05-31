from invoke import Collection, task


@task
def clean(ctx, target=None):
    if target is None:
        target = ctx.sphinx.target
    print('Cleaning %s' % target)


@task
def build(ctx, target=None):
    if target is None:
        target = ctx.sphinx.target
    print('Building %s' % target)


ns = Collection(clean, build)
ns.configure({'sphinx': {'target': 'default'}})
