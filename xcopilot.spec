Summary:	An X based PalmPilot Emulator
Name:		xcopilot
Version:	0.6.6
Release:	1
Copyright:	freeware
URL:		http://xcopilot.cuspy.com
Source0:	http://xcopilot.cuspy.com/build/%{name}-%{PACKAGE_VERSION}.tar.gz
Patch0:		%{name}-0.6.4-fancy.patch
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XCopilot is a USR/3Com PalmPilot complete hardware emulator. It
requires the ROM image from your Pilot for operation (or possibly a
Linux image now that Linux boots on the Pilot). The ROM image can be
obtained from the pilot using the pi-getrom command from the
pilot-link package if you have a Pilot or PalmPilot.

%prep
%setup -q
#%patch -p1

%build
CFLAGS="-g $RPM_OPT_FLAGS" ./configure --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=${RPM_BUILD_ROOT}/usr install

%clean
if [ ! ${RPM_BUILD_ROOT} = / ]; then
  rm -rf ${RPM_BUILD_ROOT} ;
fi

%files
%defattr(644,root,root,755)
%attr(-, root, root) %doc README
%attr(-, root, root) %{_bindir}/xcopilot
%attr(-, root, root) /usr/man/man1/xcopilot.1
