# Don't try fancy stuff like debuginfo, which is useless on binary-only
# packages. Don't strip binary too
# Be sure buildpolicy set to do nothing
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

%define date %(date +%%Y_%%m_%%d) 


Summary: A test imagick rpm package
Name: imagick-%{date}
Version: master
Release: 1
License: None
Group: Development/Tools
SOURCE0 : imagick-master.tar.gz
URL: http://www.phpimagick.com/

#AutoReqProv: no

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n imagick-master

 

%build
rm -rf %{buildroot}
mkdir -p  %{buildroot}

/usr/local/bin/phpize
./configure --libdir=/usr/lib64 --with-php-config=/usr/local/bin/php-config
# --enable-imagick-version-name
make

%install
mkdir -p %{buildroot}/usr/local/lib/php/extensions/no-debug-zts-20131226/
pwd
%{__install} -m 755 ./modules/imagick.so %{buildroot}/usr/local/lib/php/extensions/no-debug-zts-20131226/imagick.so

# in builddir
# cp -a * %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
# %doc doc/*
%dir /usr/local
%dir /usr/local/lib/
%dir /usr/local/lib/php/
%dir /usr/local/lib/php/extensions/
%dir /usr/local/lib/php/extensions/no-debug-zts-20131226
/usr/local/lib/php/extensions/no-debug-zts-20131226/imagick.so

%changelog
* Thu Apr 24 2009  Elia Pinto <devzero2000@rpm5.org> 1.0-1
- First Build

EOF
