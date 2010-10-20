################################################################################
# Author:	Soeren Gebbert
#
# Copyright (C) 2010 Soeren Gebbert
#               mail to: soerengebbert <at> googlemail <dot> com
#
# License:
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import time

class ProcessLogging():
    """This class initiates the logging mechanism and is the base class for all
    other classes, which have information to be logged.
    """

    ############################################################################
    def __init__(self, logfile):
        
        # Check if the argument is a string or a file
        # In case of a string open the file
        
        if isinstance(logfile, file):
            self.logfile = logfile
        elif isinstance(logfile, str):
             self.logfile = open(logfile, 'w')
        else:
            print "ERROR: Unable to access " + str(logfile)
            raise IOError
        
    def LogInfo(self, message):
        """Write an info message into the logfile"""
        if message != None and message != "":
            lt = time.localtime()
            localtime = str(lt.tm_hour) + ":" + str(lt.tm_min) + ":" + str(lt.tm_sec)
            self.logfile.write("\n<INFO timestamp=\"" + localtime + "\">\n")
            self.logfile.write(message)
            self.logfile.write("\n</INFO>\n")
            self.logfile.flush()
        

    def LogWarning(self, message):
        """Write a warning message into the logfile"""
        if message != None and message != "":
            lt = time.localtime()
            localtime = str(lt.tm_hour) + ":" + str(lt.tm_min) + ":" + str(lt.tm_sec)
            self.logfile.write("\n<WARNING timestamp=\"" + localtime + "\">\n")
            self.logfile.write(message)
            self.logfile.write("\n</WARNING>\n")
            self.logfile.flush()

    def LogError(self, message):
        """Write an error message into the logfile"""
        if message != None and message != "":
            lt = time.localtime()
            localtime = str(lt.tm_hour) + ":" + str(lt.tm_min) + ":" + str(lt.tm_sec)
            self.logfile.write("\n<ERROR timestamp=\"" + localtime + "\">\n")
            self.logfile.write(message)
            self.logfile.write("\n</ERROR>\n")
            self.logfile.flush()

###############################################################################
###############################################################################
###############################################################################

class ModuleLogging(ProcessLogging):
    """This class initiates the logging mechanism for the called grass module.
    """

    ############################################################################
    def __init__(self, logfile, module_output, module_error):
        ProcessLogging.__init__(self, logfile)

        if isinstance(module_output, file):
            self.module_output = module_output
        elif isinstance(module_output, str):
             self.module_output = open(module_output, 'w')
        else:
            print "ERROR: Unable to access " + str(module_output)
            raise IOError

        if isinstance(module_error, file):
            self.module_error = module_error
        elif isinstance(module_error, str):
             self.module_error = open(module_error, 'w')
        else:
            print "ERROR: Unable to access " + str(module_error)
            raise IOError

    def LogModuleStderr(self, message):
        if message != None and message != "":
            """Write the module message on stderr into the module error logfile"""
            self.module_error.write(message)
            self.module_error.flush()

    def LogModuleStdout(self, message):
        if message != None and message != "":
            """Write the module message on stdout into the module output logfile"""
            self.module_output.write(message)
            self.module_output.flush()
