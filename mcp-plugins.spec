Name:         mcp-plugins
Version:      0.4.0
Release:      1

Summary:      A set of audio plugins for LADSPA
License:      GPLv2
Group:        Sound
Source:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/MCP-plugins-%version.tar.bz2
URL:          http://kokkinizita.linuxaudio.org/linuxaudio
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

