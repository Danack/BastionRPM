
# https://trac.ffmpeg.org/wiki/CompilationGuide/Centos



Name:           ffmpeg-basereality
Version:        2.4.3
Release:        1%{?dist}
Summary:        ffmpeg the video converter

License:        GPL

URL:            http://ffmpeg.org/

Source0:    ffmpeg-2.4.3.tar.bz2

BuildRoot: %{_tmppath}/ffmpeg

%description
ffmpeg

%prep
%setup -q -n ffmpeg-%{version}

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