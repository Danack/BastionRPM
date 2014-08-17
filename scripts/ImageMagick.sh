
startDir=$(pwd)
. ./setupDirectory.sh

cp ../spec/ImageMagick.spec $RPM_DIR/SPECS/ImageMagick.spec


cp ../packages/ImageMagick-6.8.9-5.tar.gz $RPM_DIR/SOURCES/ImageMagick-6.8.9-5.tar.gz
cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/ImageMagick.spec


#cp RPMS/x86_64/ImageMagick-6.8.9-5.x86_64.rpm $startDir/../repo/RPMS/x86_64/ImageMagick-6.8.9-5.x86_64.rpm
#cp RPMS/x86_64/ImageMagick-devel-6.8.9-5.x86_64.rpm $startDir/../repo/RPMS/x86_64/ImageMagick-devel-6.8.9-5.x86_64.rpm
#cp RPMS/x86_64/ImageMagick-doc-6.8.9-5.x86_64.rpm $startDir/../repo/RPMS/x86_64/ImageMagick-doc-6.8.9-5.x86_64.rpm
# /root/rpmbuild/RPMS/x86_64/ImageMagick-libs-6.8.9-5.x86_64.rpm


cp RPMS/x86_64/* $startDir/../repo/RPMS/x86_64/
cp SRPMS/* $startDir/../repo/SRPMS


createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





