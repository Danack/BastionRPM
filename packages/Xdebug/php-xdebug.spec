%global php_extdir  %(/usr/local/bin/php-config --extension-dir 2>/dev/null || echo "undefined")
%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)

%define usrbin /usr/local/bin

Name:           xdebug
Version:        2.2.3
Release:        1
Summary:        PECL package for debugging PHP scripts

Group:          Development/Languages
License:        PHP
URL:            http://pecl.php.net/package/xdebug
Source0:        http://pecl.php.net/get/%{name}-%{version}.tgz
Source1:        xdebug.ini
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  php-devel
Requires:       php(api) = %{php_apiver}

%description
The Xdebug extension helps you debugging your script by providing a lot of
valuable debug information. The debug information that Xdebug can provide
includes the following:

* stack and function traces in error messages with:
  o full parameter display for user defined functions
  o function name, file name and line indications
  o support for member functions
* memory allocation
* protection for infinite recursions

Xdebug also provides:

* profiling information for PHP scripts
* code coverage analysis
* capabilities to debug your scripts interactively with a debug client

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
cp %{SOURCE1} %{buildroot}/etc/php.d/xdebug.ini


%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/php.d/xdebug.ini
%{php_extdir}/*.so
#/usr/local/include/php/ext/apcu/apc_serializer.h
#%exclude /usr/local/include/php/ext/apcu/apc.h

%changelog
* Sat Jan 08 2013 Chen Zhiwei <zhiweik@gmail.com> - 3.1.9-1
- Build php-apc package
