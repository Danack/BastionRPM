%global VERSION  6.9.0
%global MAJOR_VERSION  6
%global Patchlevel  7

%define date %(date +%%Y_%%m_%%d)

%define packagename ImageMagick-%{date}

Name:           %{packagename}
Version:        %{VERSION}
Release:        %{Patchlevel}
Summary:        Use ImageMagick to convert, edit, or compose bitmap images in a variety of formats.  In addition resize, rotate, shear, distort and transform images.
Group:          Applications/Multimedia
License:        http://www.imagemagick.org/script/license.php
Url:            http://www.imagemagick.org/
Source0:        http://www.imagemagick.org/download/ImageMagick/ImageMagick-%{VERSION}-%{Patchlevel}.tar.gz
Source1:        policy.xml        

BuildRoot:      %{_tmppath}/ImageMagick-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildRequires:  bzip2-devel, freetype-devel, libjpeg-devel, libpng-devel
#BuildRequires:  libtiff-devel, giflib-devel, zlib-devel, perl-devel >= 5.8.1
#BuildRequires:  ghostscript-devel, djvulibre-devel
#BuildRequires:  libwmf-devel, jasper-devel, libtool-ltdl-devel
#BuildRequires:  libX11-devel, libXext-devel, libXt-devel
#BuildRequires:  lcms-devel, libxml2-devel, librsvg2-devel, OpenEXR-devel


BuildRequires:  bzip2-devel, freetype-devel, libjpeg-devel, libpng-devel
BuildRequires: zlib-devel
BuildRequires:  libxml2-devel


%description
ImageMagick is a software suite to create, edit, and compose bitmap images. It
can read, convert and write images in a variety of formats (about 100)
including DPX, GIF, JPEG, JPEG-2000, PDF, PhotoCD, PNG, Postscript, SVG,
and TIFF. Use ImageMagick to translate, flip, mirror, rotate, scale, shear
and transform images, adjust image colors, apply various special effects,
or draw text, lines, polygons, ellipses and B�zier curves.

The functionality of ImageMagick is typically utilized from the command line
or you can use the features from programs written in your favorite programming
language. Choose from these interfaces: G2F (Ada), MagickCore (C), MagickWand
(C), ChMagick (Ch), Magick++ (C++), JMagick (Java), L-Magick (Lisp), nMagick
(Neko/haXe), PascalMagick (Pascal), PerlMagick (Perl), MagickWand for PHP
(PHP), PythonMagick (Python), RMagick (Ruby), or TclMagick (Tcl/TK). With a
language interface, use ImageMagick to modify or create images automagically
and dynamically.

ImageMagick is free software delivered as a ready-to-run binary distribution
or as source code that you may freely use, copy, modify, and distribute in
both open and proprietary applications. It is distributed under an Apache
2.0-style license, approved by the OSI.

The ImageMagick development process ensures a stable API and ABI. Before
each ImageMagick release, we perform a comprehensive security assessment that
includes memory and thread error detection to help prevent exploits.ImageMagick
is free software delivered as a ready-to-run binary distribution or as source
code that you may freely use, copy, modify, and distribute in both open and
proprietary applications. It is distributed under an Apache 2.0-style license,
approved by the OSI.


%package devel
Summary: Library links and header files for ImageMagick application development
Group: Development/Libraries
#Requires: ImageMagick = %{version}-%{release}
Requires: %{packagename}
Requires: libX11-devel, libXext-devel, libXt-devel
Requires: ghostscript-devel
Requires: bzip2-devel
Requires: freetype-devel
Requires: libtiff-devel
Requires: libjpeg-devel
Requires: lcms-devel
Requires: jasper-devel
Requires: pkgconfig
Requires: %{name}-libs = %{version}-%{release}

%description devel
ImageMagick-devel contains the library links and header files you'll
need to develop ImageMagick applications. ImageMagick is an image
manipulation program.

If you want to create applications that will use ImageMagick code or
APIs, you need to install ImageMagick-devel as well as ImageMagick.
You do not need to install it if you just want to use ImageMagick,
however.

%package libs
Summary: ImageMagick libraries to link with
Group: Applications/Multimedia

%description libs
This packages contains a shared libraries to use within other applications.


%package doc
Summary: ImageMagick HTML documentation
Group: Documentation


%description doc
ImageMagick documentation, this package contains usage (for the
commandline tools) and API (for the libraries) documentation in HTML format.
Note this documentation can also be found on the ImageMagick website:
http://www.imagemagick.org/.


%prep
%setup -q -n ImageMagick-%{VERSION}-%{Patchlevel}
sed -i 's/libltdl.la/libltdl.so/g' configure
iconv -f ISO-8859-1 -t UTF-8 README.txt > README.txt.tmp
touch -r README.txt README.txt.tmp
mv README.txt.tmp README.txt
mkdir Magick++/examples
cp -p Magick++/demo/*.cpp Magick++/demo/*.miff Magick++/examples
pwd
cp %{SOURCE1} config/policy.xml

rm -rf %{buildroot}

%build
#%configure --enable-shared \
#           --disable-static \
#           --with-modules \
#           --with-perl \
#           --with-x \
#           --with-threads \
#           --with-magick_plus_plus \
#           --with-gslib \
#           --with-wmf \
#           --with-lcms \
#           --with-rsvg \
#           --with-xml \
#           --with-perl-options="INSTALLDIRS=vendor %{?perl_prefix} CC='%__cc -L$PWD/magick/.libs' LDDLFLAGS='-shared -L$PWD/magick/.libs'" \
#           --without-dps
# Disable rpath
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Do *NOT* use %%{?_smp_mflags}, this causes PerlMagick to be silently misbuild



# --with-openexr
# --with-jemalloc
export CFLAGS="-Wno-deprecated-declarations"
%configure --with-quantum-depth=32 \
           --enable-hdri \
           --with-magick-plus-plus=no \
           --without-perl \
           --disable-static \
           --disable-docs \
           --program-suffix=hdri32 \
           --disable-openmp 

make install DESTDIR=%{buildroot} INSTALL="install -p"

#

#--exec-prefix=/usr/sbin \
#/usr/sbin
#--disable-openmp  \
# --with-rsvg=yes \

%configure --with-quantum-depth=16 \
           --with-magick-plus-plus=no \
           --without-perl \
           --disable-static \
           --exec-prefix=/usr/sbin \
           --disable-docs \
           --disable-openmp 
           
make install DESTDIR=%{buildroot} INSTALL="install -p"


%install
# rm -rf %{buildroot}

#make install DESTDIR=%{buildroot} INSTALL="install -p"
# cp -a www/source %{buildroot}%{_datadir}/doc/ImageMagick-%{MAJOR_VERSION}
rm %{buildroot}%{_libdir}/*.la


# perlmagick: cleanup various perl tempfiles from the build which get installed
find %{buildroot} -name "*.bs" |xargs rm -f
find %{buildroot} -name ".packlist" |xargs rm -f
#find %{buildroot} -name "perllocal.pod" |xargs rm -f


%clean
#rm -rf %{buildroot}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

#%post c++ -p /sbin/ldconfig

#%postun c++ -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc QuickStart.txt ChangeLog Platforms.txt
%doc README.txt LICENSE NOTICE AUTHORS.txt NEWS.txt
%{_libdir}/libMagickCore*so*
%{_libdir}/libMagickWand*so*
%{_bindir}/*
%{_libdir}/ImageMagick-%{VERSION}
%{_datadir}/ImageMagick-%{MAJOR_VERSION}
#%{_mandir}/man[145]/[a-z]*
#%{_mandir}/man1/ImageMagick.*
#%exclude %{_libdir}/ImageMagick-%{VERSION}/modules-*/coders/djvu.*
%{_sysconfdir}/ImageMagick-%{MAJOR_VERSION}


#%global incsuffixe -6
#%global libsuffixe -6.Q16

%files libs
%defattr(-,root,root,-)
#%{_libdir}/libMagickCore%{?libsuffixe}.so.2*
#%{_libdir}/libMagickWand%{?libsuffixe}.so.2*
#ln -sf /opt/bupc2.8/bin/upcc ${RPM_BUILD_ROOT}/%{_bindir}
%{_libdir}/libMagickCore*.so.2*
%{_libdir}/libMagickWand*.so.2*
%{_libdir}/ImageMagick-%{VERSION}
%{_datadir}/ImageMagick-%{MAJOR_VERSION}
%{_sysconfdir}/ImageMagick-%{MAJOR_VERSION}


%files devel
%defattr(-,root,root,-)
%{_bindir}/MagickCore-config*
%{_bindir}/Magick-config*
%{_bindir}/MagickWand-config*
%{_bindir}/Wand-config*
%{_libdir}/libMagickCore*so*
%{_libdir}/libMagickWand*so*
%{_libdir}/pkgconfig/MagickCore*.pc
%{_libdir}/pkgconfig/ImageMagick*.pc
%{_libdir}/pkgconfig/MagickWand*.pc
%{_libdir}/pkgconfig/Wand*.pc
%dir %{_includedir}/ImageMagick-%{MAJOR_VERSION}
%{_includedir}/ImageMagick-%{MAJOR_VERSION}/magick
%{_includedir}/ImageMagick-%{MAJOR_VERSION}/wand
#%{_mandir}/man1/Magick-config.*
#%{_mandir}/man1/MagickCore-config.*
#%{_mandir}/man1/Wand-config.*
#%{_mandir}/man1/MagickWand-config.*






#%files doc
#%defattr(-,root,root,-)
#%doc %{_datadir}/doc/ImageMagick-%{MAJOR_VERSION}
#%doc LICENSE


%changelog
* Sun May 01 2005 Cristy <cristy@mystic.es.dupont.com> 1.0-0
-  Port of Redhat's RPM script to support ImageMagick.
