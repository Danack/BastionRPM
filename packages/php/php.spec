# Don't try fancy stuff like debuginfo, which is useless on binary-only
# packages. Don't strip binary too
# Be sure buildpolicy set to do nothing
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

%define date %(date +%%Y_%%m_%%d) 

Summary: Custom built PHP with APCU and other extensions
Name: php-basereality-%{date}
Provides: php
Conflicts: php
Version: 5.6.2
Release: 1
License: None
Group: Development/Tools

Requires: bzip2, libcurl, libxml2

SOURCE0: http://php.net/get/php-5.6.2.tar.gz
SOURCE1:        php.ini
SOURCE2:        php-cli.ini
SOURCE3:        apcu-4.0.6.tgz
SOURCE4:        yaml-1.1.1.tgz
SOURCE5:        php-fpm.conf

URL: http://php.net/

#AutoReqProv: no


%description
%{summary}

%prep
%setup -q -n php-%{version}
#-T switch disables the automatic unpacking of the archive. -D switch tells the %setup  
#command not to delete the directory before unpacking and -a switch tells the %setup 
#command to unpack only the source directive of the given number after changing directory.
# n set the dest folder
%setup -T -D -a 3 -n php-%{version}
mv apcu-4.0.6 ext/apcu
%setup -T -D -a 4 -n php-%{version}
mv yaml-1.1.1 ext/yaml


#  --enable-inline-optimization
# --disable-debug \
# --enable-libxml \

%build
mkdir -p  %{buildroot}
rm configure
./buildconf --force
./configure  \
                --disable-cgi \
                --disable-rpath \
                --enable-xmlreader \
                --enable-xmlwriter \
                --enable-apcu \
                --enable-fpm \
                --enable-intl \
                --enable-json \
                --enable-mbregex \
                --enable-mbstring \
                --enable-pcntl \
                --enable-pdo \
                --enable-sockets \
                --enable-sysvsem \
                --enable-sysvshm \
                --enable-zip \
                --with-bz2 \
                --sysconfdir=/etc \
                --localstatedir=/var \
                --with-config-file-path=/etc \
                --with-config-file-scan-dir=/etc/php.d \
                --with-curl \
                --with-freetype-dir=/usr/lib \
                --with-gd \
                --with-jpeg-dir=/usr/lib \
                --without-mcrypt \
                --with-png-dir=/usr/lib \
                --enable-fd-setsize=8192 \
                --with-pdo-mysql \
                --with-yaml \
                --with-zlib \
                --without-mhash \
                --with-mysql \
                --with-mysqli=mysqlnd \
                --with-openssl \
                --with-pcre-regex \
                --without-pear \
                --enable-maintainer-zts

make -j2


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_initrddir}
install -Dp -m0755 sapi/fpm/init.d.php-fpm %{buildroot}%{_initrddir}/php-fpm
%{__make} install INSTALL_ROOT="%{buildroot}"
cp %{SOURCE1} %{buildroot}/etc/php.ini
cp %{SOURCE2} %{buildroot}/etc/php-cli.ini
cp %{SOURCE5} %{buildroot}/etc/php-fpm.conf
mkdir -p %{buildroot}%{_sysconfdir}/php.d
mkdir -p %{buildroot}%{_sysconfdir}/php-fpm.d
mkdir -p %{buildroot}/var/log/php
mkdir -p %{buildroot}/var/run/php-fpm
rm %{buildroot}%{_sysconfdir}/php-fpm.conf.default



%clean
 rm -rf %{buildroot}


%post
/sbin/chkconfig --add php-fpm
/sbin/chkconfig --level 2345 php-fpm on


%preun
if [ "$1" = 0 ] ; then
    /sbin/service php-fpm stop > /dev/null 2>&1
    /sbin/chkconfig --del php-fpm
fi
exit 0

%postun
if [ "$1" -ge 1 ]; then
    /sbin/service php-fpm condrestart > /dev/null 2>&1
fi
exit 0



%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/php.ini
%config(noreplace) %{_sysconfdir}/php-cli.ini
%config(noreplace) %{_sysconfdir}/php-fpm.conf
%dir %{_sysconfdir}/php.d
%dir %{_sysconfdir}/php-fpm.d
%dir /var/log/php
%dir /var/run/php-fpm
/etc/rc.d/init.d/php-fpm
/usr/local/bin/*
/usr/local/include/php/*
/usr/local/lib/php/build/*
/usr/local/php/fpm/*
/usr/local/php/man/man1/*
/usr/local/php/man/man8/*
/usr/local/sbin/*
/usr/local/lib/php/extensions/no-debug-zts-20131226/opcache.a
/usr/local/lib/php/extensions/no-debug-zts-20131226/opcache.so


%changelog
* Thu Apr 24 2009  Elia Pinto <devzero2000@rpm5.org> 1.0-1
- First Build

EOF
