from distutils.core import setup
import sys

if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version('0.4', __file__)
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()


setup(name='template-utils',
      version=version,
      description='Template-related utilities for Django applications',
      author='James Bennett',
      author_email='james@b-list.org',
      url='http://code.google.com/p/django-template-utils/',
      packages=['template_utils', 'template_utils.templatetags'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
