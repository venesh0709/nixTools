#!/usr/bin/python -tt
#-- NOTE: Tabs and spaces do NOT mix!! '-tt' will flag violations as an error.
#===============================================================================
#-- NOTE: default Python versions:
#--       RHEL4    2.3.4
#--       RHEL5    2.4.3
#--       RHEL6.0  2.6.5
#--       RHEL6.1+ 2.6.6
#--       REHL7    2.7.5
#-- Recent Fedora versions (24/25) stay current on 2.7 (2.7.12 as of 20161212)
#===============================================================================
"""
.. program:: python-script.py
   :synopsis: This is a template for single-file Python scripts

.. codeauthor:: awmyhr <awmyhr@gmail.com>

This is where a long, verbose description of the script can go, using
Sphinx-flavored reStructuredText.
"""
#===============================================================================
#-- Standard Imports
#-- NOTE: We use optparse for compatibility with python < 2.7 as (the superior)
#--       argparse wasn't standard until 2.7 (2.7 deprecates optparse)
#--       As of 20161212 the template is coded for optparse only
import logging      #: Python's standard logging facilities
import optparse     #: Argument parsing
import os           #: Misc. OS interfaces
import sys          #: System-specific parameters & functions
# import traceback    #: Print/retrieve a stack traceback
#===============================================================================
#-- Third Party Imports
#===============================================================================
#-- Application Library Imports
#===============================================================================
#-- Variables which are meta for the script should be dunders (__varname__)
#-- TODO: Update meta vars
__version__ = '0.1.0-alpha'
__revised__ = '2016-12-16'
__contact__ = 'awmyhr <awmyhr@gmail.com>'  #: primary contact for support/?'s

#-- The following few variables should be relatively static over life of script
__author__ = 'awmyhr <awmyhr@gmail.com>'    #: coder(s) of script
__created__ = '2016-12-12'                  #: date script originlly created
__copyright__ = ''                          #: Copyright short name
__cononical_name__ = 'python-script.py'     #: static name, *NOT* os.path.basename(sys.argv[0])
__project_name__ = 'nixTools'               #: name of overall project, if needed
__project_home__ = 'https://github.com/awmyhr/nixTools' #: where to find source/documentation
__template_version__ = '1.1.0'              #: version of template file used
__docformat__ = 'reStructuredText en'       #: attempted style for documentation


#===============================================================================
class _ModOptionParser(optparse.OptionParser):
    """ By default format_epilog() strips newlines, we don't want that. """
    def format_epilog(self, formatter):
        return self.epilog

def test_func():
    """ """
    logger.debug('this is a test')

#===============================================================================
def _version():
    """ Build formatted version output
    :return: The version string.
    .. note::
        GNU guidelines dictate adding copyright/license info (see
        commented code)
    .. warning::
        HOWEVER, this may not always be desierable.
        If not, REMOVE these lines -- do NOT leave them commented!
    """
    #-- NOTE: This entire function only exists to allow for outputting license
    #--       info per GNU guidelines. If not doing that, just remove it.
    #-- TODO: Like the OptionParser.epilog method, version strips newlines.
    #--        However, there is no format_version to override. If license
    #--        info is going to be output, this'll have to be fixed. It may
    #--        be possible to override print_version()
    # text = '%s (%s) %s' % (__cononical_name__, __project_name__, __version__)
    #-- NOTE: If license text is not desired, it is probably better to move
    #--       the string to the PARSER declaration and remove this function
    #-- TODO: UPDATE license
    # text += ('Copyright (c) 2016 awmyhr\n'
    #          'License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>\n'
    #          'This is free software: you are free to change and redistribute it.\n'
    #          'There is NO WARRANTY, to the extent permitted by law.\n'
    #         )


#===============================================================================
def _debug_info():
    """ Provides meta info for debug-level output """
    logger.debug('Cononical: %s', __cononical_name__)
    logger.debug('Abs Path:  %s', os.path.abspath(sys.argv[0]))
    logger.debug('Python:    %s (%s.%s.%s)',
                 sys.executable, sys.version_info[0], sys.version_info[1], sys.version_info[2]
                )
    logger.debug('Version:   %s', __version__)
    logger.debug('Created:   %s', __created__)
    logger.debug('Revised:   %s', __revised__)
    logger.debug('Coder(s):  %s', __author__)
    logger.debug('Contact:   %s', __contact__)
    logger.debug('Project:   %s', __project_name__)
    logger.debug('Project Home: %s', __project_home__)
    logger.debug('Template Version: %s', __template_version__)
    logger.debug('Platform:  %s (%s)', sys.platform, os.name)
    logger.debug('uname:     %s', os.uname())
    logger.debug('[res]uid:  %s', os.getresuid())
    logger.debug('PID/PPID:  %s/%s', os.getpid(), os.getppid())


#===============================================================================
def exit_error(error_number, error_string):
    """ Report error and exit.
    :param int error_number: Number to use for Exit Code.
    :param str error_string: Short description of error.
    .. warning:: This function exits the script.
    """
    if OPTIONS.debug:
        print '\n------ end ------\n'

    print '%s: %s' % (os.path.basename(sys.argv[0]), error_string)
    sys.exit(error_number)


#===============================================================================
def main():
    """ This is where the action takes place
    :return: Exit code. Should be os.EX_OK.
    """
    #-- TODO: Do something more interesting here...
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

    test_func()

    return os.EX_OK
    #-- NOTE: more exit codes here:
    #--   https://docs.python.org/2/library/os.html#process-management


#===============================================================================
if __name__ == '__main__':
    #-- Parse Options (rely on OptionsParser's exception handling)
    PARSER = _ModOptionParser(
        version='%s (%s) %s' % (__cononical_name__, __project_name__, __version__),
        description='Short description of script.',
        epilog=('\nLonger explanation of script purpose &/or use.\n\n'
                'Created: %s  Contact: %s\n'
                'Revised: %s  Version: %s\n'
                '%s, part of %s. Project home: %s\n'
               ) % (__created__, __contact__,
                    __revised__, __version__,
                    __cononical_name__, __project_name__, __project_home__
                   )
    )
    PARSER.add_option('--debug', help=optparse.SUPPRESS_HELP,
                      dest='debug', action='store_true', default=False
                     )
    PARSER.add_option('--debug-file', help=optparse.SUPPRESS_HELP,
                      dest='debugfile', type='string'
                     )
    (OPTIONS, ARGS) = PARSER.parse_args()

    #-- Setup output(s)
    if OPTIONS.debug:
        LEVEL = logging.DEBUG
        FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s',
                                      '%Y%m%d-%H%M'
                                     )
    else:
        LEVEL = logging.INFO
        FORMATTER = logging.Formatter('%(message)s')
    logger = logging.getLogger(__name__) #: pylint: disable=invalid-name
                                         #: lower-case is better here
    logger.setLevel(LEVEL)

    #-- Console output
    CONSOLE = logging.StreamHandler()
    CONSOLE.setLevel(LEVEL)
    CONSOLE.setFormatter(FORMATTER)
    logger.addHandler(CONSOLE)

    #-- File output
    if OPTIONS.debug and OPTIONS.debugfile:
        #: NOTE: In Python >= 2.6 normally I give FileHandler 'delay="true"'
        LOGFILE = logging.FileHandler(OPTIONS.debugfile)
        LOGFILE.setLevel(LEVEL)
        FORMATTER = logging.Formatter(
            '%(asctime)s.%(msecs)d:%(levelno)s:%(name)s.%(funcName)s:%(lineno)d:%(message)s',
            '%Y%m%d-%H%M'
            )
        LOGFILE.setFormatter(FORMATTER)
        logger.addHandler(LOGFILE)

    if OPTIONS.debug:
        _debug_info()
        print '\n----- start -----\n'

    #-- Do The Stuff
    try:
        main()
    #-- NOTE: "except Exception as variable:" syntax was added in 2.6
    #-- NOTE: "try..except..finally" does not work pre 2.5
    except (KeyboardInterrupt, SystemExit): # Catches (Ctrl-C, sys.exit())
        raise
    #: TODO: This is Not A Great Way. Known issue, will fix... eventually...
    except Exception, error: # pylint: disable=broad-except
        logger.exception('ERROR, UNEXPECTED EXCEPTION: %s', str(error))
        #: TODO: This should TOTALLY not return 1, but rather errno of error
        sys.exit(1)
    else:
        if OPTIONS.debug:
            print '\n------ end ------\n'
        sys.exit(0)
