# https://towardsdatascience.com/how-to-build-your-first-python-package-6a00b02635c9
rm -r dist ;
python setup.py sdist bdist_wheel ;
if twine check dist/* ; then
  if [ "$1" = "--test" ] ; then
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
  else
    twine upload dist/* ;
  fi
fi
