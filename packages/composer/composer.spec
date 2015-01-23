%define date %(date +%%Y_%%m_%%d) 

Name:           composer-%{date}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Composer
BuildArch:      noarch
License:        MIT

URL:            https://getcomposer.org/

Source0:    composer-master.tar.gz
SOURCE1:    composer.phar


BuildRoot: %{_tmppath}/composer

%description
RPM of Composer

%prep
%setup -q -n composer-master

%build
%{__mkdir} -p %{buildroot}
cp %{SOURCE1} ./composer_source.phar

/usr/local/bin/php -d allow_url_fopen=1 ./composer_source.phar install
/usr/local/bin/php -d phar.readonly=0 bin/compile
mv ./composer.phar ./composer

%install
mkdir -p %{buildroot}/%{_sbindir}
%{__install} -m 644 -p ./composer %{buildroot}/%{_sbindir}


# List of files that this package installs on the system
%files
%defattr(-, root, root, 0644)
%{_sbindir}/composer


%clean
# When no clean section is defined, the files get cleaned automatically
# which makes debugging hard