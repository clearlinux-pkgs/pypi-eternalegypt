#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-eternalegypt
Version  : 0.0.13
Release  : 38
URL      : https://files.pythonhosted.org/packages/b4/13/7b2141cbcbed83d5e217670ace87fae48eacc24d472a2a9db6550fbab7cc/eternalegypt-0.0.13.tar.gz
Source0  : https://files.pythonhosted.org/packages/b4/13/7b2141cbcbed83d5e217670ace87fae48eacc24d472a2a9db6550fbab7cc/eternalegypt-0.0.13.tar.gz
Summary  : Netgear LTE modem API
Group    : Development/Tools
License  : MIT
Requires: pypi-eternalegypt-license = %{version}-%{release}
Requires: pypi-eternalegypt-python = %{version}-%{release}
Requires: pypi-eternalegypt-python3 = %{version}-%{release}
Requires: pypi(flatten_json)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(aiohttp)
BuildRequires : pypi(attrs)
BuildRequires : pypi(flatten_json)

%description
# Eternal Egypt
This library piggybacks on the web interface of Netgear LTE modems to provide a simple async Python 3 API.

%package license
Summary: license components for the pypi-eternalegypt package.
Group: Default

%description license
license components for the pypi-eternalegypt package.


%package python
Summary: python components for the pypi-eternalegypt package.
Group: Default
Requires: pypi-eternalegypt-python3 = %{version}-%{release}

%description python
python components for the pypi-eternalegypt package.


%package python3
Summary: python3 components for the pypi-eternalegypt package.
Group: Default
Requires: python3-core
Provides: pypi(eternalegypt)
Requires: pypi(aiohttp)
Requires: pypi(attrs)

%description python3
python3 components for the pypi-eternalegypt package.


%prep
%setup -q -n eternalegypt-0.0.13
cd %{_builddir}/eternalegypt-0.0.13
pushd ..
cp -a eternalegypt-0.0.13 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656406448
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-eternalegypt
cp %{_builddir}/eternalegypt-0.0.13/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-eternalegypt/1e516e92e435cf640c534f48416dca1ddd6cefb7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-eternalegypt/1e516e92e435cf640c534f48416dca1ddd6cefb7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
