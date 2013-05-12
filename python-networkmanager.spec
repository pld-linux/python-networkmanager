%define		module	networkmanager
Summary:	Easy communication with NetworkManager
Name:		python-%{module}
Version:	0.9.8
Release:	1
License:	GPL v3+
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/python-networkmanager/%{name}-%{version}.tar.gz
# Source0-md5:	dbfaff8bf2b27d9448fd22ab4a3bed40
BuildRequires:	python-sphinx
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-networkmanager wraps NetworkManagers D-Bus interface so you can
be less verbose when talking to NetworkManager from Python. All
interfaces have been wrapped in classes, properties are exposed as
Python properties and function calls are forwarded to the correct
interface.

%package apidoc
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidoc
API documentation for %{module}.

%description apidoc -l pl.UTF-8
Dokumentacja API %{module}.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/n-m
%{py_sitescriptdir}/NetworkManager.py[co]
%{py_sitescriptdir}/python_networkmanager-%{version}-py*.egg-info

%files apidoc
%defattr(644,root,root,755)
%doc html/*
