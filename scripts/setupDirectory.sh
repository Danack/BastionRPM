RPM_DIR="../rpmbuild"
rm -rf $RPM_DIR

mkdir -p ../repo/RPMS/x86_64
mkdir -p ../repo/RPMS/noarch
mkdir -p ../repo/SRPMS
mkdir -p $RPM_DIR
mkdir -p $RPM_DIR/{RPMS,SRPMS,BUILD,SOURCES,SPECS,tmp}

