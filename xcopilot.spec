Summary:	An X based PalmPilot Emulator
Summary(pl.UTF-8):   Emulator PalmPilota pod X
Name:		xcopilot
Version:	0.6.6
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://xcopilot.cuspy.com/build/%{name}-%{version}.tar.gz
# Source0-md5:	26f71da5d04d3ecffb60e5423b5ff95c
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://xcopilot.cuspy.com/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XCopilot is a USR/3Com PalmPilot complete hardware emulator. It
requires the ROM image from your Pilot for operation (or possibly a
Linux image now that Linux boots on the Pilot). The ROM image can be
obtained from the pilot using the pi-getrom command from the
pilot-link package if you have a Pilot or PalmPilot.

%description -l pl.UTF-8
XCopilot to pełny emulator sprzętu USR/3Com PalmPilot. Wymaga do
działania obrazu ROM-u z Pilota (lub obrazu Linuksa, by uruchomić
Linuksa na Pilocie). Obraz ROM-u można uzyskać używając polecenia
pi-getrom z pakietu pilot-link (jeśli masz Pilota lub PalmPilota).

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xcopilot
%{_mandir}/man1/xcopilot.1*
%{_desktopdir}*
%{_pixmapsdir}/*
