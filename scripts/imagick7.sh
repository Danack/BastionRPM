#https://stereochro.me/ideas/rpm-for-the-unwilling


#yum install jasper-devel  lcms-devel libX11-devel libXext-devel libXt-devel ghostscript-devel libtiff-devel ghostscript-devel libtiff-devel
#yum install ghostscript-devel libtiff-devel

startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/imagick/imagick7.spec $RPM_DIR/SPECS/imagick7.spec
cp ../packages/imagick/* $RPM_DIR/SOURCES/
cp ../zips/imagick-phpseven.tar.gz $RPM_DIR/SOURCES/imagick-phpseven.tar.gz

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/imagick7.spec


. ${startDir}/copyAndRepo.sh





