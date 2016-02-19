import pkgutil
import inspect

# this is the package I want to inspecting -- modules under viper-trace
import modules

# this is the package we are inspecting -- for example 'email' from stdlib
import email

package = modules # hint: change to email
prefix = package.__name__ + "."

for importer, modname, ispkg in pkgutil.walk_packages(package.__path__, prefix):
    print "Found submodule %s (is a package: %s)" % (modname, ispkg)

    module = __import__(modname, fromlist="dummy")
    print "Imported", module

for member_name, member_object in inspect.getmembers(module):
    if inspect.isclass(member_object):
        print "%s is class" % (member_object)

# http://stackoverflow.com/questions/1707709/list-all-the-modules-that-are-part-of-a-python-package
