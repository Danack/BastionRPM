%global _hardened_build 1
Name:		libwebp
Version:	0.4.2
Release:	1%{?dist}
Group:		Development/Libraries
URL:		http://webmproject.org/
Summary:	Library and tools for the WebP graphics format
# Additional IPR is licensed as well. See PATENTS file for details
License:	BSD
Source0:	http://webp.googlecode.com/files/%{name}-%{version}.tar.gz
# Source1:	libwebp_jni_example.java
BuildRequires:	libjpeg-devel libpng-devel
# BuildRequires:	libjpeg-devel libpng-devel libtool swig
BuildRequires:  giflib-devel
BuildRequires:  libtiff-devel
# BuildRequires:	java-devel
# BuildRequires:	jpackage-utils

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package tools
Group:		Development/Tools
Summary:	The WebP command line tools

%description tools
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package devel
Group:		Development/Libraries
Summary:	Development files for libwebp, a library for the WebP format
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

# %package java
# Group:		Development/Libraries
# Summary:	Java bindings for libwebp, a library for the WebP format
# Requires:	%{name}%{?_isa} = %{version}-%{release}
# Requires:	java
# Requires:	jpackage-utils

# %description java
# Java bindings for libwebp.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-static --enable-libwebpmux --enable-libwebpdemux
make %{?_smp_mflags}

# Java not required
# # swig generated Java bindings
# cp %{SOURCE1} .
# cd swig
# rm -rf libwebp.jar libwebp_java_wrap.c
# mkdir -p java/com/google/webp
# swig -ignoremissing -I../src -java \
# 	-package com.google.webp  \
# 	-outdir java/com/google/webp \
# 	-o libwebp_java_wrap.c libwebp.i



# gcc %{optflags} -shared \
# 	-I/usr/lib/jvm/java/include \
# 	-I/usr/lib/jvm/java/include/linux \
# 	-I../src \
# 	-L../src/.libs -lwebp libwebp_java_wrap.c \
# 	-fPIC \
# 	-o libwebp_jni.so

# Java not required
# cd java
# javac com/google/webp/libwebp.java
# jar cvf ../libwebp.jar com/google/webp/*.class

%install
%make_install
find "%{buildroot}/%{_libdir}" -type f -name "*.la" -delete

# Java not required
# #  swig generated Java bindings
# mkdir -p %{buildroot}/%{_libdir}/%{name}-java
# cp swig/*.jar swig/*.so %{buildroot}/%{_libdir}/%{name}-java/

%post -n %{name} -p /sbin/ldconfig

%postun -n %{name} -p /sbin/ldconfig

%files tools
%{_bindir}/cwebp
%{_bindir}/dwebp
%{_bindir}/gif2webp
%{_bindir}/webpmux
%{_mandir}/man*/*

%files -n %{name}
%doc README PATENTS COPYING NEWS AUTHORS
%{_libdir}/%{name}*.so.*

%files devel
%{_libdir}/%{name}*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

# % files java
# % doc libwebp_jni_example.java
# % {_libdir}/%{name}-java/

%changelog
* Fri Jan  3 2014 Lars Kiesow <lkiesow@uos.de> - 0.3.1-3
- Fixed build for RHEL6


