Summary: DVB Daemon for GNOME
Name: gnome-dvb-daemon
Version: 0.2.9
Release: 2
License: GPLv3
Group: Video
URL: http://live.gnome.org/DVBDaemon
Source0: http://ftp.gnome.org/pub/GNOME/sources/gnome-dvb-daemon/%{name}-%{version}.tar.xz

BuildRequires: gstreamer0.10-plugins-bad
BuildRequires: gstreamer0.10-plugins-good
BuildRequires: gstreamer0.10-tools
BuildRequires: intltool
BuildRequires: python-dbus
BuildRequires: python-gi
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
	--enable-totem-plugin \
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



%changelog
* Tue May 22 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.2.9-1
+ Revision: 800111
- update to new version 0.2.9

* Tue Jun 21 2011 Götz Waschk <waschk@mandriva.org> 0.2.2-1
+ Revision: 686391
- new version
- xz tarball

* Mon May 23 2011 Götz Waschk <waschk@mandriva.org> 0.2.1-1
+ Revision: 677956
- update to new version 0.2.1

* Tue May 10 2011 Funda Wang <fwang@mandriva.org> 0.2.0-1
+ Revision: 673323
- new version 0.2.0

  + Götz Waschk <waschk@mandriva.org>
    - bump vala dep

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 0.1.23-1
+ Revision: 650290
- update to new version 0.1.23

* Fri Dec 17 2010 Götz Waschk <waschk@mandriva.org> 0.1.22-1mdv2011.0
+ Revision: 622543
- new version
- bump gst-rtsp-server dep

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.1.21-2mdv2011.0
+ Revision: 592387
- rebuild for python 2.7

* Mon Aug 23 2010 Götz Waschk <waschk@mandriva.org> 0.1.21-1mdv2011.0
+ Revision: 572419
- update to new version 0.1.21

* Thu Jul 29 2010 Götz Waschk <waschk@mandriva.org> 0.1.20-1mdv2011.0
+ Revision: 563106
- new version
- bump vala dep

* Wed Apr 14 2010 Funda Wang <fwang@mandriva.org> 0.1.17-1mdv2010.1
+ Revision: 534665
- BR gudev
- New version 0.1.17
- patch0,1,2,3 merged upstream

* Tue Apr 13 2010 Frederic Crozat <fcrozat@mandriva.com> 0.1.16-2mdv2010.1
+ Revision: 534357
- Patch0 (BZR): restart scan in case of failure (launchpad bug #540937)
- Patch1 (BZR): fix errors found by vala 0.8.0
- Patch2 (BZR):  Use tuning parameters from initial tuning data instead of NIT (launchpad bug #548738)
- Patch3 (BZR): fix locale encoded XDG dirs (launchpad #558583)

* Thu Mar 18 2010 Frederic Crozat <fcrozat@mandriva.com> 0.1.16-1mdv2010.1
+ Revision: 524952
- Release 0.1.16
- Remove patch1 (merged upstream)

* Wed Feb 24 2010 Funda Wang <fwang@mandriva.org> 0.1.15-1mdv2010.1
+ Revision: 510580
- new version 0.1.15

* Wed Dec 23 2009 Götz Waschk <waschk@mandriva.org> 0.1.14-1mdv2010.1
+ Revision: 481890
- update to new version 0.1.14

* Sat Nov 21 2009 Götz Waschk <waschk@mandriva.org> 0.1.13-1mdv2010.1
+ Revision: 467793
- new version
- drop patch 0

* Thu Oct 15 2009 Götz Waschk <waschk@mandriva.org> 0.1.12-1mdv2010.0
+ Revision: 457507
- new version
- update source URL
- reenable format string error

* Thu Oct 08 2009 Götz Waschk <waschk@mandriva.org> 0.1.11-1mdv2010.0
+ Revision: 456049
- new version
- rediff patch 0

* Thu Oct 01 2009 Götz Waschk <waschk@mandriva.org> 0.1.10-1mdv2010.0
+ Revision: 452090
- new version
- update build deps
- disable format string error checking

* Mon Aug 24 2009 Götz Waschk <waschk@mandriva.org> 0.1.9-1mdv2010.0
+ Revision: 420433
- fix python dir
- new version
- drop patch 2

* Fri Aug 07 2009 Götz Waschk <waschk@mandriva.org> 0.1.8.1-2mdv2010.0
+ Revision: 411114
- install all python modules in the arch-dependant dir

* Fri Aug 07 2009 Götz Waschk <waschk@mandriva.org> 0.1.8.1-1mdv2010.0
+ Revision: 411083
- fix python path on 64 bit
- new version
- update deps
- rediff the patch
- port to libgee 0.3

* Sat May 16 2009 Götz Waschk <waschk@mandriva.org> 0.1.7-1mdv2010.0
+ Revision: 376468
- new version
- update build deps

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 0.1.5-1mdv2009.1
+ Revision: 347538
- update deps
- update to new version 0.1.5

* Tue Feb 24 2009 Frederic Crozat <fcrozat@mandriva.com> 0.1.4-3mdv2009.1
+ Revision: 344451
- Package totem plugin
- Fix patch0

* Mon Feb 23 2009 Götz Waschk <waschk@mandriva.org> 0.1.4-2mdv2009.1
+ Revision: 344176
- fix scan dir (bug #48156)

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 0.1.4-1mdv2009.1
+ Revision: 341237
- update to new version 0.1.4

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 0.1.3-1mdv2009.1
+ Revision: 336530
- new version
- update deps
- drop patches
- disable Werror
- update file list

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.1.0-2mdv2009.1
+ Revision: 325449
- fix str fmt

* Thu Dec 04 2008 Frederic Crozat <fcrozat@mandriva.com> 0.1.0-1mdv2009.1
+ Revision: 309903
- import gnome-dvb-daemon


