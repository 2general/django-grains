from setuptools import setup


setup(name='django-grains',
      version='0.2',
      description=('Define content fragments in Django templates '
                   'and store their contents in the database. '
                   'This is yet another take '
                   'on the idea previously implemented in '
                   'django-flatblocks, django-chunks etc.'),
      author='Antti Kaihola (2General Ltd.)',
      author_email='antti@2general.com',
      url='http://github.com/2general/django-grains',
      packages=['grains', 'grains.migrations', 'grains.templatetags'],
      classifiers=['Development Status :: 4 - Beta',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Internet :: WWW/HTTP',
                   'License :: OSI Approved :: BSD License'])
