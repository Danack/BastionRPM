startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/yaml/yaml.spec $RPM_DIR/SPECS/yaml.spec
cp ../packages/yaml/* $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/yaml.spec


. ${startDir}/copyAndRepo.sh

#cp $RPM_DIR/SRPMS/*   $startDir/../repo/SRPMS/
#cp $RPM_DIR/RPMS/x86_64/*  $startDir/../repo/RPMS/x86_64/
#createrepo $startDir/../repo/SRPMS
#createrepo $startDir/../repo/RPMS/x86_64
