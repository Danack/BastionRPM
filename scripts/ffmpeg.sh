#https://stereochro.me/ideas/rpm-for-the-unwilling

startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/ffmpeg/ffmpeg.spec $RPM_DIR/SPECS/ffmpeg.spec
cp ../zips/ffmpeg-2.4.3.tar.bz2 $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/ffmpeg.spec

. ${startDir}/copyAndRepo.sh






