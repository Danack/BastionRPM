
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/libwebp/libwebp.spec $RPM_DIR/SPECS/libwebp.spec
cp ../zips/libwebp-0.4.2.tar.gz $RPM_DIR/SOURCES/


cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/libwebp.spec

. ${startDir}/copyAndRepo.sh






