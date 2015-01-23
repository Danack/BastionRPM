#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/valgrind/valgrind.spec $RPM_DIR/SPECS/valgrind.spec
cp ../zips/valgrind-3.10.0.tar.bz2 $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/valgrind.spec

. ./copyAndRepo.sh



