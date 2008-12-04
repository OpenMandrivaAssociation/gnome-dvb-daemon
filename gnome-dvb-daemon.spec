
%define major 0
%define soname %{major}.0.0
%define libnamexine %mklibname baconvideowidget-xine %major
%define libnamegstreamer %mklibname baconvideowidget-gstreamer %major


Summary: DVB Daemon for GNOME
Name: gnome-dvb-daemon
Version: 0.1.0
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 0.1.0-1mdv fix scan directory location
Patch0: gnome-dvb-daemon-0.1.0-scandir.patch
License: GPLv3
Group: Video
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://live.gnome.org/DVBDaemon
BuildRequires: gstreamer0.10-devel >= 0.10.19
BuildRequires: libgee-devel >= 0.1.4
BuildRequires: intltool
BuildRequires: sqlite3-devel >= 3.4
BuildRequires: libGConf2-devel >= 2.6.1
BuildRequires: dbus-glib-devel >= 0.74
BuildRequires: gstreamer0.10-plugins-bad
BuildRequires: python-devel
Requires: gstreamer0.10-plugins-bad >= 0.10.9
Requires: dvb-apps

%description
DVB Daemon is a daemon written in Vala to setup your DVB devices, 
record TV shows and browse EPG. It can be controlled via its D-Bus interface.

%prep
%setup -q
%patch0 -p1 -b .scandir

%build
%configure2_5x 

%make

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%_bindir/*
%py_puresitedir/gnomedvb
%_datadir/dbus-1/services/*.service
