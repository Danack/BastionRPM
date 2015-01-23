
rc=$?
if [[ $rc != 0 ]] ; then
    echo "Failed to build rpm ${file}"
    exit $rc
fi

# rpm --resign SRPMS/*
# rpm --resign RPMS/noarch/*
# rpm --resign RPMS/x86_64/*

cp --no-clobber SRPMS/*  $startDir/../repo/SRPMS/
cp --no-clobber RPMS/noarch/* $startDir/../repo/RPMS/noarch/
cp --no-clobber RPMS/x86_64/* $startDir/../repo/RPMS/x86_64/

# createrepo $startDir/../repo/SRPMS
# createrepo $startDir/../repo/RPMS/noarch
# createrepo $startDir/../repo/RPMS/x86_64