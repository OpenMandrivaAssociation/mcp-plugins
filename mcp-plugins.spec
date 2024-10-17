%define debug_package          %{nil}

Name:         mcp-plugins
Version:      0.4.0
Release:      2

Summary:      A set of audio plugins for LADSPA
License:      GPLv2
Group:        Sound
Source:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/MCP-plugins-%version.tar.bz2
URL:          https://kokkinizita.linuxaudio.org/linuxaudio
Requires:     ladspa

%description
A set of audio plugins for LADSPA by Fons Adriaensen.
Currently contains a phaser, a chorus and a moog vcf.

%prep
%setup -n MCP-plugins-%version -q
perl -pi -e 's/\/usr\/lib\/ladspa/\$(DESTDIR)/g' Makefile

%build
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
mkdir -p $RPM_BUILD_ROOT%{_datadir}
make DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ladspa install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/ladspa/*.so



%changelog
* Thu May 03 2012 Frank Kober <emuse@mandriva.org> 0.4.0-1
+ Revision: 795667
- imported package mcp-plugins
- new version 0.4.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-6mdv2009.0
+ Revision: 252144
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.3.0-4mdv2008.1
+ Revision: 129809
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import mcp-plugins


* Wed Nov 9 2005 Austin Acton <austin@mandriva.org> 0.3.0-4mdk
- lib64 fix

* Sat Sep 11 2004 Austin Acton <austin@mandrake.org> 0.3.0-3mdk
- use proper sources

* Thu Jul 22 2004 Michael Scherer <misc@mandrake.org> 0.3.0-2mdk 
- rebuild for new gcc

* Fri May 7 2004 Austin Acton <austin@mandrake.org> 0.3.0-1mdk
- 0.3.0

* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 0.2.1b-1mdk
- 0.2.1b

* Mon Oct 13 2003 Austin Acton <aacton@yorku.ca> 0.0.2-1mdk
- steal/borrow from CCRMA :-)
- install the ams patches

* Mon Jun 16 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.2-1
- updated to 0.0.2
* Wed May 21 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1-1
- initial build
