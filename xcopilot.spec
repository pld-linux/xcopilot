Summary:	An X based PalmPilot Emulator
Summary(pl):	Emulator PalmPilota pod X
Name:		xcopilot
Version:	0.6.6
Release:	2
License:	Freeware
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	http://xcopilot.cuspy.com/build/%{name}-%{version}.tar.gz
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

%description -l pl
XCopilot to pe³ny emulator sprzêtu USR/3Com PalmPilot. Wymaga do
dzia³ania obrazu ROM-u z Pilota (lub obrazu Linuksa, by uruchomiæ
Linuksa na Pilocie). Obraz ROM-u mo¿na uzyskaæ u¿ywaj±c polecenia
pi-getrom z pakietu pilot-link (je¶li masz Pilota lub PalmPilota).

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Utilities,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/xcopilot
%{_mandir}/man1/xcopilot.1*
%{_applnkdir}/Utilities/*
%{_pixmapsdir}/*
