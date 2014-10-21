
Name:           yuicompressor
Version:        2.4.8
Release:        1%{?dist}
Summary:        Yahoo yui minimizer

License:        BSD

URL:            http://yui.github.io/yuicompressor/

Source0:    yuicompressor-2.4.8.jar

# Packages that contain only architecture independent files, such as shell
# scripts or regular Java programs (not JNI libraries), should be marked as 'noarch'
BuildArch:  noarch

BuildRoot: %{_tmppath}/yuicompressor

%description
RPM of the Yahoo yuicompressor

%prep

%build

%install
%{__mkdir} -p $RPM_BUILD_ROOT/usr/lib
%{__install} -m 644 -p %{SOURCE0} $RPM_BUILD_ROOT/usr/lib/yuicompressor.jar


# List of files that this package installs on the system
%files
/usr/lib/yuicompressor.jar


