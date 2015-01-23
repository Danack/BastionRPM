
Name:           pngcrush-basereality
Version:        1.7.80
Release:        1%{?dist}
Summary:        pngcrush the png optimiser

License:        MIT

URL:            http://pmt.sourceforge.net/pngcrush/

Source0:    pngcrush-1.7.80.tar.gz

BuildRoot: %{_tmppath}/pngcrush

%description
PngCrusher

%prep
%setup -q -n pngcrush-%{version}

%build
%{__make}


%install
%{__mkdir} -p %{buildroot}/usr/bin
%{__install} -m 755 -p ./pngcrush %{buildroot}/usr/bin/pngcrush


# List of files that this package installs on the system
%files
%defattr(-, root, root, 0644)
/usr/bin/pngcrush

%clean
# When no clean section is defined, the files get cleaned automatically
# which makes debugging hard