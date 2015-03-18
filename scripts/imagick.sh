#https://stereochro.me/ideas/rpm-for-the-unwilling


#yum install jasper-devel  lcms-devel libX11-devel libXext-devel libXt-devel ghostscript-devel libtiff-devel ghostscript-devel libtiff-devel
#yum install ghostscript-devel libtiff-devel

startDir=$(pwd)
. ./setupDirectory.sh





cp ../packages/imagick/imagick.spec $RPM_DIR/SPECS/imagick.spec
cp ../packages/imagick/* $RPM_DIR/SOURCES/
# cp ../zips/imagick-master_2015_01_05.tar.gz $RPM_DIR/SOURCES/imagick-master.tar.gz

wget -O $RPM_DIR/SOURCES/imagick-master.tar.gz https://github.com/mkoppanen/imagick/archive/master.tar.gz

if [ $? -eq 0 ]; then
    echo "Download succeeded?"
else
    status=$?
    echo "Download failed"
    exit $status
fi


cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/imagick.spec


. ${startDir}/copyAndRepo.sh





