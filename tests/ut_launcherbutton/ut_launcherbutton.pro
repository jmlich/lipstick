include(../common_top.pri)
TARGET = ut_launcherbutton

MODEL_HEADERS += $$SRCDIR/launcherbuttonmodel.h

# unit test and unit
SOURCES += \
    ut_launcherbutton.cpp \
    $$SRCDIR/launcherbutton.cpp

# base classes
SOURCES += \
    $$STUBSDIR/stubbase.cpp

# unit test and unit
HEADERS += \
    ut_launcherbutton.h \
    $$SRCDIR/launcherbutton.h \
    $$SRCDIR/launcherbuttonmodel.h \
    $$SRCDIR/launcher.h

include(../common_bot.pri)
