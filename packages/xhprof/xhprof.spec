%global php_extdir  %(/usr/local/bin/php-config --extension-dir 2>/dev/null || echo "undefined")
%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)

%define usrbin /usr/local/bin

Name:           xhprof
Version:        0.9.4
Release:        1
Summary:        XHProf for profiling scripts

Group:          Development/Languages
License:        PHP
URL:            http://pecl.php.net/package/xhprof
Source0:        http://pecl.php.net/get/%{name}-%{version}.tgz
Source1:        xhprof.ini
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#Requires:       php(api) = %{php_apiver}

%description
xhprof

%prep
%setup -q

%build
cd extension
%{usrbin}/phpize
%configure --with-php-config=/usr/local/bin/php-config
%{__make} %{?_smp_mflags}

%install
cd extension
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/php.d
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

mkdir -p %{buildroot}/etc/php.d/
cp %{SOURCE1} %{buildroot}/etc/php.d/xhprof.ini

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/php.d/xhprof.ini
%{php_extdir}/*.so

