
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/ImageMagick/ImageMagick.spec $RPM_DIR/SPECS/ImageMagick.spec
cp ../packages/ImageMagick/* $RPM_DIR/SOURCES/


cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/ImageMagick.spec

cp RPMS/x86_64/* $startDir/../repo/RPMS/x86_64/
cp SRPMS/* $startDir/../repo/SRPMS

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





