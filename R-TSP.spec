#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-TSP
Version  : 1.1.10
Release  : 41
URL      : https://cran.r-project.org/src/contrib/TSP_1.1-10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/TSP_1.1-10.tar.gz
Summary  : Traveling Salesperson Problem (TSP)
Group    : Development/Tools
License  : GPL-3.0
Requires: R-TSP-lib = %{version}-%{release}
Requires: R-foreach
Requires: R-maps
Requires: R-maptools
Requires: R-sp
BuildRequires : R-foreach
BuildRequires : R-maps
BuildRequires : R-maptools
BuildRequires : R-sp
BuildRequires : buildreq-R

%description
salesperson problem (also traveling salesman problem; TSP).
    The package provides some simple algorithms and
    an interface to the Concorde TSP solver and its implementation of the
    Chained-Lin-Kernighan heuristic. The code for Concorde
    itself is not included in the package and has to be obtained separately.

%package lib
Summary: lib components for the R-TSP package.
Group: Libraries

%description lib
lib components for the R-TSP package.


%prep
%setup -q -c -n TSP
cd %{_builddir}/TSP

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589568712

%install
export SOURCE_DATE_EPOCH=1589568712
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TSP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TSP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TSP
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc TSP || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/TSP/CITATION
/usr/lib64/R/library/TSP/DESCRIPTION
/usr/lib64/R/library/TSP/INDEX
/usr/lib64/R/library/TSP/Meta/Rd.rds
/usr/lib64/R/library/TSP/Meta/data.rds
/usr/lib64/R/library/TSP/Meta/features.rds
/usr/lib64/R/library/TSP/Meta/hsearch.rds
/usr/lib64/R/library/TSP/Meta/links.rds
/usr/lib64/R/library/TSP/Meta/nsInfo.rds
/usr/lib64/R/library/TSP/Meta/package.rds
/usr/lib64/R/library/TSP/Meta/vignette.rds
/usr/lib64/R/library/TSP/NAMESPACE
/usr/lib64/R/library/TSP/NEWS.md
/usr/lib64/R/library/TSP/R/TSP
/usr/lib64/R/library/TSP/R/TSP.rdb
/usr/lib64/R/library/TSP/R/TSP.rdx
/usr/lib64/R/library/TSP/data/USCA312.rda
/usr/lib64/R/library/TSP/data/USCA312_GPS.rda
/usr/lib64/R/library/TSP/data/USCA50.rda
/usr/lib64/R/library/TSP/doc/TSP.R
/usr/lib64/R/library/TSP/doc/TSP.Rnw
/usr/lib64/R/library/TSP/doc/TSP.pdf
/usr/lib64/R/library/TSP/doc/index.html
/usr/lib64/R/library/TSP/examples/d493.tsp
/usr/lib64/R/library/TSP/help/AnIndex
/usr/lib64/R/library/TSP/help/TSP.rdb
/usr/lib64/R/library/TSP/help/TSP.rdx
/usr/lib64/R/library/TSP/help/aliases.rds
/usr/lib64/R/library/TSP/help/paths.rds
/usr/lib64/R/library/TSP/html/00Index.html
/usr/lib64/R/library/TSP/html/R.css
/usr/lib64/R/library/TSP/tests/testthat.R
/usr/lib64/R/library/TSP/tests/testthat/test-ETSP.R
/usr/lib64/R/library/TSP/tests/testthat/test-TSPLIB.R
/usr/lib64/R/library/TSP/tests/testthat/test-concorde.R
/usr/lib64/R/library/TSP/tests/testthat/test-insert_cut_etc.R
/usr/lib64/R/library/TSP/tests/testthat/test-solve_TSP.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/TSP/libs/TSP.so
/usr/lib64/R/library/TSP/libs/TSP.so.avx2
/usr/lib64/R/library/TSP/libs/TSP.so.avx512
