
Name:           yuicompressor
Version:        2.4.8
Release:        1%{?dist}
Summary:        Yahoo yui minimizer

License:        BSD
BuildArch:      noarch
URL:            http://yui.github.io/yuicompressor/

Source0:    yuicompressor-2.4.8.jar

BuildRoot: %{_tmppath}/yuicompressor

%description
RPM of the Yahoo yuicompressor

%prep

%build
#mkdir -p %{buildroot}/usr/lib
#cp %{SOURCE0} %{buildroot}/usr/lib/yuicompressor.jar

%install
%{__mkdir} -p %{buildroot}/usr/lib
%{__install} -m 644 -p %{SOURCE0} %{buildroot}/usr/lib/yuicompressor.jar


# List of files that this package installs on the system
%files
%defattr(-, root, root, 0644)
/usr/lib/yuicompressor.jar




%clean
# When no clean section is defined, the files get cleaned automatically
# which makes debugging hard