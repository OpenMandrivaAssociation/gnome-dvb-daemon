Summary: DVB Daemon for GNOME
Name: gnome-dvb-daemon
Version: 0.2.9
Release: 1
License: GPLv3
Group: Video
URL: http://live.gnome.org/DVBDaemon
Source0: http://ftp.gnome.org/pub/GNOME/sources/gnome-dvb-daemon/%{name}-%{version}.tar.xz

BuildRequires: gstreamer0.10-plugins-bad
BuildRequires: gstreamer0.10-plugins-good
BuildRequires: gstreamer0.10-tools
BuildRequires: intltool
BuildRequires: python-dbus
BuildRequires: totem
BuildRequires: vala
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gee-1.0)
BuildRequires: pkgconfig(gstreamer-0.10)
BuildRequires: pkgconfig(gst-rtsp-server-0.10)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: gstreamer0.10-python

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
%apply_patches

%build
%configure2_5x  \
	--enable-totem-plugin 
	--with-totem-plugin-dir=%{_libdir}/totem/plugins

%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{py_puresitedir}/gnomedvb
%{_datadir}/dbus-1/services/*.service
%{_libdir}/totem/plugins/dvb-daemon
%{_datadir}/applications/*.desktop
%{_iconsdir}/*/*/*/*

