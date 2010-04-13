Summary: DVB Daemon for GNOME
Name: gnome-dvb-daemon
Version: 0.1.16
Release: %mkrel 2
Source0: http://launchpad.net/%name/trunk/%version/+download/%{name}-%{version}.tar.bz2
# (fc) 0.1.16-3mdv restart scan in case of failure (launchpad bug #540937)
Patch0: gnome-dvb-daemon-0.1.16-restart-scan.patch
# (fc) 0.1.16-3mdv fix errors found by vala 0.8.0 (bzr)
Patch1: gnome-dvb-daemon-0.1.16-vala080.patch
# (fc) 0.1.16-3mdv Use tuning parameters from initial tuning data instead of NIT (launchpad bug #548738)
Patch2: scanner.patch
# (fc) 0.1.16-3mdv fix locale encoded XDG dirs (launchpad #558583)
Patch3: locale_xdg_dirs.patch
License: GPLv3
Group: Video
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://live.gnome.org/DVBDaemon
BuildRequires: gstreamer0.10-devel >= 0.10.19
BuildRequires: gst-rtsp-server-devel >= 0.10.4
BuildRequires: libgee-devel >= 0.5
BuildRequires: intltool
BuildRequires: sqlite3-devel >= 3.4
BuildRequires: libGConf2-devel >= 2.6.1
BuildRequires: dbus-glib-devel >= 0.74
BuildRequires: gstreamer0.10-plugins-good
BuildRequires: gstreamer0.10-plugins-bad
BuildRequires: python-devel
BuildRequires: python-dbus
BuildRequires: vala
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
%patch0 -p0 -b .restart-scan
%patch1 -p1 -b .vala080
%patch2 -p0 -b .initial-tuning
%patch3 -p0 -b .locale_to_utf8_xdg

%build
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
