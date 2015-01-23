
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/yuicompressor/yuicompressor.spec $RPM_DIR/SPECS/yuicompressor.spec
cp ../packages/yuicompressor/* $RPM_DIR/SOURCES/


cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/yuicompressor.spec

. ${startDir}/copyAndRepo.sh





