startDir=$(pwd)
. ./setupDirectory.sh



cp ../packages/cloud-init/cloud-init.spec $RPM_DIR/SPECS/cloud-init.spec
cp ../packages/cloud-init/SOURCES-7/* $RPM_DIR/SOURCES/
cp ../zips/cloud-init-0.7.5.tar.gz $RPM_DIR/SOURCES/cloud-init-0.7.5.tar.gz

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/cloud-init.spec

. ${startDir}/copyAndRepo.sh





