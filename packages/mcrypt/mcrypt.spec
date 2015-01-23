Summary: libmcrypt is a data encryption library.
Name: libmcrypt
Version: 2.6.8
Release: 1
License: LGPL
Source: ftp://mcrypt.hellug.gr/pub/crypto/mcrypt/mcrypt-%{version}.tar.gz
Vendor: Nikos Mavroyanopoulos <nmav@gnutls.org>
Group: System Environment/Libraries
Packager: Germano Rizzo <mano@pluto.linux.it>
Buildroot: %{_tmppath}/%{name}-%{version}-root
Prefix: /usr

%description
libmcrypt is a data encryption library. The library is thread safe
and provides encryption and decryption functions. This version of the
library supports many encryption algorithms and encryption modes. Some
algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more.

%package devel
Summary: Development files of the libmcrypt data encryption library.
Group: Development/Libraries
Requires: libmcrypt = %{version}

%description devel
Header file and static libraries of libmcrypt data encryption library.

%prep
%setup -q -n mcrypt-%{version}


%build
./configure --prefix=%{prefix}

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
ldconfig

%postun
ldconfig

%files
#%defattr(-, root, root, 0755)
%{_libdir}/libmcrypt.so
%{_libdir}/libmcrypt.so*

%files devel
#%defattr(-, root, root, 0755)
%doc doc/README* doc/example.c AUTHORS ChangeLog KNOWN-BUGS NEWS
%doc THANKS README TODO
%{_libdir}/libmcrypt.la
%{_includedir}/mcrypt.h
%{prefix}/man/man3/mcrypt.*
%{_bindir}/libmcrypt-config
%{_datadir}/aclocal/libmcrypt.m4

%changelog
* Tue Dec 17 2002 Germano Rizzo <mano@pluto.linux.it>
- modified for new installation structure

