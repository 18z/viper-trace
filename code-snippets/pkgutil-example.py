import pkgutil

# this is the package we are inspecting -- for example 'email' from stdlib
import modules

package = modules
prefix = package.__name__ + "."

for importer, modname, ispkg in pkgutil.walk_packages(package.__path__, prefix):
    print "Found submodule %s (is a package: %s)" % (modname, ispkg)

    module = __import__(modname, fromlist="dummy")
    print "Imported", module

# http://stackoverflow.com/questions/1707709/list-all-the-modules-that-are-part-of-a-python-package
