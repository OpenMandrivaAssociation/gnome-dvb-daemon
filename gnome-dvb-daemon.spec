Summary: DVB Daemon for GNOME
Name: gnome-dvb-daemon
Version: 0.1.8.1
Release: %mkrel 2
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch: gnome-dvb-daemon-0.1.8.1-fix-scan-dir.patch
#gw from bzr, needed to rebuild the vala files
Patch1: gnome-dvb-daemon-0.1.8.1-vala-api.patch
#gw port to libgee 0.3.0, replaces get_element_type method
# by a property element_type
Patch2: gnome-dvb-daemon-0.1.8.1-new-libgee.patch
License: GPLv3
Group: Video
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://live.gnome.org/DVBDaemon
BuildRequires: gstreamer0.10-devel >= 0.10.19
BuildRequires: gst-rtsp-server-devel >= 0.10.4
BuildRequires: libgee-devel >= 0.3
BuildRequires: intltool
BuildRequires: sqlite3-devel >= 3.4
BuildRequires: libGConf2-devel >= 2.6.1
BuildRequires: dbus-glib-devel >= 0.74
BuildRequires: gstreamer0.10-plugins-good
BuildRequires: gstreamer0.10-plugins-bad
BuildRequires: python-devel
BuildRequires: python-dbus
BuildRequires: vala
Requires: python-dbus
Requires: gstreamer0.10-plugins-good
Requires: gstreamer0.10-plugins-bad >= 0.10.9
Requires: dvb-apps

%description
DVB Daemon is a daemon written in Vala to setup your DVB devices, 
record TV shows and browse EPG. It can be controlled via its D-Bus interface.

%prep
%setup -q
%patch -p1 -b .scan
%patch1 -p1
%patch2 -p1
#gw force rebuild of the C code from the vala sources
rm -f src/gnome-dvb-daemon.vala.stamp

%build
%configure2_5x  --enable-totem-plugin

%make

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall_std
%find_lang %name
%if %_lib != lib
mv %buildroot%py_puresitedir/gnomedvb/* %buildroot%py_platsitedir/gnomedvb/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root,-)
%_bindir/*
%py_platsitedir/gnomedvb
%_datadir/dbus-1/services/*.service
%_libdir/totem/plugins/dvb-daemon
