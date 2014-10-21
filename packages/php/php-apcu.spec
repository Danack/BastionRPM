%global php_extdir  %(/usr/local/bin/php-config --extension-dir 2>/dev/null || echo "undefined")
%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)

%define usrbin /usr/local/bin

Name:           apcu
Version:        4.0.6
Release:        1
Summary:        APC User Cache

Group:          Development/Languages
License:        PHP
URL:            http://pecl.php.net/package/APCu
Source0:        http://pecl.php.net/get/%{name}-%{version}.tgz
Source1:        apcu.ini
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  php-devel
Requires:       php(api) = %{php_apiver}

%description
The Alternative PHP Cache (APC) is a free and open opcode cache for PHP. Its goal is to provide a free, open, and robust framework for caching and optimizing PHP intermediate code.

%prep
%setup -q

%build
%{usrbin}/phpize
%configure --with-php-config=/usr/local/bin/php-config
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/php.d
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

mkdir -p %{buildroot}/etc/php.d/
cp %{SOURCE1} %{buildroot}/etc/php.d/apcu.ini


%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/php.d/apcu.ini
%{php_extdir}/*.so
/usr/local/include/php/ext/apcu/apc_serializer.h
%exclude /usr/local/include/php/ext/apcu/apc.h
%exclude /usr/local/include/php/ext/apcu/apc_api.h
%exclude /usr/local/include/php/ext/apcu/apc_bin_api.h
%exclude /usr/local/include/php/ext/apcu/apc_cache_api.h
%exclude /usr/local/include/php/ext/apcu/apc_lock_api.h
%exclude /usr/local/include/php/ext/apcu/apc_pool_api.h
%exclude /usr/local/include/php/ext/apcu/apc_sma_api.h

%changelog
* Sat Jan 08 2013 Chen Zhiwei <zhiweik@gmail.com> - 3.1.9-1
- Build php-apc package
