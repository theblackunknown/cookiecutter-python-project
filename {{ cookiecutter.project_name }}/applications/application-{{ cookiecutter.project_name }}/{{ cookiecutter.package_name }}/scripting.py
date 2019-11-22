#!/usr/bin/env python3

import logging
from pathlib import Path

logger = logging.getLogger(__name__)

from PySide2 import QtWidgets, QtCore, QtGui

from . import __version__

# from .resources import qInitResources, qCleanupResources

def tr(context : str, text : str):
    return QtWidgets.QApplication.translate(context, text, None)

__WINDOW_TITLE = tr('window', 'Hello World')

SETTINGS_FOLDER = Path.home() / '.{{ cookiecutter.project_name }}' / __version__

def main():
    logger.debug(f'Initialization...')
    app = QtWidgets.QApplication()

    # Settings

    logger.debug(f'Initializing settings...')
    settings = QtCore.QSettings(str(SETTINGS_FOLDER / '{{ cookiecutter.project_name }}.ini'), QtCore.QSettings.IniFormat)
    settings.setFallbacksEnabled(False)

    # Resources

    logger.debug(f'Initializing resources...')
    # qInitResources()

    # UI

    logger.debug(f'Initializing UI...')
    logger.debug(f'\twindows...')
    mainwindow = QtWidgets.QMainWindow()
    mainwindow.setWindowTitle(__WINDOW_TITLE)
    # mainwindow.setWindowIcon(QtGui.QIcon(':/application-icon'))
    mainwindow.setAnimated(True)
    mainwindow.setDockNestingEnabled(True)

    logger.debug(f'\twidgets...')

    logger.debug(f'\tsignal/slots...')

    logger.debug(f'\trestoring window state...')
    if settings.contains('ui/geometry'):
        mainwindow.restoreGeometry(settings.value('ui/geometry'))

    if settings.contains('ui/windowState'):
        mainwindow.restoreState(settings.value('ui/windowState'))

    # Event loop

    logger.debug(f'initialization done')
    mainwindow.show()
    returncode = app.exec_()

    # Finalizers

    logger.debug(f'uninitializating...')

    # Resources

    logger.debug(f'\tresources...')
    # qCleanupResources()

    logger.debug(f'\tstoring settings...')

    settings.setValue('ui/windowState', mainwindow.saveState())
    settings.setValue('ui/geometry', mainwindow.saveGeometry())

    logger.debug(f'\texiting...')
    return returncode

if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG,
        format='[{name}] {message}',
        datefmt=None,
        style='{'
    )

    import sys
    sys.exit(main())
