

startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/pngcrush/pngcrush.spec $RPM_DIR/SPECS/pngcrush.spec
cp ../zips/pngcrush-1.7.80.tar.gz $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/pngcrush.spec

. ${startDir}/copyAndRepo.sh






