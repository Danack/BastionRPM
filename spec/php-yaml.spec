%global php_extdir  %(/usr/local/bin/php-config --extension-dir 2>/dev/null || echo "undefined")
%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)

%define usrbin /usr/local/bin

Name:           yaml
Version:        1.1.0
Release:        1
Summary:        Support for YAML 1.1 (YAML Ain't Markup Language) serialization using the LibYAML library.

Group:          Development/Languages
License:        PHP
URL:            http://pecl.php.net/package/yaml
Source0:        http://pecl.php.net/get/%{name}-%{version}.tgz
Source1:        yaml.ini
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  php-devel
Requires:       php(api) = %{php_apiver}
Requires:       libyaml

%description
It's yaml!

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
cp %{SOURCE1} %{buildroot}/etc/php.d/yaml.ini


%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/php.d/yaml.ini
%{php_extdir}/*.so
#/usr/local/include/php/ext/apcu/apc_serializer.h
#%exclude /usr/local/include/php/ext/apcu/apc.h

%changelog
* Sat Jan 08 2013 Chen Zhiwei <zhiweik@gmail.com> - 3.1.9-1
- Build php-apc package
