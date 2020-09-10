Name:       lipstick-qt5

# We need this folder, so that lipstick can monitor it. See the code
# in src/components/launchermodel.cpp for reference.
%define icondirectory %{_datadir}/icons/hicolor/86x86/apps

Summary:    QML toolkit for homescreen creation
Version:    0.34.7
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://github.com/nemomobile/lipstick
Source0:    %{name}-%{version}.tar.bz2
Source1:    %{name}.privileges
Requires:   mce >= 1.87.0
Requires:   pulseaudio-modules-nemo-mainvolume >= 6.0.19
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick) >= 5.2.1
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Sensors)
BuildRequires:  pkgconfig(Qt5SystemInfo)
BuildRequires:  pkgconfig(contentaction5)
BuildRequires:  pkgconfig(mlite5) >= 0.2.19
BuildRequires:  pkgconfig(mce) >= 1.22.0
BuildRequires:  pkgconfig(mce-qt5) >= 1.4.0
BuildRequires:  pkgconfig(keepalive)
BuildRequires:  pkgconfig(dsme_dbus_if) >= 0.63.2
BuildRequires:  pkgconfig(thermalmanager_dbus_if)
BuildRequires:  pkgconfig(usb_moded)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libresourceqt5)
BuildRequires:  pkgconfig(ngf-qt5)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(usb-moded-qt5) >= 1.8
BuildRequires:  pkgconfig(systemsettings) >= 0.5.28
BuildRequires:  pkgconfig(nemodevicelock)
BuildRequires:  pkgconfig(ssu-sysinfo)
BuildRequires:  qt5-qttools-linguist
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5OpenGLExtensions)
BuildRequires:  doxygen
BuildRequires:  qt5-qtbase-private-devel

Conflicts:   meegotouch-systemui < 1.5.7

Obsoletes:   libnotificationsystem0
Obsoletes:   %{name}-screenshot

%description
A QML toolkit for homescreen creation

%package devel
Summary:    Development files for lipstick
License:    LGPLv2.1
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig(Qt5WaylandCompositor) >= 5.9.5

%description devel
Files useful for building homescreens.

%package tools
Summary:    Tools for lipstick
License:    LGPLv2.1
Requires:   %{name} = %{version}-%{release}

%description tools
Tools for the lipstick package (warning: these tools installed by default).

%package ts-devel
Summary:    Translation files for lipstick
License:    LGPLv2.1
Group:      Documentation
BuildArch:  noarch

%description ts-devel
Translation files for the lipstick package.

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 VERSION=%{version}

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{icondirectory}
%qmake5_install

mkdir -p %{buildroot}%{_datadir}/mapplauncherd/privileges.d
install -m 644 -p %{SOURCE1} %{buildroot}%{_datadir}/mapplauncherd/privileges.d/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/dbus-1/system.d/lipstick.conf
%{_libdir}/lib%{name}.so.*
%{_libdir}/qt5/qml/org/nemomobile/lipstick
%{_datadir}/translations/*.qm
%{_datadir}/lipstick
%{_datadir}/mapplauncherd/privileges.d/*
%dir %{icondirectory}

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.prl
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%defattr(-,root,root,-)
%{_bindir}/notificationtool

%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/*.ts
