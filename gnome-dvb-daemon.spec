
%define major 0
%define soname %{major}.0.0
%define libnamexine %mklibname baconvideowidget-xine %major
%define libnamegstreamer %mklibname baconvideowidget-gstreamer %major


Summary: DVB Daemon for GNOME
Name: gnome-dvb-daemon
Version: 0.1.5
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch: gnome-dvb-daemon-0.1.4-fix-scan-dir.patch
License: GPLv3
Group: Video
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://live.gnome.org/DVBDaemon
BuildRequires: gstreamer0.10-devel >= 0.10.19
BuildRequires: gst-rtsp-server-devel
BuildRequires: libgee-devel >= 0.1.4
BuildRequires: intltool
BuildRequires: sqlite3-devel >= 3.4
BuildRequires: libGConf2-devel >= 2.6.1
BuildRequires: dbus-glib-devel >= 0.74
BuildRequires: gstreamer0.10-plugins-good
BuildRequires: gstreamer0.10-plugins-bad
BuildRequires: python-devel
BuildRequires: vala
Requires: gstreamer0.10-plugins-good
Requires: gstreamer0.10-plugins-bad >= 0.10.9
Requires: dvb-apps

%description
DVB Daemon is a daemon written in Vala to setup your DVB devices, 
record TV shows and browse EPG. It can be controlled via its D-Bus interface.

%prep
%setup -q
%patch -p1 -b .scan

%build
#gw the error is in the vala-generated C file
%define Werror_cflags %nil
%configure2_5x  --enable-totem-plugin

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
