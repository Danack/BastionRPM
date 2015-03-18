
rc=$?
if [[ $rc != 0 ]] ; then
    echo "Failed to build rpm ${file}"
    exit $rc
fi


cp --no-clobber RPMS/noarch/* $startDir/../repo/RPMS/noarch/
cp --no-clobber RPMS/x86_64/* $startDir/../repo/RPMS/x86_64/

