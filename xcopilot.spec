Summary: An X based PalmPilot Emulator
Name: xcopilot
Version: 0.6.6
Release: 1
Copyright: freeware
URL: http://xcopilot.cuspy.com
Source: http://xcopilot.cuspy.com/build/xcopilot-%{PACKAGE_VERSION}.tar.gz
Patch: xcopilot-0.6.4-fancy.patch
Group: X11/Utilities
BuildRoot: /var/tmp/xcopilot-root/
Prefix: /usr
Packager: Manoj Kasichainula <manojk+rpm@io.com>

%description
XCopilot is a USR/3Com PalmPilot complete hardware emulator.  It requires
the ROM image from your Pilot for operation (or possibly a Linux image now
that Linux boots on the Pilot).  The ROM image can be obtained from the
pilot using the pi-getrom command from the pilot-link package if you have a
Pilot or PalmPilot.

%changelog

* Sat Aug 29 1998 Manoj Kasichainula <manojk+rpm@io.com>

- Updated to 0.6.6

* Wed Aug 13 1998 Manoj Kasichainula <manojk+rpm@io.com>

- Updated to 0.6.5
- Addition to %description

* Mon Jul 6 1998 Manoj Kasichainula <manojk+rpm@io.com>

- Updated to 0.6.3
- Use RPM_OPT_FLAGS with -g

* Sat Jun 13 1998 <djb@redhat.com>

- updated to 0.6.2

* Tue Mar 03 1998 Donnie Barnes <djb@redhat.com>

- made package relocatable
- added %attr so that users can rebuild without being root

* Tue Feb 17 1998 Donald Barnes <djb@redhat.com>

- new package

%prep
%setup
#%patch -p1

%build
CFLAGS="-g $RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
make prefix=${RPM_BUILD_ROOT}/usr install

%clean
if [ ! ${RPM_BUILD_ROOT} = / ]; then
  rm -rf ${RPM_BUILD_ROOT} ;
fi

%files
%attr(-, root, root) %doc README
%attr(-, root, root) /usr/bin/xcopilot
%attr(-, root, root) /usr/man/man1/xcopilot.1
