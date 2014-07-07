%define		module	networkmanager
Summary:	Easy communication with NetworkManager
Summary(pl.UTF-8):	Łatwa komunikacja z NetworkManagerem
Name:		python-%{module}
Version:	0.9.12
Release:	1
License:	GPL v3+
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/python-networkmanager/%{name}-%{version}.tar.gz
# Source0-md5:	2cd400a7ca4dcd1ea98c864007032494
URL:		http://pythonhosted.org/python-networkmanager/
BuildRequires:	python-devel-tools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sphinx-pdg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-networkmanager wraps NetworkManager's D-Bus interface so you
can be less verbose when talking to NetworkManager from Python. All
interfaces have been wrapped in classes, properties are exposed as
Python properties and function calls are forwarded to the correct
interface.

%description -l pl.UTF-8
python-networkmanager obudowuje interfejs D-Bus NetworkManagera,
dzięki czemu nie trzeba pisać dużo kodu, żeby komunikować się z
NetworkManagerem z poziomu Pythona. Wszystkie interfejsy zostały
obudowane w klasach, właściwości są udostępnione jako pythonowe, a
wywołania funkcji są przekazywane do właściwego interfejsu.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API modułów networkmanagera
Group:		Documentation
Obsoletes:	python-networkmanager-apidoc

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API modułów networkmanagera.

%prep
%setup -q

%build
%{__python} setup.py build

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
%{__rm} -r html/.{doctrees,buildinfo}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains only general notice, not GPL text
%doc COPYING README
%attr(755,root,root) %{_bindir}/n-m
%{py_sitescriptdir}/NetworkManager.py[co]
%{py_sitescriptdir}/python_networkmanager-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}

%files apidoc
%defattr(644,root,root,755)
%doc html/*
