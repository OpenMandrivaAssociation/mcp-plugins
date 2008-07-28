Name:         mcp-plugins
Version:      0.3.0
Release:       %mkrel 6

Summary:      A set of audio plugins for LADSPA
License:      GPL
Group:        Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:       MCP-plugins-%version.tar.bz2
URL:	      http://alsamodular.sourceforge.net
Patch0:       mcp-plugins-makefile.patch.bz2
Requires:     ladspa

%description
A set of audio plugins for LADSPA by Fons Adriaensen.
Currently contains a phaser, a chorus and a moog vcf.

%prep
%setup -n MCP-plugins-%version -q 
%patch0 -p1
perl -pi -e 's/usr\/lib\/ladspa/usr\/%{_lib}\/ladspa/g' Makefile

%build
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
mkdir -p $RPM_BUILD_ROOT%{_datadir}
make DESTDIR=$RPM_BUILD_ROOT install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README
%{_libdir}/ladspa/*.so

