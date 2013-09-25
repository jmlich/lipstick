# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       lipstick-qt5

# >> macros
# << macros

Summary:    QML toolkit for homescreen creation
Version:    0.16.12
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://github.com/nemomobile/lipstick
Source0:    %{name}-%{version}.tar.bz2
Source100:  lipstick-qt5.yaml
Requires:   mce >= 1.12.4
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5SystemInfo)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(contentaction5)
BuildRequires:  pkgconfig(mlite5) >= 0.0.6
BuildRequires:  pkgconfig(mce) >= 1.12.2
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libresourceqt5)
BuildRequires:  pkgconfig(ngf-qt5)
BuildRequires:  pkgconfig(qmsystem2-qt5) >= 1.4.11
BuildRequires:  pkgconfig(contextkit-statefs) >= 0.2.7
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qtwayland-wayland_egl-devel >= 5.1.0+git7
BuildRequires:  doxygen
Conflicts:   meegotouch-systemui < 1.5.7
Obsoletes:   libnotificationsystem0

%description
A QML toolkit for homescreen creation

%package devel
Summary:    Development files for lipstick
License:    LGPLv2.1
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Files useful for building homescreens.

%package tests
Summary:    Tests for lipstick
License:    LGPLv2.1
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description tests
Unit tests for the lipstick package.

%package tools
Summary:    Tools for lipstick
License:    LGPLv2.1
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description tools
Tools for the lipstick package.

%package doc
Summary:    Documentation for lipstick
License:    LGPLv2.1
Group:      Documentation
BuildArch:  noarch

%description doc
Documentation for the lipstick package.

%package ts-devel
Summary:    Translation files for lipstick
License:    LGPLv2.1
Group:      Documentation
BuildArch:  noarch

%description ts-devel
Translation files for the lipstick package.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/dbus-1/system.d/lipstick.conf
%{_libdir}/liblipstick-qt5.so.*
%{_libdir}/qt5/qml/org/nemomobile/lipstick/liblipstickplugin.so
%{_libdir}/qt5/qml/org/nemomobile/lipstick/qmldir
%{_datadir}/translations/lipstick_eng_en.qm
%{_datadir}/lipstick/notificationcategories/*.conf
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/lipstick-qt5/*.h
%{_libdir}/liblipstick-qt5.so
%{_libdir}/liblipstick-qt5.prl
%{_libdir}/pkgconfig/lipstick-qt5.pc
# >> files devel
# << files devel

%files tests
%defattr(-,root,root,-)
/opt/tests/lipstick-tests/*
# >> files tests
# << files tests

%files tools
%defattr(-,root,root,-)
%{_bindir}/notificationtool
# >> files tools
# << files tools

%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/lipstick/*
# >> files doc
# << files doc

%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/lipstick.ts
# >> files ts-devel
# << files ts-devel
