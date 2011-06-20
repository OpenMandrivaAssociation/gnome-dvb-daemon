Summary: DVB Daemon for GNOME
Name: gnome-dvb-daemon
Version: 0.2.2
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/gnome-dvb-daemon/%{name}-%{version}.tar.xz
Patch0: gnome-dvb-daemon-0.2.0-link.patch
License: GPLv3
Group: Video
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://live.gnome.org/DVBDaemon
BuildRequires: gstreamer0.10-devel >= 0.10.19
BuildRequires: gst-rtsp-server-devel >= 0.10.7
BuildRequires: libgee-devel >= 0.5
BuildRequires: intltool
BuildRequires: sqlite3-devel >= 3.4
BuildRequires: dbus-glib-devel >= 0.74
BuildRequires: gstreamer0.10-plugins-good
BuildRequires: gstreamer0.10-plugins-bad
BuildRequires: python-devel
BuildRequires: python-gobject-devel
BuildRequires: python-dbus
BuildRequires: vala >= 0.11.2
BuildRequires: gstreamer0.10-python
BuildRequires: libgudev-devel
Requires: python-dbus
Requires: gstreamer0.10-plugins-good
Requires: gstreamer0.10-plugins-bad >= 0.10.9
Requires: dvb-apps
Requires: gstreamer0.10-python

%description
DVB Daemon is a daemon written in Vala to setup your DVB devices, 
record TV shows and browse EPG. It can be controlled via its D-Bus interface.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x  --enable-totem-plugin --with-totem-plugin-dir=%_libdir/totem/plugins
%make

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root,-)
%_bindir/*
%py_puresitedir/gnomedvb
%_datadir/dbus-1/services/*.service
%_libdir/totem/plugins/dvb-daemon
%_datadir/applications/*.desktop
%_iconsdir/*/*/*/*
